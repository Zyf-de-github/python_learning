##这是一个基于python和qt编写的扫雷游戏

项目目录结构：
- MineSweeper/          # 主程序文件夹
  - main.py             # 程序入口（主窗口）
  - MineSweeper_ui.py   # 由 Qt Designer 生成的主窗口界面文件
  - MineSweeper.py      #主窗口HTML原始文件

  - game.py             #游戏内容界面逻辑
  - game_ui.py          #由 Qt Designer 生成的游戏界面文件
  - game.ui             #游戏界面HTML原始文件

  - win_or_lose_ui.py   #游戏输赢弹出提示框
  - README.md           # 项目说明文件

main->(调用)game->(调用)win_or_lose

该项目除了标记地雷外，基本完成扫雷功能，包括难度选择，用户名，自定义游戏难度，时间计时，本地排行榜等（所有排行放在一块了，懒得分开做了）
排行榜默认从高级到初级排，从短时间到长时间排
