import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QWidget

class CountdownTimerApp(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Countdown Timer App")
        self.setGeometry(100,100,400,200)

        # create the timer label and display widgets
        self.timerLabel = QtWidgets.QLabel("Enter duration in HH:MM:SS format:")
        self.timerDisplay = QtWidgets.QLineEdit(self)
        self.timerDisplay.setAlignment(QtCore.Qt.AlignCenter) 

        # create the start, and reset buttons
        self.startButton = QtWidgets.QPushButton("Start")
        self.resetButton = QtWidgets.QPushButton("Reset")

        # define the layouts
        layoutVertical = QtWidgets.QVBoxLayout(self)

        layoutVertical.addWidget(self.timerLabel)
        layoutVertical.addWidget(self.timerDisplay)        

        layoutHorizontal = QtWidgets.QHBoxLayout()

        layoutHorizontal.addWidget(self.resetButton)
        layoutHorizontal.addWidget(self.startButton)
        

        # adding horizontal layout of the buttons into the main vertical layout
        layoutVertical.addLayout(layoutHorizontal)

        # set the apps layout
        self.setLayout(layoutVertical)

        # assign functions to the different buttons
        self.startButton.clicked.connect(self.timer_start)
        self.resetButton.clicked.connect(self.timer_reset)

        # use a boolean variable to help control state of time (running or not running)
        self.timer_running = False

        # make use of QTimer() to run the timer_update() function in intervals of 1 sec
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer_update)
    
    # start function
    def timer_start(self):
        self.timerLabel.setText("Timer running.")
        temp = self.timerDisplay.text().split(":")

        # extract total time duration in seconds
        self.timeDur = (
            int(temp[0]) * 3600 + int(temp[1]) * 60 + int(temp[2])
        )

        # start timer if duration>0
        if self.timeDur != 0:
            self.startButton.setText("Stop")
            self.startButton.clicked.connect(self.timer_stop)
        if not self.timer_running and self.timeDur != 0:
            self.timerDisplay.setEnabled(False)
            self.timer_update()
            self.timer_running = True

    # stop function
    def timer_stop(self):
        self.timerLabel.setText("Timer stopped.")
        self.startButton.setText("Start")
        self.startButton.clicked.connect(self.timer_start)
        if self.timer_running:
            # cancel updating of time using .stop() function
            self.timer.stop()
            self.timer_running = False

    # reset function
    def timer_reset(self):
        self.timerLabel.setText("Enter duration in HH:MM:SS format:")
        self.startButton.setText("Start")
        self.startButton.clicked.connect(self.timer_start)
        if self.timer_running:
            # cancel updating of time using .stop() function
            self.timer.stop()
            self.timer_running = False
        self.timerDisplay.setEnabled(True)
        self.timeDur = 0
        self.timerDisplay.setText("00:00:00")

    # update stopwatch function
    def timer_update(self):
        minute, second = (self.timeDur // 60, self.timeDur % 60)

        hour = 0

        if minute > 60:
            hour, minute = (minute // 60, minute % 60)

        if second < 10:
            second = "0" + str(second)
        if minute < 10:
            minute = "0" + str(minute)
        if hour < 10:
            hour = "0" + str(hour)

        # update current time
        timeNow = str(hour)+':'+str(minute)+':'+str(second)
        self.timerDisplay.setText(timeNow)

        if self.timeDur == 0:
            self.timer_reset()
            return

        self.timeDur -= 1

        self.timer.start(1000) # run the timer_update() function in an interval of 1 sec


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainApp = CountdownTimerApp()
    mainApp.show()
    sys.exit(app.exec_())