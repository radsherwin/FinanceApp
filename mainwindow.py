# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MASDAR")
        MainWindow.resize(1040, 533)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)

        sizePolicy.setHeightForWidth(self.centralWidget.sizePolicy().hasHeightForWidth())
        self.centralWidget.setSizePolicy(sizePolicy)
        self.centralWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralWidget.setAutoFillBackground(False)
        self.centralWidget.setObjectName("centralWidget")

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralWidget)
        self.horizontalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.left_constraint = QtWidgets.QVBoxLayout()
        self.left_constraint.setSpacing(6)
        self.left_constraint.setObjectName("left_constraint")

        self.financial_statements_grid = QtWidgets.QVBoxLayout()
        self.financial_statements_grid.setSpacing(6)
        self.financial_statements_grid.setObjectName("financial_statements_grid")

        self.search_box_horizontal_layout = QtWidgets.QHBoxLayout()
        self.search_box_horizontal_layout.setContentsMargins(12, -1, -1, -1)
        self.search_box_horizontal_layout.setSpacing(7)
        self.search_box_horizontal_layout.setObjectName("search_box_horizontal_layout")

        self.search_box = QtWidgets.QLineEdit(self.centralWidget)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.search_box.sizePolicy().hasHeightForWidth())

        self.search_box.setSizePolicy(sizePolicy)
        self.search_box.setText("")
        self.search_box.setObjectName("search_box")
        self.search_box_horizontal_layout.addWidget(self.search_box)

        self.search_button = QtWidgets.QPushButton(self.centralWidget)
        self.search_button.setObjectName("search_button")

        self.search_box_horizontal_layout.addWidget(self.search_button)

        self.financial_statements_grid.addLayout(self.search_box_horizontal_layout)

        self.financial_stm_label = QtWidgets.QLabel(self.centralWidget)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.financial_stm_label.sizePolicy().hasHeightForWidth())

        self.financial_stm_label.setSizePolicy(sizePolicy)
        self.financial_stm_label.setAlignment(QtCore.Qt.AlignCenter)
        self.financial_stm_label.setObjectName("financial_stm_label")

        self.financial_statements_grid.addWidget(self.financial_stm_label)

        self.left_constraint.addLayout(self.financial_statements_grid)
        self.horizontalLayout_2.addLayout(self.left_constraint)

        self.right_constraint = QtWidgets.QVBoxLayout()
        self.right_constraint.setContentsMargins(3, -1, -1, -1)
        self.right_constraint.setSpacing(6)
        self.right_constraint.setObjectName("right_constraint")

        self.graph_layout = QtWidgets.QHBoxLayout()
        self.graph_layout.setContentsMargins(0, -1, 0, -1)
        self.graph_layout.setSpacing(6)
        self.graph_layout.setObjectName("graph_layout")

        self.right_constraint.addLayout(self.graph_layout)

        self.stock_info_grid = QtWidgets.QHBoxLayout()
        self.stock_info_grid.setSpacing(6)
        self.stock_info_grid.setObjectName("stock_info_grid")
        self.stock_name = QtWidgets.QLabel(self.centralWidget)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(4)
        sizePolicy.setHeightForWidth(self.stock_name.sizePolicy().hasHeightForWidth())

        self.stock_name.setSizePolicy(sizePolicy)
        self.stock_name.setObjectName("stock_name")
        self.stock_info_grid.addWidget(self.stock_name, 0, QtCore.Qt.AlignHCenter)
        self.right_constraint.addLayout(self.stock_info_grid)
        self.horizontalLayout_2.addLayout(self.right_constraint)

        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.search_button, self.search_box)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.search_button.setText(_translate("MainWindow", "Search"))
        self.financial_stm_label.setText(_translate("MainWindow", "TextLabel"))
        self.stock_name.setText(_translate("MainWindow", "TextLabel"))

