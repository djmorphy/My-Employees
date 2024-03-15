from PyQt5.QtWidgets import *
import sys


class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('My Employees')
        self.setGeometry(350, 150, 400, 400)
        self.UI()
        self.show()

    def UI(self):
        self.mainDesing()

        pass

    def mainDesing(self):
        pass


def main():
    App = QApplication(sys.argv)
    window = Main()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()
