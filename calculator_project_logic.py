from PyQt6.QtWidgets import *
from calculator_gui import *


def find_median(dataset: list) -> float:
    """
    Static method for finding the median of a list
    Parameters: list
    Returns: float
    """
    if len(dataset) % 2 == 0:
        median = ((dataset[int(len(dataset) / 2)]) + (dataset[int((len(dataset) / 2) - 1)])) / 2
        return median
    elif len(dataset) % 2 == 1:
        median = dataset[int(len(dataset) // 2)]
        return median


class Calculator(QMainWindow, Ui_calculator_window):
    def __init__(self) -> None:
        """
        Method used to define init variables and connect button click functions
        """
        super().__init__()
        self.setupUi(self)

        self.ans = ''
        self.dataset = []

        self.data_status = False
        self.stats_status = False
        self.cursor = self.calculator_display.textCursor()
        self.button_mean.setDisabled(True)
        self.button_median.setDisabled(True)
        self.button_sum.setDisabled(True)
        self.button_1st_quart.setDisabled(True)
        self.button_3rd_quart.setDisabled(True)
        self.button_0.clicked.connect(lambda: self.clicked_0())
        self.button_1.clicked.connect(lambda: self.clicked_1())
        self.button_2.clicked.connect(lambda: self.clicked_2())
        self.button_3.clicked.connect(lambda: self.clicked_3())
        self.button_4.clicked.connect(lambda: self.clicked_4())
        self.button_5.clicked.connect(lambda: self.clicked_5())
        self.button_6.clicked.connect(lambda: self.clicked_6())
        self.button_7.clicked.connect(lambda: self.clicked_7())
        self.button_8.clicked.connect(lambda: self.clicked_8())
        self.button_9.clicked.connect(lambda: self.clicked_9())
        self.button_comma.clicked.connect(lambda: self.clicked_comma())

        self.button_data.clicked.connect(lambda: self.clicked_data())
        self.button_stats.clicked.connect(lambda: self.clicked_stats())
        self.button_clear.clicked.connect(lambda: self.clear())
        self.button_delete.clicked.connect(lambda: self.delete())
        self.button_enter.clicked.connect(lambda: self.clicked_enter())
        self.button_add.clicked.connect(lambda: self.clicked_add())
        self.button_subtract.clicked.connect(lambda: self.clicked_subtract())
        self.button_multiply.clicked.connect(lambda: self.clicked_multiply())
        self.button_divide.clicked.connect(lambda: self.clicked_divide())
        self.button_decimal.clicked.connect(lambda: self.clicked_decimal())
        self.button_mean.clicked.connect(lambda: self.clicked_mean())
        self.button_median.clicked.connect(lambda: self.clicked_median())
        self.button_sum.clicked.connect(lambda: self.clicked_sum())
        self.button_1st_quart.clicked.connect(lambda: self.clicked_1st_quart())
        self.button_3rd_quart.clicked.connect(lambda: self.clicked_3rd_quart())

    def insert_character(self, char: str) -> None:
        """
        Method for inserting button characters in the calculator display
        """
        self.calculator_display.insertPlainText(char)

    def clicked_0(self) -> None:
        """
        Method for adding a 0 to the calculator display
        """
        self.check_answer_display()
        self.insert_character('0')
    def clicked_1(self) -> None:
        """
        Method for adding a 1 to the calculator display
        """
        self.check_answer_display()
        self.insert_character('1')
    def clicked_2(self) -> None:
        """
        Method for adding a 2 to the calculator display
        """
        self.check_answer_display()
        self.insert_character('2')
    def clicked_3(self) -> None:
        """
        Method for adding a 3 to the calculator display
        """
        self.check_answer_display()
        self.insert_character('3')
    def clicked_4(self) -> None:
        """
        Method for adding a 4 to the calculator display
        """
        self.check_answer_display()
        self.insert_character('4')
    def clicked_5(self) -> None:
        """
        Method for adding a 5 to the calculator display
        """
        self.check_answer_display()
        self.insert_character('5')
    def clicked_6(self) -> None:
        """
        Method for adding a 6 to the calculator display
        """
        self.check_answer_display()
        self.insert_character('6')
    def clicked_7(self) -> None:
        """
        Method for adding a 7 to the calculator display
        """
        self.check_answer_display()
        self.insert_character('7')
    def clicked_8(self) -> None:
        """
        Method for adding an 8 to the calculator display
        """
        self.check_answer_display()
        self.insert_character('8')
    def clicked_9(self) -> None:
        """
        Method for adding a 9 to the calculator display
        """
        self.check_answer_display()
        self.insert_character('9')
    def clicked_comma(self) -> None:
        """
        Method for adding a comma to the calculator display
        """
        self.check_answer_display()
        self.insert_character(',')
    def clicked_decimal(self) -> None:
        """
        Method for adding a decimal to the calculator display
        """
        self.check_answer_display()
        self.insert_character('.')

    def clear(self) -> None:
        """
        Method for clearing the calculator display and answer display
        """
        self.calculator_display.clear()
        self.answer_display.clear()
        self.calculator_display.setText('')
        if self.data_status:
            if len(self.dataset) > 0:
                self.dataset = []
                self.label_mode.setText('')
                self.data_status = False
                self.calculator_display.clear()
                self.answer_display.clear()

    def delete(self) -> None:
        """
        Method for deleting the previous character in the calculator display
        """
        if self.answer_display.text() == '':
            self.cursor.deletePreviousChar()
        else:
            pass

    def clicked_add(self) -> None:
        """
        Method for adding an addition '+' sign to the calculator display
        """
        if self.answer_display.text() != '':
            self.clear()
            self.calculator_display.insertPlainText(f'{self.ans}+')
        elif self.ans != '' and self.answer_display.text() == '' and self.calculator_display.toPlainText() == '':
            self.calculator_display.insertPlainText(f'{self.ans}+')
        else:
            self.calculator_display.insertPlainText("+")

    def clicked_subtract(self) -> None:
        """
        Method for adding a subtraction '-' sign to the calculator display
        """
        if self.answer_display.text() != '':
            self.clear()
            self.calculator_display.insertPlainText(f'{self.ans}-')
        elif self.ans != '' and self.answer_display.text() == '' and self.calculator_display.toPlainText() == '':
            self.calculator_display.insertPlainText(f'{self.ans}-')
        else:
            self.calculator_display.insertPlainText("-")

    def clicked_multiply(self) -> None:
        """
        Method for adding a multiplication '*' sign to the calculator display
        """
        if self.answer_display.text() != '':
            self.clear()
            self.calculator_display.insertPlainText(f'{self.ans}*')
        elif self.ans != '' and self.answer_display.text() == '' and self.calculator_display.toPlainText() == '':
            self.calculator_display.insertPlainText(f'{self.ans}*')
        else:
            self.calculator_display.insertPlainText("*")

    def clicked_divide(self) -> None:
        """
        Method for adding a division '/' sign to the calculator display
        """
        if self.answer_display.text() != '':
            self.clear()
            self.calculator_display.insertPlainText(f'{self.ans}/')
        elif self.ans != '' and self.answer_display.text() == '' and self.calculator_display.toPlainText() == '':
            self.calculator_display.insertPlainText(f'{self.ans}/')
        else:
            self.calculator_display.insertPlainText("/")

    def clicked_data(self) -> None:
        """
        Method that handles the creation and saving of a dataset (list) entered to the calculator display
        """
        if not self.data_status:
            if len(self.dataset) == 0:
                self.label_mode.setText('Mode: Data')
                self.clear()
                self.calculator_display.insertPlainText('[')
                self.data_status = True
                self.stats_status = False
                self.button_stats.setDisabled(True)
                self.button_comma.setDisabled(False)
                self.button_add.setDisabled(True)
                self.button_subtract.setDisabled(True)
                self.button_multiply.setDisabled(True)
                self.button_divide.setDisabled(True)
                # self.button_decimal.setDisabled(True)
            elif len(self.dataset) > 0:
                self.label_mode.setText('Mode: Data')
                self.data_status = True
                self.stats_status = False
                self.calculator_display.setPlainText(str(self.dataset))
                self.answer_display.clear()
        elif self.data_status:
            if len(self.dataset) == 0:
                self.label_mode.setText('Saved data set')
                self.calculator_display.insertPlainText(']')
                self.dataset = eval(self.calculator_display.toPlainText())
                self.data_status = False
                self.button_stats.setDisabled(False)
                self.button_comma.setDisabled(True)
                self.button_add.setDisabled(False)
                self.button_subtract.setDisabled(False)
                self.button_multiply.setDisabled(False)
                self.button_divide.setDisabled(False)
            elif len(self.dataset) > 0:
                self.label_mode.setText('')
                self.calculator_display.setPlainText(str(self.dataset))
                self.data_status = False
            else:
                self.label_mode.setText('')
                self.data_status = False

    def clicked_stats(self) -> None:
        """
        Method that changes the calculator mode to 'stats' and enables the statistical function buttons
        """
        if not self.stats_status:
            self.label_mode.setText('Mode: Stats')
            self.stats_status = True
            self.data_status = False
            self.button_mean.setDisabled(False)
            self.button_median.setDisabled(False)
            self.button_sum.setDisabled(False)
            self.button_1st_quart.setDisabled(False)
            self.button_3rd_quart.setDisabled(False)
        elif self.stats_status:
            self.label_mode.setText('')
            self.stats_status = False
            self.button_mean.setDisabled(True)
            self.button_median.setDisabled(True)
            self.button_sum.setDisabled(True)
            self.button_1st_quart.setDisabled(True)
            self.button_3rd_quart.setDisabled(True)

    def clicked_mean(self) -> None:
        """
        Method that displays the mean of a stored dataset
        """
        mean = sum(self.dataset) / len(self.dataset)
        self.answer_display.setText(str(mean))

    def clicked_median(self) -> None:
        """
        Method that displays the median of a stored dataset
        """
        dataset = sorted(self.dataset)
        if len(dataset) > 0:
            if len(dataset) % 2 == 0:
                self.answer_display.setText(str(find_median(dataset)))
            elif len(dataset) % 2 == 1:
                self.answer_display.setText(str(find_median(dataset)))
        else:
            pass

    def clicked_sum(self) -> None:
        """
        Method that displays the sum of a stored dataset
        """
        if len(self.dataset) > 0:
            self.answer_display.setText(str(sum(self.dataset)))
        else:
            pass

    def clicked_1st_quart(self) -> None:
        """
        Method that displays the first quartile of a stored dataset
        """
        dataset = sorted(self.dataset)
        lower_data = dataset[:len(dataset)//2]
        if len(lower_data) % 2 == 0:
            self.answer_display.setText(str(find_median(lower_data)))
            pass
        else:
            self.answer_display.setText(str(find_median(lower_data)))
            pass

    def clicked_3rd_quart(self) -> None:
        """
        Method that displays the third quartile of a stored dataset
        """
        dataset = sorted(self.dataset)
        upper_data = dataset[len(dataset)//2:]
        if len(upper_data) % 2 == 0:
            self.answer_display.setText(str(find_median(upper_data)))
            pass
        else:
            upper_data = dataset[(len(dataset) // 2) + 1:]
            self.answer_display.setText(str(find_median(upper_data)))
            pass

    def clicked_enter(self) -> None:
        """
        Method that takes text on the calculator display, converts it to int, and displays an answer if valid
        """
        try:
            equation = self.calculator_display.toPlainText()
            answer = str(eval(equation))
            if len(answer) <= 25:
                if len(answer) > 10 and eval(answer) > 999999999:
                    self.answer_display.setText(f'{(answer[:1] + '.' + answer[1:10]).strip('0')}e{str((len(answer) - 1))}')
                elif eval(answer) < 999999999:
                    self.answer_display.setText(f'{str(answer[:11])}')
                    self.ans = answer[:11]
                else:
                    self.answer_display.setText(answer)
                    self.ans = answer
            else:
                self.answer_display.setText('OVERFLOW ERROR')
        except ZeroDivisionError:
            self.answer_display.setText('DIVIDE BY 0 ERROR')
        except OverflowError:
            self.answer_display.setText('OVERFLOW ERROR')
        except SyntaxError:
            self.answer_display.setText('SYNTAX ERROR')
        except:
            self.answer_display.setText('ERROR')

    def check_answer_display(self) -> bool:
        """
        Method that checks to see if the answer display is empty
        """
        if self.answer_display.text() != '':
            self.clear()
            return True
        else:
            return False
