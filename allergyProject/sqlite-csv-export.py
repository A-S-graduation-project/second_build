import sqlite3, os
import pandas as pd


def uexport(c, li):
    li += "\n"

    for row in c.execute('SELECT * FROM UserData'):
        for m in range(6):
            if m != 5:
                if m == 3:
                    li = li + '"' + str(row[m]) + '"' + ","
                else:
                    li = li + str(row[m]) + ","
            else:
                li = li + str(row[m])
        
        li += "\n"

    f = open("C:/Users/user/Project/second_build/allergyProject/Test1.csv", "w", encoding='utf-8')
    f.write(li)
    f.close

    return


def pexport(c, li):
    li += "\n"

    for row in c.execute('SELECT * FROM Product'):
        for m in range(7):
            if m != 6:
                if m == 2:
                    li = li + '"' + str(row[m]) + '"' + ","
                else:
                    li = li + str(row[m]) + ","
            else:
                li = li + str(row[m])
        
        li += "\n"

    f = open("C:/Users/user/Project/second_build/allergyProject/Test2.csv", "w", encoding='utf-8')
    f.write(li)
    f.close

    return


conn1 = sqlite3.connect('C:/Users/user/Project/second_build/allergyProject/userdata.sqlite3')
c1 = conn1.cursor()

conn2 = sqlite3.connect('C:/Users/user/Project/second_build/allergyProject/pro-db.sqlite3')
c2 = conn2.cursor()

user_te = "rnum,gender,older,allergy,prdlstNm,rating"
pro_te = "prdlstReportNo,prdlstNm,rawmtrl,allergy,prdkind,manufacture,image"

uexport(c1, user_te)
pexport(c2, pro_te)

c1.close()
c2.close()

print("export done")