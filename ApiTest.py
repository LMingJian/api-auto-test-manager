from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
from smtplib import SMTP_SSL
from traceback import format_exc
from re import search
from requests import request


# 获取接口列表，返回 字典-正常，0-出错，None-
def api_list(file):
    # noinspection PyBroadException
    try:
        api_list_dict = {}
        sheet = file.sheet_by_name('备注')
        row = sheet.nrows  # 行
        for each in range(row - 1):
            api_numbers = int(sheet.cell_value((each + 1), 1))
            api_names = sheet.cell_value(each + 1, 2)
            api_list_dict[api_numbers] = api_names
        return api_list_dict
    except BaseException:
        return 0


# 获取接口信息，返回 字典-正常，0-出错，None-无信息
def api_info(file, number):
    # noinspection PyBroadException
    try:
        api_info_dict = {}
        sheet = file.sheet_by_index(number)
        if sheet.cell_value(1, 6) == '已废弃':
            return None
        # 获取请求参数
        api_info_dict['road'] = sheet.cell_value(2, 1)
        api_info_dict['mode'] = sheet.cell_value(3, 1)
        head = {}
        if sheet.cell_value(4, 1) != '':
            h1 = sheet.cell_value(4, 1)
            h2 = search('(\")(.*)(\")', h1).group().replace('\"', '')
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
        api_info_dict['head'] = head
        api_info_dict['query'] = query
        api_info_dict['body'] = sheet.cell_value(6, 1)
        return api_info_dict
    except BaseException:
        return 0


# 单个接口测试,使用默认参数
def api_test(api_info_dict, baseurl):
    if search(':', api_info_dict['road']) is None:
        # 不带路径参数
        url = baseurl + api_info_dict['road']
        # noinspection PyBroadException
        try:
            response = request(
                api_info_dict['mode'], url, headers=api_info_dict['head'],
                params=api_info_dict['query'], data=api_info_dict['body'])
            # noinspection PyBroadException
            try:
                responseW = response.json()
                return responseW, url
            except BaseException:
                return response.text, url
        except BaseException:
            return format_exc(), url
    else:
        # 带路径参数，将路径参数即冒号后的参数，从query中提取替换
        sc = search('(:)(.*)', api_info_dict['road'])
        url = baseurl + api_info_dict['road'].replace(sc.group(),
                                                      api_info_dict['query'][sc.group().replace(':', '')])
        # noinspection PyBroadException
        try:
            response = request(
                api_info_dict['mode'], url, headers=api_info_dict['head'],
                params=api_info_dict['query'], data=api_info_dict['body'])
            # noinspection PyBroadException
            try:
                responseW = response.json()
                return responseW, url
            except BaseException:
                return response.text, url
        except BaseException:
            return format_exc(), url


# 对列表的所有接口进行测试
def api_tests(file, apiLen, baseurl):
    resultA = {}
    resultB = {}
    infoC = {}
    for x in range(apiLen):
        t = x+1
        info = api_info(file, t)
        if info is None:
            sheet = file.sheet_by_index(t)
            u = baseurl + sheet.cell_value(2, 1)
            infoC[t] = None
            resultA[t] = u
            resultB[str(t)+'废弃'] = '此接口已废弃'
        else:
            infoC[t] = info
            respond, url = api_test(info, baseurl)
            resultA[t] = url
            # noinspection PyBroadException
            try:
                if respond['status'] == 0:
                    resultB[str(t)+'Pass'] = respond
                else:
                    resultB[str(t)+'Fail'] = respond
            except BaseException:
                resultB[str(t)+'未知错误(404)'] = respond
    with open('./RESULT.txt', 'wb') as fe:
        a = 0
        b = 0
        c = 0
        d = 0
        for key in resultB.keys():
            if '废弃' in key:
                a += 1
            elif 'Pass' in key:
                b += 1
            elif 'Fail' in key:
                c += 1
            else:
                d += 1
        fe.write(('总共测试' + str(apiLen) + '个，废弃：' + str(a) +
                  '个，Pass：' + str(b) + '个，Fail:' + str(c) + '个，未知错误(404)' +
                  str(d)+'个\n\n').encode('UTF-8'))
        for xt in range(apiLen):
            each = xt+1
            fe.write(('接口路径:'+resultA[each]+'\n').encode('UTF-8'))
            fe.write(('请求参数:'+str(infoC[each])+'\n').encode('UTF-8'))
            fe.write('响应:\n'.encode('UTF-8'))
            for key, value in resultB.items():
                if str(each) in key:
                    fe.write((str(key) + ':' + str(value)).encode('UTF-8'))
                    break
            fe.write('\n\n\n'.encode('UTF-8'))
    return 0


# 自定义参数接口测试,格式错误0，无None
def api_customTest(file, number, q, h, b, baseurl):
    sheet = file.sheet_by_index(number)
    apiInfo = dict()
    if sheet.cell_value(1, 6) == '已废弃':
        u = baseurl + sheet.cell_value(2, 1)
        return None, u
    apiInfo['road'] = sheet.cell_value(2, 1)
    apiInfo['mode'] = sheet.cell_value(3, 1)
    query = {}
    if q != '' and q != '{}':
        # noinspection PyBroadException
        try:
            r2 = q.replace('\"', '').replace('{', '').replace('}', '')
            r3 = r2.split(',')
            if r3 is None:
                query = r2.split(':')
            else:
                for each in r3:
                    b, query[b] = each.split(':')
        except BaseException:
            return 0, 0
    head = {}
    if h != '':
        # noinspection PyBroadException
        try:
            h2 = h.replace('\"', '').replace('{', '').replace('}', '')
            a, head[a] = h2.split(':')
        except BaseException:
            return 0, 0
    apiInfo['head'] = head
    apiInfo['query'] = query
    apiInfo['body'] = b
    result, url = api_test(apiInfo, baseurl)
    return result, url


# 返回 1-缺少报告文件 2-邮件发送失败 0-通过
def send_mail(receiver='', backup=''):
    # noinspection PyBroadException
    try:
        with open('RESULT.txt', 'rb') as f:
            fMsg = f.read()
    except BaseException:
        return 1
    # noinspection PyBroadException
    try:
        host_server = 'smtp.qq.com'
        sender_qq = '1312635752@qq.com'
        pwd = 'nzrhoraaqlvkhedj'
        pwd2 = 'livcaxlonftafjcg'

        mail_content = "<p>您好，这是接口测试的报告，请查收。</p> <p> 备注 </p> <p>" + backup + '</p>'
        mail_title = '接口测试报告'

        msg = MIMEMultipart()
        msg["Subject"] = Header(mail_title, 'utf-8')
        msg["From"] = sender_qq
        msg["To"] = Header(receiver, 'utf-8')

        # 邮件正文内容
        msg.attach(MIMEText(mail_content, 'html', 'utf-8'))

        # 附件1
        att1 = MIMEApplication(fMsg)
        att1["Content-Type"] = 'application/octet-stream'
        att1["Content-Disposition"] = 'attachment; filename="RESULT.txt"'
        msg.attach(att1)

        # ssl登录
        smtp = SMTP_SSL(host_server)
        # set_debuglevel()是用来调试的。参数值为1表示开启调试模式，参数值为0关闭调试模式
        smtp.set_debuglevel(0)
        smtp.ehlo(host_server)
        smtp.login(sender_qq, pwd)

        smtp.sendmail(sender_qq, receiver, msg.as_string())
        smtp.quit()
        return 0
    except BaseException:
        return 2
