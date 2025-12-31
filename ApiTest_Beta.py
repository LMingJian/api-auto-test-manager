import requests
import xlrd
import re
"""
测试使用的控制台终端版本
"""
baseurl = 'http://192.168.1.243'
file_name = None


# 获取接口字典
def Choice_Api():
    api = {}
    api_number = None
    file = xlrd.open_workbook(file_name)
    sheet = file.sheet_by_name('备注')
    row = sheet.nrows  # 行
    for each in range(row-1):
        api_numbers = int(sheet.cell_value((each+1), 1))
        api_names = sheet.cell_value(each+1, 2)
        api[api_numbers] = api_names
    # 选择接口编号
    while True:
        # noinspection PyBroadException
        try:
            flag = input('请选择需要测试的API(按L打印接口列表,P退出)：')
            if flag == 'L' or flag == 'l':
                for each in api:
                    print(each, end='')
                    print('  '+api[each])
                continue
            elif flag == 'p' or flag == 'P':
                return 0
            else:
                api_number = int(flag)
                if api_number in api:
                    print(str(api_number)+'  '+api[api_number])
                    break
                else:
                    print('无此接口编号')
        except BaseException:
            print('错误输入')
    return api_number


# 单个接口测试
def Api_Test_One():
    api_number = Choice_Api()
    if api_number == 0:
        return 0
    file = xlrd.open_workbook(file_name)
    sheet = file.sheet_by_index(api_number)
    if sheet.cell_value(1, 6) == '已废弃':
        print('接口已废弃')
        return 0
    # 获取请求参数
    road = sheet.cell_value(2, 1)
    mode = sheet.cell_value(3, 1)
    head = {}
    if sheet.cell_value(4, 1) != '':
        h1 = sheet.cell_value(4, 1)
        h2 = re.search('(\")(.*)(\")', h1).group().replace('\"', '')
        a, head[a] = h2.split(':')
    query = {}
    if sheet.cell_value(5, 1) != '':
        r1 = sheet.cell_value(5, 1)
        r2 = r1.replace('\"', '').replace('{', '').replace('}', '')
        r3 = r2.split(',')
        if r3 is None:
            query = r2.split(':')
        else:
            for each in r3:
                b, query[b] = each.split(':')
    body = sheet.cell_value(6, 1)
    # 检测请求的路径是否带路径参数
    if re.search(':', road) is None:
        # 不带路径参数
        url = baseurl+road
        # noinspection PyBroadException
        try: 
            response = requests.request(mode, url, headers=head, params=query, data=body).json()
            print(response)  
        except BaseException:
            print('参数错误或404')
    else:
        # 带路径参数，将路径参数即冒号后的参数，从query中提取替换
        sc = re.search('(:)(.*)', road)
        url = baseurl+road.replace(sc.group(), query[sc.group().replace(':', '')])
        # noinspection PyBroadException
        try:
            response = requests.request(mode, url, headers=head, params=query, data=body).json()
            print(response) 
        except BaseException:
            print('参数错误或404')
    return 0


# 测试全部接口
def Api_Test_ALL():
    file = xlrd.open_workbook(file_name)
    lent = file.sheet_by_index(0).nrows
    for x in range(lent-1):
        sheet = file.sheet_by_index(x+1)
        # 获取请求参数
        road = sheet.cell_value(2, 1)
        mode = sheet.cell_value(3, 1)
        if sheet.cell_value(1, 6) == '已废弃':
            print(road+':已废弃')
            continue
        head = {}
        if sheet.cell_value(4, 1) != '':
            h1 = sheet.cell_value(4, 1)
            h2 = re.search('(\")(.*)(\")', h1).group().replace('\"', '')
            a, head[a] = h2.split(':')
        query = {}
        if sheet.cell_value(5, 1) != '':
            r1 = sheet.cell_value(5, 1)
            r2 = r1.replace('\"', '').replace('{', '').replace('}', '')
            r3 = r2.split(',')
            if r3 is None:
                query = r2.split(':')
            else:
                for each in r3:
                    b, query[b] = each.split(':')
        body = sheet.cell_value(6, 1)
        # 检测请求的路径是否带路径参数
        if re.search(':', road) is None:
            url = baseurl+road
            # noinspection PyBroadException
            try: 
                response = requests.request(mode, url, headers=head, params=query, data=body).json()
                T = (response['status'] == 0)
                if T:
                    print(str(x+1)+'   '+road+':     Pass     '+str(response['status']))
                    print('\n', end='')
                else:
                    print(str(x+1)+'   '+road+':     NoPass     '+str(response['status']))
                    print(response)
                    print('\n', end='')
            except BaseException:
                print(str(x+1)+'   '+road+':     error        404')
                print('\n', end='')
        else:
            sc = re.search('(:)(.*)', road)
            url = baseurl+road.replace(sc.group(), query[sc.group().replace(':', '')])
            # noinspection PyBroadException
            try:
                response = requests.request(mode, url, headers=head, params=query, data=body).json()
                T = (response['status'] == 0)
                if T:
                    print(str(x+1)+'   '+road+':     Pass     '+str(response['status']))
                    print('\n', end='')
                else:
                    print(str(x+1)+'   '+road+':     NoPass     '+str(response['status']))
                    print(response)
                    print('\n', end='')
            except BaseException:
                print(str(x+1)+'   '+road+':     error        404')
                print('\n', end='')
    return 0


# 自定义参数请求
def Special_Test():
    Api = Choice_Api()
    if Api == 0:
        return 0
    file = xlrd.open_workbook(file_name)
    sheet = file.sheet_by_index(Api)
    # 获取路径和请求方式
    road = sheet.cell_value(2, 1)
    mode = sheet.cell_value(3, 1)
    # 获取请求参数以及处理
    while True:
        q = input('请输入请求参数query：')
        query = {}
        if q != '':
            # noinspection PyBroadException
            try:
                r2 = q.replace('\"', '').replace('{', '').replace('}', '')
                r3 = r2.split(',')
                if r3 is None:
                    b, query[b] = r2.split(':')
                else:
                    for each in r3:
                        b, query[b] = each.split(':')
                    break
            except BaseException:
                print('请按JSON格式输入数据')
    # 获取请求头参数以及处理
    while True:
        h = input('请输入请求头参数headers：')
        head = {}
        if h != '':
            # noinspection PyBroadException
            try:
                h2 = h.replace('\"', '').replace('{', '').replace('}', '')
                a, head[a] = h2.split(':')
                break
            except BaseException:
                print('请按JSON格式输入数据')
    # 获取请求体参数
    body = input('请输入请求体参数body：')
    # 是否存在路径参数
    if re.search(':', road) is None:
        url = baseurl+road
        # noinspection PyBroadException
        try: 
            response = requests.request(mode, url, headers=head, params=query, data=body).json()
            print(response)
        except BaseException:
            print('参数错误或404')
    else:
        sc = re.search('(:)(.*)', road)
        url = baseurl+road.replace(sc.group(), query[sc.group().replace(':', '')])
        # noinspection PyBroadException
        try:
            response = requests.request(mode, url, headers=head, params=query, data=body).json()
            print(response) 
        except BaseException:
            print('参数错误或404')
    return 0
            

def Menu():
    while True:
        print('请选择功能,p退出\n')
        print('1.单个接口测试(默认参数)\n')
        print('2.所有接口测试(默认参数)\n')
        print('3.单个接口测试(特殊参数)\n')
        t = input('请输入：')
        if t == '1':
            Api_Test_One()
        elif t == '2':
            Api_Test_ALL()
        elif t == '3':
            Special_Test()
        elif t == '4':
            Choice_Api()
        elif t == 'p':
            break
        else:
            print('错误输入')


if __name__ == '__main__':
    Menu()
