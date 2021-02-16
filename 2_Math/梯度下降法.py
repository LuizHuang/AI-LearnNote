# 一个变量
def f1(x):
    """定义函数"""
    return x ** 2 + 2 * x  
def gradf1(x):
    """导数""" 
    return 2 * x + 2 

x0 = 0 # 初始值
eta = 1e-4 #学习率
for step in range(20):
    g = gradf1(x0)
    # 减去梯度（导数）方向 
    x0 = x0 - eta * g 
    print(f"Setp:{step}, {x0}, {f1(x0)}")

# 两个变量
def f2(x1, x2):
    """定义函数"""
    return x1 ** 2 + 2 * x1 + x2 ** 2 + x2 
def gradf2(x1, x2):
    return 2 * x1 + 2, 2 * x2 + 1 

x1, x2 = 0, 0 # 初始值 
eta = 0.3 # 学习率 
for step in range(200):
    g1, g2 = gradf2(x1, x2)
    # 减去梯度（导数）方向 
    x1 = x1 - eta * g1 
    x2 = x2 - eta * g2  
    print(f"Setp:{step}, {(x1, x2)}, {f2(x1, x2)}")
