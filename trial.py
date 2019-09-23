# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'trial.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!

import time
from PyQt5 import QtCore, QtGui, QtWidgets
import os,shutil
import json

queryType = 0
tables = [0,0,0,0]
userGroup = [0,0,0,0,0]
userAggregation = ""
userAggregationFunction = ""
userX = ""
zipGroup = [0,0,0,0]
zipAggregation = ""
zipAggregationFunction = ""
zipX = ""
movieGroup = [0]*22
movieAggregation = ""
movieAggregationFunction = ""
movieX = ""
ratingGroup = [0]*4
ratingAggregation = ""
ratingAggregationFunction = ""
ratingX = ""
columnForJoin=""
operator=""
joinX=""

#this is the class for choosing between Query type
class Ui_MainWindow1(object):
    #def radioButtonQuery():

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(472, 308)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayout = QtWidgets.QFormLayout(self.centralwidget)
        self.formLayout.setObjectName("formLayout")
        self.FirstLabel = QtWidgets.QLabel(self.centralwidget)
        self.FirstLabel.setObjectName("FirstLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.FirstLabel)
        self.JoinQueryRadio = QtWidgets.QRadioButton(self.centralwidget)
        self.JoinQueryRadio.setObjectName("JoinQueryRadio")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.JoinQueryRadio)
        self.GroupQueryRadio = QtWidgets.QRadioButton(self.centralwidget)
        self.GroupQueryRadio.setObjectName("GroupQueryRadio")
        if self.JoinQueryRadio.isChecked():
            queryType = 1
        else:
            queryType = 2
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.GroupQueryRadio)
        self.SubmitButton = QtWidgets.QPushButton(self.centralwidget)
        self.SubmitButton.setObjectName("SubmitButton")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.SubmitButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.formLayout.setItem(4, QtWidgets.QFormLayout.SpanningRole, spacerItem)
        MainWindow.setCentralWidget(self.centralwidget)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.SubmitButton.clicked.connect(self.closeIt)
    def closeIt(self):
        global queryType
        if self.JoinQueryRadio.isChecked():
            queryType = 1
            #print(queryType)
        else:
            queryType = 2
            #print(queryType)
        MainWindow.close()
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Choose Query"))
        self.FirstLabel.setText(_translate("MainWindow", "Choose the query type"))
        self.JoinQueryRadio.setText(_translate("MainWindow", "Join Query"))
        self.GroupQueryRadio.setText(_translate("MainWindow", "Group Query"))
        self.SubmitButton.setText(_translate("MainWindow", "Submit"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))


#this is the class for choosing the tables
class Ui_MainWindow2(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(574, 409)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.UserCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.UserCheckBox.setGeometry(QtCore.QRect(70, 40, 99, 22))
        self.UserCheckBox.setObjectName("UserCheckBox")
        self.ZipCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.ZipCheckBox.setGeometry(QtCore.QRect(70, 80, 99, 22))
        self.ZipCheckBox.setObjectName("ZipCheckBox")
        self.MovieCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.MovieCheckBox.setGeometry(QtCore.QRect(70, 120, 99, 22))
        self.MovieCheckBox.setObjectName("MovieCheckBox")
        self.RatingCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.RatingCheckBox.setGeometry(QtCore.QRect(70, 160, 99, 22))
        self.RatingCheckBox.setObjectName("RatingCheckBox")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(67, 10, 271, 20))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(230, 210, 99, 27))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton.clicked.connect(self.closeIt)
    def closeIt(self):
        global tables
        if self.UserCheckBox.isChecked():
            tables[0] = 1
        if self.ZipCheckBox.isChecked():
            tables[1] = 1
        if self.MovieCheckBox.isChecked():
            tables[2] = 1
        if self.RatingCheckBox.isChecked():
            tables[3] = 1
        MainWindow.close()
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.UserCheckBox.setText(_translate("MainWindow", "Users"))
        self.ZipCheckBox.setText(_translate("MainWindow", "Zipcodes"))
        self.MovieCheckBox.setText(_translate("MainWindow", "Movies"))
        self.RatingCheckBox.setText(_translate("MainWindow", "Rating"))
        self.label.setText(_translate("MainWindow", "Which Table do you want to query?"))
        self.pushButton.setText(_translate("MainWindow", "Submit"))
def printMessage():
    print(queryType)

#this is the class for users
class Ui_MainWindow3(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(546, 401)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayout = QtWidgets.QFormLayout(self.centralwidget)
        self.formLayout.setObjectName("formLayout")
        self.Zipcode = QtWidgets.QCheckBox(self.centralwidget)
        self.Zipcode.setObjectName("Zipcode")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.Zipcode)
        self.Age = QtWidgets.QCheckBox(self.centralwidget)
        self.Age.setObjectName("Age")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.Age)
        self.Occupation = QtWidgets.QCheckBox(self.centralwidget)
        self.Occupation.setObjectName("Occupation")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.Occupation)
        self.UserID = QtWidgets.QCheckBox(self.centralwidget)
        self.UserID.setObjectName("UserID")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.UserID)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.Aggregation = QtWidgets.QComboBox(self.centralwidget)
        self.Aggregation.setObjectName("Aggregation")
        self.Aggregation.addItem("")
        self.Aggregation.addItem("")
        self.Aggregation.addItem("")
        self.Aggregation.addItem("")
        self.Aggregation.addItem("")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.Aggregation)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.AggregationFunction = QtWidgets.QComboBox(self.centralwidget)
        self.AggregationFunction.setObjectName("AggregationFunction")
        self.AggregationFunction.addItem("")
        self.AggregationFunction.addItem("")
        self.AggregationFunction.addItem("")
        self.AggregationFunction.addItem("")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.AggregationFunction)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.ValueOfX = QtWidgets.QLineEdit(self.centralwidget)
        self.ValueOfX.setObjectName("ValueOfX")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.FieldRole, self.ValueOfX)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label)
        self.Gender = QtWidgets.QCheckBox(self.centralwidget)
        self.Gender.setObjectName("Gender")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.Gender)
        self.SubmitButton = QtWidgets.QPushButton(self.centralwidget)
        self.SubmitButton.setObjectName("SubmitButton")
        self.formLayout.setWidget(18, QtWidgets.QFormLayout.LabelRole, self.SubmitButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.SubmitButton.clicked.connect(self.closeIt)
    def closeIt(self):
        global userGroup,userAggregation,userX,userAggregationFunction
        if self.UserID.isChecked():
            userGroup[0] = 1
        if self.Age.isChecked():
            userGroup[1] = 1
        if self.Gender.isChecked():
            userGroup[2] = 1
        if self.Occupation.isChecked():
            userGroup[3] = 1
        if self.Zipcode.isChecked():
            userGroup[4] = 1
        userAggregation = str(self.Aggregation.currentText())
        userAggregationFunction = str(self.AggregationFunction.currentText())
        # print(self.AggregationFunction.currentText())

        userX = str(self.ValueOfX.text())
        MainWindow.close()
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Zipcode.setText(_translate("MainWindow", "ZipCode"))
        self.Age.setText(_translate("MainWindow", "Age"))
        self.Occupation.setText(_translate("MainWindow", "Occupation"))
        self.UserID.setText(_translate("MainWindow", "UserID"))
        self.label_2.setText(_translate("MainWindow", "Which column to aggregate over?"))
        self.Aggregation.setItemText(0, _translate("MainWindow", "UserId"))
        self.Aggregation.setItemText(1, _translate("MainWindow", "Age"))
        self.Aggregation.setItemText(2, _translate("MainWindow", "Gender"))
        self.Aggregation.setItemText(3, _translate("MainWindow", "Occupation"))
        self.Aggregation.setItemText(4, _translate("MainWindow", "ZipCode"))
        self.label_3.setText(_translate("MainWindow", "Aggregate Function?"))
        self.AggregationFunction.setItemText(0, _translate("MainWindow", "Count"))
        self.AggregationFunction.setItemText(1, _translate("MainWindow", "Max"))
        self.AggregationFunction.setItemText(2, _translate("MainWindow", "Min"))
        self.AggregationFunction.setItemText(3, _translate("MainWindow", "Sum"))
        self.label_4.setText(_translate("MainWindow", "Value of X?"))
        self.label.setText(_translate("MainWindow", "Which columns do you want to group by?"))
        self.Gender.setText(_translate("MainWindow", "Gender"))
        self.SubmitButton.setText(_translate("MainWindow", "Submit"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))

#this is the class for zipcodes
class Ui_MainWindow4(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(546, 401)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayout = QtWidgets.QFormLayout(self.centralwidget)
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label)
        self.ZipCode = QtWidgets.QCheckBox(self.centralwidget)
        self.ZipCode.setObjectName("ZipCode")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.ZipCode)
        self.ZipCodeType = QtWidgets.QCheckBox(self.centralwidget)
        self.ZipCodeType.setObjectName("ZipCodeType")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.ZipCodeType)
        self.City = QtWidgets.QCheckBox(self.centralwidget)
        self.City.setObjectName("City")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.City)
        self.State = QtWidgets.QCheckBox(self.centralwidget)
        self.State.setObjectName("State")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.State)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.Aggregation = QtWidgets.QComboBox(self.centralwidget)
        self.Aggregation.setObjectName("Aggregation")
        self.Aggregation.addItem("")
        self.Aggregation.addItem("")
        self.Aggregation.addItem("")
        self.Aggregation.addItem("")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.Aggregation)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.AggregationFunction = QtWidgets.QComboBox(self.centralwidget)
        self.AggregationFunction.setObjectName("AggregationFunction")
        self.AggregationFunction.addItem("")
        self.AggregationFunction.addItem("")
        self.AggregationFunction.addItem("")
        self.AggregationFunction.addItem("")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.AggregationFunction)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.ValueOfX = QtWidgets.QLineEdit(self.centralwidget)
        self.ValueOfX.setObjectName("ValueOfX")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.FieldRole, self.ValueOfX)
        self.SubmitButton = QtWidgets.QPushButton(self.centralwidget)
        self.SubmitButton.setObjectName("SubmitButton")
        self.formLayout.setWidget(18, QtWidgets.QFormLayout.LabelRole, self.SubmitButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.SubmitButton.clicked.connect(self.closeIt)
    def closeIt(self):
        global zipGroup,zipAggregation,zipX,zipAggregationFunction
        if self.ZipCode.isChecked():
            zipGroup[0] = 1
        if self.ZipCodeType.isChecked():
            zipGroup[1] = 1
        if self.City.isChecked():
            zipGroup[2] = 1
        if self.State.isChecked():
            zipGroup[3] = 1
        zipAggregation = str(self.Aggregation.currentText())
        zipAggregationFunction = str(self.AggregationFunction.currentText())
        zipX = str(self.ValueOfX.text())
        MainWindow.close()
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Which columns do you want to group by?"))
        self.ZipCode.setText(_translate("MainWindow", "ZipCode"))
        self.ZipCodeType.setText(_translate("MainWindow", "ZipCodeType"))
        self.City.setText(_translate("MainWindow", "City"))
        self.State.setText(_translate("MainWindow", "State"))
        self.label_2.setText(_translate("MainWindow", "Which column to aggregate over?"))
        self.Aggregation.setItemText(0, _translate("MainWindow", "ZipCodeType"))
        self.Aggregation.setItemText(1, _translate("MainWindow", "City"))
        self.Aggregation.setItemText(2, _translate("MainWindow", "State"))
        self.Aggregation.setItemText(3, _translate("MainWindow", "ZipCode"))
        self.label_3.setText(_translate("MainWindow", "Aggregate Function?"))
        self.AggregationFunction.setItemText(0, _translate("MainWindow", "Count"))
        self.AggregationFunction.setItemText(1, _translate("MainWindow", "Max"))
        self.AggregationFunction.setItemText(2, _translate("MainWindow", "Min"))
        self.AggregationFunction.setItemText(3, _translate("MainWindow", "Sum"))
        self.label_4.setText(_translate("MainWindow", "Value of X?"))
        self.SubmitButton.setText(_translate("MainWindow", "Submit"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
class Ui_MainWindow5(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(588, 401)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(9, 196, 228, 17))
        self.label_2.setObjectName("label_2")
        self.Aggregation = QtWidgets.QComboBox(self.centralwidget)
        self.Aggregation.setGeometry(QtCore.QRect(294, 196, 110, 27))
        self.Aggregation.setObjectName("Aggregation")
        self.Aggregation.addItem("")
        self.Aggregation.addItem("")
        self.Aggregation.addItem("")
        self.Aggregation.addItem("")
        self.Aggregation.addItem("")
        self.Aggregation.addItem("")
        self.Aggregation.addItem("")
        self.Aggregation.addItem("")
        self.Aggregation.addItem("")
        self.Aggregation.addItem("")
        self.Aggregation.addItem("")
        self.Aggregation.addItem("")
        self.Aggregation.addItem("")
        self.Aggregation.addItem("")
        self.Aggregation.addItem("")
        self.Aggregation.addItem("")
        self.Aggregation.addItem("")
        self.Aggregation.addItem("")
        self.Aggregation.addItem("")
        self.Aggregation.addItem("")
        self.Aggregation.addItem("")
        self.Aggregation.addItem("")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(9, 229, 143, 17))
        self.label_3.setObjectName("label_3")
        self.AggregationFunction = QtWidgets.QComboBox(self.centralwidget)
        self.AggregationFunction.setGeometry(QtCore.QRect(294, 229, 73, 27))
        self.AggregationFunction.setObjectName("AggregationFunction")
        self.AggregationFunction.addItem("")
        self.AggregationFunction.addItem("")
        self.AggregationFunction.addItem("")
        self.AggregationFunction.addItem("")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(9, 262, 77, 17))
        self.label_4.setObjectName("label_4")
        self.ValueOfX = QtWidgets.QLineEdit(self.centralwidget)
        self.ValueOfX.setGeometry(QtCore.QRect(294, 262, 146, 27))
        self.ValueOfX.setObjectName("ValueOfX")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(9, 27, 279, 17))
        self.label.setObjectName("label")
        self.SubmitButton = QtWidgets.QPushButton(self.centralwidget)
        self.SubmitButton.setGeometry(QtCore.QRect(9, 325, 85, 27))
        self.SubmitButton.setObjectName("SubmitButton")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(110, 50, 123, 136))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.Movie6 = QtWidgets.QCheckBox(self.layoutWidget)
        self.Movie6.setObjectName("Movie6")
        self.gridLayout_2.addWidget(self.Movie6, 0, 0, 1, 1)
        self.Movie7 = QtWidgets.QCheckBox(self.layoutWidget)
        self.Movie7.setObjectName("Movie7")
        self.gridLayout_2.addWidget(self.Movie7, 1, 0, 1, 1)
        self.Movie8 = QtWidgets.QCheckBox(self.layoutWidget)
        self.Movie8.setObjectName("Movie8")
        self.gridLayout_2.addWidget(self.Movie8, 2, 0, 1, 1)
        self.Movie9 = QtWidgets.QCheckBox(self.layoutWidget)
        self.Movie9.setObjectName("Movie9")
        self.gridLayout_2.addWidget(self.Movie9, 3, 0, 1, 1)
        self.Movie10 = QtWidgets.QCheckBox(self.layoutWidget)
        self.Movie10.setObjectName("Movie10")
        self.gridLayout_2.addWidget(self.Movie10, 4, 0, 1, 1)
        self.layoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_2.setGeometry(QtCore.QRect(230, 50, 127, 136))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.layoutWidget_2)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.Movie11 = QtWidgets.QCheckBox(self.layoutWidget_2)
        self.Movie11.setObjectName("Movie11")
        self.gridLayout_3.addWidget(self.Movie11, 0, 0, 1, 1)
        self.Movie12 = QtWidgets.QCheckBox(self.layoutWidget_2)
        self.Movie12.setObjectName("Movie12")
        self.gridLayout_3.addWidget(self.Movie12, 1, 0, 1, 1)
        self.Movie13 = QtWidgets.QCheckBox(self.layoutWidget_2)
        self.Movie13.setObjectName("Movie13")
        self.gridLayout_3.addWidget(self.Movie13, 2, 0, 1, 1)
        self.Movie14 = QtWidgets.QCheckBox(self.layoutWidget_2)
        self.Movie14.setObjectName("Movie14")
        self.gridLayout_3.addWidget(self.Movie14, 3, 0, 1, 1)
        self.Movie15 = QtWidgets.QCheckBox(self.layoutWidget_2)
        self.Movie15.setObjectName("Movie15")
        self.gridLayout_3.addWidget(self.Movie15, 4, 0, 1, 1)
        self.layoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_3.setGeometry(QtCore.QRect(350, 50, 123, 136))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.layoutWidget_3)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.Movie17 = QtWidgets.QCheckBox(self.layoutWidget_3)
        self.Movie17.setObjectName("Movie17")
        self.gridLayout_4.addWidget(self.Movie17, 2, 0, 1, 1)
        self.Movie18 = QtWidgets.QCheckBox(self.layoutWidget_3)
        self.Movie18.setObjectName("Movie18")
        self.gridLayout_4.addWidget(self.Movie18, 3, 0, 1, 1)
        self.Movie19 = QtWidgets.QCheckBox(self.layoutWidget_3)
        self.Movie19.setObjectName("Movie19")
        self.gridLayout_4.addWidget(self.Movie19, 4, 0, 1, 1)
        self.Movie20 = QtWidgets.QCheckBox(self.layoutWidget_3)
        self.Movie20.setObjectName("Movie20")
        self.gridLayout_4.addWidget(self.Movie20, 5, 0, 1, 1)
        self.Movie16 = QtWidgets.QCheckBox(self.layoutWidget_3)
        self.Movie16.setObjectName("Movie16")
        self.gridLayout_4.addWidget(self.Movie16, 1, 0, 1, 1)
        self.layoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_4.setGeometry(QtCore.QRect(450, 50, 123, 136))
        self.layoutWidget_4.setObjectName("layoutWidget_4")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.layoutWidget_4)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.checkBox_9 = QtWidgets.QCheckBox(self.layoutWidget_4)
        self.checkBox_9.setObjectName("checkBox_9")
        self.gridLayout_5.addWidget(self.checkBox_9, 0, 0, 1, 1)
        self.Movie22 = QtWidgets.QCheckBox(self.layoutWidget_4)
        self.Movie22.setObjectName("Movie22")
        self.gridLayout_5.addWidget(self.Movie22, 1, 0, 1, 1)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(0, 50, 123, 136))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.Movie2 = QtWidgets.QCheckBox(self.layoutWidget1)
        self.Movie2.setObjectName("Movie2")
        self.gridLayout.addWidget(self.Movie2, 4, 0, 1, 1)
        self.Movie1 = QtWidgets.QCheckBox(self.layoutWidget1)
        self.Movie1.setObjectName("Movie1")
        self.gridLayout.addWidget(self.Movie1, 1, 0, 1, 1)
        self.Movie3 = QtWidgets.QCheckBox(self.layoutWidget1)
        self.Movie3.setObjectName("Movie3")
        self.gridLayout.addWidget(self.Movie3, 6, 0, 1, 1)
        self.Movie4 = QtWidgets.QCheckBox(self.layoutWidget1)
        self.Movie4.setObjectName("Movie4")
        self.gridLayout.addWidget(self.Movie4, 7, 0, 1, 1)
        self.Movie5 = QtWidgets.QCheckBox(self.layoutWidget1)
        self.Movie5.setObjectName("Movie5")
        self.gridLayout.addWidget(self.Movie5, 8, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.SubmitButton.clicked.connect(self.closeIt)
    def closeIt(self):
        global movieGroup,movieAggregation,movieX,movieAggregationFunction
        c=0
        if self.Movie1.isChecked():
            movieGroup[c] = 1
        c=c+1
        if self.Movie12.isChecked():
            movieGroup[c] = 1
        c=c+1
        if self.Movie3.isChecked():
            movieGroup[c] = 1
        c=c+1
        if self.Movie4.isChecked():
            movieGroup[c] = 1
        c=c+1
        if self.Movie5.isChecked():
            movieGroup[c] = 1
        c=c+1
        if self.Movie6.isChecked():
            movieGroup[c] = 1
        c=c+1
        if self.Movie7.isChecked():
            movieGroup[c] = 1
        c=c+1
        if self.Movie8.isChecked():
            movieGroup[c] = 1
        c=c+1
        if self.Movie9.isChecked():
            movieGroup[c] = 1
        c=c+1
        if self.Movie10.isChecked():
            movieGroup[c] = 1
        c=c+1
        if self.Movie11.isChecked():
            movieGroup[c] = 1
        c=c+1
        if self.Movie12.isChecked():
            movieGroup[c] = 1
        c=c+1
        if self.Movie13.isChecked():
            movieGroup[c] = 1
        c=c+1
        if self.Movie14.isChecked():
            movieGroup[c] = 1
        c=c+1
        if self.Movie15.isChecked():
            movieGroup[c] = 1
        c=c+1
        if self.Movie16.isChecked():
            movieGroup[c] = 1
        c=c+1
        if self.Movie17.isChecked():
            movieGroup[c] = 1
        c=c+1
        if self.Movie18.isChecked():
            movieGroup[c] = 1
        c=c+1
        if self.Movie19.isChecked():
            movieGroup[c] = 1
        c=c+1
        if self.Movie20.isChecked():
            movieGroup[c] = 1
        c=c+1
        if self.checkBox_9.isChecked():
            movieGroup[c] = 1
        c=c+1
        if self.Movie22.isChecked():
            movieGroup[c] = 1
        c=c+1
        movieAggregation = str(self.Aggregation.currentText())
        movieAggregationFunction = str(self.AggregationFunction.currentText())
        movieX = str(self.ValueOfX.text())
        MainWindow.close()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Which column to aggregate over?"))
        self.Aggregation.setItemText(0, _translate("MainWindow", "MovieID"))
        self.Aggregation.setItemText(1, _translate("MainWindow", "Title"))
        self.Aggregation.setItemText(2, _translate("MainWindow", "Release Date"))
        self.Aggregation.setItemText(3, _translate("MainWindow", "Unknown"))
        self.Aggregation.setItemText(4, _translate("MainWindow", "Action"))
        self.Aggregation.setItemText(5, _translate("MainWindow", "Adventure"))
        self.Aggregation.setItemText(6, _translate("MainWindow", "Animation"))
        self.Aggregation.setItemText(7, _translate("MainWindow", "Children"))
        self.Aggregation.setItemText(8, _translate("MainWindow", "Comedy"))
        self.Aggregation.setItemText(9, _translate("MainWindow", "Crime"))
        self.Aggregation.setItemText(10, _translate("MainWindow", "Documentary"))
        self.Aggregation.setItemText(11, _translate("MainWindow", "Drama"))
        self.Aggregation.setItemText(12, _translate("MainWindow", "Fantasy"))
        self.Aggregation.setItemText(13, _translate("MainWindow", "Film Noir"))
        self.Aggregation.setItemText(14, _translate("MainWindow", "Horror"))
        self.Aggregation.setItemText(15, _translate("MainWindow", "Musical"))
        self.Aggregation.setItemText(16, _translate("MainWindow", "Mystery"))
        self.Aggregation.setItemText(17, _translate("MainWindow", "Romance"))
        self.Aggregation.setItemText(18, _translate("MainWindow", "Sci-Fi"))
        self.Aggregation.setItemText(19, _translate("MainWindow", "Thriller"))
        self.Aggregation.setItemText(20, _translate("MainWindow", "War"))
        self.Aggregation.setItemText(21, _translate("MainWindow", "Western"))
        self.label_3.setText(_translate("MainWindow", "Aggregate Function?"))
        self.AggregationFunction.setItemText(0, _translate("MainWindow", "Count"))
        self.AggregationFunction.setItemText(1, _translate("MainWindow", "Max"))
        self.AggregationFunction.setItemText(2, _translate("MainWindow", "Min"))
        self.AggregationFunction.setItemText(3, _translate("MainWindow", "Sum"))
        self.label_4.setText(_translate("MainWindow", "Value of X?"))
        self.label.setText(_translate("MainWindow", "Which columns do you want to group by?"))
        self.SubmitButton.setText(_translate("MainWindow", "Submit"))
        self.Movie6.setText(_translate("MainWindow", "Adventure"))
        self.Movie7.setText(_translate("MainWindow", "Animation"))
        self.Movie8.setText(_translate("MainWindow", "Children"))
        self.Movie9.setText(_translate("MainWindow", "Comedy"))
        self.Movie10.setText(_translate("MainWindow", "Crime"))
        self.Movie11.setText(_translate("MainWindow", "Documentary"))
        self.Movie12.setText(_translate("MainWindow", "Drama"))
        self.Movie13.setText(_translate("MainWindow", "Fantasy"))
        self.Movie14.setText(_translate("MainWindow", "Film Noir"))
        self.Movie15.setText(_translate("MainWindow", "Horror"))
        self.Movie17.setText(_translate("MainWindow", "Mystery"))
        self.Movie18.setText(_translate("MainWindow", "Romance"))
        self.Movie19.setText(_translate("MainWindow", "Sci-Fi"))
        self.Movie20.setText(_translate("MainWindow", "Thriller"))
        self.Movie16.setText(_translate("MainWindow", "Musical"))
        self.checkBox_9.setText(_translate("MainWindow", "War"))
        self.Movie22.setText(_translate("MainWindow", "Western"))
        self.Movie2.setText(_translate("MainWindow", "Title"))
        self.Movie1.setText(_translate("MainWindow", "MovieID"))
        self.Movie3.setText(_translate("MainWindow", "Release Date"))
        self.Movie4.setText(_translate("MainWindow", "Unknown"))
        self.Movie5.setText(_translate("MainWindow", "Action"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
#this class is for Ratings
class Ui_MainWindow6(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(588, 401)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(9, 196, 228, 17))
        self.label_2.setObjectName("label_2")
        self.Aggregation = QtWidgets.QComboBox(self.centralwidget)
        self.Aggregation.setGeometry(QtCore.QRect(294, 196, 110, 27))
        self.Aggregation.setObjectName("Aggregation")
        self.Aggregation.addItem("")
        self.Aggregation.addItem("")
        self.Aggregation.addItem("")
        self.Aggregation.addItem("")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(9, 229, 143, 17))
        self.label_3.setObjectName("label_3")
        self.AggregationFunction = QtWidgets.QComboBox(self.centralwidget)
        self.AggregationFunction.setGeometry(QtCore.QRect(294, 229, 73, 27))
        self.AggregationFunction.setObjectName("AggregationFunction")
        self.AggregationFunction.addItem("")
        self.AggregationFunction.addItem("")
        self.AggregationFunction.addItem("")
        self.AggregationFunction.addItem("")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(9, 262, 77, 17))
        self.label_4.setObjectName("label_4")
        self.ValueOfX = QtWidgets.QLineEdit(self.centralwidget)
        self.ValueOfX.setGeometry(QtCore.QRect(294, 262, 146, 27))
        self.ValueOfX.setObjectName("ValueOfX")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(9, 27, 279, 17))
        self.label.setObjectName("label")
        self.SubmitButton = QtWidgets.QPushButton(self.centralwidget)
        self.SubmitButton.setGeometry(QtCore.QRect(9, 325, 85, 27))
        self.SubmitButton.setObjectName("SubmitButton")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 50, 123, 136))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.MovieID = QtWidgets.QCheckBox(self.widget)
        self.MovieID.setObjectName("MovieID")
        self.gridLayout.addWidget(self.MovieID, 1, 0, 1, 1)
        self.Rating = QtWidgets.QCheckBox(self.widget)
        self.Rating.setObjectName("Rating")
        self.gridLayout.addWidget(self.Rating, 6, 0, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(self.widget)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout.addWidget(self.checkBox, 7, 0, 1, 1)
        self.UserID = QtWidgets.QCheckBox(self.widget)
        self.UserID.setObjectName("UserID")
        self.gridLayout.addWidget(self.UserID, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.SubmitButton.clicked.connect(self.closeIt)
    def closeIt(self):
        global ratingGroup,ratingAggregation,ratingX,ratingAggregationFunction
        if self.UserID.isChecked():
            ratingGroup[0] = 1
        if self.MovieID.isChecked():
            ratingGroup[1] = 1
        if self.Rating.isChecked():
            ratingGroup[2] = 1
        if self.checkBox.isChecked():
            ratingGroup[3] = 1

        ratingAggregation = str(self.Aggregation.currentText())
        ratingAggregationFunction = str(self.AggregationFunction.currentText())
        ratingX = str(self.ValueOfX.text())
        MainWindow.close()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Which column to aggregate over?"))
        self.Aggregation.setItemText(0, _translate("MainWindow", "MovieID"))
        self.Aggregation.setItemText(1, _translate("MainWindow", "UserID"))
        self.Aggregation.setItemText(2, _translate("MainWindow", "Rating"))
        self.Aggregation.setItemText(3, _translate("MainWindow", "TimeStamp"))
        self.label_3.setText(_translate("MainWindow", "Aggregate Function?"))
        self.AggregationFunction.setItemText(0, _translate("MainWindow", "Count"))
        self.AggregationFunction.setItemText(1, _translate("MainWindow", "Max"))
        self.AggregationFunction.setItemText(2, _translate("MainWindow", "Min"))
        self.AggregationFunction.setItemText(3, _translate("MainWindow", "Sum"))
        self.label_4.setText(_translate("MainWindow", "Value of X?"))
        self.label.setText(_translate("MainWindow", "Which columns do you want to group by?"))
        self.SubmitButton.setText(_translate("MainWindow", "Submit"))
        self.MovieID.setText(_translate("MainWindow", "MovieID"))
        self.Rating.setText(_translate("MainWindow", "Rating"))
        self.checkBox.setText(_translate("MainWindow", "TimeStamp"))
        self.UserID.setText(_translate("MainWindow", "UserID"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))

#Class for join
class Ui_MainWindow7(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(630, 397)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.ColumnValue = QtWidgets.QLineEdit(self.centralwidget)
        self.ColumnValue.setGeometry(QtCore.QRect(60, 50, 113, 27))
        self.ColumnValue.setObjectName("ColumnValue")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 20, 401, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 90, 171, 17))
        self.label_2.setObjectName("label_2")
        self.SubmitButton = QtWidgets.QPushButton(self.centralwidget)
        self.SubmitButton.setGeometry(QtCore.QRect(9, 325, 85, 27))
        self.SubmitButton.setObjectName("SubmitButton")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(60, 120, 85, 27))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(60, 170, 101, 17))
        self.label_3.setObjectName("label_3")
        self.ValueOfX = QtWidgets.QLineEdit(self.centralwidget)
        self.ValueOfX.setGeometry(QtCore.QRect(60, 190, 113, 27))
        self.ValueOfX.setObjectName("ValueOfX")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.SubmitButton.clicked.connect(self.closeIt)
    def closeIt(self):
        global columnForJoin,operator,joinX

        columnForJoin = str(self.ColumnValue.text())
        operator = str(self.comboBox.currentText())
        joinX = str(self.ValueOfX.text())
        MainWindow.close()
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Column on which condition is applied :"))
        self.label_2.setText(_translate("MainWindow", "Relational Operator :"))
        self.SubmitButton.setText(_translate("MainWindow", "Submit"))
        self.comboBox.setItemText(0, _translate("MainWindow", ">"))
        self.comboBox.setItemText(1, _translate("MainWindow", "=="))
        self.comboBox.setItemText(2, _translate("MainWindow", "!="))
        self.comboBox.setItemText(3, _translate("MainWindow", "<"))
        self.label_3.setText(_translate("MainWindow", "Value of X :"))
if __name__ == '__main__':
    import sys
    arg0 = ""
    arg1 = ""
    arg2 = ""
    arg3 = ""
    arg4 = ""
    arg5 = ""
    a = ""
    b = ""
    c = ""
    t = ""
    op = ""
    x = ""
    input1 = ""
    input2 = ""
    movieFields = {
    "Movie1" : "0",
"Movie2" : "1",
"Movie3" : "2",
"Movie4" : "3",
"Movie5" : "4",
"Movie6" : "5",
"Movie7" : "6",
"Movie8" : "7",
"Movie9" : "8",
"Movie10" : "9",
"Movie11" : "10",
"Movie12" : "11",
"Movie13" : "12",
"Movie14" : "13",
"Movie15" : "14",
"Movie16" : "15",
"Movie17" : "16",
"Movie18" : "17",
"Movie19" : "18",
"Movie20" : "19",
"checkBox_9" : "20",
"Movie22" : "21"
    }

    userFields = {
    "UserID" : "0",
    "Age" : "1",
    "Gender" : "2",
    "Occupation" : "3",
    "Zipcode" : "4"
    }

    zipcodeFields = {
        "ZipCode" : "0",
        "ZipCodeType" : "1",
        "City" : "2",
        "State" : "3"
    }

    ratingFields = {
    "UserID" : "0",
    "MovieID" : "1",
    "Rating" : "2",
    "TimeStamp" : "3"
    }

    movieF = {
    "movieid" : "0",
    "title" : "1",
    "releasedate" : "2",
    "unknown" : "3",
    "action" : "4",
    "adventure" : "5",
    "animation" : "6",
 	"children" : "7",
  	"comedy" : "8",
  	"crime" : "9",
  	"documentary" : "10",
  	"drama" : "11",
  	"fantasy" : "12",
	"film noir" : "13",
  	"horror" : "14",
  	"musical" : "15",
  	"mystery" : "16",
  	"romance" : "17",
  	"sci-fi" : "18",
	"thriller" : "19",
  	"war" : "20",
  	"western" : "21",
    }
    userF = {
    "userid" :"0", "age" :"1", "gender" :"2", "occupation":"3" , "zipcode":"4"
    }
    zipcodeF = {
    "zipcode":"0" , "zipcodetype":"1",  "city":"2",  "state":"3"
    }
    ratingF = {
    "userid":"0" , "movieid":"1",  "rating":"2" , "timestamp":"3"
    }
    dictFunc = {"Count":"0","Max":"1","Min":"2","Sum":"3"}
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui1 = Ui_MainWindow1()
    ui1.setupUi(MainWindow)
    MainWindow.show()

    app.exec()
    # print(queryType)
    ui2 = Ui_MainWindow2()
    ui2.setupUi(MainWindow)
    MainWindow.show()

    app.exec()
    tableIndex = -1
    # print(tables)
    typeOfQuery = 0
    if queryType == 1:
        ui7 = Ui_MainWindow7()
        ui7.setupUi(MainWindow)
        MainWindow.show()
        app.exec()

        typeOfQuery = 0
        #joining users and zipcodes
        if tables[0] == 1 and tables[1] == 1:
        	typeOfQuery = 1
        #joining users and ratings
        elif tables[0] == 1 and tables[3] == 1:
        	typeOfQuery = 2
        #joining movies and ratings
        elif tables[2] == 1 and tables[3] == 1:
        	typeOfQuery = 3

        c1 = columnForJoin.split(".")
        # print(typeOfQuery,type(c1[0].lower()),c1[1])
        if typeOfQuery == 1:
        	a = "4"
        	b = "0"
        	if c1[0].lower() == "users":
        		t = "0"
        		c = userF[c1[1].lower()]
        	else:
        		t = "1"
        		c = zipcodeF[c1[1].lower()]
        	input1 = "$HADOOP_HOME/input/users.csv"
        	input2 = "$HADOOP_HOME/input/zipcodes.csv"

        elif typeOfQuery == 2:
        	a = "0"
        	b = "0"
        	if c1[0].lower() == "users":
        		t = "0"
        		c = userF[c1[1].lower()]
        	else:
        		t = "1"
        		c = ratingF[c1[1].lower()]
        	input1 = "$HADOOP_HOME/input/users.csv"
        	input2 = "$HADOOP_HOME/input/rating.csv"
        elif typeOfQuery == 3:
        	a = "0"
        	b = "1"
        	if c1[0].lower() == "movies":
        		t = "0"
        		c = movieF[c1[1].lower()]
        	else:
        		t = "1"
        		c = ratingF[c1[1].lower()]
        	input1 = "$HADOOP_HOME/input/movies.csv"
        	input2 = "$HADOOP_HOME/input/rating.csv"
        else:
        	print("Not a valid request")
        	exit()
        if operator == ">":
        	op = "0"
        elif operator == "<":
        	op = "1"
        elif operator == "!=":
        	op = "3"
        else:
        	op = "2"
        x = str(joinX)
        # print(columnForJoin,operator,joinX)
    elif tables[0]==1:
        d = {""}
        tableIndex = 0
        ui3 = Ui_MainWindow3()
        ui3.setupUi(MainWindow)
        MainWindow.show()
        app.exec()
        # print(userGroup,userAggregation,userAggregationFunction,userX)
        arg2 = dictFunc[userAggregationFunction]
        arg3 = userX
        s = ""
        for i in userGroup:
            s=s+str(i)
        arg4 = s
        arg5 = userF[userAggregation.lower()]
    elif tables[1] == 1:
        tableIndex = 1
        ui4 = Ui_MainWindow4()
        ui4.setupUi(MainWindow)
        MainWindow.show()
        app.exec()
        arg2 = dictFunc[zipAggregationFunction]
        arg3 = zipX
        s = ""
        for i in zipGroup:
            s=s+str(i)
        arg4 = s
        arg5 = zipcodeF[zipAggregation.lower()]
        print(zipGroup,zipAggregation,zipAggregationFunction,zipX)
    elif tables[2] == 1:
        tableIndex = 2
        ui5 = Ui_MainWindow5()
        ui5.setupUi(MainWindow)
        MainWindow.show()
        app.exec()
        arg2 = dictFunc[movieAggregationFunction]
        arg3 = movieX
        s = ""
        for i in movieGroup:
            s=s+str(i)
        arg4 = s
        arg5 = movieF[movieAggregation.lower()]
        print(movieGroup,movieAggregation,movieAggregationFunction,movieX)
    elif tables[3] == 1:
        tableIndex = 3
        ui6 = Ui_MainWindow6()
        ui6.setupUi(MainWindow)
        MainWindow.show()
        app.exec()
        arg2 = dictFunc[ratingAggregationFunction]
        arg3 = ratingX
        s = ""
        for i in ratingGroup:
            s=s+str(i)
        arg4 = s
        arg5 = ratingF[ratingAggregation.lower()]
        print(ratingGroup,ratingAggregation,ratingAggregationFunction,ratingX)
    tableNames = ["users.csv","zipcodes.csv","movies.csv","rating.csv"]
    arg0 = "$HADOOP_HOME/input/"+tableNames[tableIndex]
    arg1 = "$HADOOP_HOME/output"
    shutil.rmtree("/usr/local/hadoop/output/",ignore_errors = True)
    timeForHadoop = -1
    if queryType == 2:
    	t0 = time.time()
    	os.system('/usr/local/hadoop/bin/hadoop jar $HADOOP_HOME/q2.jar Query2.q2 ' + arg0 + " " + arg1 + " "+ arg2 + " " +arg3+ " "+arg4+ " "+arg5)
    	t1 = time.time()
    	timeForHadoop = t1-t0
    else:
    	t0 = time.time()
    	os.system('/usr/local/hadoop/bin/hadoop jar $HADOOP_HOME/q1.jar query1.Q1 ' + input1 + " " + input2 + " "+ arg1 + " " +a+ " "+b+ " "+c +" "+t+" "+op+" "+x)
    	t1 = time.time()
    	timeForHadoop = t1-t0
    print("time to run Hadoop: ",timeForHadoop)
    timeForSpark = 0
    shutil.rmtree("input.txt",ignore_errors = True)
    file = open("input.txt","w+")
    dictForSpark = {
    0:"Users",1:"Zipcodes",2:"Movies",3:"Ratings"
    }
    dictForUser = {0:"userid",1:"age",2:"gender",3:"occupation",4:"zipcode"}
    dictForZip = {0:"zipcode",1:"zipcodetype",3:"city",4:"state"}
    dictForMovie = {0:"movieid",1:"title",2:"releasedate",3:"unknown",4:"action",5:"adventure",6:"animation",
    7:"children",8:"comedy",9:"crime",10:"documentary",11:"drama",12:"fantasy",13:"film_noir",14:"horror",15:"musical",16:"mystery",17:"romance",18:"sci_fi",19:"thriller",20:"war",21:"western"}
    dictForRating = {0:"userid",1:"movieid",2:"rating",3:"timestamp"}
    flag = 0
    if queryType == 1:
    	file.write("join\n")
    	
    	for i in range(len(tables)):
    		if tables[i] == 1:
    			file.write(dictForSpark[i]+"\n")
    	if typeOfQuery == 1:
    		file.write("zipcode\n")
    	elif typeOfQuery == 2:
    		file.write("userID\n")
    	else:
    		file.write("movieID\n")
    	col = columnForJoin.lower()
    	# col0 = columnForJoin[0].upper()
    	a = col[0].upper()
    	b = a + col[1:]
    	file.write(b+" "+operator+" "+joinX)

    else:
    	file.write("group\n")
    	if tables[0] == 1:
    		file.write("Users\n")
    		for i in range(len(userGroup)):
    			if userGroup[i]==1:
    				if flag == 0:
    					flag = 1
    					file.write(dictForUser[i])
    				else:
    					file.write(","+dictForUser[i])
    		file.write("\n")
    		file.write(userAggregationFunction+"("+userAggregation.lower()+")\n")
    		file.write(userX)
    	if tables[1] == 1:
    		file.write("Zipcodes\n")
    		for i in range(len(zipGroup)):
    			if zipGroup[i]==1:
    				if flag == 0:
    					flag = 1
    					file.write(dictForZip[i])
    				else:
    					file.write(","+dictForZip[i])
    		file.write("\n")
    		file.write(zipAggregationFunction+"("+zipAggregation.lower()+")\n")
    		file.write(zipX)
    	if tables[2] == 1:
    		file.write("Movies\n")
    		for i in range(len(movieGroup)):
    			if movieGroup[i]==1:
    				if flag == 0:
    					flag = 1
    					file.write(dictForMovie[i])
    				else:
    					file.write(","+dictForMovie[i])
    		file.write("\n")
    		file.write(movieAggregationFunction+"("+movieAggregation.lower()+")\n")
    		file.write(movieX)
    	if tables[3] == 1:
    		file.write("Ratings\n")
    		for i in range(len(ratingGroup)):
    			if ratingGroup[i]==1:
    				if flag == 0:
    					flag = 1
    					file.write(dictForRating[i])
    				else:
    					file.write(","+dictForRating[i])
    		file.write("\n")
    		file.write(ratingAggregationFunction+"("+ratingAggregation.lower()+")\n")
    		file.write(ratingX)
    	file.close()

    time.sleep(5);
    t0 = time.time()
    # os.system("source .env/bin/activate")
    os.system("python3 query_handler.py")
    t1 = time.time()
    timeForSpark = t1-t0
    print("time to run spark: ",timeForSpark)
    # f = open('/usr/local/hadoop/output/part-r-')