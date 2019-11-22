# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'upload.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector


class Ui_Form(object):
    db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="rgukt123",
    database="student"
    )
    mycursor=db.cursor()
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(727, 340)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(500, 200, 171, 101))
        self.pushButton.setObjectName("pushButton")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(20, 60, 391, 141))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.line_name = QtWidgets.QLineEdit(self.widget)
        self.line_name.setObjectName("line_name")
        self.gridLayout.addWidget(self.line_name, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.line_id = QtWidgets.QLineEdit(self.widget)
        self.line_id.setObjectName("line_id")
        self.gridLayout.addWidget(self.line_id, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.line_class = QtWidgets.QLineEdit(self.widget)
        self.line_class.setObjectName("line_class")
        self.gridLayout.addWidget(self.line_class, 2, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.pushButton.clicked.connect(self.submiting)
        self.line_class.returnPressed.connect(self.submiting)

    def submiting(self):
        self.name = str(self.line_name.text())
        self.idno = int(self.line_id.text())
        self.class_no = int(self.line_class.text())
        self.formula = "insert into face values(%s,%s,%s)"
        self.student = (self.name,self.idno,self.class_no)
        self.mycursor.execute(self.formula,self.student)
        self.db.commit()




    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "SUBMIT"))
        self.label.setText(_translate("Form", "NAME :"))
        self.label_2.setText(_translate("Form", "ID NO:"))
        self.label_3.setText(_translate("Form", "CLASS:"))
        
    



