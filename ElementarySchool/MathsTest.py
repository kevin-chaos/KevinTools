# encoding: UTF-8

import random

import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)
pd.set_option('max_colwidth', 200)


def add_and_sub(long=2, num_range=(0, 100), method=None, num=100, allow_zero=True, random_blank=True):
    """
    自动生成加减法测试题，用于小学或学前班练习
    :param long: 问题中因子的数量
    :param num_range: 运算范围
    :param method: 预算符号，数据格式为list或str
    :param num: 出题数量
    :param allow_zero: 是否允许0参与运算
    :param random_blank: 空格位置是否随机
    :return: None
    """
    # 定义运算符号
    if not method:
        method = ['+', '-']
    if isinstance(method, str):
        method = list(method)
    n = 0

    # 长度为2的运算题
    if long == 2:
        # 循环出题num道
        while n < num:
            # 生成数字、运算符和答案
            a = random.randint(num_range[0], num_range[1])
            b = random.randint(num_range[0], num_range[1])
            m = random.sample(method, 1)[0]
            c = eval(f'a{m}b')
            # 判断答案是否在数值域中
            if not num_range[0] < c < num_range[1]:
                continue
            # 判断是否允许0参与运算
            if not allow_zero and 0 in [a, b, c]:
                continue
            # 判断是否随机生成空格位置
            if not random_blank:
                r = 0
            else:
                r = random.random()
            # 根据以上设置出题
            if r > 0.667:
                q = f"{a} {m} □ = {c}"
            elif r > 0.33:
                q = f"□ {m} {b} = {c}"
            else:
                q = f"{a} {m} {b} = □"
            print(q.replace('*', 'x').replace('/', '÷'))
            n += 1
    # 长度为3的运算题
    elif long == 3:
        # 循环出题num道
        while n < num:
            # 生成数字、运算符和答案
            a = random.randint(num_range[0], num_range[1])
            b = random.randint(num_range[0], num_range[1])
            c = random.randint(num_range[0], num_range[1])
            m1 = random.sample(method, 1)[0]
            m2 = random.sample(method, 1)[0]
            d = eval(f'a{m1}b{m2}c')
            # 判断答案是否在数值域中
            if not num_range[0] < d < num_range[1]:
                continue
            # 判断是否允许0参与运算
            if not allow_zero and 0 in [a, b, c, d]:
                continue
            # 判断是否随机生成空格位置
            if not random_blank:
                r = 0
            else:
                r = random.random()
            # 根据以上设置出题
            if r > 0.75:
                q = f"□ {m1} {b} {m2} {c} = {d}"
            elif r > 0.5:
                q = f"{a} {m1} □ {m2} {c} = {d}"
            elif r > 0.25:
                q = f"{a} {m1} {b} {m2} □ = {d}"
            else:
                q = f"{a} {m1} {b} {m2} {c} = □"
            print(q.replace('*', 'x').replace('/', '÷'))
            n += 1
    return None


def multi_and_divide(factor_range=(0, 9), method=None, num=100, random_blank=True):
    # 定义运算符号
    if not method:
        method = ['*', '/']
    if isinstance(method, str):
        method = list(method)
    n = 0

    while n < num:
        a = random.randint(factor_range[0], factor_range[1])
        b = random.randint(factor_range[0], factor_range[1])
        c = a * b
        # 设置符号
        m = random.sample(method, 1)[0]
        if m == "/":
            d = c
            c = a
            a = d
            m = "÷"
        elif m == "*":
            m = 'x'
        if random_blank:
            que = random.sample([
                f"□ {m} {b} = {c}",
                f"{a} {m} □ = {c}",
                f"{a} {m} {b} = □",
            ], 1)[0]
        else:
            que = f"{a} {m} {b} = □"
        print(que)
        n += 1
    return None


if __name__ == "__main__":
    multi_and_divide(factor_range=(0, 10), method='/*')
