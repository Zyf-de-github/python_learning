import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from test_ui import Ui_Form  # 导入 UI 文件
from window2 import Calculator2

class Calculator(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()#调用父类（这里是 QMainWindow）的构造方法
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        # 按钮连接
        self.b_0.clicked.connect(lambda: self.input_value("0"))
        self.b_1.clicked.connect(lambda: self.input_value("1"))
        self.b_2.clicked.connect(lambda: self.input_value("2"))
        self.b_3.clicked.connect(lambda: self.input_value("3"))
        self.b_4.clicked.connect(lambda: self.input_value("4"))
        self.b_5.clicked.connect(lambda: self.input_value("5"))
        self.b_6.clicked.connect(lambda: self.input_value("6"))
        self.b_7.clicked.connect(lambda: self.input_value("7"))
        self.b_8.clicked.connect(lambda: self.input_value("8"))
        self.b_9.clicked.connect(lambda: self.input_value("9"))

        self.b_add.clicked.connect(lambda: self.input_value("+"))
        self.b_sub.clicked.connect(lambda: self.input_value("-"))
        self.b_mul.clicked.connect(lambda: self.input_value("*"))
        self.b_div.clicked.connect(lambda: self.input_value("/"))

        self.b_equal.clicked.connect(self.calculate)
        self.b_clear.clicked.connect(self.clear)
        self.b_new.clicked.connect(self.open_new_window)

    def input_value(self, val):
        current = self.lineEdit.text()
        self.lineEdit.setText(current + val)

    def calculate(self):
        expr = self.lineEdit.text()
        try:
            result = eval(expr)
            self.lineEdit.setText(str(result))
        except Exception:
            self.lineEdit.setText("Error")

    def clear(self):
        self.lineEdit.clear()

    def open_new_window(self):
        self.temp = Calculator2(self)  # ✅ 保留引用防止被销毁
        self.temp.show()  # ✅ 正确显示新窗口
        #self.hide()  # 可选：隐藏主窗口


if __name__ == "__main__":
    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())
