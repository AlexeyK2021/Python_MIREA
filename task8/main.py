def main(text):
    result = {}
    data = text.split(';')
    for str in data:
        if str.find(".end") == -1:
            result[str[str.find('@"') + 2:str.rfind('"')]] = \
                str[str.find('local ') + 6:str.find('->') - 1]
    return result


if __name__ == "__main__":
    print(main(
        '.do<% local geanqu -> @"sotius_407" %>'
        ';<% local atarqu_230 ->@"vetece" %>'
        ';<% local quma -> @"rigema_118"%>'
        '; .end').items())
    print(main(
        '.do <% local beesla_355 ->@"bege_107" %>; <% local orusso ->@"onbein" %>; <% local abivear_778 ->@"anrala" %>;<% local mama -> @"ledi" %>;.end').items())
