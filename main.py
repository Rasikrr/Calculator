import sys
import os

from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from PySide6.QtGui import QFontDatabase, QPixmap, QIcon
from design_rc import Ui_MainWindow
from operator import add, sub, mul, truediv, pow
from math import sqrt, ceil, factorial as fac


class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        QFontDatabase.addApplicationFont("font/Rubik-Regular.ttf")
        self.ui.lbl.clear()
        self.ui.le.setMaxLength(15)
        # operations
        self.operations = {"+": add,
                           "-": sub,
                           "/": truediv,
                           "x": mul,
                           }

        self.ui.btn_times.setText("x")
        self.ui.btn_right_bracket.setText("n!")
        self.ui.btn_left_bracket.setText("π")

        # digits

        self.ui.btn_0.clicked.connect(self.add_digit)
        self.ui.btn_1.clicked.connect(self.add_digit)
        self.ui.btn_2.clicked.connect(self.add_digit)
        self.ui.btn_3.clicked.connect(self.add_digit)
        self.ui.btn_4.clicked.connect(self.add_digit)
        self.ui.btn_5.clicked.connect(self.add_digit)
        self.ui.btn_6.clicked.connect(self.add_digit)
        self.ui.btn_7.clicked.connect(self.add_digit)
        self.ui.btn_8.clicked.connect(self.add_digit)
        self.ui.btn_9.clicked.connect(self.add_digit)

        # dot
        self.ui.btn_dot.clicked.connect(self.add_point)

        # clear all
        self.ui.btn_delete_all.clicked.connect(self.clear_all)

        # delete last digit
        self.ui.btn_delete_last_digit.clicked.connect(self.delete_last)

        # operations
        self.ui.btn_plus.clicked.connect(self.math_operations)
        self.ui.btn_minus.clicked.connect(self.math_operations)
        self.ui.btn_times.clicked.connect(self.math_operations)
        self.ui.btn_divide.clicked.connect(self.math_operations)
        self.ui.btn_extent.clicked.connect(self.add_extent_and_root)
        self.ui.btn_root.clicked.connect(self.add_extent_and_root)
        self.ui.btn_percent.clicked.connect(self.add_percent_and_factorial)
        self.ui.btn_right_bracket.clicked.connect(self.add_percent_and_factorial)
        self.ui.btn_left_bracket.clicked.connect(self.add_digit)

        # calculate
        self.ui.btn_equals.clicked.connect(self.calculate)

        # invert number
        self.ui.btn_plus_minus.clicked.connect(self.invert)

        # picture
        app_icon = QIcon()
        app_icon.addFile(os.getcwd()+r"/main_image")
        self.setWindowIcon(app_icon)

    @staticmethod
    def cut_zeros(number):
        try:
            num = str(float(number))
            return num[:-2] if num[-1:] == "0" else num
        except OverflowError:
            return "Error"

    def add_digit(self) -> None:
        btn = self.sender()
        digit_buttons = (f"btn_{i}" for i in range(10))
        if "%" not in self.ui.le.text() and "!" not in self.ui.le.text() and self.ui.le.text() != "Error":
            if btn.objectName() in digit_buttons:
                if self.ui.le.text() == "0":
                    self.ui.le.setText(btn.text())
                else:
                    self.ui.le.setText(self.ui.le.text() + btn.text())
            elif btn.objectName() == "btn_left_bracket":
                if self.ui.le.text() == "0":
                    self.ui.le.setText("3.14")

    def add_point(self):
        if "." not in self.ui.le.text() and self.ui.le.text() != "Error":
            if "=" in self.ui.lbl.text():
                self.ui.lbl.clear()
            self.ui.le.setText(self.ui.le.text() + ".")

    def clear_all(self):
        self.ui.le.setText("0")
        self.ui.lbl.clear()

    def add_temporal_expression(self):
        btn = self.sender()
        sign = btn.text()
        if not self.ui.lbl.text() or self.get_math_sign() == "=":
            self.ui.lbl.setText(self.get_le_number() + f" {sign}")
            self.ui.le.setText("0")

    def get_le_number(self):
        if "^" in self.ui.le.text():
            return self.cut_zeros(self.calculate_extent(self.ui.le.text()))
        elif "√" in self.ui.le.text():
            return self.cut_zeros(self.calculate_root())
        elif "%" in self.ui.le.text():
            return self.cut_zeros(self.calculate_percent(self.ui.le.text(), self.ui.lbl.text().split()))
        elif "!" in self.ui.le.text():
            return self.cut_zeros(self.calculate_factorial())
        else:
            return self.cut_zeros(self.ui.le.text())

    def get_lbl_number(self):
        if self.ui.lbl.text():
            return self.cut_zeros(self.ui.lbl.text().split()[0])

    def get_math_sign(self):
        if self.ui.lbl.text():
            return self.ui.lbl.text()[-1]

    def calculate(self):
        le_num = self.get_le_number()
        if le_num == "Error":
            self.ui.le.setText(le_num)
        lbl_num = self.get_lbl_number()
        if not lbl_num or "=" in self.ui.lbl.text():
            res = le_num
            if "=" in self.ui.lbl.text():
                self.ui.lbl.clear()
        else:
            try:
                res = self.cut_zeros(self.operations[self.get_math_sign()](float(lbl_num), float(le_num)))
                self.ui.lbl.setText(f"{lbl_num} {self.get_math_sign()} {le_num} =")
            except ZeroDivisionError:
                self.ui.lbl.clear()
                self.ui.le.setText("Error")
        self.ui.le.setText(res)
        return res

    def math_operations(self):
        btn = self.sender()
        sign = btn.text()
        temp = self.ui.lbl.text()
        if "^" in self.ui.le.text():
            if sign in ("+", "-"):
                self.ui.le.setText(self.ui.le.text()+sign)
                return
        if not temp:
            self.add_temporal_expression()
        else:
            if self.get_math_sign() != sign:
                if self.get_math_sign() == "=":
                    self.add_temporal_expression()
                else:
                    self.ui.lbl.setText(self.get_lbl_number() + f" {sign}")
            else:
                self.ui.lbl.setText(self.calculate() + f" {sign}")
                self.ui.le.setText("0")

    def delete_last(self):
        le_text = self.ui.le.text()
        if le_text:
            if self.get_math_sign() == "=":
                self.ui.lbl.clear()
            if len(le_text) == 1:
                self.ui.le.setText("0")
            else:
                self.ui.le.setText(le_text[:-1])

    def invert(self):
        if self.get_le_number() != "0":
            if len(self.ui.le.text()) == 15:
                self.ui.le.setMaxLength(16)
            if self.get_le_number()[0] != "-":
                self.ui.le.setText("-" + self.get_le_number())
            else:
                self.ui.le.setText(self.get_le_number()[1:])
            if "=" in self.ui.lbl.text():
                self.ui.lbl.clear()

    def add_extent_and_root(self):
        btn = self.sender()
        sign = btn.text()
        if sign == "x^n":
            sign = "^"
            if "=" in self.ui.lbl.text():
                self.ui.lbl.clear()
            self.ui.le.setText(self.get_le_number() + sign)
        else:
            if self.get_le_number() == "0":
                self.ui.le.setText("√")
            else:
                if "=" in self.ui.lbl.text():
                    self.ui.lbl.clear()
                self.ui.le.setText(sign + self.get_le_number())

    def add_percent_and_factorial(self):
        btn = self.sender()
        sign = btn.text()
        if sign == "n!":
            sign = "!"
        if sign not in self.ui.le.text():
            self.ui.le.setText(self.get_le_number() + sign)

    @staticmethod
    def calculate_percent(le_number, lbl_text):
        number = le_number[:-1]
        if lbl_text:
            if "=" not in lbl_text:
                return float(lbl_text[0]) / 100 * float(number)
        else:
            return 1 / 100 * float(number)

    @staticmethod
    def calculate_extent(number):
        num_1 = number.split("^")[0]
        num_2 = number.split("^")[1]
        return round(pow(float(num_1), float(num_2)), 7)

    def calculate_root(self):
        num = self.ui.le.text()[1:]
        try:
            return round(sqrt(float(num)), 7)
        except ValueError:
            self.ui.le.setText("Error")

    def calculate_factorial(self):
        num = self.ui.le.text()[:-1]
        try:
            return fac(int(num))
        except ValueError:
            self.ui.le.setText("Error")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Calculator()
    window.show()

    sys.exit(app.exec())
