import math
from PyQt5.QtWidgets import QTableWidgetItem, QCheckBox
import sqlite3
# page:第几页
# pageNum：一页几行
# 字典数组读表
def readTable(self,list,columnList):
    self.tableWidget.clearContents()
    self.tableWidget.setColumnCount(2)
    self.tableWidget.setRowCount(len(list))
    self.tableWidget.setHorizontalHeaderLabels(columnList)
    self.tableWidget.setColumnWidth(0, 150)
    self.tableWidget.setColumnWidth(1, 30)
    i = 0
    for item in list:
        # print(item)
        newItem = QTableWidgetItem(item[1])
        self.tableWidget.setItem(i, 0, newItem)

        newItem1 = QTableWidgetItem(item[2])
        self.tableWidget.setItem(i, 1, newItem1)
        i=i+1

# 双击读表
def readTable1(self,list,columnList):
    self.tableWidget1.clearContents()
    self.tableWidget1.setColumnCount(3)
    self.tableWidget1.setRowCount(1)
    self.tableWidget1.setHorizontalHeaderLabels(columnList)
    checkBox = QCheckBox(self.centralwidget)
    checkBox.setObjectName(u"checkBox")
    checkBox.setStyleSheet("QCheckBox{margin:3px};")
    self.tableWidget1.setCellWidget(0, 0, checkBox)
    self.tableWidget1.setColumnWidth(0, 20)
    self.tableWidget1.setColumnWidth(1, 150)

    newItem = QTableWidgetItem(list[0])
    self.tableWidget1.setItem(0, 1, newItem)
    newItem1 = QTableWidgetItem(list[1])
    self.tableWidget1.setItem(0, 2, newItem1)





