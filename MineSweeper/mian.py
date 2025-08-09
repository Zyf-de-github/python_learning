# main.py
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from MineSweeper_ui import Ui_Form  # 这里导入你生成的 py 文件类
from game import GameWindow  # 这里导入你自己编写的游戏类
class MineSweeperWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)  # 把 Ui_Form 里的控件加载到当前窗口

        # 在这里绑定你的按钮事件等
        self.ui.pushButton.clicked.connect(self.start_game)
        self.ui.radioButton.toggled.connect(self.updateLabel)
        self.ui.radioButton_2.toggled.connect(self.updateLabel)
        self.ui.radioButton_3.toggled.connect(self.updateLabel)

        self.username = "未知用户"
        self.rows = 8
        self.cols = 8
        self.mines = 10

    def start_game(self):
        self.username = self.ui.lineEdit.text().strip()
        if not self.username:
            self.username="未知用户"
        print(f"欢迎{self.username}来到扫雷游戏！")
        temp=GameWindow(self.username,self.rows,self.cols,self.mines)
        temp.show()

    def updateLabel(self):
        if self.ui.radioButton.isChecked():
            print("选项1被选中了！")
            self.rows = 8
            self.cols = 8
            self.mines = 10
        elif self.ui.radioButton_2.isChecked():
            print("选项2被选中了！")
            self.rows = 16
            self.cols = 16
            self.mines = 40
        elif self.ui.radioButton_3.isChecked():
            print("选项3被选中了！")
            self.rows = 16
            self.cols = 30
            self.mines = 99




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MineSweeperWindow()
    window.show()
    sys.exit(app.exec_())
