from UI import *
from ApiTest import *
from sys import argv
from sys import exit
from xlrd import open_workbook
from threading import Thread
from time import sleep


filename = None
file = None
flag = 0
baseurl = 'http://192.168.1.243'
apiLen = 0


# 主窗口
class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)


# 待测接口编号输入窗口
class MyDialog(QDialog, Ui_ApiNumberInput):
    def __init__(self, parent=None):
        super(MyDialog, self).__init__(parent)
        self.setupUi(self)


# 自定义信息设置窗口
class MyDialog2(QDialog, Ui_CustomOptionInput):
    def __init__(self, parent=None):
        super(MyDialog2, self).__init__(parent)
        self.setupUi(self)


# 邮件发送信息设置窗口
class MyDialog3(QDialog, Ui_MailOptionInput):
    def __init__(self, parent=None):
        super(MyDialog3, self).__init__(parent)
        self.setupUi(self)


# 待测IP设置窗口
class MyDialog4(QDialog, Ui_TestIPInput):
    def __init__(self, parent=None):
        super(MyDialog4, self).__init__(parent)
        self.setupUi(self)


# 系统繁忙提示窗口
class MyDialog5(QDialog, Ui_WaitingInterface):
    def __init__(self, parent=None):
        super(MyDialog5, self).__init__(parent)
        self.setupUi(self)


# 多线程类
class MyThread(Thread):
    result1 = None
    result2 = None

    def __init__(self, func, args=()):
        super(MyThread, self).__init__()
        self.func = func
        self.args = args

    def run(self):
        self.result1, self.result2 = self.func(*self.args)
        # 在执行函数的同时，把结果赋值给result,
        # 然后通过get_result函数获取返回的结果

    def get_result(self):
        # noinspection PyBroadException
        try:
            return self.result1, self.result2
        except Exception:
            return None


# 多线程执行函数
def Mss(info, window):
    result, furl = api_test(info, baseurl)
    sleep(0.5)
    # 等待，否则由于子进程过快，主进程未开启进度条，而执行进度条关闭命令导致矛盾
    window.close()
    return result, furl


def Mss2(sign, window):
    api_tests(file, apiLen, baseurl)
    sleep(0.5)
    window.close()
    return sign, 0


def Mss3(number, query, head, body, window):
    result, url = api_customTest(file, number, query, head, body, baseurl)
    sleep(0.5)
    window.close()
    return result, url


def Mss4(receiver, content, window):
    res = send_mail(receiver, content)
    if res == 1:
        sleep(0.5)
        window.close()
        # 错误码，缺少报告文件
        return 1, 0
    elif res == 2:
        sleep(0.5)
        window.close()
        # 错误码，邮件发送失败
        return 1, 1
    else:
        sleep(0.5)
        window.close()
        return 0, 0


# 字符串转换数字
def clickNum(num):
    # noinspection PyBroadException
    try:
        return int(num)
    except BaseException:
        return 0


# start按钮逻辑设置
def click_start():
    myWin.Right.clear()
    global file
    # 判断文件和路径是否已经配置
    if file is not None and baseurl is not None:
        # 模式配置
        if flag == 0:
            QMessageBox.warning(myWin, 'ApiTest', '请先选择模式')
        elif flag == 1:
            myDia = MyDialog(myWin)
            if myDia.exec_():
                print('执行函数1')

                number = myDia.lineEdit.text()
                number = clickNum(number)
                if 0 < number <= apiLen:
                    info = api_info(file, int(number))
                    if info == 0:
                        QMessageBox.warning(myWin, 'ApiTest', '无法读取信息，请检查文件')
                    elif info is None:
                        QMessageBox.warning(myWin, 'ApiTest', '此接口已废弃')
                    else:
                        myDia5 = MyDialog5()
                        myDia5.setWindowFlags(Qt.FramelessWindowHint)
                        t1 = MyThread(Mss, args=(info, myDia5))
                        t1.setDaemon(True)
                        t1.start()
                        if myDia5.exec_() == 0:
                            # noinspection PyBroadException
                            try:
                                result, furl = t1.get_result()
                                # 线程关闭了，但数据作为属性留在线程类里
                                myWin.Right.setText('地址：' + '\n' + furl + '\n' +
                                                    '参数：' + '\n' + str(info) + '\n' +
                                                    '结果：' + '\n' + str(result))
                            except BaseException:
                                QMessageBox.warning(myWin, 'ApiTest', '请重试，程序出错')
                else:
                    QMessageBox.warning(myWin, 'ApiTest', '请输入正确的编号')
                ''''''
            else:
                print('无执行1')
        elif flag == 2:
            t = QMessageBox.information(myWin, 'ApiTest', '将对全部接口进行测试，请确认',
                                        QMessageBox.Ok | QMessageBox.Cancel, QMessageBox.Ok)
            if t == QMessageBox.Ok:
                print('执行函数2')

                myDia5a = MyDialog5()
                myDia5a.setWindowFlags(Qt.FramelessWindowHint)
                t2 = MyThread(Mss2, args=(flag, myDia5a))
                t2.setDaemon(True)
                t2.start()
                if myDia5a.exec_() == 0:
                    myWin.Right.setText('请到软件目录下查看结果文件【RESULT.txt】')
                ''''''
            else:
                print('无执行2')
        elif flag == 3:
            myDia2 = MyDialog2(myWin)
            if myDia2.exec_():
                print('执行函数3')

                query = myDia2.lineEdit.text()
                head = myDia2.lineEdit_2.text()
                body = myDia2.lineEdit_3.text()
                number = myDia2.lineEdit_4.text()
                number = clickNum(number)
                if 0 < number <= apiLen:
                    myDia5b = MyDialog5()
                    myDia5b.setWindowFlags(Qt.FramelessWindowHint)
                    t1 = MyThread(Mss3, args=(number, query, head, body, myDia5b))
                    t1.setDaemon(True)
                    t1.start()
                    if myDia5b.exec_() == 0:
                        # noinspection PyBroadException
                        try:
                            result, furl = t1.get_result()
                            # 线程关闭了，但数据作为属性留在线程类里
                            if result == 0:
                                myWin.Right.setText('请按JSON格式输入数据！')
                            elif result is None:
                                myWin.Right.setText('地址：' + '\n' + furl + '\n' +
                                                    '结果：' + '\n' + '此接口已废弃')
                            else:
                                s = '请求参数：' + query + '\n请求头：' + head + '\n请求体：' + body
                                myWin.Right.setText('地址：' + '\n' + furl + '\n' +
                                                    '参数：' + '\n' + s + '\n' +
                                                    '结果：' + '\n' + str(result))
                        except BaseException:
                            QMessageBox.warning(myWin, 'ApiTest', '请重试，程序出错')
                else:
                    QMessageBox.warning(myWin, 'ApiTest', '请输入正确的编号')
                ''''''
            else:
                print('无执行3')
        elif flag == 4:
            myDia3 = MyDialog3(myWin)
            if myDia3.exec_():
                print('执行函数4')

                sendTo = myDia3.lineEdit.text()
                if sendTo == '' or sendTo is None:
                    QMessageBox.warning(myWin, 'ApiTest', '请先输入邮箱地址')
                    return 0
                elif '@' not in sendTo:
                    QMessageBox.warning(myWin, 'ApiTest', '请先输入正确的邮箱地址')
                    return 0
                what = myDia3.textEdit.toPlainText()
                myDia5c = MyDialog5()
                myDia5c.setWindowFlags(Qt.FramelessWindowHint)
                t1 = MyThread(Mss4, args=(sendTo, what, myDia5c))
                t1.setDaemon(True)
                t1.start()
                if myDia5c.exec_() == 0:
                    x, y = t1.get_result()
                    if x == 1 and y == 0:
                        myWin.Right.setText('查找不到报告文件，请先对全部接口进行测试')
                    elif x == 0 and y == 1:
                        myWin.Right.setText('邮件发送失败，请重试')
                    else:
                        myWin.Right.setText('邮件已成功发送')
                '''有缺陷，对邮箱地址验证不严格'''
            else:
                print('无执行4')
    else:
        QMessageBox.warning(myWin, 'ApiTest', '请先完成配置')
    return 0


# 文件打开，文件路径配置
def openfile():
    global filename
    global file, apiLen
    openfilename = QFileDialog.getOpenFileName(myWin, directory='.', filter='Excel files(*.xlsx ; *.xls)')
    if openfilename[0] != '':
        myWin.Left.clear()
        myWin.Right.clear()
        filename = openfilename[0]
        print('打开文件：' + filename)
        file = open_workbook(filename)
        apiDict = api_list(file)
        if apiDict != 0:
            myWin.Road.setText(filename)
            apiLen = len(apiDict)
            for key, value in apiDict.items():
                myWin.Left.append(str(key) + value)
        else:
            myWin.Road.clear()
            QMessageBox.warning(myWin, 'ApiTest', '请确保打开模板文件')
    return 0


# 模式选择按钮设置标志
def which():
    global flag
    if myWin.A1.isChecked():
        flag = 1
        print('模式'+str(flag))
    elif myWin.A2.isChecked():
        flag = 2
        print('模式'+str(flag))
    elif myWin.A3.isChecked():
        flag = 3
        print('模式'+str(flag))
    elif myWin.A4.isChecked():
        flag = 4
        print('模式'+str(flag))


# 路径设置
def set_url():
    global baseurl
    myDia4 = MyDialog4(myWin)
    if myDia4.exec_():
        url = myDia4.lineEdit.text()
        if url == '...':
            return 0
        temp = url.split('.')
        for each in temp:
            if int(each) > 255:
                QMessageBox.warning(myWin, 'ApiTest', '这不是一个IP地址')
                return 0
        baseurl = 'http://' + url
        myWin.Url.setText(baseurl)
    return 0


'''
# pyinstaller -F -w main.py # 无命令行单exe文件打包
# -F 表示生成单个可执行文件 -w 表示去掉控制台窗口 -i 表示可执行文件的图标
apps = QApplication(argv)
myWin = MyWindow()
myWin.show()

myWin.Url.setText(baseurl)

myWin.OK.clicked.connect(click_start)
myWin.Open.clicked.connect(openfile)
myWin.A1.clicked.connect(which)
myWin.A2.clicked.connect(which)
myWin.A3.clicked.connect(which)
myWin.A4.clicked.connect(which)
myWin.SetUrl.clicked.connect(set_url)

exit(apps.exec_())
'''
if __name__ == '__main__':
    apps = QApplication(argv)
    myWin = MyWindow()
    myWin.show()

    myWin.Url.setText(baseurl)

    myWin.OK.clicked.connect(click_start)
    myWin.Open.clicked.connect(openfile)
    myWin.A1.clicked.connect(which)
    myWin.A2.clicked.connect(which)
    myWin.A3.clicked.connect(which)
    myWin.A4.clicked.connect(which)
    myWin.SetUrl.clicked.connect(set_url)

    exit(apps.exec_())
