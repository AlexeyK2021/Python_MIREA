import struct


def main(data):
    return parse_a(data, 5)


def parse_a(data, offset):
    result = {}
    result['A1'] = \
        struct.unpack('>d', data[offset:offset + struct.calcsize('>d')])[0]
    offset += struct.calcsize('>d')
    result['A2'] = \
        struct.unpack('>Q', data[offset:offset + struct.calcsize('>Q')])[0]
    offset += struct.calcsize('>Q')
    result['A3'] = parse_b(data, offset)
    offset += 58
    addr = \
        struct.unpack('>I', data[offset:offset + struct.calcsize('>L')])[0]
    result['A4'] = parse_e(data, addr)
    return result


def parse_b(data, offset):
    result = {}
    result['B1'] = b''.join(struct.unpack('>4c', data[offset:offset + struct.calcsize('>4c')])) \
        .decode('ascii')
    offset += struct.calcsize('>4c')
    result['B2'] = \
        struct.unpack('>b', data[offset:offset + struct.calcsize('>b')])[0]
    offset += struct.calcsize('>b')
    addr = struct.unpack('>I', data[offset:offset + struct.calcsize('>I')])[0]
    offset += struct.calcsize('>I')
    result['B3'] = parse_c(data, addr)
    # offset += 10
    arr = []
    for i in range(0, 6):
        arr.append(parse_d(data, offset))
        offset += 8
    result['B4'] = arr
    result['B5'] = \
        struct.unpack('>B', data[offset:offset + struct.calcsize('>B')])[0]
    offset += struct.calcsize('>B')
    return result


def parse_c(data, offset):
    result = {}
    result['C1'] = \
        struct.unpack('>Q', data[offset:offset + struct.calcsize('>Q')])[0]
    offset += struct.calcsize('>Q')
    result['C2'] = \
        struct.unpack('>H', data[offset:offset + struct.calcsize('>H')])[0]
    offset += struct.calcsize('>H')
    return result


def parse_d(data, offset):
    result = {}
    result['D1'] = parse_array(data, offset, 'B', 2)
    offset += struct.calcsize('>2B')
    result['D2'] = parse_array(data, offset, 'B', 6)
    offset += struct.calcsize('>6B')
    return result


def parse_e(data, offset):
    result = {}
    result['E1'] = \
        struct.unpack('>Q', data[offset:offset + struct.calcsize('>Q')])[0]
    offset += struct.calcsize('>Q')
    result['E2'] = \
        struct.unpack('>h', data[offset:offset + struct.calcsize('>h')])[0]
    offset += struct.calcsize('>h')
    return result


def parse_array(data, offset, type, len):
    return list(
        struct.unpack(
            f'>{len}{type}',
            data[offset:offset + struct.calcsize(f'>{len}{type}')]
        )
    )


def decode(data):
    format = 'I'
    for i in range(3, len(data)):
        print(f"{i}: {struct.unpack(f'>{format}', data[i:i + struct.calcsize(format)])[0]}")


if __name__ == '__main__':
    print(main(b'iMXXW?\xc1\xd1\xe1M)\xb5X\xea\xe4\x9e\x1d\xb7:#\x8cjahym\x00\x00\x00SZ\xa7'
               b'\xb7\xe6X\xca\xa2#\x11b\x17\x83\xd2?\xa1\x98\xbb\xd2[\xc2\xeb<\x06\xa1p\xfb'
               b']\x0c\xd8VI<Cy\xa3\xe09\x994gF\xa7\xc9U\xf6~\xd6\xaf\x83\x00\x00\x00]\x88'
               b'4m\t\xcc\x0f\xd5,\xd5$Rg\x9d\x07\r\x07;i\xec\x16'))
    print("**********************************************************")
    print(main(b'iMXXW?\xba<\x1d\xd9[l\xb0m\xa8t\xdd\xd1?wuenra\xff\x00\x00\x00S\x8e`'
               b'H`\x15\xb5\xdc\xc2}I+\xee\x8b\xa3\xec\x06\xa4\xbd\xa6\xa9\xcb\x84+II\x88'
               b'\xae_\xee4\xea%\x86\xda\xac\'\xd7y\xb01*i\xc4"!{\xc8[\xa5\x00\x00\x00]k'
               b"\xdfP'\x92K\xf0\xf1\x12\xfb\xd7\xee\x815`\xa0\xbb\xbd\xde\x10"))
