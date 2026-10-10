#установить через терминал pip instal PyQt5
import sys
import requests
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit,
                             QPushButton, QComboBox, QVBoxLayout)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont


class CurrencyConverter(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Конвертор валют")
        self.setGeometry(300, 300, 400, 350)

        layout = QVBoxLayout()

        self.label_from = QLabel("Из валюты:")
        layout.addWidget(self.label_from)

        self.combo_from = QComboBox()
        self.combo_from.addItems(["USD", "EUR", "RUB", "GBP", "CNY", "JPY"])
        self.combo_from.setCurrentText("USD")
        layout.addWidget(self.combo_from)

        self.label_to = QLabel("В валюту:")
        layout.addWidget(self.label_to)

        self.combo_to = QComboBox()
        self.combo_to.addItems(["RUB", "USD", "EUR", "GBP", "CNY", "JPY"])
        self.combo_to.setCurrentText("RUB")
        layout.addWidget(self.combo_to)

        self.label_amount = QLabel("Сумма:")
        layout.addWidget(self.label_amount)

        self.entry_amount = QLineEdit()
        layout.addWidget(self.entry_amount)

        self.btn_convert = QPushButton("Конвертировать")
        self.btn_convert.clicked.connect(self.convert)
        layout.addWidget(self.btn_convert)

        self.label_result = QLabel("Результат: ---")
        self.label_result.setFont(QFont("Arial", 12))
        self.label_result.setAlignment(Qt.AlignCenter)
        self.label_result.setWordWrap(True)
        layout.addWidget(self.label_result)

        self.setLayout(layout)

    def convert(self):
        try:
            amount = float(self.entry_amount.text())
            from_curr = self.combo_from.currentText()
            to_curr = self.combo_to.currentText()

            url = f"https://api.exchangerate-api.com/v4/latest/{from_curr}"
            response = requests.get(url)
            data = response.json()

            if to_curr in data['rates']:
                rate = data['rates'][to_curr]
                result = amount * rate
                self.label_result.setText(
                    f"Результат: {amount} {from_curr} = {result:.2f} {to_curr}"
                )
            else:
                self.label_result.setText("Ошибка: валюта не найдена")

        except ValueError:
            self.label_result.setText("Ошибка: введите число")
        except Exception:
            self.label_result.setText("Ошибка: проверьте интернет")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CurrencyConverter()
    window.show()
    sys.exit(app.exec_())