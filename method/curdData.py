import sqlite3

from method import getConfig

def insertList(tableName,columnList,valueList):
    db = getConfig.getJson("dataDb")
    conn = sqlite3.connect(db)


# 字典
def insertDict(tableName,columnList,valueDict):
    db = getConfig.getJson("dataDb")
    conn = sqlite3.connect(db)
    sql = "insert into "+tableName+"("
    for item in columnList:
        sql=sql+item+","
    # 删除末尾的逗号
    sqlL = list(sql)
    sqlL.pop(-1)
    sql = ''.join(sqlL)
    sql1 = sql +")"
    for item in valueDict:
        sql = sql1 + " values('"+item+"','"+valueDict[item]+"')"
        cursor = conn.execute(sql)
        conn.commit()
    cursor.close()

def search(tableName,column,key):
    db = getConfig.getJson("dataDb")
    conn = sqlite3.connect(db)
    c = conn.cursor()
    sql = "select * from " + tableName + " where " + column + " like '%" + key + "%'"
    # print(sql)
    res = c.execute(sql)
    list = c.fetchall()
    return list

def isExistence(tableName,column,key):
    db = getConfig.getJson("dataDb")
    conn = sqlite3.connect(db)
    c = conn.cursor()
    sql = "select * from '" + tableName+"' where "+column+"='"+key+"'"
    res = c.execute(sql)
    f = c.fetchall()
    if len(f) == 0:
        # print("没查找")
        c.close()
        return False
    else:
        # print("查到了")
        c.close()
        return True



