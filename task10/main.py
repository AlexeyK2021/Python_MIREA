def main(data):
    return transponse(
        sort(
            date_reformat(
                erase_emails(
                    splitting_columns(
                        delete_doubles_rows(
                            delete_empty_columns(
                                delete_doubles_columns(data)
                            )
                        )
                    )
                )
            )
        )
    )


def delete_doubles_columns(data):
    columns_to_delete = []
    for str in data:
        for el1 in range(len(str)):
            for el2 in range(el1, len(str)):
                if not el1 == el2:
                    if str[el1] == str[el2]:
                        if el2 not in columns_to_delete:
                            columns_to_delete.append(el2)

    for j in columns_to_delete:
        for i in range(len(data)):
            _ = data[i].pop(j)

    return data


def delete_empty_columns(data):
    columns_to_delete = []
    rows = len(data)
    for el1 in range(len(data[0])):
        delete = True
        for str in data:
            if str[el1] is not None:
                delete = False
                break
        if delete:
            if el1 not in columns_to_delete:
                columns_to_delete.append(el1)

    for j in columns_to_delete:
        for i in range(rows):
            _ = data[i].pop(j)

    return data


def delete_doubles_rows(data):
    rows_to_delete = []
    for el1 in range(len(data)):
        for el2 in range(el1, len(data)):
            if not el1 == el2:
                if compare(data[el1], data[el2]):
                    rows_to_delete.append(el2)

    for i in rows_to_delete:
        data.pop(i)
    return data


def splitting_columns(data):
    new_data = [] * len(data)
    for i in range(len(data)):
        new_data.append([""] * (len(data[0]) + 1))

    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] is not None and ":" in data[i][j]:
                new_data[i][j] = data[i][j][data[i][j].find(":") + 1:] + '00'
                t = data[i][j].rfind("-")
                new_data[i][j + 1] = (data[i][j][3:t] +
                                      data[i][j][t + 1:data[i][j]
                                      .find(":")]).replace(' ', '-')

    for i in range(len(data)):
        for j in range(1, len(data[0])):
            new_data[i][j + 1] = data[i][j]

    return new_data


def erase_emails(data_):
    data = data_
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] is not None and data[i][j].find('@') != -1:
                data[i][j] = data[i][j][data[i][j].find('@') + 1:]
    return data


def date_reformat(data_):
    data = data_
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] is not None and data[i][j].find('/') != -1:
                data[i][j] = (data_[i][j][data_[i][j]
                              .rfind('/') + 1:] + "." +
                              data_[i][j][data_[i][j]
                              .find("/") + 1:data_[i][j]
                              .rfind('/')] + "." +
                              data_[i][j][:data_[i][j]
                              .find('/')])
    return data


def sort(data):
    data.sort(key=lambda x: x[1])
    return data


def transponse(data):
    new_data = [] * len(data[0])
    for i in range(len(data[0])):
        new_data.append([""] * len(data))

    for i in range(len(data)):
        for j in range(len(data[0])):
            new_data[j][i] = data[i][j]
    return new_data


def compare(data1, data2):
    eq = True
    for el in range(len(data1)):
        if not data1[el] == data2[el]:
            eq = False
            break
    return eq


if __name__ == "__main__":
    print(*main([['+7 978 692-67-33:0.8', '21/10/01', None, 'fadanz5@mail.ru', 'fadanz5@mail.ru'],
                 ['+7 775 186-36-24:0.1', '17/02/01', None, 'reganz6@rambler.ru', 'reganz6@rambler.ru'],
                 ['+7 451 529-34-45:0.7', '10/11/01', None, 'dedman94@rambler.ru', 'dedman94@rambler.ru'],
                 ['+7 978 692-67-33:0.8', '21/10/01', None, 'fadanz5@mail.ru', 'fadanz5@mail.ru'],
                 ['+7 516 438-25-95:0.8', '05/05/03', None, 'fesodak55@yandex.ru', 'fesodak55@yandex.ru']]),
          sep="\n")
    print("****************************************************************************")
    print(*main([['+7 750 538-11-98:0.3', '07/01/04', None, 'vikokev88@gmail.com', 'vikokev88@gmail.com'],
                 ['+7 054 214-23-38:0.4', '02/07/99', None, 'butidi35@rambler.ru', 'butidi35@rambler.ru'],
                 ['+7 965 160-17-40:0.7', '02/04/01', None, 'mifev10@yandex.ru', 'mifev10@yandex.ru'],
                 ['+7 965 160-17-40:0.7', '02/04/01', None, 'mifev10@yandex.ru', 'mifev10@yandex.ru']]), sep="\n")
