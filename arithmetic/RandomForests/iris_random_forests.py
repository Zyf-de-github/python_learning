#@----------------------------------------------------------
#@     鸢尾花随机森林分类
#@     展示单个特征对的决策边界，
#@     并绘制随机森林中的三棵决策树结构
#@----------------------------------------------------------

from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
import numpy as np
from sklearn.inspection import DecisionBoundaryDisplay
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import plot_tree

# =============================
# 1. 设置中文字体
# =============================
plt.rcParams['font.sans-serif'] = ['SimHei']        # 使用黑体显示中文
plt.rcParams['axes.unicode_minus'] = False          # 正常显示负号

# =============================
# 2. 加载数据并替换中文标签
# =============================
iris = load_iris()
iris.feature_names = ['花萼长度 (cm)', '花萼宽度 (cm)', '花瓣长度 (cm)', '花瓣宽度 (cm)']
iris.target_names = ['山鸢尾', '变色鸢尾', '维吉尼亚鸢尾']

# =============================
# 3. 随机森林分类模型训练
# =============================
forest = RandomForestClassifier(
    n_estimators=10,         # 森林中树的数量
    random_state=0,
    max_depth=4              # 限制树深，方便可视化
)
forest.fit(iris.data, iris.target)

# =============================
# 4. 绘制某两个特征的决策边界
# =============================
pair = [2, 3]   # 花瓣长度 vs 花瓣宽度
X = iris.data[:, pair]
y = iris.target

clf = RandomForestClassifier(
    n_estimators=10,
    random_state=0,
    max_depth=4
).fit(X, y)

plt.figure(figsize=(6, 5))
DecisionBoundaryDisplay.from_estimator(
    clf,
    X,
    cmap=plt.cm.RdYlBu,
    response_method="predict",
    xlabel=iris.feature_names[pair[0]],
    ylabel=iris.feature_names[pair[1]],
)
for i, color in zip(range(3), "ryb"):
    idx = np.asarray(y == i).nonzero()
    plt.scatter(X[idx, 0], X[idx, 1], c=color, label=iris.target_names[i],
                edgecolor="black", s=20)
plt.title("随机森林在花瓣长度/宽度特征对的决策边界")
plt.legend()
plt.show()

# =============================
# 5. 展示森林中三棵树的具体结构
# =============================

# 从森林中取出三棵树（每棵树是一个 DecisionTreeClassifier 对象）
estimators = forest.estimators_[:3]

plt.figure(figsize=(18, 16))
for i, tree in enumerate(estimators):
    plt.subplot(3, 1, i + 1)
    plot_tree(
        tree,
        feature_names=iris.feature_names,
        class_names=iris.target_names,
        filled=True,
        rounded=True,
        fontsize=8
    )
    plt.title(f"随机森林中的第 {i+1} 棵决策树")
plt.tight_layout()
plt.show()

# =============================
# 6. 输出三棵树的简单信息
# =============================
for i, tree in enumerate(estimators):
    print(f"\n第 {i+1} 棵树的信息：")
    print(f"节点数量：{tree.tree_.node_count}")
    print(f"树深度：{tree.tree_.max_depth}")
    print(f"特征索引：{tree.tree_.feature[:10]}")
    print(f"每个节点的阈值（前10个）：{tree.tree_.threshold[:10]}")
