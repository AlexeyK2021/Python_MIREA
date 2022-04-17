import struct

'''
(b'JTQM\x00\x00\x00\x02\x00\x00\x00\x10 
\x00\x00 \x00-\xef+ \x95\xa3\x9e{\xd4\xb3'
 b'v[~%\xd3bzt\x06\x1e\xa1\x17\xa1\x9f\xe4rw%\xe8\x13\xc6\xbf\xcdi\x0cFd.'
 b'\xe0?\xbf$ \xf2\xcc^\x00\xed\xbf%/\xe4\xc4S(\xb4g\x93,\xd9\xa7k!\xfe\x04\xd4'
 b'\xc2\xabJN\xe7\xe7\xb0i\xf5\x96sb\r=?_\xd2?p<\xfe\x00\x14\n\xc0ui\xde'
 b'\x0b\x06:\xe0')
 '''
data = {'A1': [{'B1': -17, 'B2': 43}, {'B1': -107, 'B2': 163}],
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


def main(data):
    fmt = ""
    return struct.unpack(fmt, data[0:size(fmt)])
    # b1, b2 = struct.unpack_from("bB", data[addressB:addressB+sizeB], offset=addressB.decode())


def size(fmt):
    return struct.calcsize(fmt)


def unpack_helper(data, fmt):
    size = struct.calcsize(fmt)
    return struct.unpack(fmt, data[:size])


if __name__ == "__main__":
    print(main(b'JTQM\x00\x00\x00\x02\x00\x00\x00\x10\x00\x00\x00-\xef+\x95\xa3\x9e{\xd4\xb3'
               b'v[~%\xd3bzt\x06\x1e\xa1\x17\xa1\x9f\xe4rw%\xe8\x13\xc6\xbf\xcdi\x0cFd.'
               b'\xe0?\xbf$ \xf2\xcc^\x00\xed\xbf%/\xe4\xc4S(\xb4g\x93,\xd9\xa7k!\xfe\x04\xd4'
               b'\xc2\xabJN\xe7\xe7\xb0i\xf5\x96sb\r=?_\xd2?p<\xfe\x00\x14\n\xc0ui\xde'
               b'\x0b\x06:\xe0'))
