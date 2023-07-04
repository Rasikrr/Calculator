# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)
import files_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(624, 701)
        MainWindow.setMinimumSize(QSize(624, 701))
        MainWindow.setStyleSheet(u"QWidget {\n"
"    background-color: black;\n"
"    color:white;\n"
"    font-family: Rubik;\n"
"    font-size: 16pt;\n"
"\n"
"\n"
"\n"
"}\n"
"QPushButton{\n"
"    border:none;\n"
"    background-color: #3c3c3c;\n"
"    border-radius: 50%;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: #676767;\n"
"\n"
"\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color:#B7B7B7;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lbl = QLabel(self.centralwidget)
        self.lbl.setObjectName(u"lbl")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl.sizePolicy().hasHeightForWidth())
        self.lbl.setSizePolicy(sizePolicy)
        self.lbl.setStyleSheet(u"color:#888;")
        self.lbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.lbl)

        self.le = QLineEdit(self.centralwidget)
        self.le.setObjectName(u"le")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.le.sizePolicy().hasHeightForWidth())
        self.le.setSizePolicy(sizePolicy1)
        self.le.setStyleSheet(u"font-size:40pt;\n"
"border:none;\n"
"")
        self.le.setMaxLength(10)
        self.le.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.le.setReadOnly(True)

        self.verticalLayout.addWidget(self.le)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.btn_delete_last_digit = QPushButton(self.centralwidget)
        self.btn_delete_last_digit.setObjectName(u"btn_delete_last_digit")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_delete_last_digit.sizePolicy().hasHeightForWidth())
        self.btn_delete_last_digit.setSizePolicy(sizePolicy2)
        self.btn_delete_last_digit.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_delete_last_digit.setStyleSheet(u"QWidget{\n"
"background-color:#E5971F;\n"
"}\n"
"QWidget:hover{\n"
"	background-color:#976309;\n"
"}\n"
"QWidget:pressed{\n"
"background-color:#B4B4B4;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icons/backspace_FILL1_wght400_GRAD0_opsz48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_delete_last_digit.setIcon(icon)
        self.btn_delete_last_digit.setIconSize(QSize(30, 40))

        self.gridLayout.addWidget(self.btn_delete_last_digit, 0, 4, 1, 1)

        self.btn_divide = QPushButton(self.centralwidget)
        self.btn_divide.setObjectName(u"btn_divide")
        sizePolicy2.setHeightForWidth(self.btn_divide.sizePolicy().hasHeightForWidth())
        self.btn_divide.setSizePolicy(sizePolicy2)
        self.btn_divide.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_divide.setStyleSheet(u"QWidget{\n"
"background-color:#9C9C9C;\n"
"color:black;\n"
"}\n"
"QWidget:hover{\n"
"	background-color:#D2D2D2;\n"
"}\n"
"QWidget:pressed{\n"
"background-color:#B4B4B4;\n"
"}")

        self.gridLayout.addWidget(self.btn_divide, 0, 3, 1, 1)

        self.btn_extent = QPushButton(self.centralwidget)
        self.btn_extent.setObjectName(u"btn_extent")
        sizePolicy2.setHeightForWidth(self.btn_extent.sizePolicy().hasHeightForWidth())
        self.btn_extent.setSizePolicy(sizePolicy2)
        self.btn_extent.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_extent.setStyleSheet(u"QWidget{\n"
"background-color:#E5971F;\n"
"}\n"
"QWidget:hover{\n"
"	background-color:#976309;\n"
"}\n"
"QWidget:pressed{\n"
"background-color:#B4B4B4;\n"
"}")

        self.gridLayout.addWidget(self.btn_extent, 1, 4, 1, 1)

        self.btn_right_bracket = QPushButton(self.centralwidget)
        self.btn_right_bracket.setObjectName(u"btn_right_bracket")
        sizePolicy2.setHeightForWidth(self.btn_right_bracket.sizePolicy().hasHeightForWidth())
        self.btn_right_bracket.setSizePolicy(sizePolicy2)
        self.btn_right_bracket.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_right_bracket.setStyleSheet(u"QWidget{\n"
"background-color:#E5971F;\n"
"}\n"
"QWidget:hover{\n"
"	background-color:#976309;\n"
"}\n"
"QWidget:pressed{\n"
"background-color:#B4B4B4;\n"
"}\n"
"")

        self.gridLayout.addWidget(self.btn_right_bracket, 2, 4, 1, 1)

        self.btn_times = QPushButton(self.centralwidget)
        self.btn_times.setObjectName(u"btn_times")
        sizePolicy2.setHeightForWidth(self.btn_times.sizePolicy().hasHeightForWidth())
        self.btn_times.setSizePolicy(sizePolicy2)
        self.btn_times.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.btn_times, 1, 3, 1, 1)

        self.btn_root = QPushButton(self.centralwidget)
        self.btn_root.setObjectName(u"btn_root")
        sizePolicy2.setHeightForWidth(self.btn_root.sizePolicy().hasHeightForWidth())
        self.btn_root.setSizePolicy(sizePolicy2)
        self.btn_root.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_root.setStyleSheet(u"QWidget{\n"
"background-color:#E5971F;\n"
"}\n"
"QWidget:hover{\n"
"	background-color:#976309;\n"
"}\n"
"QWidget:pressed{\n"
"background-color:#B4B4B4;\n"
"}")

        self.gridLayout.addWidget(self.btn_root, 4, 4, 1, 1)

        self.btn_left_bracket = QPushButton(self.centralwidget)
        self.btn_left_bracket.setObjectName(u"btn_left_bracket")
        sizePolicy2.setHeightForWidth(self.btn_left_bracket.sizePolicy().hasHeightForWidth())
        self.btn_left_bracket.setSizePolicy(sizePolicy2)
        self.btn_left_bracket.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_left_bracket.setStyleSheet(u"QWidget{\n"
"background-color:#E5971F;\n"
"}\n"
"QWidget:hover{\n"
"	background-color:#976309;\n"
"}\n"
"QWidget:pressed{\n"
"background-color:#B4B4B4;\n"
"}")

        self.gridLayout.addWidget(self.btn_left_bracket, 3, 4, 1, 1)

        self.btn_0 = QPushButton(self.centralwidget)
        self.btn_0.setObjectName(u"btn_0")
        sizePolicy2.setHeightForWidth(self.btn_0.sizePolicy().hasHeightForWidth())
        self.btn_0.setSizePolicy(sizePolicy2)
        self.btn_0.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.btn_0, 4, 0, 1, 2)

        self.btn_percent = QPushButton(self.centralwidget)
        self.btn_percent.setObjectName(u"btn_percent")
        sizePolicy2.setHeightForWidth(self.btn_percent.sizePolicy().hasHeightForWidth())
        self.btn_percent.setSizePolicy(sizePolicy2)
        self.btn_percent.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_percent.setStyleSheet(u"QWidget{\n"
"background-color:#9C9C9C;\n"
"color:black;\n"
"}\n"
"QWidget:hover{\n"
"	background-color:#D2D2D2;\n"
"}\n"
"QWidget:pressed{\n"
"background-color:#B4B4B4;\n"
"}")

        self.gridLayout.addWidget(self.btn_percent, 0, 2, 1, 1)

        self.btn_1 = QPushButton(self.centralwidget)
        self.btn_1.setObjectName(u"btn_1")
        sizePolicy2.setHeightForWidth(self.btn_1.sizePolicy().hasHeightForWidth())
        self.btn_1.setSizePolicy(sizePolicy2)
        self.btn_1.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.btn_1, 3, 0, 1, 1)

        self.btn_7 = QPushButton(self.centralwidget)
        self.btn_7.setObjectName(u"btn_7")
        sizePolicy2.setHeightForWidth(self.btn_7.sizePolicy().hasHeightForWidth())
        self.btn_7.setSizePolicy(sizePolicy2)
        self.btn_7.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.btn_7, 1, 0, 1, 1)

        self.btn_5 = QPushButton(self.centralwidget)
        self.btn_5.setObjectName(u"btn_5")
        sizePolicy2.setHeightForWidth(self.btn_5.sizePolicy().hasHeightForWidth())
        self.btn_5.setSizePolicy(sizePolicy2)
        self.btn_5.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.btn_5, 2, 1, 1, 1)

        self.btn_4 = QPushButton(self.centralwidget)
        self.btn_4.setObjectName(u"btn_4")
        sizePolicy2.setHeightForWidth(self.btn_4.sizePolicy().hasHeightForWidth())
        self.btn_4.setSizePolicy(sizePolicy2)
        self.btn_4.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.btn_4, 2, 0, 1, 1)

        self.btn_delete_all = QPushButton(self.centralwidget)
        self.btn_delete_all.setObjectName(u"btn_delete_all")
        sizePolicy2.setHeightForWidth(self.btn_delete_all.sizePolicy().hasHeightForWidth())
        self.btn_delete_all.setSizePolicy(sizePolicy2)
        self.btn_delete_all.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_delete_all.setStyleSheet(u"QWidget{\n"
"background-color:#9C9C9C;\n"
"color:black;\n"
"}\n"
"QWidget:hover{\n"
"	background-color:#D2D2D2;\n"
"}\n"
"QWidget:pressed{\n"
"background-color:#B4B4B4;\n"
"}")

        self.gridLayout.addWidget(self.btn_delete_all, 0, 0, 1, 1)

        self.btn_6 = QPushButton(self.centralwidget)
        self.btn_6.setObjectName(u"btn_6")
        sizePolicy2.setHeightForWidth(self.btn_6.sizePolicy().hasHeightForWidth())
        self.btn_6.setSizePolicy(sizePolicy2)
        self.btn_6.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.btn_6, 2, 2, 1, 1)

        self.btn_minus = QPushButton(self.centralwidget)
        self.btn_minus.setObjectName(u"btn_minus")
        sizePolicy2.setHeightForWidth(self.btn_minus.sizePolicy().hasHeightForWidth())
        self.btn_minus.setSizePolicy(sizePolicy2)
        self.btn_minus.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.btn_minus, 2, 3, 1, 1)

        self.btn_9 = QPushButton(self.centralwidget)
        self.btn_9.setObjectName(u"btn_9")
        sizePolicy2.setHeightForWidth(self.btn_9.sizePolicy().hasHeightForWidth())
        self.btn_9.setSizePolicy(sizePolicy2)
        self.btn_9.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.btn_9, 1, 2, 1, 1)

        self.btn_8 = QPushButton(self.centralwidget)
        self.btn_8.setObjectName(u"btn_8")
        sizePolicy2.setHeightForWidth(self.btn_8.sizePolicy().hasHeightForWidth())
        self.btn_8.setSizePolicy(sizePolicy2)
        self.btn_8.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.btn_8, 1, 1, 1, 1)

        self.btn_plus = QPushButton(self.centralwidget)
        self.btn_plus.setObjectName(u"btn_plus")
        sizePolicy2.setHeightForWidth(self.btn_plus.sizePolicy().hasHeightForWidth())
        self.btn_plus.setSizePolicy(sizePolicy2)
        self.btn_plus.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.btn_plus, 3, 3, 1, 1)

        self.btn_3 = QPushButton(self.centralwidget)
        self.btn_3.setObjectName(u"btn_3")
        sizePolicy2.setHeightForWidth(self.btn_3.sizePolicy().hasHeightForWidth())
        self.btn_3.setSizePolicy(sizePolicy2)
        self.btn_3.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.btn_3, 3, 2, 1, 1)

        self.btn_equals = QPushButton(self.centralwidget)
        self.btn_equals.setObjectName(u"btn_equals")
        sizePolicy2.setHeightForWidth(self.btn_equals.sizePolicy().hasHeightForWidth())
        self.btn_equals.setSizePolicy(sizePolicy2)
        self.btn_equals.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.btn_equals, 4, 3, 1, 1)

        self.btn_dot = QPushButton(self.centralwidget)
        self.btn_dot.setObjectName(u"btn_dot")
        sizePolicy2.setHeightForWidth(self.btn_dot.sizePolicy().hasHeightForWidth())
        self.btn_dot.setSizePolicy(sizePolicy2)
        self.btn_dot.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.btn_dot, 4, 2, 1, 1)

        self.btn_plus_minus = QPushButton(self.centralwidget)
        self.btn_plus_minus.setObjectName(u"btn_plus_minus")
        sizePolicy2.setHeightForWidth(self.btn_plus_minus.sizePolicy().hasHeightForWidth())
        self.btn_plus_minus.setSizePolicy(sizePolicy2)
        self.btn_plus_minus.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_plus_minus.setStyleSheet(u"QWidget{\n"
"background-color:#9C9C9C;\n"
"color:black;\n"
"}\n"
"QWidget:hover{\n"
"	background-color:#D2D2D2;\n"
"}\n"
"QWidget:pressed{\n"
"background-color:#B4B4B4;\n"
"}")

        self.gridLayout.addWidget(self.btn_plus_minus, 0, 1, 1, 1)

        self.pushButton_10 = QPushButton(self.centralwidget)
        self.pushButton_10.setObjectName(u"pushButton_10")
        sizePolicy2.setHeightForWidth(self.pushButton_10.sizePolicy().hasHeightForWidth())
        self.pushButton_10.setSizePolicy(sizePolicy2)
        self.pushButton_10.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.pushButton_10, 3, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Calculator", None))
        self.lbl.setText(QCoreApplication.translate("MainWindow", u"3253252+12", None))
        self.le.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_delete_last_digit.setText("")
#if QT_CONFIG(shortcut)
        self.btn_delete_last_digit.setShortcut(QCoreApplication.translate("MainWindow", u"Backspace", None))
#endif // QT_CONFIG(shortcut)
        self.btn_divide.setText(QCoreApplication.translate("MainWindow", u"/", None))
#if QT_CONFIG(shortcut)
        self.btn_divide.setShortcut(QCoreApplication.translate("MainWindow", u"/", None))
#endif // QT_CONFIG(shortcut)
        self.btn_extent.setText(QCoreApplication.translate("MainWindow", u"x^n", None))
#if QT_CONFIG(shortcut)
        self.btn_extent.setShortcut(QCoreApplication.translate("MainWindow", u"^", None))
#endif // QT_CONFIG(shortcut)
        self.btn_right_bracket.setText(QCoreApplication.translate("MainWindow", u")", None))
#if QT_CONFIG(shortcut)
        self.btn_right_bracket.setShortcut(QCoreApplication.translate("MainWindow", u")", None))
#endif // QT_CONFIG(shortcut)
        self.btn_times.setText(QCoreApplication.translate("MainWindow", u"\u00d7", None))
#if QT_CONFIG(shortcut)
        self.btn_times.setShortcut(QCoreApplication.translate("MainWindow", u"*", None))
#endif // QT_CONFIG(shortcut)
        self.btn_root.setText(QCoreApplication.translate("MainWindow", u"\u221a", None))
#if QT_CONFIG(shortcut)
        self.btn_root.setShortcut(QCoreApplication.translate("MainWindow", u"R", None))
#endif // QT_CONFIG(shortcut)
        self.btn_left_bracket.setText(QCoreApplication.translate("MainWindow", u"(", None))
#if QT_CONFIG(shortcut)
        self.btn_left_bracket.setShortcut(QCoreApplication.translate("MainWindow", u"(", None))
#endif // QT_CONFIG(shortcut)
        self.btn_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
#if QT_CONFIG(shortcut)
        self.btn_0.setShortcut(QCoreApplication.translate("MainWindow", u"0", None))
#endif // QT_CONFIG(shortcut)
        self.btn_percent.setText(QCoreApplication.translate("MainWindow", u"%", None))
#if QT_CONFIG(shortcut)
        self.btn_percent.setShortcut(QCoreApplication.translate("MainWindow", u"%", None))
#endif // QT_CONFIG(shortcut)
        self.btn_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
#if QT_CONFIG(shortcut)
        self.btn_1.setShortcut(QCoreApplication.translate("MainWindow", u"1", None))
#endif // QT_CONFIG(shortcut)
        self.btn_7.setText(QCoreApplication.translate("MainWindow", u"7", None))
#if QT_CONFIG(shortcut)
        self.btn_7.setShortcut(QCoreApplication.translate("MainWindow", u"7", None))
#endif // QT_CONFIG(shortcut)
        self.btn_5.setText(QCoreApplication.translate("MainWindow", u"5", None))
#if QT_CONFIG(shortcut)
        self.btn_5.setShortcut(QCoreApplication.translate("MainWindow", u"5", None))
#endif // QT_CONFIG(shortcut)
        self.btn_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
#if QT_CONFIG(shortcut)
        self.btn_4.setShortcut(QCoreApplication.translate("MainWindow", u"4", None))
#endif // QT_CONFIG(shortcut)
        self.btn_delete_all.setText(QCoreApplication.translate("MainWindow", u"AC", None))
#if QT_CONFIG(shortcut)
        self.btn_delete_all.setShortcut(QCoreApplication.translate("MainWindow", u"Del", None))
#endif // QT_CONFIG(shortcut)
        self.btn_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
#if QT_CONFIG(shortcut)
        self.btn_6.setShortcut(QCoreApplication.translate("MainWindow", u"6", None))
#endif // QT_CONFIG(shortcut)
        self.btn_minus.setText(QCoreApplication.translate("MainWindow", u"-", None))
#if QT_CONFIG(shortcut)
        self.btn_minus.setShortcut(QCoreApplication.translate("MainWindow", u"-", None))
#endif // QT_CONFIG(shortcut)
        self.btn_9.setText(QCoreApplication.translate("MainWindow", u"9", None))
#if QT_CONFIG(shortcut)
        self.btn_9.setShortcut(QCoreApplication.translate("MainWindow", u"9", None))
#endif // QT_CONFIG(shortcut)
        self.btn_8.setText(QCoreApplication.translate("MainWindow", u"8", None))
#if QT_CONFIG(shortcut)
        self.btn_8.setShortcut(QCoreApplication.translate("MainWindow", u"8", None))
#endif // QT_CONFIG(shortcut)
        self.btn_plus.setText(QCoreApplication.translate("MainWindow", u"+", None))
#if QT_CONFIG(shortcut)
        self.btn_plus.setShortcut(QCoreApplication.translate("MainWindow", u"+", None))
#endif // QT_CONFIG(shortcut)
        self.btn_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
#if QT_CONFIG(shortcut)
        self.btn_3.setShortcut(QCoreApplication.translate("MainWindow", u"3", None))
#endif // QT_CONFIG(shortcut)
        self.btn_equals.setText(QCoreApplication.translate("MainWindow", u"=", None))
#if QT_CONFIG(shortcut)
        self.btn_equals.setShortcut(QCoreApplication.translate("MainWindow", u"=", None))
#endif // QT_CONFIG(shortcut)
        self.btn_dot.setText(QCoreApplication.translate("MainWindow", u".", None))
#if QT_CONFIG(shortcut)
        self.btn_dot.setShortcut(QCoreApplication.translate("MainWindow", u".", None))
#endif // QT_CONFIG(shortcut)
        self.btn_plus_minus.setText(QCoreApplication.translate("MainWindow", u"+/-", None))
#if QT_CONFIG(shortcut)
        self.btn_plus_minus.setShortcut(QCoreApplication.translate("MainWindow", u"]", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"2", None))
#if QT_CONFIG(shortcut)
        self.pushButton_10.setShortcut(QCoreApplication.translate("MainWindow", u"2", None))
#endif // QT_CONFIG(shortcut)
    # retranslateUi

