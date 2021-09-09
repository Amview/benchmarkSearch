import sqlite3
import sys

from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSlot, Qt, QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QCursor
from PyQt5.QtWidgets import QApplication, QPushButton

from method import RReadTable, passmark, curdData, getConfig, UUpdate
from ui import ui


class pymain(ui):
    def __init__(self):
        super(pymain, self).__init__()
        self.setupUi(self)
        self.mythread = MyThread()
        # 判断下拉列表索引，选择不同数据源
        self.i = 1

        self.t_layout.addWidget(self.pushButton_close, 0, 0, 1, 1)
        self.t_layout.addWidget(self.pushButton_visit, 0, 1, 1, 1)
        self.t_layout.addWidget(self.pushButton_mini, 0, 2, 1, 1)

        self.gridLayout.addWidget(self.t_widget, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.k_widget, 0, 1, 1, 10)
        self.gridLayout.addWidget(self.listWidget, 1, 0, 7, 2)
        self.gridLayout.addWidget(self.stackedWidget, 1, 2, 1, 1)

        self.right_layout.addWidget(self.h1_widget,0,0,1,1)
        self.right_layout.addWidget(self.horizontal_widget,1,0,10,1)

        self.h1_Layout.setAlignment(QtCore.Qt.AlignLeft)
        self.h1_Layout.addWidget(self.lineEdit)
        self.h1_Layout.addWidget(self.search)
        self.h1_Layout.addWidget(self.singleScore)
        self.h1_Layout.addWidget(self.dScore)
        self.h1_Layout.addWidget(self.gpuScore)
        self.h1_Layout.addWidget(self.updateScore)
        self.h1_Layout.addWidget(self.button1)
        self.h1_Layout.addWidget(self.button2)
        self.h1_Layout.addWidget(self.labelTable)
        self.h1_Layout.addWidget(self.pbar)

        self.horizontalLayout.addWidget(self.splitter)

        self.splitter.addWidget(self.tableWidget)
        self.splitter.addWidget(self.tableWidget1)
        self.splitter.setStretchFactor(0, 3)
        self.splitter.setStretchFactor(1, 5)


        self.listWidget.currentRowChanged.connect(self.stackedWidget.setCurrentIndex)
        self.listWidget.clicked.connect(self.currentRow1)

        self.tableWidget.doubleClicked.connect(self.tableWidget_)
        self.pushButton_close.clicked.connect(self.pushButton_close_clicked)
        self.pushButton_mini.clicked.connect(self.pushButton_mini_clicked)
        self.pushButton_visit.clicked.connect(self.pushButton_visit_clicked)
        self.upPage.clicked.connect(self.pageUp)
        self.nextPage.clicked.connect(self.pageDown)
        self.firstPage.clicked.connect(self.firstPage1)
        self.endPage.clicked.connect(self.endPage1)
        self.lineEdit.returnPressed.connect(self.search1)
        self.search.clicked.connect(self.search1)
        self.singleScore.clicked.connect(self.singleScore1)
        self.dScore.clicked.connect(self.dScore1)
        self.gpuScore.clicked.connect(self.gpuScore1)
        self.updateScore.clicked.connect(self.updateScore1)

        self.tableName = 'passmark_manyCpu'
    def tableWidget_(self):
        row = self.tableWidget.currentRow()
        name = self.tableWidget.item(row,0).text()
        scores = self.tableWidget.item(row,1).text()
        print(name+"--"+scores)
        list = [name,scores]
        columnList = ['', '名字','分数']
        RReadTable.readTable1(self,list,columnList)

    def updateScore1(self):
        UUpdate.updateScore(self,'passmark_manyCpu')
        UUpdate.updateScore(self, 'passmark_singleCpu')
        UUpdate.updateScore(self, 'passmarkGpu')
        self.labelTable.setText("更新完成")


    def gpuScore1(self):
        self.tableName = 'passmarkGpu'
        self.tableWidget.clearContents()
        self.search1()

    def dScore1(self):
        self.tableName = 'passmark_manyCpu'
        self.tableWidget.clearContents()
        self.search1()

    def singleScore1(self):
        self.tableName = 'passmark_singleCpu'
        self.tableWidget.clearContents()
        self.search1()


    def currentRow1(self):
        name = self.listWidget.item(self.listWidget.currentRow()).text()
        self.labelTable.setText(name)
        self.search1()

    def search1(self):
        key = self.lineEdit.text()
        list = curdData.search(self.tableName,"name",key)
        columnList = ['名字','分数']
        RReadTable.readTable(self,list,columnList)

    # 上一页
    def pageUp(self):
        self.i = self.i - 1
        if self.i < 1:
            self.i = 1
        self.labelOn.setText(str(self.i))
        RReadTable.readTable(self, (self.i - 1) * 20, 20)

    # 下一页
    def pageDown(self):
        self.i = self.i + 1
        if self.i >= int(self.totlerow / 20):
            self.i = int(self.totlerow / 20)
        RReadTable.readTable(self, (self.i - 1) * 20, 20)
        self.labelOn.setText(str(self.i))

    def firstPage1(self):
        self.i = 1
        RReadTable.readTable(self, self.i - 1, 20)
        self.labelOn.setText(str(self.i))

    def endPage1(self):
        print(self.totlerow)
        self.i = int(self.totlerow / 20)
        RReadTable.readTable(self, self.i * 20, 20)
        self.labelOn.setText(str(self.i))

    @pyqtSlot()
    def pushButton_close_clicked(self):
        """
        关闭窗口
        """
        self.close()

    @pyqtSlot()
    def pushButton_mini_clicked(self):
        """
        最小化窗口
        """
        self.showMinimized()

    def pushButton_visit_clicked(self):
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))  # 更改鼠标图标

    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos() - self.m_Position)  # 更改窗口位置
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False
        self.setCursor(QCursor(Qt.ArrowCursor))


class MyThread(QThread):
    def __int__(self):
        super(MyThread, self).__init__()

    def run(self):
        print("123")


if __name__ == "__main__":
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    win = pymain()
    win.setWindowTitle('性能Search')
    win.resize(800, 600)
    win.setWindowIcon(QIcon('icon.ico'))
    win.setWindowTitle("性能Search")
    # win.setStyleSheet("#MainWindow{background-color: white}")
    # win.setStyleSheet("#MainWindow{border-image:url(./bg.jpg);}")
    win.show()
    if app.exec_():
        sys.exit()
