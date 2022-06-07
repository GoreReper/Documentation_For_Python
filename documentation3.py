def main(n, a, m, p):
    result = 0
    for j in range(1, m + 1):
        sum2 = 0
        for k in range(1, a + 1):
            sum1 = 1
            for i in range(1, n + 1):
                sum1 *= (77 * i + (78 * k ** 2 - j ** 3 - 1) ** 3
                         + (j ** 3 + 56 * p) ** 4)
            sum2 += sum1
        result += sum2
    return result
