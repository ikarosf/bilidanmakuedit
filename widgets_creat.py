# -*- coding: utf-8 -*-

from PySide2 import QtCore, QtGui, QtWidgets
import global_env


# def pushButton_creator():
#     pushButton = QtWidgets.QPushButton(self.centralwidget)

class danmu_tableWidget(QtWidgets.QTableWidgetItem):
    def __init__(self):
        super(danmu_tableWidget, self).__init__()
        self.setCheckState(QtCore.Qt.Unchecked)
        self.setFlags(QtCore.Qt.NoItemFlags)
        self.index = None

    def getclick(self):
        if self.text() == '':
            return
        flag = self.checkState()
        if flag == QtCore.Qt.Unchecked:
            flag = QtCore.Qt.Checked
            fflag = True
        else:
            flag = QtCore.Qt.Unchecked
            fflag = False

        self.setCheckState(flag)
        global_env.edit_danmu_whether_del(self.index, fflag)

    def setCheckState(self, state):
        super().setCheckState(state)
        if state == QtCore.Qt.Unchecked:
            self.setForeground(QtGui.QBrush(QtGui.QColor(0, 150, 0)))
        else:
            self.setForeground(QtGui.QBrush(QtGui.QColor(255, 0, 0)))

    def setCheckFlag(self, flag):
        if flag:
            state = QtCore.Qt.Checked
        else:
            state = QtCore.Qt.Unchecked
        self.setCheckState(state)
