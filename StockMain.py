import quandl
import sys
import requests
import json
import mainwindow
import datetime as dtime
import locale
from dateutil.relativedelta import relativedelta
import collections

import PyQt5
from PyQt5.QtCore import QTimeLine
from PyQt5.QtWidgets import  (QApplication, QWidget, QLabel, QLineEdit, QPushButton, QToolTip,
                              QMessageBox, QDesktopWidget, QMainWindow, QMenu, QAbstractScrollArea, qApp,
                              QHeaderView, QTableWidgetItem)
from matplotlib import  transforms, colors
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.dates import DateFormatter, DayLocator, date2num, num2date
import matplotlib.finance as finance
from requests.auth import HTTPBasicAuth
from pandas.io.json import json_normalize

#Main class
class MainClass(QMainWindow, mainwindow.Ui_MainWindow):
    quandl.ApiConfig.api_key = 'uWUJWnrbmYn4xydaHzR3'
    quandl.ApiConfig.api_version = '2017-11-11'



    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.change_page(0)
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)

        intrinio_username = '1125400bde12246e110be20eb51bbc39'
        intrinio_password = '8b011688d9ae1b93fac9f2ecf21ac1f2'
        #intrinio_username = '8eac0c8e0c05166514a6b0c910a764dc'
        #intrinio_password = 'ea291002ebb39759301ebe409b00ce4d'

        self.api_base_url = 'https://api.intrinio.com'
        self.request_auth = HTTPBasicAuth(intrinio_username, intrinio_password)
        self.today_date = dtime.datetime.today()

        self.next_page_button_page1.clicked.connect(lambda:self.change_page(1))
        self.next_page_button_page2.clicked.connect(lambda: self.change_page(1))
        self.last_page_button_page1.clicked.connect(lambda: self.change_page(0))
        self.last_page_button_page2.clicked.connect(lambda: self.change_page(0))

        self.inputTicker()

        QWidget.updateGeometry(self)

    #centers the app window
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    hide_func = """
    #Message box when you close the program
    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message',
            "Are you sure?", QMessageBox.Yes, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
    """

    #right click menu
    def contextMenuEvent(self, event):
        cmenu = QMenu(self)

        newAct = cmenu.addAction("New")
        opnAct = cmenu.addAction("Open")
        quitAct = cmenu.addAction("Quit")
        action = cmenu.exec_(self.mapToGlobal(event.pos()))

        if action == quitAct:
            qApp.quit()

    #input text for the ticker
    def inputTicker(self):
        self.time_frame_combo_box.activated.connect(self.displayTicker)
        self.statement_type_combo_center.activated.connect(self.displayTicker)

        self.search_box_2.setText(self.search_box.text())
        self.search_box.returnPressed.connect(self.search_text_page1)
        self.search_box_2.returnPressed.connect(self.search_text_page2)

    def search_text_page2(self):
        self.search_box.setText(self.search_box_2.text())
        self.displayTicker()

    def search_text_page1(self):
        self.search_box_2.setText(self.search_box.text())
        self.displayTicker()


    def queryHolder(self):
        self.stock_price_url = self.api_base_url + '/prices'
        self.stock_price_query = {
            'identifier': self.tickerVar.upper(),
            'start_date': str(self.user_date)
        }

        self.statements_url = self.api_base_url + '/financials/standardized'
        self.statements_query = {
            'identifier': self.tickerVar.upper(),
            'statement': self.statement_request,
            'fiscal_year': '2016',
            'fiscal_period': 'FY'
        }

        self.company_info_url = self.api_base_url + '/companies'

        self.news_url = self.api_base_url + '/news'
        self.identifier_query = {
            'identifier': self.tickerVar.upper()
        }

        self.key_values_url = self.api_base_url + '/data_point'
        self.key_values_query = {
            'identifier': self.tickerVar.upper(),
            'item': 'close_price,open_price,low_price,high_price,52_week_high,52_week_low,marketcap,'
                    'volume,average_daily_volume,pricetoearnings,basiceps,beta,dividend'
        }

    def jsonRequests(self):
        #stock prices
        stock_prices_json = requests.get(self.stock_price_url,params=self.stock_price_query,
                                                    auth=self.request_auth )

        #basis financial statement values
        financial_statements_json = requests.get(self.statements_url, params=self.statements_query,
            auth=self.request_auth)

        #company info
        company_info_json = requests.get(self.company_info_url, params=self.stock_price_query,
                                         auth=self.request_auth)

        #news
        news_json = requests.get(self.news_url, params=self.identifier_query, auth=self.request_auth)

        #key values
        keyvalues_json = requests.get(self.key_values_url,params=self.key_values_query, auth=self.request_auth)

        key_values = json.loads(keyvalues_json.text)
        stock_prices = json.loads(stock_prices_json.text)
        finance_data = json.loads(financial_statements_json.text)
        self.company_info = json.loads(company_info_json.text)
        company_news = json.loads(news_json.text)

        try:
            self.normalized_keyvalues = json_normalize(key_values['data'])
            self.normalized_news = json_normalize(company_news['data'])
            self.normalized_prices = json_normalize(stock_prices['data'])
            self.normalized_fin = json_normalize(finance_data['data'])
        except AttributeError:
            pass

    def displayTicker(self):
        if not self.search_box.text() == "":
            self.tickerVar = self.search_box.text()

            self.requested_time_frame = str(self.time_frame_combo_box.currentText())
            self.time_frame_func(self.requested_time_frame)

            self.requested_statement = str(self.statement_type_combo_center.currentText())
            self.statement_type_func(self.requested_statement)

            self.fiscal_year = '2016'

            self.queryHolder()
            self.jsonRequests()

            try:
                self.data_stock_price = self.normalized_prices
                self.company_name_label.setText('Company Name\n' + self.company_info['legal_name']
                                                + '\n' + self.company_info['ticker'] + ' ('
                                                + self.company_info['stock_exchange'] + ')')
                self.stock_price_label.setText('Last Trade\n' + '$' + str(self.data_stock_price['close'][0]))
                self.company_summary.setText(self.company_info['long_description'])

                self.financeStatements()
                self.news_page()

                self.plotData()
                self.key_stats()
            except (KeyError, TypeError, NameError, AttributeError):
                pass



    #financial statements
    def financeStatements(self):
        self.center_statements_table.setRowCount(len(self.normalized_fin))
        self.center_statements_table.setColumnCount(2)
        self.center_statements_table.setHorizontalHeaderLabels([str(self.statement_type_combo_center.currentText()), self.fiscal_year])
        self.center_statements_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        headerView = self.center_statements_table.horizontalHeader();

        for column, key in enumerate(self.normalized_fin):
            for row, item in enumerate(self.normalized_fin[key]):
                str_item = str(item)
                xblr_key = QTableWidgetItem(str_item)
                self.center_statements_table.setItem(row, column, xblr_key)

        headerView.setStretchLastSection(True)
        self.center_statements_table.resizeColumnsToContents()


    #function to plot the data from displayTicker
    def plotData(self):
        ax = self.figure.add_subplot(111)
        #ax2 = ax.twinx()
        ax.clear()

        import matplotlib.ticker as ticker


        finance.candlestick2_ohlc(ax, self.data_stock_price['open'], self.data_stock_price['high'],
                          self.data_stock_price['low'], self.data_stock_price['close']
                          ,width=0.7, colorup='g', colordown='r')

        stock_date = [dtime.datetime.strptime(j, "%Y-%m-%d") for j in self.data_stock_price['date']]
        date_format = '%b-%y'
        x_date = [dtime.datetime.strftime(i, date_format) for i in stock_date]
        ax.xaxis.set_major_locator(ticker.MaxNLocator(6))
        ax.set_facecolor((.2117, .2314, .302))
        def mydate(x, pos):
            try:
                return x_date[int(x)]
            except IndexError:
                return ''

        x_date = x_date[::-1]
        ax.xaxis.set_major_formatter(ticker.FuncFormatter(mydate))
        ax.yaxis.tick_right()

        self.graph_layout.addWidget(self.canvas)
        self.canvas.draw_idle()


    def time_frame_func(self, argument):
        switcher = {
            'Today': (dtime.datetime.today() - relativedelta(days=2)),
            '5 Days': (dtime.datetime.today() - relativedelta(days=5)),
            '1 Week': (dtime.datetime.today() - relativedelta(days=7)),
            '1 Month': (dtime.datetime.today() - relativedelta(months=1)),
            '3 Months': (dtime.datetime.today() - relativedelta(months=3)),
            '6 Months': (dtime.datetime.today() - relativedelta(months=6)),
            'YTD': (dtime.datetime(dtime.datetime.today().year, 1, 1)),
            '3 Years': (dtime.datetime.today() - relativedelta(years=3)),
            '5 Years': (dtime.datetime.today() - relativedelta(years=5)),
            '10 Years': (dtime.datetime.today() - relativedelta(years=5))

        }
        self.user_date = switcher.get(argument , "nothing")

    def statement_type_func(self, argument):
        switcher = {
            'Income Statement': 'income_statement',
            'Balance Sheet': 'balance_sheet',
            'Cash Flows': 'cash_flow_statement',
            'Key Ratios': 'calculations'
        }
        self.statement_request = switcher.get(argument, "calculations")

    def change_page(self, page):
        self.stackedWidget.setCurrentIndex(page)

    def news_page(self):
        self.news_table.setRowCount(len(self.normalized_news))
        self.news_table.setHorizontalHeaderLabels(
            ['Released', 'Headline'])
        publication_date = [dtime.datetime.strptime(j, "%Y-%m-%dT%H:%M:%S.000+00:00") for j in self.normalized_news['publication_date']]
        date_format = '%b-%d-%y %I:%M%p'
        news_date = [dtime.datetime.strftime(i, date_format) for i in publication_date]

        for key in self.normalized_news:
                if (key == 'title'):
                    for row, item in enumerate(self.normalized_news[key]):
                        str_item = str(item)
                        xblr_key = QTableWidgetItem(str_item)
                        self.news_table.setItem(row, 1, xblr_key)

        for rowd, date in enumerate(news_date):
            date_key = QTableWidgetItem(date)
            self.news_table.setItem(rowd, 0, date_key)

    def key_stats(self):
        self.key_table_left.setRowCount(len(self.normalized_keyvalues['item']))
        for row, item in enumerate(self.normalized_keyvalues['item']):
            itemkey = QTableWidgetItem(str(item))
            self.key_table_left.setItem(row, 0, itemkey)

        for row, value in enumerate(self.normalized_keyvalues['value']):
            valuekey = QTableWidgetItem(str(value))
            self.key_table_left.setItem(row, 1, valuekey)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainClass()
    main.show()
    app.exec_()
    #sys.exit(app.exec_())

