import struct


def main(data):
    return parse_a(data, 4
                   )


def parse_a(data, offset):
    result = {}
    result['A1'] = struct.unpack('>Q', data[offset:offset + struct.calcsize('>Q')])[0]
    offset += struct.calcsize('>Q')
    result['A2'] = struct.unpack('>b', data[offset:offset + struct.calcsize('>b')])[0]
    offset += struct.calcsize('>b')
    result['A3'] = struct.unpack('>I', data[offset:offset + struct.calcsize('>I')])[0]
    offset += struct.calcsize('>I')
    result['A4'] = struct.unpack('>b', data[offset:offset + struct.calcsize('>b')])[0]
    offset += struct.calcsize('>b')
    result['A5'] = struct.unpack('>l', data[offset:offset + struct.calcsize('>l')])[0]
    offset += struct.calcsize('>l')
    result['A6'] = parse_b(data, 54)  # offset=54
    offset += struct.calcsize('>Q')
    result['A7'] = struct.unpack('>b', data[offset:offset + struct.calcsize('b')])
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
    result['B2'] = b''.join(struct.unpack(f'>{size}c', data[addr:addr + struct.calcsize(f'>{size}c')])).decode('ascii')
    offset = 104
    addr = struct.unpack('>H', data[offset:offset + struct.calcsize('>H')])[0] #off 104
    offset = addr
    result['B3'] = parse_d(data, offset) # off 29
    offset += 23
    result['B4'] = struct.unpack('>q', data[offset:offset + struct.calcsize('>q')])
    offset += struct.calcsize('>q')
    result['B5'] = parse_array(data, offset, 'Q', 4)
    offset += struct.calcsize('>Q') * 4
    result['B6'] = struct.unpack('>f', data[offset:offset + struct.calcsize('>f')])
    offset += struct.calcsize('>f')
    result['B7'] = struct.unpack('>f', data[offset:offset + struct.calcsize('>f')])
    offset += struct.calcsize('>f')
    result['B8'] = parse_array(data, offset, 'B', 4)
    return result


def parse_c(data, offset):
    result = {}
    result['C1'] = struct.unpack('>L', data[offset:offset + struct.calcsize('>L')])[0]
    offset += struct.calcsize('>L')
    result['C2'] = struct.unpack('>b', data[offset:offset + struct.calcsize('>b')])[0]
    offset += struct.calcsize('>b')
    result['C3'] = struct.unpack('>b', data[offset:offset + struct.calcsize('>b')])[0]
    offset += struct.calcsize('>b')
    return result


def parse_d(data, offset):
    result = {}
    result['D1'] = struct.unpack('>l', data[offset:offset + struct.calcsize('>l')])
    offset += struct.calcsize('>l')
    result['D2'] = parse_array(data, offset, 'h', 2)
    offset += struct.calcsize('h') * 2
    result['D3'] = struct.unpack('>q', data[offset:offset + struct.calcsize('>q')])
    offset += struct.calcsize('>q')
    result['D4'] = struct.unpack('>b', data[offset:offset + struct.calcsize('>b')])
    offset += struct.calcsize('>b')
    result['D5'] = struct.unpack('>d', data[offset:offset + struct.calcsize('>d')])
    offset += struct.calcsize('>d')
    return result


def parse_array(data, offset, type, len):
    return list(struct.unpack(f'>{len}{type}', data[offset:offset + struct.calcsize(f'>{len}{type}')])), \
           offset + struct.calcsize(f'>{len}{type}')


def decode(data):
    for i in range(3, len(data)):
        print(f"{i}: {struct.unpack('>H', data[i:i + struct.calcsize('H')])[0]}")


if __name__ == '__main__':
    print(main(b'eGZQ_\x00\x11\x86\x99\x16\xafRJ\xd7\xe7\xb6\xbb86\xb4\xdb7\x006\x11tfz'
               b'k\xdc?#^\xed\x16\xea e\xa4&w\xa69\x02z\xe1\xbf\xda\x01\x1b\xbf\x9d'
               b'\x0e\x1c\xe3\xe8\xd1\xe5S\xdb,\x1e,~_(\x91\x94Wh\x89I\x86\xab\xcf\xd4\xa6L:4'
               b'\x0eh\n\xcd\x9cA\xc3o\x19\xf2g\xc9)4\xe5\xe5\x00\x00\x00\x04\x00\x00\x00\x19'
               b'\x00\x1d\xe3h-\xc9\xee\xe1\x07\x05N\xac\xb2m3)\xd2\x12\xec\xd3w\xd3\xb0:'
               b"\x15\xfa\xbf\xa7\xa0\x9e\x9c\xfba2NE'\\\xf1\xb0\xc6i\xbeI\x14\x97\xbf?"
               b'\xc4g\xb5\xb8!~'))
