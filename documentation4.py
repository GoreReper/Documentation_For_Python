def main(n):
    if n == 0:
        return -0.1
    elif n == 1:
        return 0.76
    else:
        return abs(main(n - 1) ** 3) - (main(n - 2) - main(n - 1) ** 3) ** 2
