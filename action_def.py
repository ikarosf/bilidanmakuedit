# -*- coding: utf-8 -*-
#frx
from PySide2 import QtCore, QtGui, QtWidgets
import global_env
import widgets_creat
from xml.dom import minidom
import os
import logging


def test():
    table_row_updata()


def sc_load_file(sc_file):
    load_file(sc_file)


def window_load_file():
    fdir = global_env.get_file_dir()
    fileName_choose, filetype = QtWidgets.QFileDialog.getOpenFileName(global_env.myWin,
                                                                      "选取弹幕文件",
                                                                      fdir,  # 起始路径
                                                                      "XML Files (*.xml)")  # 设置文件扩展名过滤,用双分号间隔

    if fileName_choose == "":
        logging.debug("取消选择")
        return

    load_file(fileName_choose)


def load_file(fileName_choose):
    logging.debug(fileName_choose)

    if not fileName_choose.lower().endswith(".xml"):
        QtWidgets.QMessageBox.critical(global_env.myWin, '打开文件错误', "不是xml文件", QtWidgets.QMessageBox.Ok)
        return

    dirname, filename = os.path.split(fileName_choose)

    domTree = minidom.parse(fileName_choose)
    rootNode = domTree.documentElement
    danmu = rootNode.getElementsByTagName("d")
    logging.debug(len(danmu))

    if len(danmu) < 1:
        QtWidgets.QMessageBox.critical(global_env.myWin, '打开文件错误', "一条弹幕都没有哦", QtWidgets.QMessageBox.Ok)
        return

    global_env.recent_file = fileName_choose
    global_env.recent_file_dir = dirname
    global_env.recent_file_name = filename
    global_env.recent_file_rootnode = rootNode
    global_env.danmu_data = danmu

    if not global_env.keep_data_read():
        # QtWidgets.QMessageBox.information(global_env.myWin, '缓存未找到', "新的弹幕文件或缓存文件丢失\n》》》新创建缓存",
        #                                   QtWidgets.QMessageBox.Ok)
        global_env.keep_data_init()
    else:
        global_env.keep_data_read()

    global_env.data_saved = True

    table_updata(global_env.recent_row)


def table_init():
    row_count = global_env.row_count
    for i in range(0, row_count):
        item = widgets_creat.danmu_tableWidget()
        global_env.tableWidget.setItem(i, 0, item)

        item = QtWidgets.QTableWidgetItem()
        global_env.tableWidget.setVerticalHeaderItem(i, item)


def table_updata(start_num=None):
    row_count = global_env.row_count

    if start_num is None:
        start_num = global_env.recent_row

    if start_num < 0:
        QtWidgets.QMessageBox.critical(global_env.myWin, '跳页错误', "页码为负", QtWidgets.QMessageBox.Ok)
        return

    if not global_env.has_danmu_text(start_num):
        QtWidgets.QMessageBox.critical(global_env.myWin, '跳页错误', "页码过大", QtWidgets.QMessageBox.Ok)
        return

    recent_page = int(start_num / row_count) + 1
    for i in range(0, row_count):
        index = start_num + i
        str1 = global_env.get_danmu_text(index)
        if str1 is not None:
            global_env.set_tableWidget_text_and_index(i, str1, index)
        else:
            table_row_clean(i)

    global_env.edit_recent_page_and_row(recent_page, start_num)


def table_updata_by_page(start_page=None):
    if start_page is None:
        table_updata()
        return
    row_count = global_env.row_count
    start_num = int((start_page - 1) * row_count)
    table_updata(start_num)


def table_row_clean(row_num):
    # noinspection PyBroadException
    try:
        global_env.set_tableWidget_text_and_index(row_num, '', '')
    except:
        pass


def table_clean():
    for i in range(0, global_env.row_count):
        # noinspection PyBroadException
        try:
            global_env.set_tableWidget_text_and_index(i, '', '')
        except:
            pass


# def table_del():
#     for i in range(0, global_env.row_count):
#         # noinspection PyBroadException
#         try:
#             global_env.tableWidget.setItem(i, 0, None)
#         except:
#             pass


def table_row_updata(num=None):
    if num is None:
        row_count = global_env.row_count
        global_env.tableWidget.setRowCount(row_count)
    else:
        global_env.row_count = num
        global_env.tableWidget.setRowCount(num)


def edit_rowcount():
    num, ok = QtWidgets.QInputDialog.getInt(global_env.myWin, '修改显示弹幕行数', '输入数字',
                                            value=global_env.row_count, minValue=10, maxValue=30)
    if ok and num:
        table_row_updata(num)
    else:
        return
    table_init()
    if global_env.recent_file is not None:
        table_updata()


def tableWidgetItemClick(item):
    item.getclick()


def jump_page():
    if global_env.recent_file is None:
        QtWidgets.QMessageBox.critical(global_env.myWin, '跳页错误', "还没有打开弹幕文件", QtWidgets.QMessageBox.Ok)
        return
    maxpage = int(len(global_env.danmu_data) / global_env.row_count) + 1
    num, ok = QtWidgets.QInputDialog.getInt(global_env.myWin, '跳页', '输入数字',
                                            value=global_env.recent_row, minValue=1, maxValue=maxpage)
    if ok and num:
        table_updata_by_page(num)
    else:
        return


def previous_page():
    page, row = global_env.get_recent_page_and_row()
    if page is None:
        QtWidgets.QMessageBox.critical(global_env.myWin, '跳页错误', "还没有打开弹幕文件", QtWidgets.QMessageBox.Ok)
        return
    num = page - 1
    table_updata_by_page(num)


def next_page():
    page, row = global_env.get_recent_page_and_row()
    if page is None:
        QtWidgets.QMessageBox.critical(global_env.myWin, '跳页错误', "还没有打开弹幕文件", QtWidgets.QMessageBox.Ok)
        return
    num = page + 1
    table_updata_by_page(num)


def save_data():
    if global_env.recent_file is None:
        QtWidgets.QMessageBox.critical(global_env.myWin, '跳页错误', "还没有打开弹幕文件", QtWidgets.QMessageBox.Ok)
        return
    global_env.keep_data_store()
    QtWidgets.QMessageBox.information(global_env.myWin, '提示', "已保存", QtWidgets.QMessageBox.Ok)


def output_file():
    if global_env.recent_file is None:
        QtWidgets.QMessageBox.critical(global_env.myWin, '输出错误', "还没有打开弹幕文件", QtWidgets.QMessageBox.Ok)
        return
    file_url = os.path.join(global_env.recent_file_dir, global_env.recent_file_name[0:-4]) + '_dmke.xml'
    fileName_choose, filetype = QtWidgets.QFileDialog.getSaveFileName(global_env.myWin,
                                                                      "弹幕文件输出",
                                                                      file_url,  # 起始路径
                                                                      "Text Files (*.xml)")  # 设置文件扩展名过滤,用双分号间隔
    logging.debug(fileName_choose)
    if fileName_choose == "":
        logging.debug("取消选择")
        return

    danmu = global_env.danmu_data
    dom = minidom.Document()
    root_node = dom.createElement('i')
    dom.appendChild(root_node)

    for i in ("chatid", "chatserver", "mission", "maxlimit", "state", "real_name", "source"):
        # noinspection PyBroadException
        try:
            nnode = global_env.recent_file_rootnode.getElementsByTagName(i)[0]
            root_node.appendChild(nnode)
        except:
            pass

    for i in range(0, len(danmu)):
        if not global_env.get_danmu_whether_del(i):
            root_node.appendChild(danmu[i])

    with open(fileName_choose, 'w', encoding='UTF-8') as fh:
        dom.writexml(fh, indent='', addindent='\t', newl='\n', encoding='UTF-8')
        QtWidgets.QMessageBox.information(global_env.myWin, '提示', "输出弹幕文件成功", QtWidgets.QMessageBox.Ok)


def reverse_election():
    row_count = global_env.row_count

    for i in range(0, row_count):
        global_env.tableWidget.item(i, 0).getclick()


def about_text():
    about_str = '''
    作者:ikarosf    
    v0.1
    项目地址: https://github.com/ikarosf/bilidanmakuedit
    '''
    QtWidgets.QMessageBox.about(global_env.myWin, "关于", about_str)