# def main(hex_num):
#     result = ""
#     binary_num = bin(hex_num)[2:]
#     temp = ""
#     for i in range(32 - len(binary_num)):
#         temp += "0"
#     binary_num = temp + binary_num
#     result += '0b' + binary_num[9:13] + binary_num[23:32] + binary_num[4] + \
#               binary_num[3] + binary_num[0] + binary_num[13:23] + \
#               binary_num[5:9] + binary_num[1:3]
#     return hex(int(result, 2))

'''
  H  G F E   D    C       B        A
f(0_00_1_0_0101_0000_1111101001_111100111) =
  0000_111100111_0_1_0_1111101001_0101_00
    C     A      E F H      B      D    G
'''

'''
1)XOR
IN:    00010010100001111101001111100111     0_00_1_0_0101_0000_1111101001_111100111
MASK:  00011101101111010010100110110011
OUT:   00001111001110101111101001010100     0000_111100111_0_1_0_1111101001_0101_00

2)XOR
IN:     11010110101011011001001100100101
MASK:   10001111100001100010000101010011
OUT:    01011001001010111011001001110110
'''
'''
00001111001110101111101001010100
00001111001110101111101001010100
'''

"1100010000100010010001010010010101"
"00011101101111010010100110110011"


def main(x):
    a = x & 0b111111111
    b = (x >> 9) & 0b1111111111
    c = (x >> 19) & 0b1111
    d = (x >> 23) & 0b1111
    e = (x >> 27) & 0b1
    f = (x >> 28) & 0b1
    g = (x >> 29) & 0b11
    h = (x >> 31) & 0b1
    result = g << 0 | d << 2 | b << 6 \
        | h << 16 | f << 17 \
        | e << 18 | a << 19 | c << 28
    return result


if __name__ == "__main__":
    print(main(0x1287d3e7))
    print(main(310891495))
