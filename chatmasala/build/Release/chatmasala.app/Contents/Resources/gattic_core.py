# -*- coding: utf-8 -*-
'''
    Gattic Core Functionality Module
    
    Provides an outlet of pure data / errors / exceptions for the UI controllers.
    Does all the Foo Bar magic :D
    
    Copyright (C) Abhishek Mishra <ideamonk@gmail.com>
'''

import urllib
import urllib2

import sqlite3
from mechanize import Browser
from BeautifulSoup import BeautifulSoup

from helpers import *

# global browser object
br = Browser()
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; \
              rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
br.set_handle_robots(False)

def get_connection():
    return sqlite3.connect(applicationSupportFolder() + '/gattic.db')
    
def validate_auth(email, password):
    ''' validation for email address and password length '''
    def validateEmail(a):
        sep=[x for x in a if not x.isalpha()]
        sepjoined=''.join(sep)
        ## sep joined must be ..@.... form
        if sepjoined.strip('.') != '@': return False
        end=a
        for i in sep:
            part,i,end=end.partition(i)
            if len(part)<2: return False
        return True
    
    return validateEmail(email) and len(password.strip())>3
    

def do_auth(callback, email, password):
    ''' does authentication, prepares a browser with logged in state '''
    callback(2,"Connecting to Gmail...")
    global br
    
    del br              # start afresh to get rid of cookies, captcha, etc
    br = Browser()
    
    try:
        response = br.open("https://mail.google.com/mail")
    except urllib2.URLError, e:
        return callback(1, "Can't reach Gmail, no routes available")
    except urllib2.HTTPError, e:
        return callback(1, "Gmail couldn't fullfill the request, code - %s" % e.code)
    except:
        return callback(1, "Unable to sign-in due to connectivity issues")
    
    try:
        login_form = br.forms().next()
    except:
        return callback(1, "Unable to find a way to sign-in")
    
    callback(2,"Signing in..")
    # Authentication
    login_form["Email"] = email
    login_form["Passwd"] = password
    try:
        br.open( login_form.click() )
    except:
        print br.title()
        return callback(1, "Unable sign-in at this moment, please retry")
    callback(2,"Signing in...")
    try:
        br.open( "https://mail.google.com/mail/h/" )
    except:
        return callback(1, "Unable sign-in at this moment, please retry")
        
    verification = br.title().lower()
    if "inbox" in verification:
        # signed in
        callback(0,"Signed in as %s" % email)
    else:
        # invalid login
        return callback(1, "Wrong email adress or password")
        

def fetchLogs():
    db_conn = get_connection()
    db_cur = db_conn.cursor()

    # here callback is more of a status indicator
    try:
        db_cur.execute("select * from chats order by date")
    except:
        # maybe the table isn't created yet
        db_cur.execute('''create table chats
                        (date text, sender text, chunk blob)''')
        db_cur.execute("""insert into chats
          values ('0000-01-01','Welcome to Gattic','<div class="msg">
          <div><span style="display:block;float:left;color:#888">6:56 PM </span><span style="display:block;padding-left:6em"><span><span style="font-weight:bold">Gattic</span>: Hi there! <br /> Thank you for using Gattic</div></div>')""")
        db_conn.commit()
        db_cur.execute("select * from chats order by date")
    return [r for r in db_cur]
    
    