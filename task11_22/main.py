import struct


def main(data):
    return parse_a(data, 4)


def parse(d, of, t, ar):
    return list(struct.unpack(f'>{ar}{t}', d[of:of + ar * struct.calcsize(t)]))


def parse_b(d, of):
    result = dict()
    result['B1'] = struct.unpack('>d', d[of:of + struct.calcsize('>d')])[0]
    of += struct.calcsize('>d')
    result['B2'] = struct.unpack('>f', d[of:of + struct.calcsize('>f')])[0]

    return result


def parse_g(d, of):
    result = dict()
    of = 15
    result['G1'] = struct.unpack('>f', d[of:of + struct.calcsize('>f')])[0]
    of = 19
    result['G2'] = struct.unpack('>H', d[of:of + struct.calcsize('>H')])[0]
    of = 21
    result['G3'] = struct.unpack('>f', d[of:of + struct.calcsize('>f')])[0]
    of = 25
    result['G4'] = struct.unpack('>f', d[of:of + struct.calcsize('>f')])[0]
    of = 29
    result['G5'] = struct.unpack('>d', d[of:of + struct.calcsize('>d')])[0]
    return result


def parse_e_1(d, of):
    result = dict()
    of = 49
    result['E1'] = parse(d, of, 'b', 2)
    of = 106
    result['E2'] = struct.unpack('>d', d[of:of + struct.calcsize('>d')])[0]
    of += struct.calcsize('>d')
    result['E3'] = struct.unpack('>b', d[of:of + struct.calcsize('>b')])[0]
    of += struct.calcsize('>b')
    result['E4'] = struct.unpack('>h', d[of:of + struct.calcsize('>h')])[0]
    of = 117
    result['E5'] = struct.unpack('>d', d[of:of + struct.calcsize('>d')])[0]
    of += struct.calcsize('>d')
    result['E6'] = struct.unpack('>B', d[of:of + struct.calcsize('>B')])[0]
    return result


def parse_e_2(d, of):
    result = dict()
    of = 51
    result['E1'] = parse(d, of, 'b', 2)
    of = 132
    result['E2'] = struct.unpack('>d', d[of:of + struct.calcsize('>d')])[0]
    of += struct.calcsize('>d')
    result['E3'] = struct.unpack('>b', d[of:of + struct.calcsize('>b')])[0]
    of += struct.calcsize('>b')
    result['E4'] = struct.unpack('>h', d[of:of + struct.calcsize('>h')])[0]
    of = 143
    result['E5'] = struct.unpack('>d', d[of:of + struct.calcsize('>d')])[0]
    of += struct.calcsize('>d')
    result['E6'] = struct.unpack('>B', d[of:of + struct.calcsize('>B')])[0]
    return result


def parse_f(d, of):
    result = dict()
    result['F1'] = struct.unpack('>f', d[of:of + struct.calcsize('>f')])[0]
    of = 59
    result['F2'] = struct.unpack('>b', d[of:of + struct.calcsize('>b')])[0]
    of = 60
    result['F3'] = struct.unpack('>i', d[of:of + struct.calcsize('>i')])[0]
    of = 53
    result['F4'] = parse(d, of, 'B', 2)
    of = 70
    result['F5'] = parse(d, of, 'B', 8)
    of = 78
    result['F6'] = struct.unpack('>q', d[of:of + struct.calcsize('>q')])[0]
    of = 86
    result['F7'] = struct.unpack('>h', d[of:of + struct.calcsize('>h')])[0]
    return result


def parse_d(d, of):
    result = dict()
    result['D1'] = struct.unpack('>f', d[of:of + struct.calcsize('>f')])[0]
    of += struct.calcsize('>f')
    result['D2'] = struct.unpack('>d', d[of:of + struct.calcsize('>d')])[0]
    of += struct.calcsize('>d')
    result['D3'] = [parse_e_1(d, 49), parse_e_2(d, 51)]
    of = 152
    result['D4'] = parse(d, of, 'H', 4)
    of += struct.calcsize('>H') * 4
    result['D5'] = parse_f(d, 55)
    of = 164
    result['D6'] = struct.unpack('>i', d[of:of + struct.calcsize('>i')])[0]
    of += struct.calcsize('>i')
    return result


def parse_c(d, of):
    result = dict()
    result['C1'] = struct.unpack('>i', d[of:of + struct.calcsize('>i')])[0]
    of += struct.calcsize('>i')
    result['C2'] = parse_d(d, 88)
    of += struct.calcsize('>I')
    result['C3'] = struct.unpack('>b', d[of:of + struct.calcsize('>b')])[0]
    return result


def parse_a(d, of):
    result = dict()
    result['A1'] = parse_b(d, 37)
    of = + struct.calcsize('>H')
    result['A2'] = parse_c(d, 168)
    of = 10
    result['A3'] = struct.unpack('>B', d[of:of + struct.calcsize('>B')])[0]
    of = 11
    result['A4'] = struct.unpack('>I', d[of:of + struct.calcsize('>I')])[0]
    of += struct.calcsize('>I')
    result['A5'] = parse_g(d, 15)
    return result


def decode(data):
    for i in range(4, len(data)):
        print(f"{i}: {struct.unpack('>d', data[i:i + struct.calcsize('>d')])[0]}")


if __name__ == "__main__":
    print(main(
        b'\xc2AZN\x00%\x00\x00\x00\xa8T\x8c\xfe%\xd7?{\xd5\xd6Q\x99\xbev\x07W?\x7fj'
        b'\x05?\xea\xe7\xf4\xa9`~\xd2\xbf\xd7\x80\xc0\x8a\xfe^\xf4\xbd\xe8\x81'
        b'\xd4\xb7\x94\x18h?H\xbcG\xb3t\xe0\xd4_\xee\xee\x00\x02\x00\x00\x005$\x17'
        b'~\x0e\xa2\x84\xdc\x99\xb6\xb2\xee2h\x1b\x9c\xffc\x07<\x89\xbb\x05?\xecc4'
        b'U}\xadj\x00\x00\x00\x02\x001?\xe7w\xd0\xaaj\x1d\xd8\x83\x83\x82\xbf\xd4z'
        b'jS\xdd\xb3\x14\x95\x00\x00\x00\x02\x003?\xef\x8b2\x87\xf2A*4\x94\x96\xbf'
        b'w\xecY\xa1\xab\n\x00"(\x1ad[\xbeT\tH\x00\x00\x007\x16\xf5\x1dZ'
        b'\xb2\xba\xee\xa6\x00\x00\x00X\xa5'
    ))
    print("***********************************************************************")
    print(main(
        b'\xc2AZN\x00%\x00\x00\x00\xa8T\x8c\xfe%\xd7?{\xd5\xd6Q\x99\xbev\x07W?\x7fj\x05?\xea\xe7\xf4\xa9`~\xd2\xbf\xd7\x80\xc0\x8a\xfe^\xf4\xbd\xe8\x81\xd4\xb7\x94\x18h?H\xbcG\xb3t\xe0\xd4_\xee\xee\x00\x02\x00\x00\x005$\x17~\x0e\xa2\x84\xdc\x99\xb6\xb2\xee2h\x1b\x9c\xffc\x07<\x89\xbb\x05?\xecc4U}\xadj\x00\x00\x00\x02\x001?\xe7w\xd0\xaaj\x1d\xd8\x83\x83\x82\xbf\xd4zjS\xdd\xb3\x14\x95\x00\x00\x00\x02\x003?\xef\x8b2\x87\xf2A*4\x94\x96\xbfw\xecY\xa1\xab\n\x00"(\x1ad[\xbeT\tH\x00\x00\x007\x16\xf5\x1dZ\xb2\xba\xee\xa6\x00\x00\x00X\xa5'))
    print(main(
        b"\xc2AZN\x00%\x00\x00\x00\xa9:K\x15\xc1\x9f?Y\xde\x8e\x87\xfe=\x8f:h?!\x99\x01?\xd9\xe8\xd9\x0e^o\xcc\xbf\xed\xccwU\xe0\xad\xc6?]j\xaa\xbd\xad\x9c\xb6\xa0Xe\xbfX\x82\xb0\x0e\x89\xc9\xc3\r\x00\x03\x00\x00\x005\xbc\x80\x1a\xbat\xe3w%\xafd&\xd4\xf8Lk\xber\x81\xbd\xca\x82\x8f\xbf\xeb\xa8\xa7)i\xf7\x98\x00\x00\x00\x02\x001?\xe5'\xea{\x1a\xbanP\xa8\x99\xbf\xea\xce\tH\xe9\xc8l \x00\x00\x00\x02\x003?\xe1\xb0\xc7\xdd\x84tZ\x13w\x1d?\xbb?g\x84\x02\xba\x80z\x86r\x803\xe1\xf4\x8c\xc1\x00\x00\x008*ckH8\xf6\xd1\x16\x00\x00\x00Y\xbb"))
