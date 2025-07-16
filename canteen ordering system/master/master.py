import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from master_ui import Ui_Form
from pay.pay import Pay
class Master(QMainWindow, Ui_Form):
    def __init__(self):
        super(Master, self).__init__()
        self.setupUi(self)
        self.initUI()
        self.current_dish = None
        self.waiting.addItem("您将点的菜品将会显示在此处")
        self.dish_prices = {
            "锅盔": 2,
            "米饭": 1,
            "面条": 3,
            "炒白菜": 15,
            "炒西兰花": 18,
            "糖醋里脊": 25,
            "回锅肉盖饭": 25,
            "酸辣白菜盖饭": 18,
            "红烧茄子盖饭": 20,
            "土豆丝盖饭": 18,
            "冰红茶": 3,
            "冰糖雪梨": 3,
            "大窑": 3,
            "酸梅汤": 3,
        }

    def initUI(self):
        self.menu.itemClicked.connect(self.on_category_changed)
        self.bind_dish_buttons()
        self.add.clicked.connect(self.add_to_waiting)
        self.deleted.clicked.connect(self.deleted_from_waiting)
        self.pay.clicked.connect(self.pay_waiting)

    def on_category_changed(self, item):
        name = item.text()
        if name == "主食":
            self.stackedWidget.setCurrentIndex(0)
        elif name == "炒菜":
            self.stackedWidget.setCurrentIndex(1)
        elif name == "盖饭":
            self.stackedWidget.setCurrentIndex(2)
        elif name == "饮品":
            self.stackedWidget.setCurrentIndex(3)


    def bind_dish_buttons(self):
        self.GK.clicked.connect(lambda: self.select_dish("锅盔"))
        self.MF.clicked.connect(lambda: self.select_dish("米饭"))
        self.MT.clicked.connect(lambda: self.select_dish("面条"))
        self.CBC.clicked.connect(lambda: self.select_dish("炒白菜"))
        self.CXLH.clicked.connect(lambda: self.select_dish("炒西兰花"))
        self.TCLJ.clicked.connect(lambda: self.select_dish("糖醋里脊"))
        self.HGR.clicked.connect(lambda: self.select_dish("回锅肉盖饭"))
        self.SLBC.clicked.connect(lambda: self.select_dish("酸辣白菜盖饭"))
        self.HSQZ.clicked.connect(lambda: self.select_dish("红烧茄子盖饭"))
        self.TDS.clicked.connect(lambda: self.select_dish("土豆丝盖饭"))
        self.BHC.clicked.connect(lambda: self.select_dish("冰红茶"))
        self.BTXL.clicked.connect(lambda: self.select_dish("冰糖雪梨"))
        self.DY.clicked.connect(lambda: self.select_dish("大窑"))
        self.SMT.clicked.connect(lambda: self.select_dish("酸梅汤"))

    def select_dish(self, dish_name):
        self.current_dish = dish_name
        self.message.setText(f"已选中：{dish_name}")

    def add_to_waiting(self):
        if self.current_dish is None:
            self.message.setText("请先选择一个菜品再加入购物车")
        else:
            if self.waiting.item(0).text() == "您将点的菜品将会显示在此处":
                self.waiting.clear()
            price = self.dish_prices.get(self.current_dish)
            self.waiting.addItem(f"{self.current_dish}-{price}")
            self.message.setText("菜品加入成功")
            self.current_dish = None

    def deleted_from_waiting(self):
        for item in self.waiting.selectedItems():
            self.waiting.takeItem(self.waiting.row(item))
            self.message.setText("菜品移除成功")
        if self.waiting.count() == 0:
            self.waiting.addItem("您将点的菜品将会显示在此处")

    def pay_waiting(self):
        total = 0
        for i in range(self.waiting.count()):
            item_text = self.waiting.item(i).text()
            if "-" in item_text:
                try:
                    #split(x)是以x把字符串分割，返回一个列表，这里-1是取最后一个元素
                    price_part = item_text.split("-")[-1]
                    total += int(price_part)
                except ValueError:
                    continue
        if total == 0:
            self.message.setText("购物车为空，无法支付。")
            return
        self.temp = Pay(self, total)
        self.temp.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Master = Master()
    Master.show()
    sys.exit(app.exec_())

# from PyQt5.QtWidgets import QApplication, QMainWindow
# from master_ui import Ui_Form
#
#
# class MasterWindow(QMainWindow, Ui_Form):
#     def __init__(self):
#         super().__init__()
#         self.setupUi(self)
#
#         # 当前选中的菜名
#         self.current_dish = None
#
#         # 初始化购物车提示
#         self.waitting.addItem("您将点的菜品将会显示在此处")
#
#         # 绑定菜单栏分类切换
#         self.menu.itemClicked.connect(self.change_category)
#
#         # 绑定菜品按钮
#         self.bind_dish_buttons()
#
#         # 绑定按钮事件
#         self.add.clicked.connect(self.add_to_cart)
#         self.deleat.clicked.connect(self.remove_from_cart)
#
#     def change_category(self, item):
#         text = item.text()
#         if text == "主食":
#             self.stackedWidget.setCurrentIndex(0)
#         elif text == "炒菜":
#             self.stackedWidget.setCurrentIndex(1)
#         elif text == "盖饭":
#             self.stackedWidget.setCurrentIndex(2)
#         elif text == "饮品":
#             self.stackedWidget.setCurrentIndex(3)
#
#     def bind_dish_buttons(self):
#         dish_map = {
#             self.GK: "锅盔", self.MF: "米饭", self.MT: "面条",
#             self.CBC: "炒白菜", self.CXLH: "炒西兰花", self.TCLJ: "糖醋里脊",
#             self.HGR: "回锅肉盖饭", self.SLBC: "酸辣白菜盖饭",
#             self.HSQZ: "红烧茄子盖饭", self.TDS: "土豆丝盖饭",
#             self.BHC: "冰红茶", self.BTXL: "冰糖雪梨", self.DY: "大窑", self.SMT: "酸梅汤"
#         }
#
#         for btn, name in dish_map.items():
#             btn.clicked.connect(lambda _, dish=name: self.select_dish(dish))
#
#     def select_dish(self, dish_name):
#         self.current_dish = dish_name
#         self.statusBar().showMessage(f"已选中：{dish_name}", 2000)
#
#     def add_to_cart(self):
#         if self.current_dish is None:
#             self.statusBar().showMessage("请先选择一个菜品再加入购物车", 2000)
#             return
#
#         # 第一次添加清空提示
#         if self.waitting.count() == 1 and self.waitting.item(0).text() == "您将点的菜品将会显示在此处":
#             self.waitting.clear()
#
#         self.waitting.addItem(self.current_dish)
#         self.current_dish = None
#
#     def remove_from_cart(self):
#         selected_items = self.waitting.selectedItems()
#         if not selected_items:
#             self.statusBar().showMessage("请先选中购物车中的菜品", 2000)
#             return
#
#         for item in selected_items:
#             self.waitting.takeItem(self.waitting.row(item))
#
#         if self.waitting.count() == 0:
#             self.waitting.addItem("您将点的菜品将会显示在此处")
#
# if __name__ == "__main__":
#     import sys
#     app = QApplication(sys.argv)
#     window = MasterWindow()
#     window.show()
#     sys.exit(app.exec_())
