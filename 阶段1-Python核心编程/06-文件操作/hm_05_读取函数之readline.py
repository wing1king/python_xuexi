f = open('test.txt', 'r')

# readline: 每次读取一行
con = f.readline()
print(con)

con = f.readline()
print(con)

con = f.readline()
print(con)

f.close()