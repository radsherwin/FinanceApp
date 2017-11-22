# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/radsherwin/StockWindow/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1080)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        MainWindow.setFont(font)
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("QMainWindow {\n"
"    background: rgb(26, 28, 36);\n"
"    \n"
"} \n"
"\n"
"QFrame {\n"
"    background: rgb(46, 49, 68);\n"
"    border-radius: 20px;\n"
"    padding: 4px;\n"
"    margin: 4px;\n"
"    font: thin \"Helvetica Neue\";\n"
"}\n"
"\n"
"QLabel {\n"
"font: thin \"Helvetica Neue\";\n"
"    color: rgb(245,245,245);\n"
"}\n"
"\n"
"QComboBox {\n"
"font: thin \"Helvetica Neue\";\n"
"    border: 1px;\n"
"    border-radius: 10px;\n"
"    background: rgb(62, 67, 85);\n"
"    padding: 1px 18px 1px 8px;\n"
"    height: 22px;\n"
"    color: rgb(245,245,245);\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"font: thin \"Helvetica Neue\";\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 25px;\n"
"    \n"
"    border-left-width: 1px;\n"
"    border-left-color: rgb(46, 49, 68);\n"
"    border-left-style: solid; \n"
"    border-top-right-radius: 3px; \n"
"    border-bottom-right-radius: 3px;\n"
"\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(/Users/radsherwin/PycharmProjects/StockApp/icons/down_arrow.ico);\n"
"    width: 15px;\n"
"}\n"
"\n"
"QComboBox::down-arrow:on {\n"
"    image: url(/Users/radsherwin/PycharmProjects/StockApp/icons/up_arrow.ico);\n"
"    width: 15px;\n"
"}\n"
"\n"
"QLineEdit {\n"
"font: thin \"Helvetica Neue\";\n"
"    border-style: none;\n"
"     border-radius: 10px;\n"
"     background: rgb(62, 67, 85);\n"
"    padding: 0px 0px 0px 8px;\n"
"     min-width: 40px;\n"
"     height: 22px;\n"
"    selection-background-color: darkgrey;\n"
"    color: rgb(245,245,245);\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    outline: none;\n"
"    border-style: none;\n"
"border: 0px;\n"
"}\n"
"\n"
"QPushButton {\n"
"font: thin \"Helvetica Neue\";\n"
"    border: 1px;\n"
"    border-radius: 10px;\n"
"    background: rgb(62, 67, 85);\n"
"    height: 20px;\n"
"    color: rgb(245,245,245);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(75, 81, 108);\n"
"}\n"
"")
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralWidget.sizePolicy().hasHeightForWidth())
        self.centralWidget.setSizePolicy(sizePolicy)
        self.centralWidget.setMaximumSize(QtCore.QSize(1920, 1080))
        self.centralWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralWidget.setAutoFillBackground(False)
        self.centralWidget.setStyleSheet("")
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setMaximumSize(QtCore.QSize(1920, 1080))
        self.stackedWidget.setStyleSheet("QStackedWidget {\n"
"    background-color: none;\n"
"    border-style: none;\n"
"    border: 0px;\n"
"    outline: none;\n"
"    padding: 0px;\n"
"    margin: 0px;\n"
"}")
        self.stackedWidget.setFrameShape(QtWidgets.QFrame.Box)
        self.stackedWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.stackedWidget.setLineWidth(0)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.page.sizePolicy().hasHeightForWidth())
        self.page.setSizePolicy(sizePolicy)
        self.page.setObjectName("page")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.page)
        self.gridLayout_2.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.page_frame_page1 = QtWidgets.QFrame(self.page)
        self.page_frame_page1.setStyleSheet("QFrame {\n"
"    padding-left: 9px;\n"
"    padding-right: 9px;\n"
"}")
        self.page_frame_page1.setObjectName("page_frame_page1")
        self.page_change_layout_page2_2 = QtWidgets.QHBoxLayout(self.page_frame_page1)
        self.page_change_layout_page2_2.setContentsMargins(1, 1, 1, 1)
        self.page_change_layout_page2_2.setSpacing(6)
        self.page_change_layout_page2_2.setObjectName("page_change_layout_page2_2")
        self.last_page_button_page1 = QtWidgets.QPushButton(self.page_frame_page1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.last_page_button_page1.sizePolicy().hasHeightForWidth())
        self.last_page_button_page1.setSizePolicy(sizePolicy)
        self.last_page_button_page1.setObjectName("last_page_button_page1")
        self.page_change_layout_page2_2.addWidget(self.last_page_button_page1)
        self.next_page_button_page1 = QtWidgets.QPushButton(self.page_frame_page1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.next_page_button_page1.sizePolicy().hasHeightForWidth())
        self.next_page_button_page1.setSizePolicy(sizePolicy)
        self.next_page_button_page1.setDefault(False)
        self.next_page_button_page1.setObjectName("next_page_button_page1")
        self.page_change_layout_page2_2.addWidget(self.next_page_button_page1)
        self.gridLayout_2.addWidget(self.page_frame_page1, 0, 2, 1, 1)
        self.left_constraint = QtWidgets.QGridLayout()
        self.left_constraint.setSpacing(6)
        self.left_constraint.setObjectName("left_constraint")
        self.stock_chart_layout_frame = QtWidgets.QFrame(self.page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stock_chart_layout_frame.sizePolicy().hasHeightForWidth())
        self.stock_chart_layout_frame.setSizePolicy(sizePolicy)
        self.stock_chart_layout_frame.setMinimumSize(QtCore.QSize(621, 486))
        self.stock_chart_layout_frame.setMaximumSize(QtCore.QSize(800, 600))
        self.stock_chart_layout_frame.setStyleSheet("QFrame {\n"
"    padding: 0px;\n"
"    border-style: none;\n"
"    \n"
"}")
        self.stock_chart_layout_frame.setObjectName("stock_chart_layout_frame")
        self.stock_chart_vertical_layout = QtWidgets.QVBoxLayout(self.stock_chart_layout_frame)
        self.stock_chart_vertical_layout.setContentsMargins(11, 11, 11, 11)
        self.stock_chart_vertical_layout.setSpacing(6)
        self.stock_chart_vertical_layout.setObjectName("stock_chart_vertical_layout")
        self.time_frame_combo_box = QtWidgets.QComboBox(self.stock_chart_layout_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.time_frame_combo_box.sizePolicy().hasHeightForWidth())
        self.time_frame_combo_box.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        self.time_frame_combo_box.setFont(font)
        self.time_frame_combo_box.setStyleSheet("QComboBox {\n"
"    margin-top: 5px;\n"
"}")
        self.time_frame_combo_box.setObjectName("time_frame_combo_box")
        self.time_frame_combo_box.addItem("")
        self.time_frame_combo_box.addItem("")
        self.time_frame_combo_box.addItem("")
        self.time_frame_combo_box.addItem("")
        self.time_frame_combo_box.addItem("")
        self.time_frame_combo_box.addItem("")
        self.time_frame_combo_box.addItem("")
        self.time_frame_combo_box.addItem("")
        self.time_frame_combo_box.addItem("")
        self.time_frame_combo_box.addItem("")
        self.stock_chart_vertical_layout.addWidget(self.time_frame_combo_box)
        self.graph_frame_ss = QtWidgets.QFrame(self.stock_chart_layout_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graph_frame_ss.sizePolicy().hasHeightForWidth())
        self.graph_frame_ss.setSizePolicy(sizePolicy)
        self.graph_frame_ss.setStyleSheet("QFrame {\n"
"    background: rgb(54, 59, 77);\n"
"    padding: 0px;\n"
"    margin: 0px;\n"
"}")
        self.graph_frame_ss.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.graph_frame_ss.setFrameShadow(QtWidgets.QFrame.Raised)
        self.graph_frame_ss.setObjectName("graph_frame_ss")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.graph_frame_ss)
        self.gridLayout_3.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_3.setSpacing(6)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.graph_layout = QtWidgets.QGridLayout()
        self.graph_layout.setContentsMargins(0, 0, -1, -1)
        self.graph_layout.setSpacing(0)
        self.graph_layout.setObjectName("graph_layout")
        self.gridLayout_3.addLayout(self.graph_layout, 0, 0, 1, 1)
        self.stock_chart_vertical_layout.addWidget(self.graph_frame_ss)
        self.chart_info_frame = QtWidgets.QFrame(self.stock_chart_layout_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chart_info_frame.sizePolicy().hasHeightForWidth())
        self.chart_info_frame.setSizePolicy(sizePolicy)
        self.chart_info_frame.setStyleSheet("QFrame {\n"
"    border: 1px;\n"
"    border-radius: 25px;\n"
"    border-style: none;\n"
"    padding: 0px;\n"
"    background: none;\n"
"}")
        self.chart_info_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.chart_info_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.chart_info_frame.setObjectName("chart_info_frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.chart_info_frame)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.company_name_label = QtWidgets.QLabel(self.chart_info_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.company_name_label.sizePolicy().hasHeightForWidth())
        self.company_name_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        self.company_name_label.setFont(font)
        self.company_name_label.setObjectName("company_name_label")
        self.horizontalLayout.addWidget(self.company_name_label)
        self.stock_price_label = QtWidgets.QLabel(self.chart_info_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stock_price_label.sizePolicy().hasHeightForWidth())
        self.stock_price_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        self.stock_price_label.setFont(font)
        self.stock_price_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.stock_price_label.setAutoFillBackground(False)
        self.stock_price_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.stock_price_label.setObjectName("stock_price_label")
        self.horizontalLayout.addWidget(self.stock_price_label)
        self.stock_chart_vertical_layout.addWidget(self.chart_info_frame)
        self.left_constraint.addWidget(self.stock_chart_layout_frame, 1, 0, 1, 1)
        self.company_info = QtWidgets.QFrame(self.page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.company_info.sizePolicy().hasHeightForWidth())
        self.company_info.setSizePolicy(sizePolicy)
        self.company_info.setMinimumSize(QtCore.QSize(300, 100))
        self.company_info.setMaximumSize(QtCore.QSize(800, 500))
        self.company_info.setStyleSheet("QFrame {\n"
"    padding-top: 4px;\n"
"\n"
"}")
        self.company_info.setObjectName("company_info")
        self.advanced_stock_info = QtWidgets.QGridLayout(self.company_info)
        self.advanced_stock_info.setContentsMargins(11, 11, 11, 11)
        self.advanced_stock_info.setSpacing(6)
        self.advanced_stock_info.setObjectName("advanced_stock_info")
        self.company_summary = QtWidgets.QLabel(self.company_info)
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        self.company_summary.setFont(font)
        self.company_summary.setStyleSheet("QFrame {\n"
"    margin: 0px;\n"
"    border-style: none;\n"
"    background: rgb(54, 59, 77);\n"
"    padding: 12px;\n"
"}")
        self.company_summary.setWordWrap(True)
        self.company_summary.setObjectName("company_summary")
        self.advanced_stock_info.addWidget(self.company_summary, 1, 0, 1, 1)
        self.copmany_info_comboBox = QtWidgets.QComboBox(self.company_info)
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        self.copmany_info_comboBox.setFont(font)
        self.copmany_info_comboBox.setStyleSheet("QComboBox {\n"
"    margin-bottom: 5px;\n"
"}")
        self.copmany_info_comboBox.setObjectName("copmany_info_comboBox")
        self.copmany_info_comboBox.addItem("")
        self.copmany_info_comboBox.addItem("")
        self.advanced_stock_info.addWidget(self.copmany_info_comboBox, 0, 0, 1, 1)
        self.left_constraint.addWidget(self.company_info, 2, 0, 1, 1)
        self.gridLayout_2.addLayout(self.left_constraint, 1, 0, 1, 1)
        self.right_constraint = QtWidgets.QGridLayout()
        self.right_constraint.setSpacing(6)
        self.right_constraint.setObjectName("right_constraint")
        self.top_layout_right_frame = QtWidgets.QFrame(self.page)
        self.top_layout_right_frame.setStyleSheet("QFrame {\n"
"    \n"
"}")
        self.top_layout_right_frame.setObjectName("top_layout_right_frame")
        self.top_layout_right = QtWidgets.QVBoxLayout(self.top_layout_right_frame)
        self.top_layout_right.setContentsMargins(11, 11, 11, 11)
        self.top_layout_right.setSpacing(6)
        self.top_layout_right.setObjectName("top_layout_right")
        self.top_layout_combo_right = QtWidgets.QComboBox(self.top_layout_right_frame)
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        self.top_layout_combo_right.setFont(font)
        self.top_layout_combo_right.setObjectName("top_layout_combo_right")
        self.top_layout_right.addWidget(self.top_layout_combo_right)
        self.key_frame = QtWidgets.QFrame(self.top_layout_right_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.key_frame.sizePolicy().hasHeightForWidth())
        self.key_frame.setSizePolicy(sizePolicy)
        self.key_frame.setStyleSheet("QFrame {\n"
"    background: rgb(54, 59, 77);\n"
"border-style: none;\n"
"padding: 10px;\n"
"}")
        self.key_frame.setObjectName("key_frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.key_frame)
        self.horizontalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.key_layout_left = QtWidgets.QHBoxLayout()
        self.key_layout_left.setSpacing(6)
        self.key_layout_left.setObjectName("key_layout_left")
        self.key_table_left = QtWidgets.QTableWidget(self.key_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.key_table_left.sizePolicy().hasHeightForWidth())
        self.key_table_left.setSizePolicy(sizePolicy)
        self.key_table_left.setStyleSheet("QTableWidget {\n"
"    padding: 0px;\n"
"    margin: 0px;\n"
"}")
        self.key_table_left.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.key_table_left.setAutoScroll(False)
        self.key_table_left.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.key_table_left.setTabKeyNavigation(False)
        self.key_table_left.setProperty("showDropIndicator", False)
        self.key_table_left.setDragDropOverwriteMode(False)
        self.key_table_left.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.key_table_left.setShowGrid(False)
        self.key_table_left.setWordWrap(False)
        self.key_table_left.setCornerButtonEnabled(False)
        self.key_table_left.setRowCount(6)
        self.key_table_left.setColumnCount(2)
        self.key_table_left.setObjectName("key_table_left")
        self.key_table_left.horizontalHeader().setHighlightSections(True)
        self.key_table_left.horizontalHeader().setSortIndicatorShown(False)
        self.key_table_left.horizontalHeader().setStretchLastSection(True)
        self.key_table_left.verticalHeader().setVisible(False)
        self.key_layout_left.addWidget(self.key_table_left)
        self.horizontalLayout_2.addLayout(self.key_layout_left)
        self.key_layout_right = QtWidgets.QHBoxLayout()
        self.key_layout_right.setSpacing(6)
        self.key_layout_right.setObjectName("key_layout_right")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.key_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget_2.sizePolicy().hasHeightForWidth())
        self.tableWidget_2.setSizePolicy(sizePolicy)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(0)
        self.key_layout_right.addWidget(self.tableWidget_2)
        self.horizontalLayout_2.addLayout(self.key_layout_right)
        self.top_layout_right.addWidget(self.key_frame)
        self.right_constraint.addWidget(self.top_layout_right_frame, 0, 0, 1, 1)
        self.bottom_layout_right_frame = QtWidgets.QFrame(self.page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bottom_layout_right_frame.sizePolicy().hasHeightForWidth())
        self.bottom_layout_right_frame.setSizePolicy(sizePolicy)
        self.bottom_layout_right_frame.setStyleSheet("QFrame {\n"
"\n"
"}")
        self.bottom_layout_right_frame.setObjectName("bottom_layout_right_frame")
        self.bottom_layout_right = QtWidgets.QVBoxLayout(self.bottom_layout_right_frame)
        self.bottom_layout_right.setContentsMargins(11, 11, 11, 11)
        self.bottom_layout_right.setSpacing(6)
        self.bottom_layout_right.setObjectName("bottom_layout_right")
        self.bottom_layout_combo_right = QtWidgets.QComboBox(self.bottom_layout_right_frame)
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        self.bottom_layout_combo_right.setFont(font)
        self.bottom_layout_combo_right.setObjectName("bottom_layout_combo_right")
        self.bottom_layout_right.addWidget(self.bottom_layout_combo_right)
        self.bottom_layout_table_right = QtWidgets.QTableWidget(self.bottom_layout_right_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bottom_layout_table_right.sizePolicy().hasHeightForWidth())
        self.bottom_layout_table_right.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        self.bottom_layout_table_right.setFont(font)
        self.bottom_layout_table_right.setStyleSheet("QFrame {\n"
"    background: rgbrgb(54, 59, 77);\n"
"    \n"
"}")
        self.bottom_layout_table_right.setObjectName("bottom_layout_table_right")
        self.bottom_layout_table_right.setColumnCount(0)
        self.bottom_layout_table_right.setRowCount(0)
        self.bottom_layout_right.addWidget(self.bottom_layout_table_right)
        self.right_constraint.addWidget(self.bottom_layout_right_frame, 1, 0, 1, 1)
        self.gridLayout_2.addLayout(self.right_constraint, 1, 2, 1, 1)
        self.search_box_frame = QtWidgets.QFrame(self.page)
        self.search_box_frame.setMaximumSize(QtCore.QSize(16777215, 55))
        self.search_box_frame.setStyleSheet("QFrame {\n"
"    padding: 0px;\n"
"}")
        self.search_box_frame.setObjectName("search_box_frame")
        self.search_box_horizontal_layout = QtWidgets.QHBoxLayout(self.search_box_frame)
        self.search_box_horizontal_layout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.search_box_horizontal_layout.setContentsMargins(11, 11, 11, 11)
        self.search_box_horizontal_layout.setSpacing(6)
        self.search_box_horizontal_layout.setObjectName("search_box_horizontal_layout")
        self.search_box = QtWidgets.QLineEdit(self.search_box_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.search_box.sizePolicy().hasHeightForWidth())
        self.search_box.setSizePolicy(sizePolicy)
        self.search_box.setMaximumSize(QtCore.QSize(200, 22))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        self.search_box.setFont(font)
        self.search_box.setStyleSheet("QLineEdit:focus {\n"
"    border-style: none;\n"
"    border: 60px;\n"
"}")
        self.search_box.setInputMask("")
        self.search_box.setText("")
        self.search_box.setObjectName("search_box")
        self.search_box_horizontal_layout.addWidget(self.search_box)
        self.trading_type_combo = QtWidgets.QComboBox(self.search_box_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.trading_type_combo.sizePolicy().hasHeightForWidth())
        self.trading_type_combo.setSizePolicy(sizePolicy)
        self.trading_type_combo.setMaximumSize(QtCore.QSize(16777215, 22))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        self.trading_type_combo.setFont(font)
        self.trading_type_combo.setObjectName("trading_type_combo")
        self.trading_type_combo.addItem("")
        self.trading_type_combo.addItem("")
        self.search_box_horizontal_layout.addWidget(self.trading_type_combo)
        self.gridLayout_2.addWidget(self.search_box_frame, 0, 0, 1, 1)
        self.center_constraint_frame = QtWidgets.QFrame(self.page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.center_constraint_frame.sizePolicy().hasHeightForWidth())
        self.center_constraint_frame.setSizePolicy(sizePolicy)
        self.center_constraint_frame.setMaximumSize(QtCore.QSize(16777215, 1000))
        self.center_constraint_frame.setStyleSheet("")
        self.center_constraint_frame.setObjectName("center_constraint_frame")
        self.center_constraint = QtWidgets.QGridLayout(self.center_constraint_frame)
        self.center_constraint.setContentsMargins(11, 11, 11, 11)
        self.center_constraint.setSpacing(6)
        self.center_constraint.setObjectName("center_constraint")
        self.center_combo_box_layout = QtWidgets.QHBoxLayout()
        self.center_combo_box_layout.setContentsMargins(-1, -1, -1, 0)
        self.center_combo_box_layout.setObjectName("center_combo_box_layout")
        self.statement_type_combo_center = QtWidgets.QComboBox(self.center_constraint_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statement_type_combo_center.sizePolicy().hasHeightForWidth())
        self.statement_type_combo_center.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        self.statement_type_combo_center.setFont(font)
        self.statement_type_combo_center.setStyleSheet("")
        self.statement_type_combo_center.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToMinimumContentsLength)
        self.statement_type_combo_center.setFrame(False)
        self.statement_type_combo_center.setObjectName("statement_type_combo_center")
        self.statement_type_combo_center.addItem("")
        self.statement_type_combo_center.addItem("")
        self.statement_type_combo_center.addItem("")
        self.statement_type_combo_center.addItem("")
        self.center_combo_box_layout.addWidget(self.statement_type_combo_center)
        self.time_frame_combo_center = QtWidgets.QComboBox(self.center_constraint_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.time_frame_combo_center.sizePolicy().hasHeightForWidth())
        self.time_frame_combo_center.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        self.time_frame_combo_center.setFont(font)
        self.time_frame_combo_center.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToMinimumContentsLength)
        self.time_frame_combo_center.setFrame(False)
        self.time_frame_combo_center.setObjectName("time_frame_combo_center")
        self.time_frame_combo_center.addItem("")
        self.time_frame_combo_center.addItem("")
        self.center_combo_box_layout.addWidget(self.time_frame_combo_center)
        self.center_constraint.addLayout(self.center_combo_box_layout, 0, 0, 1, 1)
        self.center_table_frame = QtWidgets.QFrame(self.center_constraint_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.center_table_frame.sizePolicy().hasHeightForWidth())
        self.center_table_frame.setSizePolicy(sizePolicy)
        self.center_table_frame.setStyleSheet("QFrame {\n"
"    background: rgb(39, 41, 60);\n"
"    alternate-background-color: rgb(47, 51, 69);\n"
"    color: rgb(245,245,245);\n"
"    gridline-color: rgb(24, 24, 37);\n"
"    border: 0px;\n"
"    border-style: none;\n"
"    padding: 3px;\n"
"    margin: 0px;\n"
"}\n"
"\n"
"QHeaderView {\n"
"    \n"
"}")
        self.center_table_frame.setObjectName("center_table_frame")
        self.center_frame_layout = QtWidgets.QGridLayout(self.center_table_frame)
        self.center_frame_layout.setContentsMargins(11, 11, 11, 11)
        self.center_frame_layout.setSpacing(6)
        self.center_frame_layout.setObjectName("center_frame_layout")
        self.center_statements_table = QtWidgets.QTableWidget(self.center_table_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.center_statements_table.sizePolicy().hasHeightForWidth())
        self.center_statements_table.setSizePolicy(sizePolicy)
        self.center_statements_table.setMinimumSize(QtCore.QSize(0, 200))
        self.center_statements_table.setMaximumSize(QtCore.QSize(16777215, 1000))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        self.center_statements_table.setFont(font)
        self.center_statements_table.setStyleSheet("QHeaderView {\n"
"    padding: 0px;\n"
"    margin: 0px;\n"
"    color: black;\n"
"    background-color: white;\n"
"}")
        self.center_statements_table.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.center_statements_table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.center_statements_table.setAutoScroll(False)
        self.center_statements_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.center_statements_table.setTabKeyNavigation(False)
        self.center_statements_table.setProperty("showDropIndicator", False)
        self.center_statements_table.setDragDropOverwriteMode(False)
        self.center_statements_table.setAlternatingRowColors(True)
        self.center_statements_table.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.center_statements_table.setIconSize(QtCore.QSize(0, 0))
        self.center_statements_table.setShowGrid(False)
        self.center_statements_table.setGridStyle(QtCore.Qt.SolidLine)
        self.center_statements_table.setWordWrap(False)
        self.center_statements_table.setCornerButtonEnabled(False)
        self.center_statements_table.setRowCount(13)
        self.center_statements_table.setColumnCount(2)
        self.center_statements_table.setObjectName("center_statements_table")
        item = QtWidgets.QTableWidgetItem()
        self.center_statements_table.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.center_statements_table.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.center_statements_table.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.center_statements_table.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.center_statements_table.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.center_statements_table.setItem(3, 0, item)
        self.center_statements_table.horizontalHeader().setVisible(True)
        self.center_statements_table.horizontalHeader().setCascadingSectionResizes(False)
        self.center_statements_table.horizontalHeader().setDefaultSectionSize(254)
        self.center_statements_table.horizontalHeader().setSortIndicatorShown(False)
        self.center_statements_table.horizontalHeader().setStretchLastSection(True)
        self.center_statements_table.verticalHeader().setVisible(False)
        self.center_statements_table.verticalHeader().setCascadingSectionResizes(False)
        self.center_statements_table.verticalHeader().setDefaultSectionSize(62)
        self.center_statements_table.verticalHeader().setStretchLastSection(False)
        self.center_frame_layout.addWidget(self.center_statements_table, 0, 0, 1, 1)
        self.center_constraint.addWidget(self.center_table_frame, 1, 0, 1, 1)
        self.gridLayout_2.addWidget(self.center_constraint_frame, 1, 1, 1, 1)
        self.top_bar_page1 = QtWidgets.QFrame(self.page)
        self.top_bar_page1.setObjectName("top_bar_page1")
        self.center_top_bar_page1 = QtWidgets.QHBoxLayout(self.top_bar_page1)
        self.center_top_bar_page1.setContentsMargins(11, 11, 11, 11)
        self.center_top_bar_page1.setSpacing(6)
        self.center_top_bar_page1.setObjectName("center_top_bar_page1")
        self.gridLayout_2.addWidget(self.top_bar_page1, 0, 1, 1, 1)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.page_2.sizePolicy().hasHeightForWidth())
        self.page_2.setSizePolicy(sizePolicy)
        self.page_2.setObjectName("page_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.page_2)
        self.gridLayout_4.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_4.setSpacing(6)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.left_frame_page2 = QtWidgets.QFrame(self.page_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.left_frame_page2.sizePolicy().hasHeightForWidth())
        self.left_frame_page2.setSizePolicy(sizePolicy)
        self.left_frame_page2.setStyleSheet("QFrame {\n"
"    border: 0px;\n"
"    border-style: none;\n"
"    padding: 0px;\n"
"    margin: 6px;\n"
"}")
        self.left_frame_page2.setObjectName("left_frame_page2")
        self.left_page_2 = QtWidgets.QGridLayout(self.left_frame_page2)
        self.left_page_2.setContentsMargins(11, 11, 11, 11)
        self.left_page_2.setSpacing(6)
        self.left_page_2.setObjectName("left_page_2")
        self.news_table = QtWidgets.QTableWidget(self.left_frame_page2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.news_table.sizePolicy().hasHeightForWidth())
        self.news_table.setSizePolicy(sizePolicy)
        self.news_table.setStyleSheet("QFrame {\n"
"    background: none;\n"
"}")
        self.news_table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.news_table.setAutoScroll(False)
        self.news_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.news_table.setTabKeyNavigation(False)
        self.news_table.setProperty("showDropIndicator", False)
        self.news_table.setDragDropOverwriteMode(False)
        self.news_table.setAlternatingRowColors(True)
        self.news_table.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.news_table.setCornerButtonEnabled(False)
        self.news_table.setColumnCount(2)
        self.news_table.setObjectName("news_table")
        self.news_table.setRowCount(8)
        item = QtWidgets.QTableWidgetItem()
        self.news_table.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.news_table.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.news_table.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.news_table.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.news_table.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.news_table.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.news_table.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.news_table.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.news_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.news_table.setHorizontalHeaderItem(1, item)
        self.news_table.horizontalHeader().setMinimumSectionSize(19)
        self.news_table.horizontalHeader().setSortIndicatorShown(False)
        self.news_table.horizontalHeader().setStretchLastSection(True)
        self.news_table.verticalHeader().setVisible(False)
        self.left_page_2.addWidget(self.news_table, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.left_frame_page2, 1, 0, 1, 1)
        self.right_frame_page2 = QtWidgets.QFrame(self.page_2)
        self.right_frame_page2.setObjectName("right_frame_page2")
        self.right_page_2 = QtWidgets.QGridLayout(self.right_frame_page2)
        self.right_page_2.setContentsMargins(11, 11, 11, 11)
        self.right_page_2.setSpacing(6)
        self.right_page_2.setObjectName("right_page_2")
        self.gridLayout_4.addWidget(self.right_frame_page2, 1, 2, 1, 1)
        self.center_constraint_frame_page_2 = QtWidgets.QFrame(self.page_2)
        self.center_constraint_frame_page_2.setMaximumSize(QtCore.QSize(16777215, 1000))
        self.center_constraint_frame_page_2.setStyleSheet("")
        self.center_constraint_frame_page_2.setObjectName("center_constraint_frame_page_2")
        self.center_constraint_2 = QtWidgets.QGridLayout(self.center_constraint_frame_page_2)
        self.center_constraint_2.setContentsMargins(11, 11, 11, 11)
        self.center_constraint_2.setSpacing(6)
        self.center_constraint_2.setObjectName("center_constraint_2")
        self.gridLayout_4.addWidget(self.center_constraint_frame_page_2, 1, 1, 1, 1)
        self.page_frame_page2 = QtWidgets.QFrame(self.page_2)
        self.page_frame_page2.setStyleSheet("QFrame {\n"
"    padding-left: 9px;\n"
"    padding-right: 9px;\n"
"}")
        self.page_frame_page2.setObjectName("page_frame_page2")
        self.page_change_layout_page2_3 = QtWidgets.QHBoxLayout(self.page_frame_page2)
        self.page_change_layout_page2_3.setContentsMargins(1, 1, 1, 1)
        self.page_change_layout_page2_3.setSpacing(6)
        self.page_change_layout_page2_3.setObjectName("page_change_layout_page2_3")
        self.last_page_button_page2 = QtWidgets.QPushButton(self.page_frame_page2)
        self.last_page_button_page2.setObjectName("last_page_button_page2")
        self.page_change_layout_page2_3.addWidget(self.last_page_button_page2)
        self.next_page_button_page2 = QtWidgets.QPushButton(self.page_frame_page2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.next_page_button_page2.sizePolicy().hasHeightForWidth())
        self.next_page_button_page2.setSizePolicy(sizePolicy)
        self.next_page_button_page2.setDefault(False)
        self.next_page_button_page2.setObjectName("next_page_button_page2")
        self.page_change_layout_page2_3.addWidget(self.next_page_button_page2)
        self.gridLayout_4.addWidget(self.page_frame_page2, 0, 2, 1, 1)
        self.search_box_frame_2 = QtWidgets.QFrame(self.page_2)
        self.search_box_frame_2.setMaximumSize(QtCore.QSize(16777215, 55))
        self.search_box_frame_2.setStyleSheet("QFrame {\n"
"    padding: 0px;\n"
"}")
        self.search_box_frame_2.setObjectName("search_box_frame_2")
        self.search_box_horizontal_layout_2 = QtWidgets.QHBoxLayout(self.search_box_frame_2)
        self.search_box_horizontal_layout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.search_box_horizontal_layout_2.setContentsMargins(11, 11, 11, 11)
        self.search_box_horizontal_layout_2.setSpacing(6)
        self.search_box_horizontal_layout_2.setObjectName("search_box_horizontal_layout_2")
        self.search_box_2 = QtWidgets.QLineEdit(self.search_box_frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.search_box_2.sizePolicy().hasHeightForWidth())
        self.search_box_2.setSizePolicy(sizePolicy)
        self.search_box_2.setMaximumSize(QtCore.QSize(200, 22))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        self.search_box_2.setFont(font)
        self.search_box_2.setInputMask("")
        self.search_box_2.setText("")
        self.search_box_2.setObjectName("search_box_2")
        self.search_box_horizontal_layout_2.addWidget(self.search_box_2)
        self.trading_type_combo_2 = QtWidgets.QComboBox(self.search_box_frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.trading_type_combo_2.sizePolicy().hasHeightForWidth())
        self.trading_type_combo_2.setSizePolicy(sizePolicy)
        self.trading_type_combo_2.setMaximumSize(QtCore.QSize(16777215, 22))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        self.trading_type_combo_2.setFont(font)
        self.trading_type_combo_2.setObjectName("trading_type_combo_2")
        self.trading_type_combo_2.addItem("")
        self.trading_type_combo_2.addItem("")
        self.search_box_horizontal_layout_2.addWidget(self.trading_type_combo_2)
        self.gridLayout_4.addWidget(self.search_box_frame_2, 0, 0, 1, 1)
        self.top_bar_page2 = QtWidgets.QFrame(self.page_2)
        self.top_bar_page2.setObjectName("top_bar_page2")
        self.center_top_bar_page2 = QtWidgets.QHBoxLayout(self.top_bar_page2)
        self.center_top_bar_page2.setContentsMargins(11, 11, 11, 11)
        self.center_top_bar_page2.setSpacing(6)
        self.center_top_bar_page2.setObjectName("center_top_bar_page2")
        self.gridLayout_4.addWidget(self.top_bar_page2, 0, 1, 1, 1)
        self.stackedWidget.addWidget(self.page_2)
        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralWidget)
        self.actionTest2 = QtWidgets.QAction(MainWindow)
        self.actionTest2.setObjectName("actionTest2")

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MASDAR"))
        self.last_page_button_page1.setText(_translate("MainWindow", "Last Page"))
        self.next_page_button_page1.setText(_translate("MainWindow", "Next Page"))
        self.time_frame_combo_box.setItemText(0, _translate("MainWindow", "Today"))
        self.time_frame_combo_box.setItemText(1, _translate("MainWindow", "5 Days"))
        self.time_frame_combo_box.setItemText(2, _translate("MainWindow", "1 Week"))
        self.time_frame_combo_box.setItemText(3, _translate("MainWindow", "1 Month"))
        self.time_frame_combo_box.setItemText(4, _translate("MainWindow", "3 Months"))
        self.time_frame_combo_box.setItemText(5, _translate("MainWindow", "6 Months"))
        self.time_frame_combo_box.setItemText(6, _translate("MainWindow", "YTD"))
        self.time_frame_combo_box.setItemText(7, _translate("MainWindow", "3 Years"))
        self.time_frame_combo_box.setItemText(8, _translate("MainWindow", "5 Years"))
        self.time_frame_combo_box.setItemText(9, _translate("MainWindow", "10 Years"))
        self.company_name_label.setText(_translate("MainWindow", "company"))
        self.stock_price_label.setText(_translate("MainWindow", "price"))
        self.company_summary.setText(_translate("MainWindow", "TextLabel"))
        self.copmany_info_comboBox.setItemText(0, _translate("MainWindow", "Description"))
        self.copmany_info_comboBox.setItemText(1, _translate("MainWindow", "Basic Information"))
        self.search_box.setPlaceholderText(_translate("MainWindow", "Ticker"))
        self.trading_type_combo.setItemText(0, _translate("MainWindow", "Fundamental Analysis"))
        self.trading_type_combo.setItemText(1, _translate("MainWindow", "Technical Analysis"))
        self.statement_type_combo_center.setItemText(0, _translate("MainWindow", "Income Statement"))
        self.statement_type_combo_center.setItemText(1, _translate("MainWindow", "Balance Sheet"))
        self.statement_type_combo_center.setItemText(2, _translate("MainWindow", "Cash Flows"))
        self.statement_type_combo_center.setItemText(3, _translate("MainWindow", "Key Ratios"))
        self.time_frame_combo_center.setItemText(0, _translate("MainWindow", "Annual"))
        self.time_frame_combo_center.setItemText(1, _translate("MainWindow", "Quarterly"))
        item = self.center_statements_table.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.center_statements_table.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.center_statements_table.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "New Row"))
        __sortingEnabled = self.center_statements_table.isSortingEnabled()
        self.center_statements_table.setSortingEnabled(False)
        item = self.center_statements_table.item(0, 0)
        item.setText(_translate("MainWindow", "555"))
        item = self.center_statements_table.item(1, 0)
        item.setText(_translate("MainWindow", "5555"))
        item = self.center_statements_table.item(3, 0)
        item.setText(_translate("MainWindow", "555"))
        self.center_statements_table.setSortingEnabled(__sortingEnabled)
        self.news_table.setSortingEnabled(True)
        item = self.news_table.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.news_table.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.news_table.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.news_table.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.news_table.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.news_table.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.news_table.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.news_table.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.news_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "New Column"))
        item = self.news_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "New Column"))
        self.last_page_button_page2.setText(_translate("MainWindow", "Last Page"))
        self.next_page_button_page2.setText(_translate("MainWindow", "Next Page"))
        self.search_box_2.setPlaceholderText(_translate("MainWindow", "Ticker"))
        self.trading_type_combo_2.setItemText(0, _translate("MainWindow", "Fundamental Analysis"))
        self.trading_type_combo_2.setItemText(1, _translate("MainWindow", "Technical Analysis"))
        self.actionTest2.setText(_translate("MainWindow", "Test2"))

