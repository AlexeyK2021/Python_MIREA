# столбики есть
def del_dubl_col(table):
    a = []
    b = []
    for str in table:
        for col in str:
            if col not in b:
                b.append(col)
        a.append(b)
        b = []
    return a


# строки есть
def del_dubl_str(table):
    a = []
    for str in table:
        if str not in a:
            a.append(str)
    return a


# пустые столбики есть
def del_empty(table):
    temp = []
    temp_row = []
    for i in table:
        for j in i:
            if j is not None:
                temp_row.append(j)
        temp.append(temp_row)
        temp_row = []
    return temp


# разделение столбцов доработать
def divide(table):
    temp = [] * len(table)
    for i in range(len(table)):
        temp.append([""] * (len(table[0]) + 1))
    print(temp)
    print(table)
    for i in range(len(temp)):
        for j in range(len(temp[0])):
            if j == 0:
                temp[i][j] = table[i][j]
    for i in range(len(table)):
        for j in range(len(table[i])):
            if table[i][j] is not None and ";" in table[i][j]:
                t = table[i][j].rfind(";")
                temp[i][j] = table[i][j][table[i][j].find(";") - 3:t] + '00'
                print(temp[i][j + 2], " ", table[i][j])

    for i in range(len(table)):
        for j in range(1, len(table[0])):
            temp[i][j + 1] = table[i][j]
            temp[i][j + 1] = (table[i][j][table[i][j].rfind(";") + 1:])

    return temp


# Замена емейлов есть
def emails(table):
    temp = table
    for i in range(len(temp)):
        for j in range(len(temp[i])):
            if temp[i][j] is not None and temp[i][j].find('[at]') != -1:
                temp[i][j] = table[i][j].replace("[at]", "@")
    return temp


# Переделать реформат даты
def date_reform(table):
    temp = table
    for i in range(len(temp)):
        for j in range(len(temp[i])):
            if temp is not None and temp[i][j].find('/') != -1:
                temp[i][j] = (table[i][j][-2:] + "-" +
                              table[i][j][table[i][j].find("/") +
                                          1:table[i][j].rfind('/')] + "-" +
                              table[i][j][2:table[i][j].find('/')])
    return temp


# Транспонировка есть
def transp(table):
    response = []
    for i in range(len(table[0])):
        response.append([])
        for j in range(len(table)):
            response[i].append(table[j][i])
    return response


def main(table):
    return date_reform(
        divide(
            emails(
                del_dubl_str(
                    del_dubl_col(
                        del_empty(table)
                    )
                )
            )
        )
    )


print(main([[None, "david24[at]gmail.com", "0.8;Давид Г. Галев", "2000/06/26", None, "2000/06/26"],
            [None, "salofuk26[at]mail.ru", "0.6;Дамир С. Салофук", "2001/05/13", None, "2001/05/13"],
            [None, "salofuk26[at]mail.ru", "0.6;Дамир С. Салофук", "2001/05/13", None, "2001/05/13"],
            [None, "vamubman54[at]gmail.com", "0.0;Радмир Р. Вамубман", "2004/10/04", None, "2004/10/04"],
            [None, "salofuk26[at]mail.ru", "0.6;Дамир С. Салофук", "2001/05/13", None, "2001/05/13"],
            [None, "vasilij53[at]rambler.ru", "0.3;Василий З. Бавянц", "2000/03/17", None, "2000/03/17"]]))
