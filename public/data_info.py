import xlrd,sys
import os
from config.basic_config import ConfigInit


PATH = os.path.join(os.path.abspath(os.path.join(os.getcwd(), "..")), 'data\\test_data', ConfigInit.data_file_name)

# print(PATH)
def get_excel_dict(path, index=0):
    paralList=[]
    workbook=xlrd.open_workbook(path) # 打开文件
    sheet=workbook.sheets()[index]  # sheet索引从0开始
    firstRowDataList=sheet.row_values(0)#第一行数据
    #print firstRowDataList
    for rownum in range(1, sheet.nrows):#循环每一行数据
        list = sheet.row_values(rownum)
        #print type(list[3])
        dict={}
        dictTestCaseName={}

        for caseData in list:
            dict[firstRowDataList[list.index(caseData)]] =caseData #每一行数据与第一行数据对应转为字典
            #json.dumps(json.loads(caseData), ensure_ascii=False)
        # print(list)
        dictTestCaseName[list[0]]=dict#转为字典后与用例名字对应转为字典
        paralList.append(dictTestCaseName)#将处理后的数据放入列表里
    return (paralList)


def get_test_case_data(filename,testCaseName):
    testData = get_excel_dict(filename)
    getTestCaseDataList = []
    for data in testData:
        if (list(data.keys())[0]) == testCaseName:
            getTestCaseDataList.append(data[testCaseName])
    return getTestCaseDataList

a = get_test_case_data(PATH, 'login')
print(a)

