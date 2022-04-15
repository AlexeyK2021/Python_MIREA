data_ = [
    ['+7 978 692-67-33:0.8', '21/10/01', None, 'fadanz5@mail.ru', 'fadanz5@mail.ru'],
    ['+7 775 186-36-24:0.1', '17/02/01', None, 'reganz6@rambler.ru', 'reganz6@rambler.ru'],
    ['+7 451 529-34-45:0.7', '10/11/01', None, 'dedman94@rambler.ru', 'dedman94@rambler.ru'],
    ['+7 978 692-67-33:0.8', '21/10/01', None, 'fadanz5@mail.ru', 'fadanz5@mail.ru'],
    ['+7 516 438-25-95:0.8', '05/05/03', None, 'fesodak55@yandex.ru', 'fesodak55@yandex.ru']
]


def delete_blank_column(data):
    blank_column = {}
    new_data = [] * len(data)
    for i in range(len(data[0])):
        new_data.append([] * len(data[0]))

    column_to_delete = 0
    for i in range(len(data)):
        for j in range(len(data)):
            if data[i][j] is None:
                blank_column[j] += 1

    for (key, value) in blank_column:
        if value == len(data):
            column_to_delete = key

    for i in range(len(data)):
        for j in range(len(data[i])):
            if j == column_to_delete:
                continue
            else:
                new_data[i][j] = data[i][j]


def main(data):
    print(delete_blank_column(data))


if __name__ == "__main__":
    main(data_)
