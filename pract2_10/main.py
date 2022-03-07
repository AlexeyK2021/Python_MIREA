bad_subj = ['main.py', 'k17 14', 'K13 18', 'к02 1', 'ИВБО-11 Вариант№14', 'к02 21', '1.3.py', 'В 11 4',
            '\ufeff\u200b\u200bк20 21', 'B7 21', 'Фамилия Имя Задача 1.1', 'В03 12', 'к08 24', 'к07 23',
            '1.2.py, 1.3.py, 1.4.py', '1.1.py', 'K14 23', 'в7 ', 'к6 ', '\u200b\u200bк20 21', 'к2 в3', 'В104', 'В1013',
            'B3 29', 'v10 15', 'k13 30', 'В 7 10', 'Фамилия И.О. к7 31', '1.2.py', 'К10', 'ПитонН4 н11', 'K13 28', 'К4',
            'K17 10', 'и4 11', 'Н1', 'н01 28', 'б3 5', 'Re: в6 28', 'к-11 3', '2_1.py, 2_2.py']


def parse_subj(text):
    for seq in text:
        if len(seq) == 6 and not seq.__contains__(".py"):
            if seq[0].lower() == "к" or seq[0].lower() == "k":
                print("ИКБО", end=" ")
            elif seq[0].lower() == "в" or seq[0].lower() == "v":
                print("ИВБО", end=" ")
            elif seq[0].lower() == "м" or seq[0].lower() == "m":
                print("ИМБО", end=" ")
            elif seq[0].lower() == "н" or seq[0].lower() == "n":
                print("ИНБО", end=" ")

            print(seq[1:3] if seq[1] != "-" else seq[2:3], end=" ")
            print(f"Вариант {seq[4:6]}")


if __name__ == "__main__":
    parse_subj(bad_subj)
