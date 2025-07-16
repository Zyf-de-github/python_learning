import os
from PyQt5.QtWidgets import QApplication, QMainWindow
from .pay_ui import Ui_Form  # 导入 UI 文件
from PyQt5.QtGui import QPixmap

class Pay(QMainWindow, Ui_Form):
    def __init__(self, parent=None,total=0):
        super().__init__(parent)
        self.parent_window = parent  # 保存主窗口对象
        self.setupUi(self)
        self.initUI()
        self.total.setText(f"应付款：{total}")
        pixmap = QPixmap(os.path.join(os.path.dirname(__file__), "pay.jpg"))
        self.label.setPixmap(pixmap)
        self.label.setScaledContents(True)

    def initUI(self):
        self.back.clicked.connect(self.return_main)

    def return_main(self):
        self.parent_window.show()
        self.close()
