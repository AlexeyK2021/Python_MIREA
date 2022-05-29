import struct


def main(data):
    return parse_a(data, 5)[0]


def parse_a(data, offset):
    result = {}

    addr = struct.unpack('<I', data[offset:offset + struct.calcsize('<I')])[0]
    offset += struct.calcsize('<I')
    result['A1'] = parse_b(data, addr)[0]

    result['A2'] = \
        struct.unpack('<f', data[offset:offset + struct.calcsize('<f')])[0]
    offset += struct.calcsize('<f')

    result['A3'] = \
        struct.unpack('<Q', data[offset:offset + struct.calcsize('<Q')])[0]
    offset += struct.calcsize('<Q')

    return result, offset


def parse_b(data, offset):
    result = {}

    result['B1'] = b''.join(
        struct.unpack(
            '>8c',
            data[offset:offset + struct.calcsize('>8c')]
        )
    ).decode('ascii')
    offset += struct.calcsize('>8c')

    arr = []
    for i in range(3):
        arr.append(
            parse_c(
                data,
                struct.unpack(
                    '<H',
                    data[offset:offset + struct.calcsize('<H')]
                )[0]
            )[0]
        )
        offset += struct.calcsize('<H')
    result['B2'] = arr

    result['B3'] = \
        struct.unpack('<I', data[offset:offset + struct.calcsize('<I')])[0]
    offset += struct.calcsize('<I')

    result['B4'] = \
        struct.unpack('<d', data[offset:offset + struct.calcsize('<d')])[0]
    offset += struct.calcsize('<d')

    result['B5'] = \
        parse_array(data, offset, 'i', 6)
    offset += struct.calcsize('<6i')

    result['B6'] = \
        struct.unpack('<q', data[offset:offset + struct.calcsize('<q')])[0]
    offset += struct.calcsize('<q')

    result['B7'], offset = parse_d(data, offset)

    return result, offset


def parse_c(data, offset):
    result = {}

    result['C1'] = \
        struct.unpack('<h', data[offset:offset + struct.calcsize('<h')])[0]
    offset += struct.calcsize('<h')

    result['C2'] = \
        struct.unpack('<B', data[offset:offset + struct.calcsize('<B')])[0]
    offset += struct.calcsize('<B')

    result['C3'] = \
        struct.unpack('<h', data[offset:offset + struct.calcsize('<h')])[0]
    offset += struct.calcsize('<h')

    result['C4'] = \
        struct.unpack('<f', data[offset:offset + struct.calcsize('<f')])[0]
    offset += struct.calcsize('<f')

    return result, offset


def parse_d(data, offset):
    result = {}

    result['D1'] = parse_array(data, offset, 'f', 4)
    offset += struct.calcsize('<f') * 4

    result['D2'] = \
        struct.unpack('<d', data[offset:offset + struct.calcsize('<d')])[0]
    offset += struct.calcsize('<d')

    result['D3'] = \
        struct.unpack('<H', data[offset:offset + struct.calcsize('<H')])[0]
    offset += struct.calcsize('<H')

    result['D4'] = \
        struct.unpack('<f', data[offset:offset + struct.calcsize('<f')])[0]
    offset += struct.calcsize('<f')

    return result, offset


def parse_array(data, offset, type, len):
    return list(
        struct.unpack(
            f'<{len}{type}',
            data[offset:offset + struct.calcsize(f'<{len}{type}')]
        )
    )


if __name__ == "__main__":
    print(main(
        b'}BXUM0\x00\x00\x00.\xa3\xa4\xbc\xa4\xb0P\xd5a5\xff\xe7\x04IA\x10b\xcf\xfe'
        b's=\xd7\x03E\r)\xa7\xb7\xdd>&b\xf3\x95z<\xa3S\xbflboppusx\x15\x00\x1e\x00'
        b"'\x00%\xd1\x9d!\x82\xcf\xa5l!\xf2\xee?\xcd\x99\xf7\t\x18\x0f\xdaq\xf4\x14"
        b'\x1e\x0c\xd2\x156\x05\xa6\xa7Z@eG\x01!\xda`\xb2\x9cJ\xb4\xe81\xb4\x97'
        b'\x01>\x95\x1d\x13\xbf\x85=Y?=1L\xbf\xa6N\xd3\x82\x86\xd5\xef?}\xb8F\xce\x17>'))
    print(main(
        b'}BXUM0\x00\x00\x00\xa6\xab}\xbf\x98\x1dFjR\xa7xS\x19\x8btLL\\\x9f\x1c?\xbf\n'
        b'O\xcf\xe0\xadj\x9b\xbe+\x98\x7ff\x97\x1d\x0c\xdc=dsbryfpt\x15\x00\x1e\x00'
        b"'\x00\x840L\x9e@\xe3\x15>\x11^\xeb\xbf\xce\x01_\x82\xacf\xf0\xe4\xc6\xdf"
        b'\xe5\xe4\xe2\xa9r?\r\xef_Q/\x87\x1bF]\xd0fq\x9d5\xd9\xcah\xc9\xf6>/py?2\xfb'
        b'\x06?P\xd9\xbc\xbe\x86\xac:$A\x0c\xe6?\x11C\xad\x037?'))
