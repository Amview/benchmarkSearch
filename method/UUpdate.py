from method import passmark, curdData, getConfig


def updateScore(self,tableName):
    url = getConfig.getJson(tableName)
    dict = passmark.passmarkData(url)
    columnList = ['name', 'scores']
    i = 0
    for item in dict:
        self.pbar.setValue(i)
        i = i + len(dict)/100
        boo = curdData.isExistence(tableName, 'name', item)
        if boo is False:
            dict1 = {item: dict[item]}
            curdData.insertDict(tableName, columnList, dict1)
            # print(dict1)
        else:
            print("没有新数据")