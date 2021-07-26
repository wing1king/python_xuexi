# 需求：尝试已r打开文件，如果有异常以w打开这个文件，最终关闭关闭
try:
    f = open('test100.txt', 'r')
except Exception as e:
    f = open('text100.txt', 'w')
finally:
    f.close()
