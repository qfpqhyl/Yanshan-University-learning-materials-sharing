# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'imgr.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import sys
import requests
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import base64

API_KEY = "WfVYEUGlwDOFajaGO0b45fPv"
SECRET_KEY = "aQajyV5ZqKkKuZb5vWTYwrPLlNiKSyTU"


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(912, 722)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(40, 50, 421, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.comboBox = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout.addWidget(self.comboBox)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(40, 150, 421, 51))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.image = QtWidgets.QLabel(Form)
        self.image.setGeometry(QtCore.QRect(40, 250, 421, 381))
        self.image.setAutoFillBackground(False)
        self.image.setStyleSheet("border-width:1px;border-style:solid;border-color: rgb(0, 0, 0);")
        self.image.setText("")
        self.image.setObjectName("image")
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(480, 20, 361, 611))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setStyleSheet("border-width:1px;border-style:solid;border-color: rgb(0, 0, 0);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setStyleSheet("background-color: rgb(200, 200, 200);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "AI图像识别工具之《嗨害嗨》"))
        self.label.setText(_translate("Form", "选择识别类型"))
        self.comboBox.setItemText(0, _translate("Form", "银行卡"))
        self.comboBox.setItemText(1, _translate("Form", "动物"))
        self.comboBox.setItemText(2, _translate("Form", "植物"))
        self.comboBox.setItemText(3, _translate("Form", "果蔬识别"))
        self.comboBox.setItemText(4, _translate("Form", "营业执照"))
        self.comboBox.setItemText(5, _translate("Form", "身份证"))
        self.comboBox.setItemText(6, _translate("Form", "车牌号"))
        self.comboBox.setItemText(7, _translate("Form", "驾驶证"))
        self.comboBox.setItemText(8, _translate("Form", "货币"))
        self.comboBox.setItemText(9, _translate("Form", "车型"))
        self.comboBox.setItemText(10, _translate("Form", "logo"))
        self.label_3.setText(_translate("Form", "选择要识别的图片"))
        self.pushButton.setText(_translate("Form", "选择"))
        self.pushButton_2.setText(_translate("Form", "复制到剪贴板"))
        self.pushButton.clicked.connect(self.openfile)
        self.pushButton_2.clicked.connect(self.copyText)

    def copyText(self):
        # 复制文字到剪贴版中
        clipboard = QApplication.clipboard()
        # 设置复制的内容
        clipboard.setText(self.label_4.text())
    def openfile(self):
        self.download_path = QFileDialog.getOpenFileName(self.horizontalLayoutWidget_2,"选择要识别的图片","/","Image File(*.png *.jpg)")
        if not self.download_path[0].strip():
            pass
        else:
            self.lineEdit.setText(self.download_path[0])
            pixmap = QPixmap(self.download_path[0])
            scarePixmap = pixmap.scaled(QSize(421,381),aspectRatioMode=Qt.KeepAspectRatio)
            self.image.setPixmap(scarePixmap)
            self.typeTp()
            pass
    # 获取token值
    def get_token(self):
        host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=' + API_KEY + '&client_secret=' + SECRET_KEY
        response = requests.get(host)
        if response:
            print(response.json())
            self.access_token = response.json()['access_token']
            return self.access_token

    # 识别图片
    def typeTp(self):
        # 银行卡
        if self.comboBox.currentIndex() == 0:
            self.get_bankcard(self.get_token())
            pass
        # 动物
        elif self.comboBox.currentIndex() == 1:
            self.get_animal(self.get_token())
            pass
        # 植物
        elif self.comboBox.currentIndex() == 2:
            self.get_plant(self.get_token())
            pass
        # 果蔬识别
        elif self.comboBox.currentIndex() == 3:
            self.get_ingredient(self.get_token())
            pass
        # 营业执照
        elif self.comboBox.currentIndex() == 4:
            self.get_business_license(self.get_token())
            pass
        # 身份证
        elif self.comboBox.currentIndex() == 5:
            self.get_idcard(self.get_token())
            pass
        # 车牌号
        elif self.comboBox.currentIndex() == 6:
            self.get_license_plate(self.get_token())
            pass
        # 驾驶证
        elif self.comboBox.currentIndex() == 7:
            pass
        # 货币
        elif self.comboBox.currentIndex() == 8:
            self.get_currency(self.get_token())
            pass
        # 车型
        elif self.comboBox.currentIndex() == 9:
            self.get_car(self.get_token())
            pass
        # logo
        elif self.comboBox.currentIndex() == 10:
            self.get_logo(self.get_token())
            pass
        pass
    # 银行卡识别
    def get_bankcard(self, access_token):
        request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/bankcard"
        # 二进制方式打开图片文件
        f = open(self.download_path[0], 'rb')
        img = base64.b64encode(f.read())
        params = {"image": img}
        request_url = request_url + "?access_token=" + access_token
        headers = {'content-type': 'application/x-www-form-urlencoded'}
        response = requests.post(request_url, data=params, headers=headers)
        if response:
            print(response.json())
            bankcards = response.json()
            strover = '识别结果：\n'
            # 捕捉异常
            try:
                if bankcards['result']['bank_card_type']  == 0:
                    bank_card_type='不能识别'
                elif bankcards['result']['bank_card_type'] == 1:
                    bank_card_type = '借记卡'
                elif bankcards['result']['bank_card_type'] == 2:
                    bank_card_type = '信用卡'
                strover += '     卡号：{}\n     银行：{}\n     类型：{}\n'.format(bankcards['result']['bank_card_number'],bankcards['result']['bank_name'],bank_card_type)
            except BaseException:
                error_msg = bankcards['error_msg']
                strover += '错误:{}\n {}\n'.format(error_msg)
            # 显示出识别结果
            self.label_4.setText(strover)
    # 动物识别
    def get_animal(self, access_token):
        request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/animal"
        # 二进制方式打开图片文件
        f = open(self.download_path[0], 'rb')
        img = base64.b64encode(f.read())
        params = {"image": img}
        request_url = request_url + "?access_token=" + access_token
        headers = {'content-type': 'application/x-www-form-urlencoded'}
        response = requests.post(request_url, data=params, headers=headers)
        if response:
            print(response.json())
            animals = response.json()
            strover = '识别结果：\n'
            # 捕捉异常
            try:
                i = 1
                for animal in animals['result']:
                    strover += '{}、动物名称：{}\n'.format(i, animal['name'])
                    i += 1
            except BaseException:
                error_msg = animals['error_msg']
                strover += '错误:{}\n {}\n'.format(error_msg)
            # 显示出识别结果
            self.label_4.setText(strover)
    # 植物识别
    def get_plant(self, access_token):
        request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/plant"
        # 二进制方式打开图片文件
        f = open(self.download_path[0], 'rb')
        img = base64.b64encode(f.read())
        params = {"image": img}
        request_url = request_url + "?access_token=" + access_token
        headers = {'content-type': 'application/x-www-form-urlencoded'}
        response = requests.post(request_url, data=params, headers=headers)
        if response:
            print(response.json())
            plants = response.json()
            strover = '识别结果：\n'
            # 捕捉异常
            try:
                i = 1
                for plant in plants['result']:
                    strover+='{}、植物名称：{}\n'.format(i,plant['name'])
                    i+=1
            except BaseException:
                error_msg = plants['error_msg']
                strover += '错误:{}\n {}\n'.format(error_msg)
            # 显示出识别结果
            self.label_4.setText(strover)
    # logo识别
    def get_logo(self, access_token):
        request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v2/logo"
        # 二进制方式打开图片文件
        f = open(self.download_path[0], 'rb')
        img = base64.b64encode(f.read())
        params = {"image": img}
        request_url = request_url + "?access_token=" + access_token
        headers = {'content-type': 'application/x-www-form-urlencoded'}
        response = requests.post(request_url, data=params, headers=headers)
        if response:
            print(response.json())
            logos = response.json()
            strover = '识别结果：\n'
            # 捕捉异常
            try:
                i = 1
                for logo in logos['result']:
                    strover += '{}、logo名称：{}\n'.format(i, logo['name'])
                    i += 1
            except BaseException:
                error_msg = logos['error_msg']
                strover += '错误:{}\n {}\n'.format(error_msg)
            # 显示出识别结果
            self.label_4.setText(strover)
    # 果蔬识别
    def get_ingredient(self, access_token):
        request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/classify/ingredient"
        # 二进制方式打开图片文件
        f = open(self.download_path[0], 'rb')
        img = base64.b64encode(f.read())

        params = {"image": img}
        request_url = request_url + "?access_token=" + access_token
        headers = {'content-type': 'application/x-www-form-urlencoded'}
        response = requests.post(request_url, data=params, headers=headers)
        if response:
            print(response.json())
            ingredients = response.json()
            strover = '识别结果：\n'
            # 捕捉异常
            try:
                i = 1
                for ingredient in ingredients['result']:
                    strover += '{}、果蔬名称：{}\n'.format(i, ingredient['name'])
                    i += 1
            except BaseException:
                error_msg = ingredients['error_msg']
                strover += '错误:{}\n {}\n'.format(error_msg)
            # 显示出识别结果
            self.label_4.setText(strover)
    # 营业执照
    def get_business_license(self, access_token):
        request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/business_license"
        # 二进制方式打开图片文件
        f = open(self.download_path[0], 'rb')
        img = base64.b64encode(f.read())

        params = {"image": img}
        request_url = request_url + "?access_token=" + access_token
        headers = {'content-type': 'application/x-www-form-urlencoded'}
        response = requests.post(request_url, data=params, headers=headers)
        if response:
            print(response.json())
            business_licenses = response.json()
            strover = '识别结果：\n'
            # 捕捉异常
            try:
                socialcode = business_licenses['words_result']["社会信用代码"]['words']
                made = business_licenses['words_result']["组成形式"]['words']
                ranges = business_licenses['words_result']["经营范围"]['words']
                madetime = business_licenses['words_result']["成立日期"]['words']
                faren = business_licenses['words_result']["法人"]['words']
                ziben = business_licenses['words_result']["注册资本"]['words']
                code = business_licenses['words_result']["证件编号"]['words']
                adress = business_licenses['words_result']["地址"]['words']
                name = business_licenses['words_result']["单位名称"]['words']
                youxiaoqi = business_licenses['words_result']["有效期"]['words']
                leixing = business_licenses['words_result']["类型"]['words']
                strover += '     社会信用代码：{}\n     组成形式：{}\n     经营范围：{}\n     成立日期：{}\n     法人：{}\n     注册资本：{}\n     证件编号：{}\n     地址：{}\n     单位名称：{}\n     有效期：{}\n     类型：{}\n'.format(socialcode,
                                                                                                                                                                                           made, ranges, madetime, faren, ziben,
                                                                                                                                                                                           code, adress, name, youxiaoqi, leixing)
            except BaseException:
                error_msg = business_licenses['error_msg']
                strover += '错误:{}\n {}\n'.format(error_msg)
            # 显示出识别结果
            self.label_4.setText(strover)
    # 货币识别
    def get_currency(self, access_token):
        request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/currency"
        # 二进制方式打开图片文件
        f = open(self.download_path[0], 'rb')
        img = base64.b64encode(f.read())
        params = {"image": img}
        request_url = request_url + "?access_token=" + access_token
        headers = {'content-type': 'application/x-www-form-urlencoded'}
        response = requests.post(request_url, data=params, headers=headers)
        if response:
            print(response.json())
            currencys = response.json()
            strover = '识别结果：\n'
            # 捕捉异常
            try:
                currencyName = currencys['result']['currencyName']
                currencyCode = currencys['result']['currencyCode']
                currencyDenomination = currencys['result']['currencyDenomination']
                year = currencys['result']['year']
                strover += '     货币名称：{}\n     货币代码：{}\n     货币面值：{}\n     货币年份：{}\n'.format(currencyName, currencyCode, currencyDenomination, year)
            except BaseException:
                error_msg = currencys['error_msg']
                strover += '错误:{}\n {}\n'.format(error_msg)
            # 显示出识别结果
            self.label_4.setText(strover)
    # 身份证识别
    def get_idcard(self, access_token):
        request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/idcard"
        # 二进制方式打开图片文件
        f = open(self.download_path[0], 'rb')
        img = base64.b64encode(f.read())

        params = {"id_card_side": "front", "image": img}
        request_url = request_url + "?access_token=" + access_token
        headers = {'content-type': 'application/x-www-form-urlencoded'}
        response = requests.post(request_url, data=params, headers=headers)
        if response:
            print(response.json())
            idcards = response.json()
            strover = '识别结果：\n'
            # 捕捉异常
            try:
                name = idcards['words_result']['姓名']['words']
                minzu = idcards['words_result']['民族']['words']
                adress = idcards['words_result']['住址']['words']
                number = idcards['words_result']['公民身份号码']['words']
                chusheng = idcards['words_result']['出生']['words']
                sex = idcards['words_result']['性别']['words']
                strover += '     姓名：{}\n     性别：{}\n     民族：{}\n     出生日期：{}\n     身份证号码：{}\n     住址：{}\n'.format(name, sex, minzu, chusheng, number, adress)
            except BaseException:
                error_msg = idcards['error_msg']
                strover += '错误:{}\n {}\n'.format(error_msg)
            # 显示出识别结果
            self.label_4.setText(strover)
    # 车牌号
    def get_license_plate(self, access_token):
        request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/license_plate"
        # 二进制方式打开图片文件
        f = open(self.download_path[0], 'rb')
        img = base64.b64encode(f.read())

        params = {"image": img}
        request_url = request_url + "?access_token=" + access_token
        headers = {'content-type': 'application/x-www-form-urlencoded'}
        response = requests.post(request_url, data=params, headers=headers)
        if response:
            print(response.json())
            license_plates = response.json()
            strover = '识别结果：\n'
            # 捕捉异常
            try:
                color = license_plates['words_result']['color']
                number = license_plates['words_result']['number']
                strover += '     车牌颜色：{}\n     车牌号：{}\n'.format(color, number)
            except BaseException:
                error_msg = license_plates['error_msg']
                strover += '错误:{}\n {}\n'.format(error_msg)
            # 显示出识别结果
            self.label_4.setText(strover)
    # 车型识别
    def get_car(self, access_token):
        request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/car"
        # 二进制方式打开图片文件
        f = open(self.download_path[0], 'rb')
        img = base64.b64encode(f.read())

        params = {"image": img, "top_num": 5}
        request_url = request_url + "?access_token=" + access_token
        headers = {'content-type': 'application/x-www-form-urlencoded'}
        response = requests.post(request_url, data=params, headers=headers)
        if response:
            print(response.json())
            cars = response.json()
            color = cars['color_result']
            strover = '识别结果：\n     车身颜色：{}\n'.format(color)
            # 捕捉异常
            try:

                i = 1
                for car in cars['result']:
                    strover += '        {}、车型：{}\n        年份：{}\n'.format(i, car['name'], car['year'])
                    i += 1
            except BaseException:
                error_msg = cars['error_msg']
                strover += '错误:{}\n {}\n'.format(error_msg)
            # 显示出识别结果
            self.label_4.setText(strover)
# 初始化
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Form()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())