#
#  Controller_MainWindow.py
#  chatmasala
#
#  Created by ideamonk on 30/09/10.
#  Copyright (c) 2010 ideamonk.in. All rights reserved.
#

from Foundation import *
from AppKit import *
from objc import IBOutlet, IBAction

from helpers import *
import gattic_core

class Controller_MainWindow(NSWindowController):
    mainWindow = IBOutlet()
    helpWebVew = IBOutlet()
    chatSplitView = IBOutlet()
    overviewView = IBOutlet()
    
    myTableGrid = IBOutlet()
    myWebView = IBOutlet()    
    helpView = IBOutlet()
    
    menuPanel = IBOutlet()
    statusView = IBOutlet()
    spinnerStatus = IBOutlet()
    labelStatus = IBOutlet()
    warningStatus = IBOutlet()
    loginView = IBOutlet()
    gattic_username = IBOutlet()
    gattic_password = IBOutlet()
    gattic_BtnLogin = IBOutlet()
    
    # default configs, etc
    MAIN_WIDTH = 524
    MAIN_HEIGHT = 470
    MAIN_CONTENT_HEIGHT = None
    SCREEN_FRAME = None
    TOOL_HEIGHT = None
    STATUS_HEIGHT = None
    
    # auth params
    auth_login = None
    auth_pass = None

    def showGattic(self):
        ''' Default view - Gattic '''
        self.overviewView.setFrameOrigin_(
            NSPoint(0,self.STATUS_HEIGHT)
        )
        self.overviewView.animator().setAlphaValue_(1.0)
        
        self.chatSplitView.setFrameOrigin_(
            NSPoint(0, self.mainWindow.contentView().frame().size.height)
        )
        self.chatSplitView.animator().setAlphaValue_(0.0)
        self.helpView.setFrameOrigin_(
            NSPoint(0,self.mainWindow.contentView().frame().size.height)
        )
        self.helpView.animator().setAlphaValue_(0.0)
        
    def showMyAttic(self):
        ''' My Attic - list + webkit '''
        self.chatSplitView.setFrameOrigin_(
            NSPoint(0,self.STATUS_HEIGHT)
        )
        self.chatSplitView.animator().setAlphaValue_(1.0)
        
        self.overviewView.animator().setAlphaValue_(0.0)
        self.overviewView.setFrameOrigin_(
            NSPoint(0,self.mainWindow.contentView().frame().size.height)
        )
        
        self.helpView.animator().setAlphaValue_(0.0)
        self.helpView.setFrameOrigin_(
            NSPoint(0,self.mainWindow.contentView().frame().size.height)
        )
    
    def showHelp(self):
        ''' Help View '''
        self.helpView.setFrameOrigin_(
            NSPoint(0,self.STATUS_HEIGHT)
        )
        self.helpView.animator().setAlphaValue_(1.0)
        
        self.chatSplitView.animator().setAlphaValue_(0.0)
        self.chatSplitView.setFrameOrigin_(
            NSPoint(0,self.mainWindow.contentView().frame().size.height)
        )
        
        self.overviewView.animator().setAlphaValue_(0.0)
        self.overviewView.setFrameOrigin_(
            NSPoint(0,self.mainWindow.contentView().frame().size.height)
        )

    def awakeFromNib(self):
        # collect spread out controllers one over the other
        self.menuPanel.setAllowsUserCustomization_(NO)
        self.TOOL_HEIGHT = self.mainWindow.frame().size.height \
                    - self.mainWindow.contentView().frame().size.height
        self.SCREEN_FRAME = self.mainWindow.screen().frame()
        self.spinnerStatus.setHidden_(YES)
        self.labelStatus.setNeedsDisplay_(YES)
        self.spinnerStatus.setNeedsDisplay_(YES)
        
        # reset your own size
        self.mainWindow.setFrame_display_(
            NSRect(
                    self.mainWindow.frame().origin,
                    (self.MAIN_WIDTH,self.MAIN_HEIGHT + self.TOOL_HEIGHT)
                ), 
            YES
        )
        
        # fix status to bottom
        self.statusView.setFrame_(
            NSRect((0,0), (self.MAIN_WIDTH, 22)) 
        )
            
        self.STATUS_HEIGHT = self.statusView.frame().size.height
        self.MAIN_CONTENT_HEIGHT = self.mainWindow.contentView().frame().size.height - self.STATUS_HEIGHT
                
        # setup other view heights        
        self.chatSplitView.setFrame_(
            NSRect(
                (0, self.STATUS_HEIGHT),
                (self.MAIN_WIDTH, self.MAIN_CONTENT_HEIGHT)
            )
        )
        self.overviewView.setFrame_(
            NSRect(
                (0, self.STATUS_HEIGHT),
                (self.MAIN_WIDTH-22, self.MAIN_CONTENT_HEIGHT)
            )
        )
        self.helpView.setFrame_(
            NSRect(
                (0, self.STATUS_HEIGHT),
                (self.MAIN_WIDTH, self.MAIN_CONTENT_HEIGHT)
            )
        )
        self.loginView.setFrame_(
            NSRect(
                (60, self.STATUS_HEIGHT-50),
                (self.MAIN_WIDTH-120, self.MAIN_CONTENT_HEIGHT)
            )
        )
        
        # hide nondefault views
        self.showGattic()        
    
    @IBAction
    def BtnSyncUpClick_(self, sender):
        print "SYNC"
        
    @IBAction
    def BtnActionPanelClick_(self, sender):
        pressed = sender.labelForSegment_( sender.selectedSegment() )
        if pressed=="Gattic":
            self.showGattic()
        if pressed=="My Attic":
            self.showMyAttic()
        if pressed=="Help":
            self.showHelp()
            
    def toggleLoginControls(self, bool):
        self.gattic_password.setEnabled_(bool)
        self.gattic_username.setEnabled_(bool)
        self.gattic_BtnLogin.setEnabled_(bool)
        
    @IBAction
    def BtnSignInClick_(self,sender):
        self.auth_login = email = self.gattic_username.stringValue()
        self.auth_pass = password = self.gattic_password.stringValue()
        
        if gattic_core.validate_auth(email, password):
            # lock the buttons etc
            self.toggleLoginControls(NO)
            # activate status bar msg
            self.spinnerStatus.startAnimation_(self)
            # authenticate
            thread = NSThread.detachNewThreadSelector_toTarget_withObject_(
                                                    'start_do_auth',self, None)
        else:
            print "rejected"
    
    @AutoPooled
    def start_do_auth(self):        
        gattic_core.do_auth(self.return_do_auth,self.auth_login,self.auth_pass)
        
    def return_do_auth(self,code, msg):
        if code==1:
            # failed
            self.labelStatus.setStringValue_(msg)
            self.spinnerStatus.setHidden_(YES)
            self.warningStatus.setHidden_(NO)
            self.toggleLoginControls(YES)
        elif code==2:
            #progress
            self.labelStatus.setStringValue_(msg)
            self.warningStatus.setHidden_(YES)
            self.spinnerStatus.setHidden_(NO)
        else:
            self.spinnerStatus.setHidden_(NO)
            self.labelStatus.setStringValue_("Signed in as " + self.auth_login)
            print "PASSED"
