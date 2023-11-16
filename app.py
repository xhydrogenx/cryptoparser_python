import sys

import ccxt
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QRunnable, QThread, QThreadPool
from PyQt6.QtWidgets import QApplication
from module1.parse_crypto import get_data, save_to_json


class ParserRunnable(QRunnable):
    def __init__(self, ticker, market, window):
        super().__init__()
        self.ticker = ticker
        self.market = market
        self.exchange = getattr(ccxt, self.market)()
        self.window = window
        self._stopped = False

    def run(self):
        while not self._stopped:
            try:
                current = self.exchange.fetch_ticker(self.ticker)
                self.window.current_price.setText(str(current["last"]))
                print(current['last'])
                QThread.msleep(5000)
            except Exception as e:
                print(f'Error: {e}')
                self._stopped = True

    def stop(self):
        self._stopped = True
        print("stopping loop")
        self.exchange.close()


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(798, 589)

        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.graphicsView = QtWidgets.QGraphicsView(parent=self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(40, 260, 721, 291))
        self.graphicsView.setAlignment(QtCore.Qt.AlignmentFlag.AlignJustify | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.graphicsView.setObjectName("graphicsView")

        self.gridLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(40, 30, 231, 191))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")

        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setVerticalSpacing(6)
        self.gridLayout.setObjectName("gridLayout")

        self.comboBox = QtWidgets.QComboBox(parent=self.gridLayoutWidget)
        self.comboBox.setCurrentText("132")
        self.comboBox.setObjectName("comboBox")
        self.gridLayout.addWidget(self.comboBox, 3, 0, 1, 1)

        self.label = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.pair_input = QtWidgets.QLineEdit(parent=self.gridLayoutWidget)
        self.pair_input.setMaximumSize(QtCore.QSize(200, 40))
        self.pair_input.setObjectName("pair_input")
        self.gridLayout.addWidget(self.pair_input, 1, 0, 1, 1)

        self.comboBox_2 = QtWidgets.QComboBox(parent=self.gridLayoutWidget)
        self.comboBox_2.setObjectName("comboBox_2")
        self.gridLayout.addWidget(self.comboBox_2, 2, 0, 1, 1)

        self.pushButton = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 4, 0, 1, 1)

        self.gridLayoutWidget_2 = QtWidgets.QWidget(parent=self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(330, 30, 301, 191))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")

        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")

        self.label_2 = QtWidgets.QLabel(parent=self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)

        self.label_3 = QtWidgets.QLabel(parent=self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)

        current_font = QtGui.QFont()
        current_font.setPointSize(18)

        self.current_price = QtWidgets.QLabel(parent=self.gridLayoutWidget_2)
        self.current_price.setText("")
        self.current_price.setStyleSheet("background-color: #EFEFEF;")
        self.current_price.setFont(current_font)
        self.current_price.setObjectName("current_price")
        self.gridLayout_2.addWidget(self.current_price, 0, 1, 1, 1)

        self.label_4 = QtWidgets.QLabel(parent=self.gridLayoutWidget_2)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 2, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.scene = QtWidgets.QGraphicsScene()

        self.scene.addText("Hello, world!")

        self.graphicsView.setScene(self.scene)

        self.comboBox.addItems(["Binance", "Kucoin", "Coinbase", "Yobit", "Bybit"])
        self.comboBox_2.addItems(["Минута", "Час", "Месяц", "Год"])

        self.pushButton.clicked.connect(self.on_push_button_clicked)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CryptoParser"))
        self.comboBox.setPlaceholderText(_translate("MainWindow", "Выберите биржу"))

        self.label.setText(_translate("MainWindow", "Валютная пара:"))
        self.pair_input.setPlaceholderText(_translate("MainWindow", "Например: BTC/USDT"))
        self.comboBox_2.setPlaceholderText(_translate("MainWindow", "Выберите интервал"))
        self.pushButton.setText(_translate("MainWindow", "Пуск"))
        self.label_2.setText(_translate("MainWindow", "Текущий курс:"))
        self.label_3.setText(_translate("MainWindow", "Рекомендации по паре:"))

        self.label_4.setText(_translate("MainWindow", "TextLabel"))

    def parse_crypto(self, ticker, interval, market):
        """Подключение модуля для парсинга исторических данных и записи в файл"""
        data = get_data(currency_pair=ticker, interval=interval, market=market)
        save_to_json(data)

    def on_push_button_clicked(self):
        """Проверка вводных данных, запуск сервиса парсинга и обновление цены"""
        if not self.pair_input.text():
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите валюту правильно")
            return
        if not self.comboBox.currentText() or not self.comboBox_2.currentText():
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Выберите биржу и интервал")
            return

        ticker = self.pair_input.text()
        market = self.comboBox.currentText().lower()
        interval = self.comboBox_2.currentText()

        intervals = {
            "Минута": "1m",
            "Час": "1h",
            "Месяц": "1m",
            "Год": "1y"
        }
        if interval in intervals:
            interval = intervals[interval]

        self.parse_crypto(ticker, interval, market)

        parser_runnable = ParserRunnable(ticker, market, self)
        QThreadPool.globalInstance().start(parser_runnable)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
    pool = QThreadPool()


if __name__ == "__main__":
    main()
