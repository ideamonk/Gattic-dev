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
import sqlite3

try:
    from mechanize import Browser
except ImportError:
    print "Mechanize required but missing"
    sys.exit(1)
    
__author__ = "Abhishek Mishra"
__copyright__ = "Copyright 2010, Abhishek Mishra"
__credits__ = ["Abhishek Mishra"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Abhishek Mishra"
__email__ = "ideamonk@gmail.com"
__status__ = "Beta"

