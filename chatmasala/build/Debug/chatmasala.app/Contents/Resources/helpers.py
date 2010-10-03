#
#  helpers.py
#  chatmasala
#
#  Created by ideamonk on 01/10/10.
#  Copyright (c) 2010 ideamonk.in. All rights reserved.
#

from Foundation import *
from AppKit import *
import os

APPNAME = "ChatMasala"

def applicationBundlePath():
    return os.path.dirname(__file__)
    
def applicationSupportFolder(appname=None):
    if appname is None:
        appname = APPNAME
        
    paths = NSSearchPathForDirectoriesInDomains(NSApplicationSupportDirectory,NSUserDomainMask,True)
    basePath = (len(paths) > 0 and paths[0]) or NSTemporaryDirectory()
    fullPath = basePath.stringByAppendingPathComponent_(appname)
    if not os.path.exists(fullPath):
        os.mkdir(fullPath)
    return fullPath

def pathForFilename(filename,appname=None):
    base = (appname and applicationSupportFolder(appname)) or applicationSupportFolder()
    return base.stringByAppendingPathComponent_(filename)