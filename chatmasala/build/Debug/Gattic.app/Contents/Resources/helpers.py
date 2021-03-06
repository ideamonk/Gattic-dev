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
import threading

APPNAME = "Gattic"

# signal contstants
SIG_ADDROW = 1
SIG_DBERROR = 2

def applicationBundlePath():
    return NSBundle.mainBundle().bundlePath()
    
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
    
def AutoPooled(f):
    def pooled_func(self):
        pool = NSAutoreleasePool.alloc().init()
        f(self)
        del pool
    return pooled_func
    