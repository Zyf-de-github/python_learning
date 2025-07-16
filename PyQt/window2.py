import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from window2_ui import Ui_Form2  # 导入 UI 文件

# class Calculator2(QMainWindow, Ui_Form2):
#     def __init__(self):
#         super().__init__()
#         self.setupUi(self)
#         self.initUI()

class Calculator2(QMainWindow, Ui_Form2):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent_window = parent  # 保存主窗口对象
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        # 按钮连接
        self.b_return.clicked.connect(self.return_main)

    def return_main(self):
        # if self.parent():
        #     self.parent().show()
        self.parent_window.show()
        self.close()

