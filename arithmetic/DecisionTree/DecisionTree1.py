

#@-----------------------------
#@     鸢尾花剪枝
#@     展示剪枝算法的分类决策树可视化
#@-----------------------------

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score

# 中文显示设置
plt.rcParams['font.sans-serif'] = ['SimHei']  # 黑体显示中文
plt.rcParams['axes.unicode_minus'] = False    # 正常显示负号

# ====== 1. 载入鸢尾花数据集 ======
iris = load_iris()
# 用中文特征名
feature_names_cn = ['花萼长度(cm)', '花萼宽度(cm)', '花瓣长度(cm)', '花瓣宽度(cm)']
X = pd.DataFrame(iris.data, columns=feature_names_cn)
# 中文类别
class_names_cn = ['山鸢尾', '杂色鸢尾', '维吉尼亚鸢尾']
y = pd.Series(iris.target)

# ====== 2. 人为加入离群值 ======
np.random.seed(0)
n_outliers = 10
outliers = X.sample(n_outliers, random_state=1).copy()
outliers += np.random.normal(0, 5, size=outliers.shape)  # 扰动特征
y_outliers = np.random.choice([0, 1, 2], size=n_outliers)  # 随机类别

# 拼接原数据 + 离群点
X_full = pd.concat([X, outliers], ignore_index=True)
y_full = pd.concat([y, pd.Series(y_outliers)], ignore_index=True)

print(f"原始样本数: {len(X)}, 加入离群点后: {len(X_full)}")

# ====== 3. 划分训练集与测试集 ======
X_train, X_test, y_train, y_test = train_test_split(X_full, y_full, test_size=0.3, random_state=42)

# ====== 4. 训练未剪枝的决策树 ======
model_full = DecisionTreeClassifier(random_state=0)
model_full.fit(X_train, y_train)

# ====== 5. 剪枝（基于成本复杂度剪枝） ======
path = model_full.cost_complexity_pruning_path(X_train, y_train)
ccp_alpha_opt = path.ccp_alphas[3]  # 选择一个中等剪枝强度

model_pruned = DecisionTreeClassifier(random_state=0, ccp_alpha=ccp_alpha_opt)
model_pruned.fit(X_train, y_train)

# ====== 6. 准确率对比 ======
y_pred_full = model_full.predict(X_test)
y_pred_pruned = model_pruned.predict(X_test)

print(f"\n未剪枝准确率: {accuracy_score(y_test, y_pred_full):.3f}")
print(f"剪枝后准确率: {accuracy_score(y_test, y_pred_pruned):.3f}")

# ====== 7. 完全中文化决策树可视化 ======
plt.figure(figsize=(18, 7), dpi=200)

plt.subplot(1, 2, 1)
plot_tree(model_full,
          feature_names=feature_names_cn,
          class_names=class_names_cn,
          filled=True,
          rounded=True,
          fontsize=10)
plt.title("未剪枝的决策树", fontsize=14)

plt.subplot(1, 2, 2)
plot_tree(model_pruned,
          feature_names=feature_names_cn,
          class_names=class_names_cn,
          filled=True,
          rounded=True,
          fontsize=10)
plt.title(f"剪枝后的决策树 (ccp_alpha={ccp_alpha_opt:.5f})", fontsize=14)

plt.tight_layout()
plt.show()
