#
#  chatmasalaAppDelegate.py
#  chatmasala
#
#  Created by ideamonk on 29/09/10.
#  Copyright ideamonk.in 2010. All rights reserved.
#

from Foundation import *
from AppKit import *
from objc import IBOutlet, IBAction

class chatmasalaAppDelegate(NSObject):        
    def applicationDidFinishLaunching_(self, sender):
        NSLog("Application did finish launching.")

