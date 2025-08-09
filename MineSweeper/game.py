import sys
import random
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from PyQt5 import uic, QtGui
from game_ui import Ui_Form  # 这里是你 pyuic5 转换出来的文件名（我假设是 game_ui.py）

class GameWindow(QWidget):
    def __init__(self, name="未知用户", rows=9, cols=9,mines=10,level=0):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.first_flag = True#判断是否是开局第一次点击
        self.enable_flag = True  # 用于判断是否可以点击

        self.elapsed_time = 0
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_timer)
        self.ui.label_2.setText("时间：0秒")

        self.rows = rows
        self.cols = cols
        self.mine_count = mines
        self.level = level

        self.name = name
        self.buttons = [[None for _ in range(self.cols)] for _ in range(self.rows)]
        self.total_cells = self.rows * self.cols -self.mine_count
        # 在 Qt Designer 的 gridLayout 里批量添加按钮
        for r in range(self.rows):
            for c in range(self.cols):
                btn = QPushButton("")
                btn.setFixedSize(30, 30)
                btn.clicked.connect(lambda _, x=r, y=c: self.on_click(x, y))
                self.buttons[r][c] = btn
                self.ui.gridLayout.addWidget(btn, r, c)
                self.buttons[r][c].setStyleSheet("background-color: #d3d3d3; color: black;")


    def start_game(self, first_r, first_c):
        self.mine_nums = [[0] * self.cols for _ in range(self.rows)]
        # 排除第一次点击格子及周围8格
        exclude = [(first_r + dr, first_c + dc) for dr in (-1, 0, 1) for dc in (-1, 0, 1) if 0 <= first_r + dr < self.rows and 0 <= first_c + dc < self.cols]
        available_cells = [cell for cell in [(i, j) for i in range(self.rows) for j in range(self.cols)] if cell not in exclude]
        mine_positions = random.sample(available_cells, self.mine_count)
        for (r, c) in mine_positions:
            self.mine_nums[r][c] = 1
        self.elapsed_time = 0
        self.ui.label_2.setText("时间：0秒")
        self.timer.start(1000)  # 启动计时器，每秒触发一次

    def update_timer(self):
        self.elapsed_time += 1
        self.ui.label_2.setText(f"时间：{self.elapsed_time}秒")

    def on_click(self, r, c):
        if not self.enable_flag:
            return
        self.buttons[r][c].setStyleSheet("background-color: white; color: #333333;")
        if self.first_flag == True:
            self.buttons[r][c].setText(str('-'))
            self.start_game(r,c)
            self.first_flag = False

        if self.mine_nums[r][c]==1:
            QMessageBox.critical(None, '游戏结束', '你被炸死了！',QMessageBox.StandardButton.Ok)
            self.enable_flag = False
            self.timer.stop()

        count=0
        for i in range(-1,2):
            for j in range(-1,2):
                if 0<=r+i<self.rows and 0<=c+j<self.cols and self.mine_nums[r+i][c+j]==1:
                    count=count+1
        print(f"点击了 {r}, {c},值是 {self.mine_nums[r][c]}")
        if count:
            self.buttons[r][c].setText(str(count))
        else:
            self.buttons[r][c].setText(str('-'))
            for i in range(-1, 2):
                for j in range(-1, 2):
                    nr, nc = r + i, c + j
                    if 0 <= nr < self.rows and 0 <= nc < self.cols:
                        if self.buttons[nr][nc].text() == "":
                            self.on_click(nr, nc)

        self.total_cells = self.total_cells - 1
        if not self.total_cells:
            QMessageBox.information(None, '游戏结束', '恭喜您，通关！', QMessageBox.StandardButton.Ok)
            self.enable_flag = False
            self.timer.stop()
            self.save_score()

    def save_score(self):
        # 难度为0不记录
        if self.level == 0:
            return
        try:
            with open("scores.txt", "a", encoding="utf-8") as f:
                f.write(f"{self.name},{self.elapsed_time},{self.level}\n")
        except Exception as e:
            print("保存成绩失败:", e)


# 如果想单独运行游戏窗口
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = GameWindow()
    win.show()
    sys.exit(app.exec_())
