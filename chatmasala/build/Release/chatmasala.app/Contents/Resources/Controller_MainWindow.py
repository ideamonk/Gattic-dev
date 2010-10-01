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

class Controller_MainWindow(NSWindowController):
    myWebView = IBOutlet()
    myTableGrid = IBOutlet()
    chatSplitView = IBOutlet()
    overviewView = IBOutlet()
    prefsView = IBOutlet()
    mainWindow = IBOutlet()
    menuPanel = IBOutlet()
    
    # default configs, etc
    MAIN_WIDTH = 524
    MAIN_HEIGHT = 470
    SCREEN_FRAME = None
    TOOL_HEIGHT = None
    
    def awakeFromNib(self):
        # collect spread out controllers one over the other
        self.menuPanel.setAllowsUserCustomization_(NO)
        self.TOOL_HEIGHT = self.mainWindow.frame().size.height \
                    - self.mainWindow.contentView().frame().size.height
        self.SCREEN_FRAME = self.mainWindow.screen().frame()
        
        # reset your own size
        self.mainWindow.setFrame_display_(
            NSRect(
                    self.mainWindow.frame().origin,
                    (self.MAIN_WIDTH,self.MAIN_HEIGHT + self.TOOL_HEIGHT)
                ), 
            YES
        )
        self.chatSplitView.setFrame_(
            NSRect(
                (0, 0),
                (self.MAIN_WIDTH, self.mainWindow.contentView().frame().size.height)
            )
        )
        self.overviewView.setFrame_(
            NSRect(
                (0, 0),
                (self.MAIN_WIDTH, self.mainWindow.contentView().frame().size.height)
            )
        )
        self.prefsView.setFrame_(
            NSRect(
                (0, 0),
                (self.MAIN_WIDTH, self.mainWindow.contentView().frame().size.height)
            )
        )
        
        # hide nondefault views
        self.prefsView.setAlphaValue_(0.0)
        self.chatSplitView.setAlphaValue_(0.0)
        
        
    @IBAction
    def BtnSyncClick_(self, sender):
        self.myWebView.setMainFrameURL_("file://" + applicationBundlePath() + "/chatview.html")
        
    @IBAction
    def BtnActionPanelClick_(self, sender):
        pressed = sender.labelForSegment_( sender.selectedSegment() )
        if pressed=="Overview":
            self.overviewView.animator().setAlphaValue_(1.0)
            self.chatSplitView.animator().setAlphaValue_(0.0)
            self.prefsView.animator().setAlphaValue_(0.0)

        if pressed=="Chat Logs":
            self.chatSplitView.animator().setAlphaValue_(1.0)
            self.overviewView.animator().setAlphaValue_(0.0)
            self.prefsView.animator().setAlphaValue_(0.0)
            
        if pressed=="Preferences":
            self.prefsView.animator().setAlphaValue_(1.0)
            self.chatSplitView.animator().setAlphaValue_(0.0)
            self.overviewView.animator().setAlphaValue_(0.0)