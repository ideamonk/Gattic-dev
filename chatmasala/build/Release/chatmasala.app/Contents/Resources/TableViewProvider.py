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
    def init(self):
        self.chatLogs = gattic_core.fetchLogs()
        return self
        
    def numberOfRowsInTableView_(self, tableView):
        return len(self.chatLogs)
        
    def getRow(self, row_index):
        if row_index<len(self.chatLogs):
            return self.chatLogs[row_index][2]
        else:
            return ''
        
    def tableView_objectValueForTableColumn_row_(self,sender,tableColumn,row):
        if row < len(self.chatLogs):
            if tableColumn.identifier() == "date":
                return self.chatLogs[row][0]
            else:
                return self.chatLogs[row][1]
        else:
            return None
