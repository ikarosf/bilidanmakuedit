# -*- coding: utf-8 -*-

import os
import pickle

recent_file = None

recent_file_name = None

recent_file_dir = None

danmu_data = None

data_saved = True

keep_data = {}

row_count = 20

recent_page = 1

recent_row = 0


def get_value(key, defValue=None):
    """ 获得一个全局变量,不存在则返回默认值 """
    try:
        str1 = 'global ' + key
        exec(str1)
        val = eval(key)
        return val
    except KeyError:
        return defValue


def get_file_dir():
    return recent_file_dir


def get_danmu_text(num, defValue=None):
    try:
        name_text_node = danmu_data[num].childNodes[0]
        return name_text_node.data
    except IndexError:
        return defValue


def has_danmu_text(num):
    try:
        danmu_data[num].childNodes[0]
        return True
    except IndexError:
        return False


def get_recent_page_and_row():
    if recent_file is None:
        return None, None
    else:
        return recent_page, recent_row


def edit_recent_page_and_row(page, row):
    global recent_page, recent_row, pageinfoLabel
    if recent_file is None:
        recent_page = 1
        recent_row = 0
    else:
        recent_page = page
        recent_row = row
        num = int(len(danmu_data) / row_count) + 1
        pageinfoLabel.setText("%d/%d" % (page, num))


def set_tableWidget_text_and_index(i, text, index):
    global tableWidget
    item = tableWidget.item(i, 0)
    item.setText(text)
    tableWidget.verticalHeaderItem(i).setText(str(index))
    item.setCheckFlag(get_danmu_whether_del(index))
    item.index = index


def keep_data_init():
    global keep_data, danmu_data, recent_file_name
    keep_data = keep_data
    damu_len = len(danmu_data)
    keep_data = {
        'user_setting': {
            'file_name': recent_file_name,
            'row_count': 20,
            'recent_row': 0
        },
        'danmu_whether_del': dict.fromkeys(range(damu_len), False)
    }


def keep_data_store():
    global keep_data, recent_file_name, recent_file_dir, data_saved
    (filename, extension) = os.path.splitext(recent_file_name)
    filename = filename + '.dmke'
    file_path = os.path.join(recent_file_dir, filename)

    get_user_setting()['row_count'] = row_count
    get_user_setting()['recent_row'] = recent_row

    with open(file_path, 'wb') as f:
        pickle.dump(keep_data, f)
        data_saved = True


def keep_data_read():
    global keep_data, recent_file_name, recent_file_dir,row_count,recent_row
    (filename, extension) = os.path.splitext(recent_file_name)
    filename = filename + '.dmke'
    file_path = os.path.join(recent_file_dir, filename)
    try:
        with open(file_path, 'rb') as f:
            read_data = pickle.load(f)
    except FileNotFoundError:
        row_count = 20
        recent_row = 0
        return False
    if read_data['user_setting']['file_name'] != recent_file_name:
        row_count = 20
        recent_row = 0
        return False
    keep_data = read_data
    del read_data
    row_count = get_user_setting()['row_count']
    recent_row = get_user_setting()['recent_row']
    return True


def edit_danmu_whether_del(index, flag):
    global keep_data, data_saved
    keep_data['danmu_whether_del'][index] = flag
    data_saved = False


def get_danmu_whether_del(index):
    global keep_data
    try:
        return keep_data['danmu_whether_del'][index]
    except KeyError:
        return False


def get_user_setting():
    return keep_data['user_setting']
