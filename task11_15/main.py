import struct


def main(data):
    return parse_a(data, 4)


def parse_a(data, offset):
    result = {}
    result['A1'], result['A2'] = \
        struct.unpack('<dd', data[offset:offset + struct.calcsize('<dd')])
    offset += struct.calcsize('<dd')
    size, addr = \
        struct.unpack('<II', data[offset:offset + struct.calcsize('<II')])
    offset += struct.calcsize('<II')
    arr = []
    for i in range(size):
        arr.append(
            parse_b(
                data,
                struct.unpack('<H', data[addr:addr + struct.calcsize('<H')])[0]
            )
        )
        addr += struct.calcsize('<H')
    result['A3'] = arr
    result['A4'] = \
        struct.unpack('<b', data[offset:offset + struct.calcsize('<b')])[0]
    offset += struct.calcsize('<b')
    result['A5'] = \
        struct.unpack('<B', data[offset:offset + struct.calcsize('<B')])[0]
    offset += struct.calcsize('<B')
    result['A6'] = parse_c(data, offset)
    offset += 48
    result['A7'], result['A8'] = \
        struct.unpack('<BB', data[offset:offset + struct.calcsize('<BB')])
    offset += struct.calcsize('<BB')
    return result


def parse_b(data, offset):
    result = {}
    result['B1'] = \
        struct.unpack('<q', data[offset:offset + struct.calcsize('<q')])[0]
    offset += struct.calcsize('<q')
    size, addr = \
        struct.unpack('<HH', data[offset:offset + struct.calcsize('<HH')])
    offset += struct.calcsize('<HH')
    result['B2'] = \
        b''.join(
            struct.unpack(
                f'>{size}c',
                data[addr:addr + struct.calcsize(f'>{size}c')]
            )
        ).decode('ascii')
    offset += struct.calcsize(f'>{size}c')
    return result


def parse_c(data, offset):
    result = {}
    result['C1'] = \
        struct.unpack('<h', data[offset:offset + struct.calcsize('<h')])[0]
    offset += struct.calcsize('<h')
    result['C2'] = parse_d(data, offset)
    offset += 44
    result['C3'] = \
        struct.unpack('<h', data[offset:offset + struct.calcsize('<h')])[0]
    offset += struct.calcsize('<h')
    return result


def parse_d(data, offset):
    result = {}
    result['D1'] = \
        struct.unpack('<h', data[offset:offset + struct.calcsize('<h')])[0]
    offset += struct.calcsize('<h')
    size, addr = \
        struct.unpack('<II', data[offset:offset + struct.calcsize('<II')])
    offset += struct.calcsize('<II')
    arr = []
    for i in range(0, size):
        arr.append(
            struct.unpack('<B', data[addr:addr + struct.calcsize('<B')])[0]
        )
        addr += struct.calcsize('<B')
    result['D2'] = arr
    arr1 = []
    for i in range(0, 4):
        arr1.append(
            struct.unpack('<L', data[offset:offset + struct.calcsize('<L')])[0]
        )
        offset += struct.calcsize('<L')
    result['D3'] = arr1

    result['D4'] = \
        struct.unpack('<B', data[offset:offset + struct.calcsize('<B')])[0]
    offset += struct.calcsize('<B')
    result['D5'] = \
        struct.unpack('<b', data[offset:offset + struct.calcsize('<b')])[0]
    offset += struct.calcsize('<b')
    result['D6'] = \
        struct.unpack('<I', data[offset:offset + struct.calcsize('<I')])[0]
    offset += struct.calcsize('<I')
    result['D7'] = \
        struct.unpack('<i', data[offset:offset + struct.calcsize('<i')])[0]
    offset += struct.calcsize('<i')
    result['D8'] = \
        struct.unpack('<Q', data[offset:offset + struct.calcsize('<Q')])[0]
    offset += struct.calcsize('<Q')
    return result


def parse_array(data, offset, type, len):
    return list(
        struct.unpack(
            f'>{len}{type}',
            data[offset:offset + struct.calcsize(f'>{len}{type}')]
        )
    )


def decode(data):
    format = '<h'
    for i in range(3, len(data)):
        print(f"{i}: {struct.unpack(f'{format}', data[i:i + struct.calcsize(format)])[0]}")


if __name__ == '__main__':
    print(main(b'GPLA\x881F\x19\x06\x9e\xec\xbf`L\xa6|\x98\x07\xcd\xbf\x03\x00\x00\x00'
               b'}\x00\x00\x00\x10\x80\xf7h\x80\xe9\x02\x00\x00\x00\x83\x00\x00\x00\x9cv'
               b'\xdaV\x8bXW\x12e\xbb%\xa5\xfc\x18iF\x86\x06\xee\x05\x90\x0b\x00\xb2\x83\xcf'
               b'\xd8\x9f\x97m\x90fF\x9c\xcc\x15\x85qqaj/n\x84\xdc\x8d\x0bUO\x03\x00P\x00c'
               b'm\n\x8f\x841\xffp\x8ef\x02\x00_\x00qsoa\xe2!Vf!\x12\xb3\xd2\x04\x00m'
               b'\x00S\x00a\x00q\x00\x10\x92'))
    print("**********************************************************")
    print(main(b'GPLA\xbc\x85R\xc9\x93}\xeb?\xc8\xb5\x06\x88ml\xcb\xbf\x03\x00\x00\x00'
               b"|\x00\x00\x00E\x80b\xfbCK\x02\x00\x00\x00\x82\x00\x00\x00\x1f\xb66^ '"
               b'3\x19\xc1\x064\xd5[\xb0\x13\x8a8\x008\xc5\xa2\x8e/#\xa9\\\xc1\xaf,Q'
               b'\xeb\xca\x87\xeb\x95\xce>\xd6od\xe3Y\xed\ta\xb8\xc7x\x02\x00P\x00kv'
               b'g\xd1\xd8\xef\x1a\xce\x90\xd8\x81\x03\x00^\x00rbve\xb9\x8c\xf2'
               b'\xb3\x1a\xd6\x85\x03\x00m\x00R\x00a\x00p\x00\xf9M'))
