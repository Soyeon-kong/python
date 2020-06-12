import pymysql
from db.memberDAO import *

dao = Dao()

file1 = open('member.txt','r')
member = file1.read().splitlines()
for m in member:
    data = m.split(' ')
    dao.insert(tuple(data))

file2 = open('member2.txt', 'w')
rows = dao.select()
for member in rows:
    for data in member:
        file2.write(data+' ')
    file2.write('\n')
