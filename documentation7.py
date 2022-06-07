def main(digit):
    A = digit & 0b1
    digit = digit >> 1
    B = digit & 0b11111111111
    digit = digit >> 11
    C = digit & 0b11111111
    digit = digit >> 8
    D = digit & 0b1111
    digit = digit >> 4
    E = digit & 0b11
    digit = digit >> 2
    F = digit & 0b111
    digit = digit >> 3
    G = digit & 0b1
    digit = digit >> 1
    H = digit & 0b11
    result = (((D << 28) | (E << 26) |
               (G << 25) | (A << 24) | (C << 16) |
               (F << 13) | (H << 11) | (B << 0)))
    return result


