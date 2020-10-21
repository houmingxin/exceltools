"""
    读取excel
"""
import xlrd

def read_excel(excel_path, sheet_name, skip_first=True):
    """
        方法：读取excel
        参数：
            excel_path: excel的目录
            sheet_name：表单的名字
            skip_first：是否跳过首行
    """
    results = []
    # 打开excel
    datas = xlrd.open_workbook(excel_path)
    # 获取对应的表单
    table = datas.sheet_by_name(sheet_name)
    # 如果skip_first的值为True，start_row= 1> 从excel的第二行开始
    # 否则，start_row = 0 > 从excel的第一行开始
    if skip_first == True:
        start_row = 1
    else:
        start_row = 0

    # 循环读取每一行的数据
    for row in range(start_row, table.nrows):
        results.append(table.row_values(row))

    return results
#运行脚本
#安装allure-pytest第三方包：1.pip install allure-pytest -i https://pypi.tuna.tsinghua.edu.cn/simple
#运行脚本并生成结果：2.pytest --alluredir=result
#把测试结果编译成测试报告：3.allure generate result -o report --clean
#打开测试报告：4.allure open -h 127.0.0.1 -p 10086 report


if __name__ == "__main__":
    excel_path = "C:\\workhome\\test24\\pytesttest24\\data\\测谈网接口测试用例.xlsx"
    sheet_name = "登录"
    a = read_excel(excel_path, sheet_name)
    print(a)
    
    
    
