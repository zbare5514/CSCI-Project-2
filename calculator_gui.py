# Form implementation generated from reading ui file 'calculator_gui.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_calculator_window(object):
    def setupUi(self, calculator_window):
        calculator_window.setObjectName("calculator_window")
        calculator_window.resize(432, 630)
        calculator_window.setMinimumSize(QtCore.QSize(432, 630))
        calculator_window.setMaximumSize(QtCore.QSize(432, 630))
        calculator_window.setStyleSheet("background-color: rgb(0, 51, 79);")
        self.centralwidget = QtWidgets.QWidget(parent=calculator_window)
        self.centralwidget.setObjectName("centralwidget")
        self.button_1 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_1.setGeometry(QtCore.QRect(30, 470, 81, 51))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.button_1.setFont(font)
        self.button_1.setStyleSheet("background-color: rgb(147, 147, 147);\n"
"color: rgb(243, 241, 232);")
        self.button_1.setObjectName("button_1")
        self.button_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_2.setGeometry(QtCore.QRect(120, 470, 81, 51))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.button_2.setFont(font)
        self.button_2.setStyleSheet("background-color: rgb(147, 147, 147);\n"
"color: rgb(243, 241, 232);")
        self.button_2.setObjectName("button_2")
        self.button_3 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_3.setGeometry(QtCore.QRect(210, 470, 81, 51))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.button_3.setFont(font)
        self.button_3.setStyleSheet("background-color: rgb(147, 147, 147);\n"
"color: rgb(243, 241, 232);")
        self.button_3.setObjectName("button_3")
        self.button_5 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_5.setGeometry(QtCore.QRect(120, 410, 81, 51))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.button_5.setFont(font)
        self.button_5.setStyleSheet("background-color: rgb(147, 147, 147);\n"
"color: rgb(243, 241, 232);")
        self.button_5.setObjectName("button_5")
        self.button_4 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_4.setGeometry(QtCore.QRect(30, 410, 81, 51))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.button_4.setFont(font)
        self.button_4.setStyleSheet("background-color: rgb(147, 147, 147);\n"
"color: rgb(243, 241, 232);")
        self.button_4.setObjectName("button_4")
        self.button_6 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_6.setGeometry(QtCore.QRect(210, 410, 81, 51))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.button_6.setFont(font)
        self.button_6.setStyleSheet("background-color: rgb(147, 147, 147);\n"
"color: rgb(243, 241, 232);")
        self.button_6.setObjectName("button_6")
        self.button_8 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_8.setGeometry(QtCore.QRect(120, 350, 81, 51))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.button_8.setFont(font)
        self.button_8.setStyleSheet("background-color: rgb(147, 147, 147);\n"
"color: rgb(243, 241, 232);")
        self.button_8.setObjectName("button_8")
        self.button_7 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_7.setGeometry(QtCore.QRect(30, 350, 81, 51))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.button_7.setFont(font)
        self.button_7.setStyleSheet("background-color: rgb(147, 147, 147);\n"
"color: rgb(243, 241, 232);")
        self.button_7.setObjectName("button_7")
        self.button_9 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_9.setGeometry(QtCore.QRect(210, 350, 81, 51))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.button_9.setFont(font)
        self.button_9.setStyleSheet("background-color: rgb(147, 147, 147);\n"
"color: rgb(243, 241, 232);")
        self.button_9.setObjectName("button_9")
        self.button_multiply = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_multiply.setGeometry(QtCore.QRect(320, 350, 81, 51))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.button_multiply.setFont(font)
        self.button_multiply.setStyleSheet("background-color: rgb(77, 77, 77);\n"
"color: rgb(243, 241, 232);")
        self.button_multiply.setObjectName("button_multiply")
        self.button_add = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_add.setGeometry(QtCore.QRect(320, 470, 81, 51))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.button_add.setFont(font)
        self.button_add.setStyleSheet("background-color: rgb(77, 77, 77);\n"
"color: rgb(243, 241, 232);")
        self.button_add.setObjectName("button_add")
        self.button_subtract = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_subtract.setGeometry(QtCore.QRect(320, 410, 81, 51))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.button_subtract.setFont(font)
        self.button_subtract.setStyleSheet("background-color: rgb(77, 77, 77);\n"
"color: rgb(243, 241, 232);")
        self.button_subtract.setObjectName("button_subtract")
        self.button_divide = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_divide.setGeometry(QtCore.QRect(320, 290, 81, 51))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.button_divide.setFont(font)
        self.button_divide.setStyleSheet("background-color: rgb(77, 77, 77);\n"
"color: rgb(243, 241, 232);")
        self.button_divide.setObjectName("button_divide")
        self.button_enter = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_enter.setGeometry(QtCore.QRect(320, 530, 81, 51))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.button_enter.setFont(font)
        self.button_enter.setStyleSheet("background-color: rgb(77, 77, 77);\n"
"color: rgb(243, 241, 232);")
        self.button_enter.setObjectName("button_enter")
        self.button_clear = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_clear.setGeometry(QtCore.QRect(320, 230, 81, 51))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.button_clear.setFont(font)
        self.button_clear.setStyleSheet("background-color: rgb(39, 39, 39);\n"
"color: rgb(243, 241, 232);")
        self.button_clear.setObjectName("button_clear")
        self.calculator_display = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.calculator_display.setGeometry(QtCore.QRect(30, 20, 361, 71))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(16)
        self.calculator_display.setFont(font)
        self.calculator_display.setStyleSheet("background-color: rgb(232, 230, 216);\n"
"color: rgb(0, 0, 0);")
        self.calculator_display.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.calculator_display.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.calculator_display.setDocumentTitle("")
        self.calculator_display.setUndoRedoEnabled(False)
        self.calculator_display.setAcceptRichText(False)
        self.calculator_display.setTextInteractionFlags(QtCore.Qt.TextInteractionFlag.TextSelectableByKeyboard|QtCore.Qt.TextInteractionFlag.TextSelectableByMouse)
        self.calculator_display.setPlaceholderText("")
        self.calculator_display.setObjectName("calculator_display")
        self.label_mode = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_mode.setGeometry(QtCore.QRect(30, 140, 351, 16))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(12)
        self.label_mode.setFont(font)
        self.label_mode.setStyleSheet("color: rgb(244, 243, 224);")
        self.label_mode.setText("")
        self.label_mode.setObjectName("label_mode")
        self.button_delete = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_delete.setGeometry(QtCore.QRect(210, 230, 81, 51))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.button_delete.setFont(font)
        self.button_delete.setStyleSheet("background-color: rgb(39, 39, 39);\n"
"color: rgb(243, 241, 232);")
        self.button_delete.setObjectName("button_delete")
        self.button_data = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_data.setGeometry(QtCore.QRect(30, 170, 81, 51))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.button_data.setFont(font)
        self.button_data.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.button_data.setStyleSheet("background-color: rgb(39, 39, 39);\n"
"color: rgb(243, 241, 232);")
        self.button_data.setObjectName("button_data")
        self.button_decimal = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_decimal.setGeometry(QtCore.QRect(210, 530, 81, 51))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.button_decimal.setFont(font)
        self.button_decimal.setStyleSheet("background-color: rgb(147, 147, 147);\n"
"color: rgb(243, 241, 232);")
        self.button_decimal.setObjectName("button_decimal")
        self.button_0 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_0.setGeometry(QtCore.QRect(30, 530, 81, 51))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.button_0.setFont(font)
        self.button_0.setStyleSheet("background-color: rgb(147, 147, 147);\n"
"color: rgb(243, 241, 232);")
        self.button_0.setObjectName("button_0")
        self.button_comma = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_comma.setEnabled(False)
        self.button_comma.setGeometry(QtCore.QRect(120, 530, 81, 51))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.button_comma.setFont(font)
        self.button_comma.setStyleSheet("background-color: rgb(147, 147, 147);\n"
"color: rgb(243, 241, 232);")
        self.button_comma.setObjectName("button_comma")
        self.answer_display = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.answer_display.setGeometry(QtCore.QRect(30, 90, 361, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(16)
        self.answer_display.setFont(font)
        self.answer_display.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.answer_display.setStyleSheet("background-color: rgb(232, 230, 216);\n"
"color: rgb(0, 0, 0);\n"
"border: none")
        self.answer_display.setText("")
        self.answer_display.setMaxLength(32)
        self.answer_display.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.answer_display.setReadOnly(True)
        self.answer_display.setObjectName("answer_display")
        self.button_mean = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_mean.setGeometry(QtCore.QRect(30, 290, 81, 51))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.button_mean.setFont(font)
        self.button_mean.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.button_mean.setStyleSheet("background-color: rgb(39, 39, 39);\n"
"color: rgb(243, 241, 232);")
        self.button_mean.setObjectName("button_mean")
        self.button_median = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_median.setGeometry(QtCore.QRect(120, 290, 81, 51))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.button_median.setFont(font)
        self.button_median.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.button_median.setStyleSheet("background-color: rgb(39, 39, 39);\n"
"color: rgb(243, 241, 232);")
        self.button_median.setObjectName("button_median")
        self.button_sum = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_sum.setGeometry(QtCore.QRect(210, 290, 81, 51))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.button_sum.setFont(font)
        self.button_sum.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.button_sum.setStyleSheet("background-color: rgb(39, 39, 39);\n"
"color: rgb(243, 241, 232);")
        self.button_sum.setObjectName("button_sum")
        self.button_3rd_quart = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_3rd_quart.setGeometry(QtCore.QRect(120, 230, 81, 51))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.button_3rd_quart.setFont(font)
        self.button_3rd_quart.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.button_3rd_quart.setStyleSheet("background-color: rgb(39, 39, 39);\n"
"color: rgb(243, 241, 232);")
        self.button_3rd_quart.setObjectName("button_3rd_quart")
        self.button_1st_quart = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_1st_quart.setGeometry(QtCore.QRect(30, 230, 81, 51))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.button_1st_quart.setFont(font)
        self.button_1st_quart.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.button_1st_quart.setStyleSheet("background-color: rgb(39, 39, 39);\n"
"color: rgb(243, 241, 232);")
        self.button_1st_quart.setObjectName("button_1st_quart")
        self.button_stats = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_stats.setGeometry(QtCore.QRect(120, 170, 81, 51))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.button_stats.setFont(font)
        self.button_stats.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.button_stats.setStyleSheet("background-color: rgb(39, 39, 39);\n"
"color: rgb(243, 241, 232);")
        self.button_stats.setObjectName("button_stats")
        calculator_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=calculator_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 432, 21))
        self.menubar.setObjectName("menubar")
        calculator_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=calculator_window)
        self.statusbar.setObjectName("statusbar")
        calculator_window.setStatusBar(self.statusbar)

        self.retranslateUi(calculator_window)
        QtCore.QMetaObject.connectSlotsByName(calculator_window)

    def retranslateUi(self, calculator_window):
        _translate = QtCore.QCoreApplication.translate
        calculator_window.setWindowTitle(_translate("calculator_window", "MainWindow"))
        self.button_1.setText(_translate("calculator_window", "1"))
        self.button_2.setText(_translate("calculator_window", "2"))
        self.button_3.setText(_translate("calculator_window", "3"))
        self.button_5.setText(_translate("calculator_window", "5"))
        self.button_4.setText(_translate("calculator_window", "4"))
        self.button_6.setText(_translate("calculator_window", "6"))
        self.button_8.setText(_translate("calculator_window", "8"))
        self.button_7.setText(_translate("calculator_window", "7"))
        self.button_9.setText(_translate("calculator_window", "9"))
        self.button_multiply.setText(_translate("calculator_window", "*"))
        self.button_add.setText(_translate("calculator_window", "+"))
        self.button_subtract.setText(_translate("calculator_window", "-"))
        self.button_divide.setText(_translate("calculator_window", "/"))
        self.button_enter.setText(_translate("calculator_window", "enter"))
        self.button_clear.setText(_translate("calculator_window", "clear"))
        self.button_delete.setText(_translate("calculator_window", "delete"))
        self.button_data.setText(_translate("calculator_window", "data"))
        self.button_decimal.setText(_translate("calculator_window", "."))
        self.button_0.setText(_translate("calculator_window", "0"))
        self.button_comma.setText(_translate("calculator_window", ","))
        self.button_mean.setText(_translate("calculator_window", "mean"))
        self.button_median.setText(_translate("calculator_window", "median"))
        self.button_sum.setText(_translate("calculator_window", "sum"))
        self.button_3rd_quart.setText(_translate("calculator_window", "3rd quart."))
        self.button_1st_quart.setText(_translate("calculator_window", "1st quart."))
        self.button_stats.setText(_translate("calculator_window", "stats"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    calculator_window = QtWidgets.QMainWindow()
    ui = Ui_calculator_window()
    ui.setupUi(calculator_window)
    calculator_window.show()
    sys.exit(app.exec())
