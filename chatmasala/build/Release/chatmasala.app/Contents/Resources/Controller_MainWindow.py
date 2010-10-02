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
import chatmasala_core

class Controller_MainWindow(NSWindowController):
    myWebView = IBOutlet()
    helpWebVew = IBOutlet()
    myTableGrid = IBOutlet()
    chatSplitView = IBOutlet()
    overviewView = IBOutlet()
    helpView = IBOutlet()
    mainWindow = IBOutlet()
    menuPanel = IBOutlet()
    statusView = IBOutlet()
    spinnerStatus = IBOutlet()
    labelStatus = IBOutlet()
    loginView = IBOutlet()
    gattic_username = IBOutlet()
    gattic_password = IBOutlet()
    
    # default configs, etc
    MAIN_WIDTH = 524
    MAIN_HEIGHT = 470
    MAIN_CONTENT_HEIGHT = None
    SCREEN_FRAME = None
    TOOL_HEIGHT = None
    STATUS_HEIGHT = None

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
    def BtnHelpClick_(self, sender):
        self.showHelp()
        
    @IBAction
    def BtnActionPanelClick_(self, sender):
        pressed = sender.labelForSegment_( sender.selectedSegment() )
        if pressed=="Gattic":
            self.showGattic()

        if pressed=="My Attic":
            self.showMyAttic()
            
    @IBAction
    def BtnSignInClick_(self,sender):
        print self.gattic_username.stringValue()
        print self.gattic_password.stringValue()
        print "pressed"
        pass