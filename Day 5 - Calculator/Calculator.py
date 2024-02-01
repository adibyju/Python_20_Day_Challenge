import sys
import re
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QSpacerItem, QSizePolicy
import pyshorteners


class CalculatorApp(QWidget):
    """Main application class for a basic calculator using PyQt5."""

    def __init__(self):
        QWidget.__init__(self)

        # Setup window properties
        self.setWindowTitle("Calculator")
        self.setGeometry(100, 100, 400, 400)

        # Define display areas for calculation and result
        self.CalculationSpace = QtWidgets.QLineEdit(self)
        self.CalculationSpace.setReadOnly(True)
        self.CalculationSpace.setMaxLength(50)

        self.ResultSpace = QtWidgets.QLabel(self)
        self.ResultSpace.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        self.ResultSpace.setObjectName("result_space")
        self.ResultSpace.setStyleSheet("QLabel#result_space {color: blue}")

        self.ResultLabel = QtWidgets.QLabel(self)
        self.ResultLabel.setText("RESULT:")

        # Result horizontal layout
        layoutResult = QtWidgets.QHBoxLayout()
        layoutResult.addWidget(self.ResultLabel)
        layoutResult.addWidget(self.ResultSpace)

        # Delete button horizontal layout
        self.DeleteButton = QtWidgets.QPushButton("Del")
        layoutDelete = QtWidgets.QHBoxLayout()
        layoutDelete.addItem(
            QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        )
        layoutDelete.addWidget(self.DeleteButton)

        # 1st row of calculator
        self.ResetButton = QtWidgets.QPushButton("C")
        self.ParanthesesButton = QtWidgets.QPushButton("()")
        self.PercentageButton = QtWidgets.QPushButton("%")
        self.DivideButton = QtWidgets.QPushButton("/")
        layout1stRow = QtWidgets.QHBoxLayout()
        layout1stRow.addWidget(self.ResetButton)
        layout1stRow.addWidget(self.ParanthesesButton)
        layout1stRow.addWidget(self.PercentageButton)
        layout1stRow.addWidget(self.DivideButton)

        # 2nd row of calculator
        self._7Button = QtWidgets.QPushButton("7")
        self._8Button = QtWidgets.QPushButton("8")
        self._9Button = QtWidgets.QPushButton("9")
        self.MultiplyButton = QtWidgets.QPushButton("*")
        layout2ndRow = QtWidgets.QHBoxLayout()
        layout2ndRow.addWidget(self._7Button)
        layout2ndRow.addWidget(self._8Button)
        layout2ndRow.addWidget(self._9Button)
        layout2ndRow.addWidget(self.MultiplyButton)

        # 3rd row of calculator
        self._4Button = QtWidgets.QPushButton("4")
        self._5Button = QtWidgets.QPushButton("5")
        self._6Button = QtWidgets.QPushButton("6")
        self.SubtractButton = QtWidgets.QPushButton("-")
        layout3rdRow = QtWidgets.QHBoxLayout()
        layout3rdRow.addWidget(self._4Button)
        layout3rdRow.addWidget(self._5Button)
        layout3rdRow.addWidget(self._6Button)
        layout3rdRow.addWidget(self.SubtractButton)

        # 4th row of calculator
        self._1Button = QtWidgets.QPushButton("1")
        self._2Button = QtWidgets.QPushButton("2")
        self._3Button = QtWidgets.QPushButton("3")
        self.AddButton = QtWidgets.QPushButton("+")
        layout4thRow = QtWidgets.QHBoxLayout()
        layout4thRow.addWidget(self._1Button)
        layout4thRow.addWidget(self._2Button)
        layout4thRow.addWidget(self._3Button)
        layout4thRow.addWidget(self.AddButton)

        # 5th row of calculator
        self.SignButton = QtWidgets.QPushButton("+/-")
        self._0Button = QtWidgets.QPushButton("0")
        self.DotButton = QtWidgets.QPushButton(".")
        self.EqualButton = QtWidgets.QPushButton("=")
        layout5thRow = QtWidgets.QHBoxLayout()
        layout5thRow.addWidget(self.SignButton)
        layout5thRow.addWidget(self._0Button)
        layout5thRow.addWidget(self.DotButton)
        layout5thRow.addWidget(self.EqualButton)

        # Create a vertical layout of all the components using QVBoxLayout
        layoutMain = QtWidgets.QVBoxLayout()
        layoutMain.addWidget(self.CalculationSpace)
        layoutMain.addLayout(layoutResult)
        layoutMain.addLayout(layoutDelete)
        layoutMain.addLayout(layout1stRow)
        layoutMain.addLayout(layout2ndRow)
        layoutMain.addLayout(layout3rdRow)
        layoutMain.addLayout(layout4thRow)
        layoutMain.addLayout(layout5thRow)

        # Set the layout to the main app
        self.setLayout(layoutMain)

        # Initialize the count of open parentheses
        self.numOpenParenthesis = 0

        # Connect buttons to their respective functions
        self.ResetButton.clicked.connect(self.reset_function)
        self.DeleteButton.clicked.connect(self.delete_function)
        self.EqualButton.clicked.connect(self.eval_function)

        self._0Button.clicked.connect(lambda: self.add_function(self._0Button))
        self._1Button.clicked.connect(lambda: self.add_function(self._1Button))
        self._2Button.clicked.connect(lambda: self.add_function(self._2Button))
        self._3Button.clicked.connect(lambda: self.add_function(self._3Button))
        self._4Button.clicked.connect(lambda: self.add_function(self._4Button))
        self._5Button.clicked.connect(lambda: self.add_function(self._5Button))
        self._6Button.clicked.connect(lambda: self.add_function(self._6Button))
        self._7Button.clicked.connect(lambda: self.add_function(self._7Button))
        self._8Button.clicked.connect(lambda: self.add_function(self._8Button))
        self._9Button.clicked.connect(lambda: self.add_function(self._9Button))

        self.DotButton.clicked.connect(lambda: self.add_function(self.DotButton))
        self.AddButton.clicked.connect(lambda: self.add_function(self.AddButton))
        self.SubtractButton.clicked.connect(
            lambda: self.add_function(self.SubtractButton)
        )
        self.MultiplyButton.clicked.connect(
            lambda: self.add_function(self.MultiplyButton)
        )
        self.DivideButton.clicked.connect(lambda: self.add_function(self.DivideButton))
        self.PercentageButton.clicked.connect(
            lambda: self.add_function(self.PercentageButton)
        )
        self.ParanthesesButton.clicked.connect(
            lambda: self.add_function(self.ParanthesesButton)
        )
        self.SignButton.clicked.connect(lambda: self.add_function(self.SignButton))

    def reset_function(self):
        """Clears all input and resets the calculator."""
        self.numOpenParenthesis = 0
        self.CalculationSpace.setText("")

    def delete_function(self):
        """Deletes the last character from the input field."""
        temp = self.CalculationSpace.text()
        if temp == "":
            return
        if temp[-1] == ")":
            self.numOpenParenthesis += 1
        elif temp[-1] == "(":
            self.numOpenParenthesis -= 1
        self.CalculationSpace.setText(temp[:-1])

    def eval_function(self):
        """Evaluates the expression entered in the calculator."""
        exp = self.CalculationSpace.text()
        exp = exp.replace("%", "/100")
        for char in exp:
            if char not in "0123456789.()+-/*%":
                return
        if exp == "" or exp[-1] in "-*/":
            return
        if self.numOpenParenthesis != 0:
            exp += ")" * self.numOpenParenthesis
        try:
            result = eval(exp)
        except:
            self.ResultSpace.setText("Error: Div by 0")
            return
        if not isinstance(result, int):
            result = format(result, ".4f")
        self.ResultSpace.setText(str(result))

    def find_function(self, x):
        """Finds the index of the first non-digit character in the given string."""
        return next((i for i, char in enumerate(x) if not char.isdigit()), -1)

    def add_function(self, button):
        """Adds the character of the pressed button to the calculation space."""
        calcText = self.CalculationSpace.text()
        bText = button.text()
        result = ""
        if bText == "%":
            if calcText != "" and calcText[-1] in "0123456789":
                result = calcText + "%"
            else:
                return
        elif bText in "+-/*":
            if calcText == "":
                result = ""
            elif calcText[-1] in "+-/*":
                result = calcText[:-1] + bText
            else:
                result = calcText + bText
        elif bText == ".":
            if calcText == "":
                result = "0."
            elif calcText[-1] in "0123456789":
                result = calcText + "."
            elif calcText[-1] in "%()":
                result = calcText + "*0."
            elif calcText[-1] == ".":
                return
            else:
                result = calcText + "0."
        elif bText == "()":
            if calcText == "":
                result = "("
                self.numOpenParenthesis += 1
            elif calcText[-1] in "0123456789%.)":
                if self.numOpenParenthesis > 0:
                    result = calcText + ")"
                    self.numOpenParenthesis -= 1
                else:
                    result = calcText + "*("
                    self.numOpenParenthesis += 1
            elif calcText[-1] in "+-/*(":
                result = calcText + "("
                self.numOpenParenthesis += 1
        elif bText == "+/-":
            if calcText == "":
                result = "(-"
                self.numOpenParenthesis += 1
            elif calcText[-2:] == "(-":
                result = calcText[:-2]
            elif calcText[-1] == "%":
                result = calcText + "*(-"
                self.numOpenParenthesis += 1
            elif calcText[-1] in "+-/*":
                result = calcText + "(-"
                self.numOpenParenthesis += 1
            else:
                size = len(calcText)
                tempText = calcText[::-1]
                index = self.find_function(tempText)
                index = size - index - 1
                if index == size:
                    result = "(-" + calcText
                    self.numOpenParenthesis += 1
                elif calcText[index - 1 : index + 1] == "(-":
                    result = calcText[: index - 1] + calcText[index + 1 :]
                    self.numOpenParenthesis -= 1
                else:
                    result = calcText[: index + 1] + "(-" + calcText[index + 1 :]
                    self.numOpenParenthesis += 1
        else:
            result = calcText + bText
        self.CalculationSpace.setText(result)


# Main entry point for the application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainApp = CalculatorApp()
    mainApp.show()
    sys.exit(app.exec_())
