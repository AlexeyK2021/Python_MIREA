def main(find_text):
    tree = {
        'PERL': {
            'NIX': {
                'IDRIS': {'APEX': 0,
                          'XTEND': 1},
                'XTEND': {'APEX': 2,
                          'XTEND': 3},
                'NGINX': 4
            },
            'LLVM': {
                'IDRIS': {'APEX': 5,
                          'XTEND': 6},
                'XTEND': 7,
                'NGINX': 8
            }
        },
        'OZ': 9,
        'TWIG': 10,
    }
    way = tree
    for key in find_text:
        value = way.get(key)
        if type(value) is int:
            return value
        elif isinstance(value, dict):
            way = value
            continue


if __name__ == "__main__":
    # print(main(['OZ', 'LLVM', 'IDRIS', 'APEX', 'RHTML']))
    # print(main(['TWIG', 'NIX', 'NGINX', 'APEX', 'RHTML']))
    print(main(['PERL', 'NIX', 'IDRIS', 'APEX', 'RHTML']))
