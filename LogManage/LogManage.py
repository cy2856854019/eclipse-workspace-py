# !/usr/bin/python2.7
# -*- coding: utf-8 -*-

import os, datetime, sys

# 字节bytes转化kb\m\g
def formatSize(bytes):
    try:
#         bytes = float(bytes)
        kb = bytes // 1024
    except:
        print("传入的字节格式不对")
        return "Error"

    if kb >= 1024:
        M = kb // 1024
        return "%d" % (M)
    else:
        return 0


# 获取文件大小
def getDocSize(path):
    try:
        size = os.path.getsize(path)
        return formatSize(size)
    except Exception as err:
        print(err)
#文件重命名        
def rename(path):
    newpath = path.split('.')[0]
    os.rename(path, newpath + '_' + datetime.datetime.now().strftime('%Y-%m-%d') + '.log')

def splitLog(path):
    size = int(getDocSize(path))
    if size >= 1024:
        rename(path)
        

if __name__ == '__main__':
    print len(sys.argv)
    if len(sys.argv) != 2:
        print('参数有误')
        print('格式如: python LogManage.py 1.log')
        sys.exit()
#     path = '/home/cy/eclipse-workspace-py/51job/cookie1.py'
    path = sys.argv[1]
    print(path)
    size = getDocSize(path)
    print(size)
    splitLog(path)
    
    