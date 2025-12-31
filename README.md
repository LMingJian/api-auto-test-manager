# PyQt5 设计的接口自动测试软件

@LM 2021-01-15 至 2021-04-28

## 介绍

毕业设计课题，使用 PyQt5 设计的一个带 GUI 的接口自动测试软件。

**在此做存档作用，很大概率还是能用的，但是当时忘记写文档，导致不知道怎么用了**。

## 需要额外安装的库

```
pip install xlrd==1.2.0 PyQt5 PyQt5-tools requests
```

## 执行

执行`Main.py`文件

## 文件介绍

`ApiTest.py`: 接口测试主体程序

`ApiTest.py`: 接口测试命令行主体程序

`Main.py`: 软件入口程序，GUI交互逻辑程序

`UI.py`: GUI界面布局程序

## 打包

```cmd
pyinstaller -F -w main.py
```

## 图示

![alt text](<images/屏幕截图 2021-02-24 161146.jpg>)

![alt text](<images/屏幕截图 2021-02-24 161202.jpg>)

![alt text](<images/屏幕截图 2021-02-24 161324.jpg>)

![alt text](<images/屏幕截图 2021-02-24 161348.jpg>)

![alt text](<images/屏幕截图 2021-02-24 161358.jpg>)
