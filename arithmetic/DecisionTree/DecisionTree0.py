

#@----------------------------------------------------------
#@              身高的影响
#@              展示一个正常的决策树分类模型的可视化过程
#@----------------------------------------------------------

import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeRegressor, plot_tree
import matplotlib.pyplot as plt
from matplotlib import font_manager

plt.rcParams['font.sans-serif'] = ['SimHei']        # 使用黑体显示中文
plt.rcParams['axes.unicode_minus'] = False          # 正常显示负号


# ====== 1. 构造模拟数据集 ======
np.random.seed(0)

n = 120  # 学生数量
df = pd.DataFrame({
    '家庭收入': np.random.normal(15, 5, n).clip(5, 30),      # 家庭年收入(万元)
    '性别编码': np.random.choice([0, 1], size=n),             # 0=女, 1=男
    '蛋白质': np.random.normal(60, 15, n).clip(30, 100),      # 每日蛋白质摄入(g)
    '运动时间': np.random.normal(1.2, 0.6, n).clip(0, 3),     # 每日运动小时
})

# ====== 2. 生成“身高”作为目标变量 ======
# 模拟规律：收入、蛋白质、运动时间、性别均正相关 + 一点随机波动
df['身高'] = (
    150
    + df['性别编码'] * 10
    + df['蛋白质'] * 0.3
    + df['运动时间'] * 4
    + (df['家庭收入'] - 15) * 0.8
    + np.random.normal(0, 3, n)
)

# ====== 3. 训练决策树回归模型 ======
X = df[['家庭收入', '性别编码', '蛋白质', '运动时间']]
y = df['身高']

model = DecisionTreeRegressor(max_depth=3, random_state=0)
model.fit(X, y)

# ====== 4. 输出特征重要性 ======
importance = dict(zip(X.columns, model.feature_importances_))
print("特征重要性：")
for k, v in importance.items():
    print(f"{k:10s}  {v:.3f}")

# ====== 5. 可视化决策树 ======
plt.figure(figsize=(20, 15))
plot_tree(model, feature_names=X.columns, filled=True, rounded=True)
plt.title("高中生身高影响因素决策树（模拟数据）", fontsize=14)
plt.show()

# ====== 6. 查看前几行数据 ======
print("\n数据样例：")
print(df.head())
