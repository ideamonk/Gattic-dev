#
#  main.py
#  chatmasala
#
#  Created by ideamonk on 29/09/10.
#  Copyright ideamonk.in 2010. All rights reserved.
#

#import modules required by application
import objc
import Foundation
import AppKit

from PyObjCTools import AppHelper

# import modules containing classes required to start application and load MainMenu.nib
import chatmasalaAppDelegate
import Controller_MainWindow

# pass control to AppKit
AppHelper.runEventLoop()
