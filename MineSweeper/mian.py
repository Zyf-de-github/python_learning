import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from MineSweeper_ui import Ui_Form
from game import GameWindow
class MineSweeperWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle("扫雷游戏——zyf")
        #事件绑定
        self.ui.pushButton.clicked.connect(self.start_game)
        self.ui.radioButton.toggled.connect(self.updateLabel)
        self.ui.radioButton_2.toggled.connect(self.updateLabel)
        self.ui.radioButton_3.toggled.connect(self.updateLabel)
        self.ui.pushButton_2.clicked.connect(self.load_and_show_scores)
        #初始化
        self.load_and_show_scores()#初始化排行榜
        self.username = "未知用户"#初始化用户名
        #默认配置参数
        self.rows = 8
        self.cols = 8
        self.mines = 10
        self.level = 0

    #点击开始游戏按钮后，创建游戏窗口，并默认初始化用户名
    def start_game(self):
        self.username = self.ui.lineEdit.text().strip()
        if not self.username:
            self.username="未知用户"
        print(f"欢迎{self.username}来到扫雷游戏！")
        temp=GameWindow(self.username,self.rows,self.cols,self.mines,self.level)
        temp.show()

    #选择难度并修改行列参数
    def updateLabel(self):
        if self.ui.radioButton.isChecked():
            print("选项1被选中了！")
            self.rows = 8
            self.cols = 8
            self.mines = 10
            self.level = 1
        elif self.ui.radioButton_2.isChecked():
            print("选项2被选中了！")
            self.rows = 16
            self.cols = 16
            self.mines = 40
            self.level = 2
        elif self.ui.radioButton_3.isChecked():
            print("选项3被选中了！")
            self.rows = 16
            self.cols = 30
            self.mines = 99
            self.level = 3
        elif self.ui.radioButton_4.isChecked():
            print("选项4被选中了！")
            if self.ui.lineEdit_3.text().strip()=='' or self.ui.lineEdit_4.text().strip()=='' or self.ui.lineEdit_2.text().strip()=='':
                QMessageBox.warning(None, '警告', '请填写完整，否则将以默认配置开始游戏！',QMessageBox.StandardButton.Ok)
                return
            self.rows = int(self.ui.lineEdit_3.text().strip())
            self.cols = int(self.ui.lineEdit_2.text().strip())
            if self.rows<3 or self.cols<3 or self.rows>50 or self.cols>50:
                QMessageBox.warning(None, '警告', '行数和列数必须大于等于3且小于50！',QMessageBox.StandardButton.Ok)
                return
            self.mines = int(self.ui.lineEdit_4.text().strip())
            if self.mines<1 or self.mines>=self.rows*self.cols:
                QMessageBox.warning(None, '警告', '雷数必须大于零且小于行数乘列数！',QMessageBox.StandardButton.Ok)
                return
            self.level = 0
            print(self.rows)
            print(self.cols)
            print(self.mines)

    #排行榜读文件数据，并显示
    def load_and_show_scores(self):
        try:
            with open("scores.txt", "r", encoding="utf-8") as f:
                lines = f.readlines()
        except FileNotFoundError:
            self.ui.textEdit.setPlainText("暂无成绩记录")
            return

        scores = []
        for line in lines:
            line = line.strip()
            if not line:
                continue
            parts = line.split(",")
            if len(parts) != 3:
                continue
            name, time_str, level_str = parts
            try:
                time_val = int(time_str)
                level_val = int(level_str)
            except:
                continue
            scores.append((level_val, time_val, name))
        # 先按难度升序，难度相同按时间升序
        scores.sort(key=lambda x: (x[0], x[1]))
        # 格式化显示
        display_text = "难度 | 时间(秒) | 用户名\n"
        display_text += "-" * 30 + "\n"
        for lvl, t, nm in scores:
            display_text += f"{lvl:^6} | {t:^8} | {nm}\n"
        self.ui.textEdit.setPlainText(display_text)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MineSweeperWindow()
    window.show()
    sys.exit(app.exec_())
