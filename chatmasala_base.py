#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
                     ,--. .       .  ,-,-,-.               .      
                    | `-' |-. ,-. |- `,| | |   ,-. ,-. ,-. |  ,-. 
                    |   . | | ,-| |    | ; | . ,-| `-. ,-| |  ,-| 
                    `--'  ' ' `-^ `'   '   `-' `-^ `-' `-^ `' `-^ 

                                    by Abhishek Mishra      <ideamonk@gmail.com >

Keywords: python, tools, gmail, chat
Copyright (C) 2010 Abhishek Mishra, ideamonk.com
'''
import sys
import getpass
import sqlite3  # TODO: storage, incremental backup
#from lxml.html import parse     # TODO: switch to XPath and faster, lighter lxml

try:
    from mechanize import Browser
except ImportError:
    print "Mechanize required but missing"
    sys.exit(1)

try:
    from BeautifulSoup import BeautifulSoup, NavigableString
except ImportError:
    print "Beautiful required but missing"
    sys.exit(1)
    
__author__ = "Abhishek Mishra"
__copyright__ = "Copyright 2010, Abhishek Mishra"
__credits__ = ["Abhishek Mishra"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Abhishek Mishra"
__email__ = "ideamonk@gmail.com"
__status__ = "Beta"

def strip_ml_tags(in_text):
    # from http://code.activestate.com/recipes/440481-strips-xmlhtml-tags-from-string/
    # convert in_text to a mutable object (e.g. list)
    s_list = list(in_text)
    i,j = 0,0
    
    while i < len(s_list):
        # iterate until a left-angle bracket is found
        if s_list[i] == '<':
            while s_list[i] != '>':
                # pop everything from the the left-angle bracket until the right-angle bracket
                s_list.pop(i)
                
            # pops the right-angle bracket, too
            s_list.pop(i)
        else:
            i=i+1
            
    # convert the list back into text
    join_char=''
    return join_char.join(s_list)

def fetcher(br):
    # goto chat page 
    list_page = br.open("https://mail.google.com/mail/h/?s=q&q=subject:(\"Chat+with\")&nvp_site_mail=Search+Mail").read()
    search_start = 20
    search_finished = False
    while "<b>Older" in list_page:
        list_soup = BeautifulSoup(list_page)
        main_table = list_soup.findAll('table', {'cellpadding':'2', 'cellspacing':'0', 
                                                    'width':'100%', 'border':'0', 'class':'th', 
                                                                            'bgcolor':'#e8eef7'})[0]
        list_rows = main_table.findAll('tr')
        for row in list_rows:
            link = row.find('td').findNext('td').findNext('td').a['href']
            expanded_link = "/mail/h/" + link + '&d=e'
            msg_id = expanded_link.split("th=")[1].split("&")[0]
            chat_soup = BeautifulSoup( br.open(expanded_link).read() )
            msg_timestamp = chat_soup.find('a', {'name':'m_'+msg_id}).findNext('table').find('td').findNext('td').contents[0].strip()
            #list_xml = parse(br.open(expanded_link)).getroot() # TODO 
            #list_xml.xpath("//table[2]/tr/td[2]/table/tr/td[2]/table[4]/tr/td/table/tr[4]/td/div/div")[0].text_content()
            chat_table = chat_soup.findAll('table', {'cellpadding':'1', 'cellspacing':'0', 
                                                    'width':'98%', 'border':'0', 'bgcolor':'#cccccc' })[0]
                                            
            person = row.find('td').findNext('td').contents[0].encode("utf-8").strip()
            date_time = chat_table.find('td', {'align':'right', 'valign':'top'}).contents[0].encode("utf-8")
            
            #print "WITH %s   at   %s _______________________" % (person, date_time)
            chat_divs = chat_soup.findAll('div', {'class':'msg'})
            chat_log = ""
            for div in chat_divs:
                #for msg_line in div.findAll('div'):
                #    print strip_ml_tags(msg_line.encode("utf-8").strip())
                chat_log += str(div)
            yield (msg_timestamp, person, msg_id, chat_log)
        list_page = br.open("/mail/h/?s=q&q=subject:(\"Chat+with\")&st=%s" % search_start).read()
        search_start += 20
            
if __name__ == '__main__':
    #print "Email address:",
    email = "ideamonk@gmail.com"
    passwd = getpass.getpass()

    br = Browser()
    br.open("http://mail.google.com")
    login_form = br.forms().next()

    # Authentication
    login_form["Email"] = email
    login_form["Passwd"] = passwd
    br.open( login_form.click() )
    
    f = fetcher(br)
    data = f.next();
    while data:
        print data
        data = f.next()