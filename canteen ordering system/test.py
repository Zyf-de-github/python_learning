from PyQt5.QtWidgets import (
    QApplication, QWidget, QListWidget, QStackedWidget,
    QHBoxLayout, QVBoxLayout, QLabel, QPushButton
)
import sys

class MenuPage(QWidget):
    def __init__(self, category_name, items):
        super().__init__()
        layout = QVBoxLayout()
        layout.addWidget(QLabel(f"【{category_name}】菜单"))
        for name in items:
            btn = QPushButton(f"{name} - 点击添加")
            layout.addWidget(btn)
        layout.addStretch()
        self.setLayout(layout)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("美团点单模拟")
        self.resize(600, 400)

        # 左边分类列表
        self.category_list = QListWidget()
        self.category_list.addItems(["奶茶", "主食", "小吃"])
        self.category_list.currentRowChanged.connect(self.switch_page)

        # 右边内容区：用 QStackedWidget 管理不同分类页面
        self.stack = QStackedWidget()
        self.stack.addWidget(MenuPage("奶茶", ["珍珠奶茶", "椰果奶茶"]))
        self.stack.addWidget(MenuPage("主食", ["牛肉饭", "盖浇饭"]))
        self.stack.addWidget(MenuPage("小吃", ["炸鸡", "薯条", "章鱼小丸子"]))

        # 主布局
        layout = QHBoxLayout()
        layout.addWidget(self.category_list, 1)
        layout.addWidget(self.stack, 3)
        self.setLayout(layout)

    def switch_page(self, index):
        self.stack.setCurrentIndex(index)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
