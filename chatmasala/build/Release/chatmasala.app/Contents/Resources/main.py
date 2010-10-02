#
#  main.py
#  chatmasala
#
#  Created by ideamonk on 29/09/10.
#  Copyright ideamonk.in 2010. All rights reserved.
#

#import modules required by application
from PyObjCTools import AppHelper
import WebKit       # this makes py2app aware of WebView

import objc
import Foundation
import AppKit


# import modules containing classes required to start application and load MainMenu.nib
import chatmasalaAppDelegate
import Controller_MainWindow

#base_path = os.path.join(os.path.dirname(os.getcwd()), 'Frameworks')
# pass control to AppKit
AppHelper.runEventLoop()
