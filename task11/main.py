'''
input:
(b'JTQM\x00\x00\x00\x02\x00\x00\x00\x10\x00\x00\x00-\xef+\x95\xa3\x9e{\xd4\xb3'
 b'v[~%\xd3bzt\x06\x1e\xa1\x17\xa1\x9f\xe4rw%\xe8\x13\xc6\xbf\xcdi\x0cFd.'
 b'\xe0?\xbf$ \xf2\xcc^\x00\xed\xbf%/\xe4\xc4S(\xb4g\x93,\xd9\xa7k!\xfe\x04\xd4'
 b'\xc2\xabJN\xe7\xe7\xb0i\xf5\x96sb\r=?_\xd2?p<\xfe\x00\x14\n\xc0ui\xde'
 b'\x0b\x06:\xe0)'
 '''
'''
output
{'A1': [{'B1': -17, 'B2': 43}, {'B1': -107, 'B2': 163}],
 'A2': {'C1': [-0.22976830899312173, 0.12164503028576945],
        'C2': [-306240209,
               -456895704,
               -1268280532,
               -643339487,
               -33237822,
               -1421193497,
               -407868939,
               -1770823155],
        'C3': {'D1': 0.04672224074602127, 'D2': 0.938430666923523},
        'C4': {'E1': -98,
               'E2': 8922954082650301907,
               'E3': [1652192262, 513873825, 2682548855, 635966406]},
        'C5': 10,
        'C6': -4578637043763627296}}
        '''

import struct


def main(data):
    return parse_a(data, 3)


def parse_a(data, offset):
    result = {}
    offset_ = offset
    c_link, b_size, b_link = struct. \
        unpack('III', data[offset_:offset_ + struct.calcsize('>III')])
    offset_ += struct.calcsize('>III')
    offset_ = b_link
    a1_arr = []
    for i in range(b_size):
        num, offset_ = parse_b(data, offset_)
        a1_arr.append(num)
    result['A1'] = a1_arr
    result['A2'], offset_ = parse_c(data, 45)
    return result


def parse_b(data, offset):
    result = {}
    offset_ = offset
    result['B1'] = struct \
        .unpack('b', data[offset_:offset_ + struct.calcsize('>b')])[0]
    offset_ += struct.calcsize('>b')
    result['B2'] = struct \
        .unpack('B', data[offset_:offset_ + struct.calcsize('>B')])[0]
    offset_ += struct.calcsize('>B')
    return result, offset_


def parse_c(data, offset):
    result = {}
    offset_ = offset
    result['C1'], offset_ = parse_array(data, offset_, 'd', 2)
    result['C2'], offset_ = parse_array(data, offset_, 'l', 8)
    result['C3'], offset_ = parse_d(data, offset_)
    result['C4'] = parse_e(data, 20)[0]
    offset_ = 103
    result['C5'] = struct \
        .unpack('>B', data[offset_:offset_ + struct.calcsize('>B')])[0]
    offset_ += struct.calcsize('>B')
    result['C6'] = struct \
        .unpack('>q', data[offset_:offset_ + struct.calcsize('>q')])[0]
    offset_ += struct.calcsize('>q')
    return result, offset_


def parse_d(data, offset):
    result = {}
    offset_ = offset
    result['D1'] = struct \
        .unpack('>f', data[offset_:offset_ + struct.calcsize('>f')])[0]
    offset_ += struct.calcsize('>f')
    result['D2'] = struct \
        .unpack('>f', data[offset_:offset_ + struct.calcsize('>f')])[0]
    offset_ += struct.calcsize('>f')
    return result, offset_


def parse_e(data, offset):
    result = {}
    offset_ = offset
    result['E1'] = struct \
        .unpack('>b', data[offset_:offset_ + struct.calcsize('>b')])[0]
    offset_ = offset_ + struct.calcsize('>b')
    result['E2'] = struct \
        .unpack('>q', data[offset_:offset_ + struct.calcsize('>q')])[0]
    offset_ = offset_ + struct.calcsize('>q')
    result['E3'], offset_ = parse_array(data, offset_, 'L', 4)
    return result, offset_


def parse_array(data, offset, type, len):
    return list(struct.unpack(f'>{len}{type}',
                              data[offset:offset + struct.calcsize(f'>{len}{type}')])), \
           offset + struct.calcsize(f'>{len}{type}')


# def unpack_helper(data, fmt):
#     size = struct.calcsize(fmt)
#     return struct.unpack(fmt, data[:size])

# def decode(data):
#     for i in range(3, len(data)):
#         print(f"{i}: {struct.unpack('>B', data[i:i + struct.calcsize('B')])[0]}")


if __name__ == "__main__":
    print(main((b'JTQM\x00\x00\x00\x02\x00\x00\x00\x10\x00\x00\x00-\xef+\x95\xa3\x9e{\xd4\xb3'
                b'v[~%\xd3bzt\x06\x1e\xa1\x17\xa1\x9f\xe4rw%\xe8\x13\xc6\xbf\xcdi\x0cFd.'
                b'\xe0?\xbf$ \xf2\xcc^\x00\xed\xbf%/\xe4\xc4S(\xb4g\x93,\xd9\xa7k!\xfe\x04\xd4'
                b'\xc2\xabJN\xe7\xe7\xb0i\xf5\x96sb\r=?_\xd2?p<\xfe\x00\x14\n\xc0ui\xde'
                b'\x0b\x06:\xe0')))
    print("*****************************************************************************************")
    print(main(b'JTQM\x00\x00\x00\x02\x00\x00\x00\x10\x00\x00\x00-4\x95\x00B2>\xd4*'
               b'\xd6\x9c\xaaB\xa7\xeb\xaek.\xd7\xdb\xe9\xc2`\xcb\xf6\xee2G\xc9'
               b'\xfd\xbf\xd4\xc8\xb7\xdb\x9a\xc6p?\xba\xa5\x12\xee>\x18\xf0\xb33l\xe0\xa6@O'
               b'\xe3\x94\xb3\xb4\xa5\x005\x83\x84{\xc4+q\xb1\x8e\xd7}\x91\x14\x07'
               b'\xa3\x84\xbaM\xb1\xbe\x98\xb8k\xbeV\xd5n\x00\x14\x1de\x00P\x9c\xfc~\xc9t'))
    print("*******************************************************************************************")
    print(main(
        b'JTQM\x00\x00\x00\x02\x00\x00\x00\x10\x00\x00\x00-\xef+\x95\xa3\x9e{\xd4\xb3v[~%\xd3bzt\x06\x1e\xa1\x17\xa1\x9f\xe4rw%\xe8\x13\xc6\xbf\xcdi\x0cFd.\xe0?\xbf$ \xf2\xcc^\x00\xed\xbf%/\xe4\xc4S(\xb4g\x93,\xd9\xa7k!\xfe\x04\xd4\xc2\xabJN\xe7\xe7\xb0i\xf5\x96sb\r=?_\xd2?p<\xfe\x00\x14\n\xc0ui\xde\x0b\x06:\xe0'))
