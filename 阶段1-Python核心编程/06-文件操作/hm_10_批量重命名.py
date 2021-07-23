# 需求1： 把code文件所有的文件重命名 python_xxxx
# 需求2： 删除python_ 重命名： 1.构造条件的数据 2.书写if

import os

# 构造条件的数据
flag = 2

# 1. 找到所有文件： 获取code文件夹的目录列表 -- listdir()
file_list = os.listdir()

# 2. 构造名字
for i in file_list:
    if flag == 1:
        # new_name = 'python_' + 原文件i
        new_name = 'py_' + i
        print(new_name)
    elif flag == 2:
        # 删除前缀
        num = len('hm_')
        new_name = i[num:]
    # 3. 重命名
    os.rename(i, new_name)