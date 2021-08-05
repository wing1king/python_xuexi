# 方法一
"""
1. 导入
import 报名.模块名
2. 调用功能
包名.模块名.功能
"""

# 导入mypackage包下的模块1，使用这个模块内的info__print1函数
# import mypackage.my_module1
# mypackage.my_module1.info_print1()


# 方法二： 注意设置__init__.py 文件里面的all列表，添加的是允许要入的模块
"""
from 包名 import *
模块名.目标
"""

from mypackage import *
my_module1.info_print1()