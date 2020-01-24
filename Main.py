# -*- coding: utf-8 -*-

import sys, os

# import PySide2
# dirname = os.path.dirname(PySide2.__file__)
# plugin_path = os.path.join(dirname, 'plugins', 'platforms')
# os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path
# print(plugin_path)

# if hasattr(sys,'frozen'):
#     os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']

from PySide2.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide2 import QtGui
from MainWindow import *
import global_env
import action_def
import logging
import resource_rc

# 打包exe文件用，编程时请注释
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = os.path.join('.', 'plugins')


class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        self.setAcceptDrops(True)
        self.setWindowIcon(QtGui.QIcon(':/file_edit1.ico'))

    def closeEvent(self, event):
        if not global_env.data_saved:
            reply = QtWidgets.QMessageBox.question(self,
                                                   '将关闭程序',
                                                   "是否保存？",
                                                   QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No | QtWidgets.QMessageBox.Cancel,
                                                   QtWidgets.QMessageBox.Cancel)
            if reply == QtWidgets.QMessageBox.Yes:
                global_env.keep_data_store()
                event.accept()
            elif reply == QtWidgets.QMessageBox.No:
                event.accept()
            else:
                event.ignore()
        else:
            event.accept()

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls:
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls:
            try:
                event.setDropAction(QtCore.Qt.CopyAction)
            except Exception as e:
                print(e)
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        try:
            if event.mimeData().hasUrls:
                event.setDropAction(QtCore.Qt.CopyAction)
                event.accept()
                for url in event.mimeData().urls():
                    link = str(url.toLocalFile())
                    break
                action_def.sc_load_file(link)
            else:
                event.ignore()
        except Exception as e:
            print(e)


if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s',
                        datefmt="%Y/%d/%m %H:%M:%S",
                        level=logging.CRITICAL)
    app = QApplication(sys.argv)
    myWin = MyWindow()
    global_env.myWin = myWin
    myWin.show()
    sys.exit(app.exec_())
