from turtle import *
import time


def InitSize(length, width):  # 初始化
    screensize(1000, 800, "blue")  # 图像大小及背景颜色
    penup()
    pensize(3)
    goto(-length / 2, -width / 2)  # 开始绘图位置
    pendown()
    # 画出赛道占地最大范围
    tracer(False)
    fd(length)
    left(90)
    fd(width)
    left(90)
    fd(length)
    left(90)
    fd(width)
    left(90)
    tracer(True)

def InitSite(x, y):
    # 把笔移至开始位置
    penup()
    goto(x, y)
    pencolor("white")  # 更改笔的颜色
    pensize(50)  # 赛道宽度50cm
    pendown()  # 放下笔，准备画赛道


def Straight(len):  # 直道；单位厘米
    fd(len)


def TurnLeft(radius, angle):  # 左转弯；半径、角度
    circle(radius, angle)


def TurnRight(radius, angle):  # 左转弯；半径、角度
    circle(-radius, angle)


def LeftCircle(radius):  # 左侧圆环；半径
    TurnLeft(radius, 360)


def RightCircle(radius):  # 右侧圆环；半径
    TurnRight(radius, 360)


def main():
    InitSize(1400, 1200)  # 初始化绘制占地大小
    InitSite(-250, -250)  # 初始化画笔初始位置
    speed(10)  # 设置绘图速度；如果还嫌慢的话可以用InitSize函数中用到的tracer
    left(90)
    Straight(500)
    TurnRight(120/3.14,60)
    Straight(250)
    TurnRight(120/3.14,120)
    Straight(250)
    TurnLeft(160/3.14,90)
    Straight(250)
    TurnRight(200/3.14,90)
    Straight(250)
    TurnRight(300/3.14,120)

main()
exitonclick()