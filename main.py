from calculator_project_logic import *


def main():
    application = QApplication([])
    window = Calculator()
    window.show()
    application.exec()


if __name__ == "__main__":
    main()