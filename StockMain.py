import quandl
import sys
import requests
import json
import mainwindow
import datetime as dtime
from dateutil.relativedelta import relativedelta

from pprint import  pprint
from PyQt5.QtWidgets import  (QApplication, QWidget, QLabel, QLineEdit, QPushButton, QToolTip,
                              QMessageBox, QDesktopWidget, QMainWindow, QMenu, QAction, qApp,
                              QHBoxLayout, QVBoxLayout, QInputDialog, QGridLayout)
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.dates import DateFormatter, DayLocator, date2num
from matplotlib.finance import candlestick2_ohlc
from requests.auth import HTTPBasicAuth
from pandas.io.json import json_normalize

#Main class
class MainClass(QMainWindow, mainwindow.Ui_MainWindow):
    quandl.ApiConfig.api_key = 'uWUJWnrbmYn4xydaHzR3'
    quandl.ApiConfig.api_version = '2017-11-11'

    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        intrinio_username = '1125400bde12246e110be20eb51bbc39'
        intrinio_password = '8b011688d9ae1b93fac9f2ecf21ac1f2'
        self.request_auth = HTTPBasicAuth(intrinio_username, intrinio_password)
        self.now = dtime.datetime.now()
        self.today_date = dtime.datetime.today()

        self.inputTicker()

        QWidget.updateGeometry(self)

    #centers the app window
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    #Message box when you close the program
    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message',
            "Are you sure?", QMessageBox.Yes, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

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

        print("test")
        self.search_box.returnPressed.connect(self.search_button.click)
        self.search_button.clicked.connect(self.displayTicker)

    def displayTicker(self):
        self.tickerVar = self.search_box.text()
        self.stock_name.setText(self.tickerVar.upper())
        r = requests.get(
            'https://api.intrinio.com/financials/reported?identifier=' + self.tickerVar.upper() +
            '&statement=income_statement&fiscal_year=2015&fiscal_period=FY',
            auth=self.request_auth)

        self.finance_data = json.loads(r.text)
        self.normalized_fin = json_normalize(self.finance_data['data'])

        six_months = self.today_date - relativedelta(months=6)

        try:
            del self.normalized_fin['domain_tag']
        except KeyError:
            pass

        self.financial_stm_label.setText(str(self.normalized_fin))

        self.requested_time_frame = str(self.time_frame_combo_box.currentText())
        self.user_date = self.today_date
        self.time_frame_func(self.requested_time_frame)


        try:
            self.data = quandl.get('WIKI/' + self.tickerVar, start_date=self.user_date, end_date=self.today_date,
                               order="asc|desc", collapse='daily')
        except (RuntimeError, TypeError, NameError, AttributeError):
            pass

        try:
            print(self.normalized_fin)
            self.plotData()
        except (AttributeError):
            pass

    #function to plot the data from displayTicker
    def plotData(self):
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        ax = self.figure.add_subplot(111)
        ax.clear()

        ##Work on date time

        import matplotlib.ticker as ticker

        candlestick2_ohlc(ax, self.data.reset_index()['Open'], self.data.reset_index()['High'],
                          self.data.reset_index()['Low'], self.data.reset_index()['Close'], width=0.6)
        date_format = '%Y-%m-%d'
        x_date = [dtime.datetime.strftime(i, date_format) for i in self.data.reset_index()['Date']]
        ax.xaxis.set_major_locator(ticker.MaxNLocator(6))

        def mydate(x, pos):
            try:
                return x_date[int(x)]
            except IndexError:
                return ''
        x_date = x_date[::-1]
        y_price = self.data.reset_index()['Close']
        ax.xaxis.set_major_formatter(ticker.FuncFormatter(mydate))
        ax.plot(x_date, y_price)
        ax = self.figure.suptitle(self.tickerVar.upper(), fontsize=20)
        ax = self.figure.autofmt_xdate()
        ax = self.figure.tight_layout()
        self.graph_layout.addWidget(self.canvas)
        self.canvas.draw()


    def time_frame_func(self, argument):
        switcher = {
            'Today': (dtime.datetime.today()),
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
        #self.user_date = userdate

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainClass()
    main.show()
    app.exec_()
    #sys.exit(app.exec_())


# print(data)
