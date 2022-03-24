def main(text):
    result = {}
    data = text.split('; ')
    for str in data:
        result[str[str.find('->@"') + 4:str.find('" %')]] = str[str.find('local ') + 6:str.find(' ->')]
    return result


if __name__ == "__main__":
    print(main(
        '.do <% local beesla_355 ->@"bege_107" %>; <% local orusso ->@"onbein"%>; <% local abivear_778 ->@"anrala" '
        '%>;<% local mama -> @"ledi"%>;.end').items(),
          sep="\n")
