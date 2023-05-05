import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget

class CountdownTimerApp(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Countdown Timer App using Python")
        self.setGeometry(100,100,400,200)

        # create the timer label and display widgets
        self.timerLabel = QtWidgets.QLabel("Enter duration in HH:MM:SS format:")
        self.timerDisplay = QtWidgets.QLineEdit(self)

        # create the start, pause, and reset buttons
        self.startButton = QtWidgets.QPushButton("Start")
        self.pauseButton = QtWidgets.QPushButton("Pause")
        self.resetButton = QtWidgets.QPushButton("Reset")

        # define the layouts
        layoutVertical = QtWidgets.QVBoxLayout(self)

        layoutVertical.addWidget(self.timerLabel)
        layoutVertical.addWidget(self.timerDisplay)        

        layoutHorizontal = QtWidgets.QHBoxLayout()

        layoutHorizontal.addWidget(self.startButton)
        layoutHorizontal.addWidget(self.pauseButton)
        layoutHorizontal.addWidget(self.resetButton)

        # adding horizontal layout of the buttons into the main vertical layout
        layoutVertical.addLayout(layoutHorizontal)

        # set the apps layout
        self.setLayout(layoutVertical)

        # assign functions to the different buttons
        self.startButton.clicked.connect(self.)
        self.pauseButton.clicked.connect(self.)
        self.resetButton.clicked.connect(self.)





    



if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainApp = CountdownTimerApp()
    mainApp.show()
    sys.exit(app.exec_())