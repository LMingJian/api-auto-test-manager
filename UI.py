from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(860, 551)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(860, 551))
        MainWindow.setMaximumSize(QSize(860, 551))
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(280, 150, 210, 251))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.A1 = QRadioButton(self.verticalLayoutWidget)
        self.A1.setObjectName(u"A1")

        self.verticalLayout.addWidget(self.A1)

        self.A2 = QRadioButton(self.verticalLayoutWidget)
        self.A2.setObjectName(u"A2")

        self.verticalLayout.addWidget(self.A2)

        self.A3 = QRadioButton(self.verticalLayoutWidget)
        self.A3.setObjectName(u"A3")

        self.verticalLayout.addWidget(self.A3)

        self.A4 = QRadioButton(self.verticalLayoutWidget)
        self.A4.setObjectName(u"A4")

        self.verticalLayout.addWidget(self.A4)

        self.OK = QPushButton(self.centralwidget)
        self.OK.setObjectName(u"OK")
        self.OK.setGeometry(QRect(330, 440, 101, 41))
        self.Right = QTextEdit(self.centralwidget)
        self.Right.setObjectName(u"Right")
        self.Right.setGeometry(QRect(500, 50, 361, 501))
        self.Right.setReadOnly(True)
        self.Left = QTextEdit(self.centralwidget)
        self.Left.setObjectName(u"Left")
        self.Left.setGeometry(QRect(0, 50, 261, 501))
        self.Left.setReadOnly(True)
        self.Road = QLineEdit(self.centralwidget)
        self.Road.setObjectName(u"Road")
        self.Road.setGeometry(QRect(0, 0, 401, 51))
        self.Road.setReadOnly(True)
        self.Open = QPushButton(self.centralwidget)
        self.Open.setObjectName(u"Open")
        self.Open.setGeometry(QRect(280, 70, 101, 41))
        self.Url = QLineEdit(self.centralwidget)
        self.Url.setObjectName(u"URL")
        self.Url.setGeometry(QRect(400, 0, 461, 51))
        self.Url.setReadOnly(True)
        self.SetUrl = QPushButton(self.centralwidget)
        self.SetUrl.setObjectName(u"SetURL")
        self.SetUrl.setGeometry(QRect(390, 70, 101, 41))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"ApiTest", None))
        self.A1.setText(QCoreApplication.translate("MainWindow", u"\u5355\u4e2a\u63a5\u53e3\u6d4b\u8bd5(\u9ed8\u8ba4\u53c2\u6570)", None))
        self.A2.setText(QCoreApplication.translate("MainWindow", u"\u6240\u6709\u63a5\u53e3\u6d4b\u8bd5(\u9ed8\u8ba4\u53c2\u6570)", None))
        self.A3.setText(QCoreApplication.translate("MainWindow", u"\u5355\u4e2a\u63a5\u53e3\u6d4b\u8bd5(\u81ea\u5b9a\u4e49\u53c2\u6570)", None))
        self.A4.setText(QCoreApplication.translate("MainWindow", u"\u62a5\u544a\u53d1\u9001", None))
        self.OK.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.Open.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.SetUrl.setText(QCoreApplication.translate("MainWindow", u"SetUrl", None))
        pass
    # retranslateUi


class Ui_ApiNumberInput(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.setWindowModality(Qt.ApplicationModal)
        Dialog.setEnabled(True)
        Dialog.resize(331, 102)
        Dialog.setMinimumSize(QSize(331, 102))
        Dialog.setMaximumSize(QSize(331, 102))
        Dialog.setMouseTracking(False)
        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(120, 50, 191, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 20, 171, 21))
        self.label.setTextFormat(Qt.AutoText)
        self.lineEdit = QLineEdit(Dialog)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(20, 50, 91, 31))
        self.lineEdit.setFocus()

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"ApiTest", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">\u8bf7\u8f93\u5165\u5f85\u6d4b\u63a5\u53e3\u7f16\u53f7</span></p></body></html>", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u63a5\u53e3\u7f16\u53f7", None))
        pass
    # retranslateUi


class Ui_CustomOptionInput(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(402, 300)
        Dialog.setMinimumSize(QSize(402, 300))
        Dialog.setMaximumSize(QSize(402, 300))
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 20, 171, 21))
        self.label.setTextFormat(Qt.AutoText)
        self.lineEdit = QLineEdit(Dialog)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(20, 50, 361, 41))
        self.lineEdit_2 = QLineEdit(Dialog)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(20, 110, 361, 41))
        self.lineEdit_3 = QLineEdit(Dialog)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(20, 170, 361, 41))
        self.lineEdit_4 = QLineEdit(Dialog)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(50, 230, 101, 41))
        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(180, 240, 193, 28))
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"ApiTest", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">\u8bf7\u8f93\u5165\u81ea\u5b9a\u4e49\u7684\u53c2\u6570</span></p></body></html>", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u8bf7\u6c42\u53c2\u6570\uff1aquery", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u8bf7\u6c42\u5934\u53c2\u6570\uff1ahead", None))
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u8bf7\u6c42\u4f53\u53c2\u6570\uff1abody", None))
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u63a5\u53e3\u7f16\u53f7", None))
        pass
    # retranslateUi


class Ui_MailOptionInput(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(382, 267)
        Dialog.setMinimumSize(QSize(382, 267))
        Dialog.setMaximumSize(QSize(382, 267))
        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(180, 210, 181, 41))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.lineEdit = QLineEdit(Dialog)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(20, 50, 341, 41))
        self.lineEdit.setFocus()
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 20, 251, 21))
        self.textEdit = QTextEdit(Dialog)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(20, 100, 341, 101))

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"ApiTest", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u76ee\u7684\u90ae\u7bb1", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">\u5c06\u53d1\u9001\u62a5\u544a\uff0c\u8bf7\u7f16\u8f91\u76f8\u5e94\u4fe1\u606f</span></p></body></html>", None))
        self.textEdit.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u5907\u6ce8", None))
        pass
    # retranslateUi


class Ui_TestIPInput(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(315, 130)
        Dialog.setMinimumSize(QSize(315, 130))
        Dialog.setMaximumSize(QSize(315, 130))
        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(60, 80, 191, 31))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.lineEdit = QLineEdit(Dialog)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(150, 20, 151, 41))
        self.lineEdit.setInputMask('000.000.000.000')
        self.lineEdit.setFocus()
        self.lineEdit.setCursorMoveStyle(Qt.VisualMoveStyle)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 30, 151, 31))

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"ApiTest", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">\u8bf7\u8f93\u5165IP\u5730\u5740</span></p></body></html>", None))
        pass
    # retranslateUi


class Ui_WaitingInterface(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(270, 119)
        Dialog.setMinimumSize(QSize(270, 119))
        Dialog.setMaximumSize(QSize(270, 119))
        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(QRect(20, 50, 261, 41))
        self.pbar.setMaximum(0)
        self.pbar.setMinimum(0)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 20, 141, 21))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"ApiTest", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">\u7cfb\u7edf\u7e41\u5fd9\u4e2d\u3002\u3002\u3002</span></p></body></html>", None))
        pass
    # retranslateUi
