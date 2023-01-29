def double_to_bit(f:float):
    if f >= 1 or f <= 0:
        return 'ERROR'

    s = "0."

    # 10進数を2倍していって(2進数は左シフト)、整数部を並べたものが10進数の小数を2進数で表す
    f *= 2
    while f != 0:
        if len(s) > 32:
            return 'ERROR'

        if f < 1:
            s += "0"
        else:
            s += "1"
            f -= 1
        f *=2
    return s

if __name__ == "__main__":
    f = 0.625
    print("Before replace:{}".format(f))
    print("After  replace:{}".format(double_to_bit(f)))
