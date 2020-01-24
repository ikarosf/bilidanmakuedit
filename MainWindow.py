# -*- coding: utf-8 -*-
#frx

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PySide2 import QtCore, QtGui, QtWidgets
import action_def
import global_env


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(825, 792)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        global_env.centralwidget = self.centralwidget

        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        global_env.verticalLayout = self.verticalLayout

        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        global_env.tableWidget = self.tableWidget

        self.tableWidget.setColumnCount(1)
        row_count = global_env.row_count
        self.tableWidget.setRowCount(row_count)
        self.tableWidget.itemClicked.connect(action_def.tableWidgetItemClick)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)


        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        # 列宽度自动
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        action_def.table_init()

        self.verticalLayout.addWidget(self.tableWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(6, -1, 6, -1)
        self.horizontalLayout.setSpacing(8)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.reverse_election_button = QtWidgets.QPushButton(self.centralwidget)
        self.reverse_election_button.setMinimumSize(QtCore.QSize(0, 30))
        self.reverse_election_button.setObjectName("reverse_election")
        self.reverse_election_button.clicked.connect(action_def.reverse_election)
        self.horizontalLayout.addWidget(self.reverse_election_button)

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)

        self.pageinfoLabel = QtWidgets.QLabel(self.centralwidget)
        self.pageinfoLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.horizontalLayout.addWidget(self.pageinfoLabel)
        global_env.pageinfoLabel = self.pageinfoLabel

        self.previous_page_button = QtWidgets.QPushButton(self.centralwidget)
        self.previous_page_button.setMinimumSize(QtCore.QSize(0, 30))
        self.previous_page_button.setObjectName("previous_page")
        self.previous_page_button.clicked.connect(action_def.previous_page)
        self.horizontalLayout.addWidget(self.previous_page_button)

        self.next_page_button = QtWidgets.QPushButton(self.centralwidget)
        self.next_page_button.setMinimumSize(QtCore.QSize(0, 30))
        self.next_page_button.setObjectName("next_page")
        self.next_page_button.clicked.connect(action_def.next_page)
        self.horizontalLayout.addWidget(self.next_page_button)

        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 825, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.file_menu = self.menubar.addMenu("file")
        self.edit_menu = self.menubar.addMenu("edit")
        self.help_menu = self.menubar.addMenu("help")

        self.load_file_action = self.file_menu.addAction('load')
        self.load_file_action.triggered.connect(action_def.window_load_file)

        self.save_data_action = self.file_menu.addAction('save_data')
        self.save_data_action.triggered.connect(action_def.save_data)

        self.output_file_action = self.file_menu.addAction('output_file')
        self.output_file_action.triggered.connect(action_def.output_file)

        # self.test_action = self.file_menu.addAction('test')
        # self.test_action.triggered.connect(action_def.test)

        self.edit_rowcount_action = self.edit_menu.addAction('edit_rowcount')
        self.edit_rowcount_action.triggered.connect(action_def.edit_rowcount)

        self.jump_page_action = self.edit_menu.addAction('jump_page')
        self.jump_page_action.triggered.connect(action_def.jump_page)

        self.about_action = self.help_menu.addAction('about')
        self.about_action.triggered.connect(action_def.about_text)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "bili弹幕整理器"))

        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "弹幕文本"))
        self.tableWidget.setSortingEnabled(False)

        self.reverse_election_button.setText(_translate("MainWindow", "反选"))
        self.pushButton_2.setText(_translate("MainWindow", "***"))
        self.previous_page_button.setText(_translate("MainWindow", "上一页"))
        self.next_page_button.setText(_translate("MainWindow", "下一页"))

        self.file_menu.setTitle(_translate("MainWindow", "文件"))
        self.edit_menu.setTitle(_translate("MainWindow", "编辑"))
        self.help_menu.setTitle(_translate("MainWindow", "帮助"))

        self.load_file_action.setText(_translate("MainWindow", "载入"))
        self.save_data_action.setText(_translate("MainWindow", "保存"))
        self.output_file_action.setText(_translate("MainWindow", "输出"))
        self.edit_rowcount_action.setText(_translate("MainWindow", "修改行数"))
        self.jump_page_action.setText(_translate("MainWindow", "跳页"))
        self.about_action.setText(_translate("MainWindow", "关于"))
