import struct


def main(data):
    return parse_a(data, 4)


def parse_a(data, offset):
    result = {}
    result['A1'] = \
        struct.unpack('>Q', data[offset:offset + struct.calcsize('>Q')])[0]
    offset += struct.calcsize('>Q')

    result['A2'] = \
        struct.unpack('>b', data[offset:offset + struct.calcsize('>b')])[0]
    offset += struct.calcsize('>b')

    result['A3'] = \
        struct.unpack('>I', data[offset:offset + struct.calcsize('>I')])[0]
    offset += struct.calcsize('>I')

    result['A4'] = \
        struct.unpack('>b', data[offset:offset + struct.calcsize('>b')])[0]
    offset += struct.calcsize('>b')

    result['A5'] = \
        struct.unpack('>l', data[offset:offset + struct.calcsize('>l')])[0]
    offset += struct.calcsize('>l')

    addr = \
        struct.unpack('>H', data[offset:offset + struct.calcsize('>H')])[0]
    offset += struct.calcsize('>H')

    result['A6'] = parse_b(data, addr)

    result['A7'] = \
        struct.unpack('>b', data[offset:offset + struct.calcsize('b')])[0]

    return result


def parse_b(data, offset):
    result = {}
    arr = []
    for i in range(0, 7):
        arr.append(parse_c(data, offset))
        offset += 6
    result['B1'] = arr
    size = struct.unpack('>I', data[offset:offset + struct.calcsize('>I')])[0]
    offset += struct.calcsize('>I')
    addr = struct.unpack('>I', data[offset:offset + struct.calcsize('>I')])[0]
    offset += struct.calcsize('>I')
    result['B2'] = \
        b''.join(struct.unpack(f'>{size}c', data[addr:addr + struct.calcsize(f'>{size}c')])) \
        .decode('ascii')

    addr += struct.calcsize('>c') * size
    result['B3'] = parse_d(data, addr)
    offset += 2

    result['B4'] = \
        struct.unpack('>q', data[offset:offset + struct.calcsize('>q')])[0]
    offset += struct.calcsize('>q')

    result['B5'] = parse_array(data, offset, 'Q', 4)[0]
    offset += struct.calcsize('>Q') * 4

    result['B6'] = \
        struct.unpack('>f', data[offset:offset + struct.calcsize('>f')])[0]
    offset += struct.calcsize('>f')

    result['B7'] = \
        struct.unpack('>f', data[offset:offset + struct.calcsize('>f')])[0]
    offset += struct.calcsize('>f')

    result['B8'] = parse_array(data, offset, 'B', 4)[0]

    return result


def parse_c(data, offset):
    result = {}
    result['C1'] = \
        struct.unpack('>L', data[offset:offset + struct.calcsize('>L')])[0]
    offset += struct.calcsize('>L')

    result['C2'] = \
        struct.unpack('>b', data[offset:offset + struct.calcsize('>b')])[0]
    offset += struct.calcsize('>b')

    result['C3'] = \
        struct.unpack('>b', data[offset:offset + struct.calcsize('>b')])[0]
    offset += struct.calcsize('>b')

    return result


def parse_d(data, offset):
    result = {}
    result['D1'] = \
        struct.unpack('>l', data[offset:offset + struct.calcsize('>l')])[0]
    offset += struct.calcsize('>l')

    result['D2'] = parse_array(data, offset, 'h', 2)[0]
    offset += struct.calcsize('h') * 2

    result['D3'] = \
        struct.unpack('>q', data[offset:offset + struct.calcsize('>q')])[0]
    offset += struct.calcsize('>q')

    result['D4'] = \
        struct.unpack('>b', data[offset:offset + struct.calcsize('>b')])[0]
    offset += struct.calcsize('>b')

    result['D5'] = \
        struct.unpack('>d', data[offset:offset + struct.calcsize('>d')])[0]
    offset += struct.calcsize('>d')

    return result


def parse_array(data, offset, type, len):
    return list(struct.unpack(f'>{len}{type}',
                              data[offset:offset + struct.calcsize(f'>{len}{type}')])), \
           offset + struct.calcsize(f'>{len}{type}')


def decode(data):
    format = 'b'
    for i in range(3, len(data)):
        print(f"{i}: {struct.unpack(f'>{format}', data[i:i + struct.calcsize(format)])[0]}")


if __name__ == '__main__':
    print(main(b'eGZQ_\x00\x11\x86\x99\x16\xafRJ\xd7\xe7\xb6\xbb86\xb4\xdb7\x006\x11tfz'
               b'k\xdc?#^\xed\x16\xea e\xa4&w\xa69\x02z\xe1\xbf\xda\x01\x1b\xbf\x9d'
               b'\x0e\x1c\xe3\xe8\xd1\xe5S\xdb,\x1e,~_(\x91\x94Wh\x89I\x86\xab\xcf\xd4\xa6L:4'
               b'\x0eh\n\xcd\x9cA\xc3o\x19\xf2g\xc9)4\xe5\xe5\x00\x00\x00\x04\x00\x00\x00\x19'
               b'\x00\x1d\xe3h-\xc9\xee\xe1\x07\x05N\xac\xb2m3)\xd2\x12\xec\xd3w\xd3\xb0:'
               b"\x15\xfa\xbf\xa7\xa0\x9e\x9c\xfba2NE'\\\xf1\xb0\xc6i\xbeI\x14\x97\xbf?"
               b'\xc4g\xb5\xb8!~'))
    print(main(b'eGZQB\xa2\xe9\xc6B\xaee\x9b\xda\xabyI\xd1~XV\xb0,\x004rsd\x9c\xe1\xb2\x1fZ'
               b'\xe2\xfd\x9ao/]$\xd1\xa8\xbc\x92\xbd\xbf\xd3\xb7\x82#^9\x90\x91\x0c\xc1!'
               b'\x90y\xf6\x83\xda7jV@\xe46I\xbf>\xad{\xf7\x87\xef\xdd@\xcb\xf6O_\xbb\xf0\x9c'
               b'\xa5iH\xe6\xfb,\xad\x83\xecm\x00\x00\x00\x02\x00\x00\x00\x19\x00\x1bS@\xa52'
               b'\xaaII\xda\xefD\xbc\xf1\x97L\xf1\xf8\xa5\xfb\n\x1a\xc7\xd7\xcf\xe1'
               b'\xa6\x1c(\x1b\xada\x1d\xab\xd7\x07\xc1\x96\x9dX\xa3\xd7\xbfS\xc0\xcd'
               b'>\xf9\xc0\xaf\x17j\x94\x1c'))
