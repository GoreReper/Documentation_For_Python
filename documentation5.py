def main(x, y, z):
    n = len(x)
    result = 0
    for i in range(1, n + 1):
        y1 = y[n + 1 - i - 1] / 32
        z1 = 26 * z[abs((i - 1) // 2)] ** 3
        x1 = (x[abs((i - 1) // 4)] ** 2) / 49
        result += 35 * (y1 + z1 + x1) ** 5 / 22
    return result
