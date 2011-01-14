#
#  TableViewProvider.py
#  chatmasala
#
#  Created by ideamonk on 14/10/10.
#  Copyright (c) 2010 appstokill.com. All rights reserved.
#

from objc import YES, NO, IBAction, IBOutlet
from Foundation import *
from AppKit import *

import gattic_core

class TableViewProvider(NSObject):
    tableView = IBOutlet()
    myWebView = IBOutlet()
    
    def init(self):
        self.chatLogs = gattic_core.fetchLogs()
        return self
        
    def numberOfRowsInTableView_(self, tableView):
        return len(self.chatLogs)
        
    def getRow(self, row_index):
        if row_index<len(self.chatLogs):
            if self.chatLogs[row_index][2] == None:
                # fetch this uncached one
                self.chatLogs[row_index][2] = gattic_core.getChatLog(self.chatLogs[row_index][:2])
            return self.chatLogs[row_index][2]
        else:
            return ''
    
    def insertInto(self,date,sender,chunk):
        #try:
        gattic_core.addChat(date,sender,chunk)
        #except:
        #pass
        self.chatLogs.append([date,sender,chunk])
        
    def tableView_objectValueForTableColumn_row_(self,sender,tableColumn,row):
        if row < len(self.chatLogs):
            if tableColumn.identifier() == "date":
                return self.chatLogs[row][0]
            else:
                return self.chatLogs[row][1]
        else:
            return None

    def tableViewSelectionDidChange_(self, notification):
        if self.tableView.selectedRow() != -1:
            chunk = self.tableView.dataSource().getRow(self.tableView.selectedRow()).replace("'","\\'").replace("\n","") 
            self.myWebView.stringByEvaluatingJavaScriptFromString_("foo('%s');" % (chunk))
        else:
            print "got click"