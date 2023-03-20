# -*- CODING: UTF-8 -*-
# @time 2023/3/20 22:01
# @Author tyqqj
# @File main.py
# @Aim 二项分布计算器，输入总数和概率，输出概率分布


import numpy as np
import matplotlib.pyplot as plt


def binomial(n, p):
    """
    二项分布计算器
    :param n: 总数
    :param p: 概率
    :return: 概率分布
    """
    x = np.arange(n + 1)
    y = np.zeros(n + 1)
    for i in range(n + 1):
        y[i] = np.math.factorial(n) / (np.math.factorial(i) * np.math.factorial(n - i)) * p ** i * (1 - p) ** (n - i)
    return x, y


if __name__ == '__main__':
    n = 5
    p = 0.1
    x, y = binomial(n, p)
    # 显示概率分布
    # 直方图
    # 需要显示具体概率值
    # x轴设置为整数
    plt.xticks(x)
    plt.bar(x, y, width=0.5, facecolor='lightskyblue', edgecolor='white')
    # 在直方图上显示概率值
    for a, b in zip(x, y):
        # 去掉小数点后面的0
        plt.text(a, b, '%f' % b, ha='center', va='bottom', fontsize=10)
    plt.show()