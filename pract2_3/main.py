def generate_groups():
    groups = []
    letter_1 = "И"
    letter_2 = ["В", "К", "Н", "М"]
    letter_3 = "Б"
    letter_4 = "О"
    it = 0
    for letter in letter_2:
        if letter == "В":
            it = 9
        elif letter == "К":
            it = 28
        elif letter == "Н":
            it = 13
        else:
            it = 2
        for i in range(1, it + 1):
            if i == 9 and letter == "В":
                i = 13
                add_group(groups, letter_1, letter, letter_3, letter_4, i)
                break
            elif i == 28 and letter == "К":
                i = 30
                add_group(groups, letter_1, letter, letter_3, letter_4, i)
                break
            elif i == 12 and letter == "Н":
                i += 1
                add_group(groups, letter_1, letter, letter_3, letter_4, i)
                continue
            elif i == 13 and letter == "Н":
                i += 2
                add_group(groups, letter_1, letter, letter_3, letter_4, i)
                break
            else:
                add_group(groups, letter_1, letter, letter_3, letter_4, i)

    return groups


def add_group(groups_array, letter_1, letter, letter_3, letter_4, i):
    if i < 10:
        groups_array.append(f"{letter_1}{letter}{letter_3}{letter_4}-0{i}-20")
    else:
        groups_array.append(f"{letter_1}{letter}{letter_3}{letter_4}-{i}-20")


if __name__ == "__main__":
    print(*generate_groups(), sep="\n")
