import numpy as np
import matplotlib.pyplot as plt


def generate_prn1(length=1023):
    """生成PRN1的C/A码序列"""
    g1 = [1] * 10
    g2 = [1] * 10
    ca_code = []

    for _ in range(length):
        # G1寄存器更新
        g1_tmp = g1[2] ^ g1[9]
        g1_ans = g1[9]
        for i in range(9, 0, -1):
            g1[i] = g1[i - 1]
        g1[0] = g1_tmp

        # G2寄存器更新
        g2_tmp = g2[1] ^ g2[2] ^ g2[5] ^ g2[7] ^ g2[8] ^ g2[9]
        g2_ans = g1_ans ^ g2[1] ^ g2[5]  # PRN1的相位选择
        for i in range(9, 0, -1):
            g2[i] = g2[i - 1]
        g2[0] = g2_tmp

        ca_code.append(g2_ans)

    return np.array(ca_code)*2-1


def generate_prn2(length=1023):
    """生成PRN2的C/A码序列"""
    g1 = [1] * 10
    g2 = [1] * 10
    ca_code = []

    for _ in range(length):
        # G1寄存器更新
        g1_tmp = g1[2] ^ g1[9]
        g1_ans = g1[9]
        for i in range(9, 0, -1):
            g1[i] = g1[i - 1]
        g1[0] = g1_tmp

        # G2寄存器更新
        g2_tmp = g2[1] ^ g2[2] ^ g2[5] ^ g2[7] ^ g2[8] ^ g2[9]
        g2_ans = g1_ans ^ g2[2] ^ g2[6]  # PRN2的相位选择
        for i in range(9, 0, -1):
            g2[i] = g2[i - 1]
        g2[0] = g2_tmp

        ca_code.append(g2_ans)

    return np.array(ca_code)*2-1


def generate_B1I1(length=1023):
    g1 = [1] * 11
    g2 = [1] * 11
    ca_code = []

    for _ in range(length):
        # G1寄存器更新
        g1_tmp = g1[0] ^ g1[6] ^ g1[7] ^ g1[8] ^ g1[9] ^ g1[10]
        g1_ans = g1[10]
        for i in range(10, 0, -1):
            g1[i] = g1[i - 1]
        g1[0] = g1_tmp

        # G2寄存器更新
        g2_tmp = g1[0] ^ g1[1] ^ g1[2] ^ g1[3] ^ g1[4] ^ g1[7] ^ g1[8] ^ g1[10]
        g2_ans = g1_ans ^ g2[0] ^ g2[2]  # PRN2的相位选择
        for i in range(9, 0, -1):
            g2[i] = g2[i - 1]
        g2[0] = g2_tmp

        ca_code.append(g2_ans)

    return np.array(ca_code)*2-1



def generate_B1I2(length=1023):
    """生成PRN2的C/A码序列"""
    g1 = [1] * 11
    g2 = [1] * 11
    ca_code = []

    for _ in range(length):
        # G1寄存器更新
        g1_tmp = g1[0] ^ g1[6] ^ g1[7] ^ g1[8] ^ g1[9] ^ g1[10]
        g1_ans = g1[10]
        for i in range(9, 0, -1):
            g1[i] = g1[i - 1]
        g1[0] = g1_tmp

        # G2寄存器更新
        g2_tmp = g1[0] ^ g1[1] ^ g1[2] ^ g1[3] ^ g1[4] ^ g1[7] ^ g1[8] ^ g1[10]
        g2_ans = g1_ans ^ g2[0] ^ g2[3]  # PRN2的相位选择
        for i in range(9, 0, -1):
            g2[i] = g2[i - 1]
        g2[0] = g2_tmp

        ca_code.append(g2_ans)

    return np.array(ca_code)*2-1



# 生成C/A码
prn1 = generate_prn1()
prn2 = generate_prn2()
B1I1 = generate_B1I1()
B1I2 = generate_B1I2()
# 计算相关函数
p_auto_corr = np.correlate(prn1, prn1, mode='full')
p_cross_corr = np.correlate(prn1, prn2, mode='full')

b_auto_corr = np.correlate(B1I1, B1I1, mode='full')
b_cross_corr = np.correlate(B1I1, B1I2, mode='full')

# 创建延迟数组（0在中间）
lags = np.arange(-len(prn1) + 1, len(prn1))

# 绘图
plt.figure(figsize=(15, 5))

# 自相关图
plt.subplot(2, 2, 1)
plt.plot(lags, p_auto_corr)
plt.title('PRN1')
plt.grid(True)
plt.axvline(x=0, color='r', linestyle='--', alpha=0.5, label=' ')
plt.legend()

# 互相关图
plt.subplot(2, 2, 2)
plt.plot(lags, p_cross_corr)
plt.title('PRN1 & PRN2')
plt.grid(True)
plt.axvline(x=0, color='r', linestyle='--', alpha=0.5, label=' ')
plt.legend()

plt.subplot(2, 2, 3)
plt.plot(lags, b_auto_corr)
plt.title('B1I1')
plt.grid(True)
plt.axvline(x=0, color='r', linestyle='--', alpha=0.5, label=' ')
plt.legend()

plt.subplot(2, 2, 4)
plt.plot(lags, b_cross_corr)
plt.title('B1I1 & B1I2')
plt.grid(True)
plt.axvline(x=0, color='r', linestyle='--', alpha=0.5, label=' ')
plt.legend()
plt.tight_layout()
plt.show()