import matplotlib.pyplot as plt


def check(point1, point2, point3):
    x1, y1 = point1
    x2, y2 = point2
    x3, y3 = point3

    collinear = (y2 - y1) * (x3 - x1) == (y3 - y1) * (x2 - x1)

    return collinear


def plot(point1, point2, point3):
    x = [point1[0], point2[0], point3[0], point1[0]]
    y = [point1[1], point2[1], point3[1], point1[1]]

    plt.plot(x, y)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)

    plt.show()


def threepoints(n):
    if len(n) != 3:
        print("输入的点数不正确")
        return

    point1 = n[0]
    point2 = n[1]
    point3 = n[2]

    if check(point1, point2, point3):
        print("They lie on a straight line")
    else:
        plot(point1, point2, point3)

