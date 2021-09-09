from PyQt5 import QtCore, QtWidgets, Qt
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QLineEdit, QHeaderView, QLabel, QSizePolicy, \
    QListWidget, QMainWindow, QStackedWidget, QListWidgetItem, QTableWidget, QProgressBar, QSplitter

import SSetStyleSheet


class ui(QMainWindow):
    def setupUi(self, MainWindow):
        # 主窗口
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        # 隐藏边框
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        # 设置窗口透明度
        # MainWindow.setWindowOpacity(0.9)
        MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        MainWindow.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框

        # self.effect = QtWidgets.QGraphicsDropShadowEffect(self)
        # self.effect.setOffset(0,0)
        # self.effect.setBlurRadius(10)
        # self.effect.setColor(QtCore.Qt.gray)
        # self.centralwidget.setGraphicsEffect(self.effect)
        self.main_widget = QtWidgets.QWidget()
        self.main_widget.setStyleSheet('''QWidget{border-radius: 7px;background-color: rgb(255, 255, 255);}''')


        # 布局
        # 整体网格布局
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout.setSpacing(0)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        # 三大件
        self.t_widget = QtWidgets.QWidget()  # 创建窗口主部件
        self.t_layout = QtWidgets.QGridLayout()  # 创建主部件的网格布局
        self.t_widget.setLayout(self.t_layout)
        # 空白
        self.k_widget = QtWidgets.QWidget()  # 创建窗口主部件
        self.k_layout = QtWidgets.QGridLayout()  # 创建主部件的网格布局
        self.k_widget.setLayout(self.k_layout)
        # 右边部件
        self.right_widget = QtWidgets.QWidget()  # 创建窗口主部件
        self.right_layout = QtWidgets.QGridLayout()  # 创建主部件的网格布局
        self.right_widget.setLayout(self.right_layout)

        # 右边部件按钮水平布局
        self.h1_widget = QtWidgets.QWidget()  # 创建窗口主部件
        self.h1_Layout = QtWidgets.QHBoxLayout()
        self.h1_widget.setLayout(self.h1_Layout)

        # 右边部件table水平布局
        self.horizontal_widget = QtWidgets.QWidget()  # 创建窗口主部件
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontal_widget.setLayout(self.horizontalLayout)



        self.splitter = QSplitter(QtCore.Qt.Horizontal)

        # 文本框
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setFixedSize(100, 20)
        self.lineEdit.setPlaceholderText("GTX 750")

        # 记录当前页数
        self.labelOn = QLabel(self.centralwidget)
        self.labelOn.setObjectName(u"labelOn")
        self.labelOn.setFixedSize(30,30)

        # 记录总页数
        self.labelTotal = QLabel(self.centralwidget)
        self.labelTotal.setObjectName(u"labelTotal")
        self.labelTotal.setFixedSize(30, 30)

        # 记录表单
        self.labelTable = QLabel(self.centralwidget)
        self.labelTable.setObjectName(u"labelTable")
        self.labelTable.setFixedSize(80, 20)
        self.labelTable.setAlignment(QtCore.Qt.AlignCenter)


        # 表
        self.tableWidget = QTableWidget(self.centralwidget)
        # 自适应宽度
        # self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)
        # 隐藏列标题
        self.tableWidget.verticalHeader().hide()
        # 不显示框线
        self.tableWidget.setShowGrid(False)
        # 不设置焦点
        self.tableWidget.setFocusPolicy(QtCore.Qt.NoFocus)
        # 不可编辑
        self.tableWidget.setEditTriggers(QTableWidget.NoEditTriggers)
        # 标题左对齐
        self.tableWidget.horizontalHeader().setDefaultAlignment(QtCore.Qt.AlignLeft)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.setColumnWidth(0, 100)

        # 表
        self.tableWidget1 = QTableWidget(self.centralwidget)
        # 自适应宽度
        # self.tableWidget1.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # self.tableWidget1.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.tableWidget1.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)
        # 隐藏列标题
        self.tableWidget1.verticalHeader().hide()
        # 隐藏行标题
        self.tableWidget1.horizontalHeader().hide()
        # 不显示框线
        self.tableWidget1.setShowGrid(False)
        # 不设置焦点
        self.tableWidget1.setFocusPolicy(QtCore.Qt.NoFocus)
        # 不可编辑
        self.tableWidget1.setEditTriggers(QTableWidget.NoEditTriggers)
        self.tableWidget1.horizontalHeader().setStretchLastSection(True)

        # newItem = QTableWidgetItem("张三")  # 添加张三 到（0，0）
        # self.tableWidget.setItem(0, 0, newItem)
        # 进度条
        self.pbar = QProgressBar(self)
        self.pbar.setFixedSize(100, 20)

        # list部件
        self.listWidget = QListWidget(self.centralwidget)
        self.Item1 = QListWidgetItem()
        self.listWidget.addItem(self.Item1)
        self.Item1.setText("Passmark")
        self.Item1.setTextAlignment(QtCore.Qt.AlignCenter)
        self.Item1.setSizeHint(QSize(20, 50))
        self.listWidget.setFixedWidth(150)

        self.Item2 = QListWidgetItem()
        self.listWidget.addItem(self.Item2)
        self.Item2.setText("Cinebench")
        self.Item2.setTextAlignment(QtCore.Qt.AlignCenter)
        self.Item2.setSizeHint(QSize(20, 50))
        self.listWidget.setFixedWidth(150)

        self.Item3 = QListWidgetItem()
        self.listWidget.addItem(self.Item3)
        self.Item3.setText("Dram")
        self.Item3.setTextAlignment(QtCore.Qt.AlignCenter)
        self.Item3.setSizeHint(QSize(20, 50))
        self.listWidget.setFixedWidth(150)

        self.Item4 = QListWidgetItem()
        self.listWidget.addItem(self.Item4)
        self.Item4.setText("Nand")
        self.Item4.setTextAlignment(QtCore.Qt.AlignCenter)
        self.Item4.setSizeHint(QSize(20, 50))
        self.listWidget.setFixedWidth(150)

        self.Item5 = QListWidgetItem()
        self.listWidget.addItem(self.Item5)
        self.Item5.setText("Antutu")
        self.Item5.setTextAlignment(QtCore.Qt.AlignCenter)
        self.Item5.setSizeHint(QSize(20, 50))
        self.listWidget.setFixedWidth(150)

        self.Item6 = QListWidgetItem()
        self.listWidget.addItem(self.Item6)
        self.Item6.setText("DxoMark")
        self.Item6.setTextAlignment(QtCore.Qt.AlignCenter)
        self.Item6.setSizeHint(QSize(20, 50))
        self.listWidget.setFixedWidth(150)


        #  QStackedWidget
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.addWidget(self.right_widget)

        # 按钮
        # 最大最小化
        self.pushButton_close = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_close.setFixedSize(18, 18)
        self.pushButton_close.setObjectName("pushButton_close")
        self.pushButton_mini = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_mini.setObjectName("pushButton_mini")
        self.pushButton_mini.setFixedSize(18, 18)
        self.pushButton_visit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_visit.setFixedSize(18, 18)
        self.pushButton_visit.setObjectName("pushButton_visit")

        # 上一页按钮
        self.upPage = QtWidgets.QPushButton(self.centralwidget)
        self.upPage.setFixedSize(50, 30)
        self.upPage.setObjectName("upPage")
        self.upPage.setText("上一页")

        # 下一页按钮
        self.nextPage = QtWidgets.QPushButton(self.centralwidget)
        self.nextPage.setFixedSize(50, 30)
        self.nextPage.setObjectName("nextPage")
        self.nextPage.setText("下一页")

        # 最后一页
        self.endPage = QtWidgets.QPushButton(self.centralwidget)
        self.endPage.setFixedSize(60, 30)
        self.endPage.setObjectName("endPage")
        self.endPage.setText("最后一页")

        # 第一页
        self.firstPage = QtWidgets.QPushButton(self.centralwidget)
        self.firstPage.setFixedSize(50, 30)
        self.firstPage.setObjectName("firstPage")
        self.firstPage.setText("第一页")

        # 查询
        self.search = QtWidgets.QPushButton(self.centralwidget)
        self.search.setFixedSize(50, 20)
        self.search.setObjectName("search")
        self.search.setText("查询")

        # cpu单核
        self.singleScore = QtWidgets.QPushButton(self.centralwidget)
        self.singleScore.setFixedSize(50, 20)
        self.singleScore.setObjectName("singleScore")
        self.singleScore.setText("单核")

        # cpu多核
        self.dScore = QtWidgets.QPushButton(self.centralwidget)
        self.dScore.setFixedSize(50, 20)
        self.dScore.setObjectName("dScore")
        self.dScore.setText("多核")

        # gpu
        self.gpuScore = QtWidgets.QPushButton(self.centralwidget)
        self.gpuScore.setFixedSize(50, 20)
        self.gpuScore.setObjectName("gpuScore")
        self.gpuScore.setText("GPU")

        # 更新数据
        self.updateScore = QtWidgets.QPushButton(self.centralwidget)
        self.updateScore.setFixedSize(50, 20)
        self.updateScore.setObjectName("updateScore")
        self.updateScore.setText("更新")
        # 柱状图
        self.button1 = QtWidgets.QPushButton(self.centralwidget)
        self.button1.setFixedSize(50, 20)
        self.button1.setObjectName("button1")
        self.button1.setText("柱状图")
        # 天梯图
        self.button2 = QtWidgets.QPushButton(self.centralwidget)
        self.button2.setFixedSize(50, 20)
        self.button2.setObjectName("button2")
        self.button2.setText("天梯图")

        # 三大键固定位置
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_close.sizePolicy().hasHeightForWidth())
        self.pushButton_close.setSizePolicy(sizePolicy)
        sizePolicy.setHeightForWidth(self.pushButton_visit.sizePolicy().hasHeightForWidth())
        self.pushButton_visit.setSizePolicy(sizePolicy)
        sizePolicy.setHeightForWidth(self.pushButton_mini.sizePolicy().hasHeightForWidth())
        self.pushButton_mini.setSizePolicy(sizePolicy)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        SSetStyleSheet.setStyleSheet(self)

