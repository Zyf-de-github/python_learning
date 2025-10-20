
#@----------------------------------------------------------
#@     鸢尾花决策树分类
#@     展示单个特征对的决策边界，以及怎么通过单个特征对训练分类决策树
#@----------------------------------------------------------


from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
import numpy as np
from sklearn.inspection import DecisionBoundaryDisplay
from sklearn.tree import DecisionTreeClassifier, plot_tree

# =============================
# 1. 设置中文字体（很重要）
# =============================
plt.rcParams['font.sans-serif'] = ['SimHei']        # 使用黑体显示中文
plt.rcParams['axes.unicode_minus'] = False          # 正常显示负号

# =============================
# 2. 加载数据
# =============================
iris = load_iris()

# 用中文替换特征名和类别名
iris.feature_names = ['花萼长度 (cm)', '花萼宽度 (cm)', '花瓣长度 (cm)', '花瓣宽度 (cm)']
iris.target_names = ['山鸢尾', '变色鸢尾', '维吉尼亚鸢尾']

# =============================
# 3. 绘制不同特征对的决策边界
# =============================
n_classes = 3
plot_colors = "ryb"
plot_step = 0.02

for pairidx, pair in enumerate([[0, 1], [0, 2], [0, 3], [1, 2], [1, 3], [2, 3]]):
    # 取出两个特征列
    X = iris.data[:, pair]
    y = iris.target

    # 训练决策树
    clf = DecisionTreeClassifier(random_state=0).fit(X, y)

    # 绘制决策边界
    ax = plt.subplot(2, 3, pairidx + 1)
    plt.tight_layout(h_pad=0.5, w_pad=0.5, pad=2.5)
    DecisionBoundaryDisplay.from_estimator(
        clf,
        X,
        cmap=plt.cm.RdYlBu,
        response_method="predict",
        ax=ax,
        xlabel=iris.feature_names[pair[0]],
        ylabel=iris.feature_names[pair[1]],
    )

    # 绘制训练点
    for i, color in zip(range(n_classes), plot_colors):
        idx = np.asarray(y == i).nonzero()
        plt.scatter(
            X[idx, 0],
            X[idx, 1],
            c=color,
            label=iris.target_names[i],
            edgecolor="black",
            s=15,
        )

plt.suptitle("基于不同特征组合的决策树分类边界")
plt.legend(loc="lower right", borderpad=0, handletextpad=0)
_ = plt.axis("tight")

# =============================
# 4. 绘制整棵决策树结构
# =============================
plt.figure(figsize=(12, 8))
clf = DecisionTreeClassifier(random_state=0).fit(iris.data, iris.target)
plot_tree(
    clf,
    feature_names=iris.feature_names,    # 特征中文
    class_names=iris.target_names,       # 类别中文
    filled=True,
    rounded=True
)
plt.title("基于所有特征训练的鸢尾花决策树模型")
plt.show()
