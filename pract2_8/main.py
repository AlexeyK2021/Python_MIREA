import random

# families = ["Смирнов", "Иванов", "Кузнецов", "Соколов", "Попов", "Лебедев", "Козлов", "Новиков", "Морозов", "Петров",
#             "Волков", "Соловьёв", "Васильев", "Зайцев", "Павлов", "Семёнов", "Голубев", "Виноградов", "Богданов",
#             "Воробьёв", "Фёдоров", "Михайлов", "Беляев", "Тарасов", "Белов"]
names = ["Александр", "Михаил", "Иван", "Максим", "Артём", "Даниил", "Дмитрий", "Кирилл", "Андрей", "Егор", "Илья",
         "Алексей", "Роман", "Фёдор", "Никита", "Марк", "Сергей", "Владислав", "Степан"]


def fam_gen(num):
    full_names = []
    for i in range(num):
        random_name = names[random.randint(0, len(names) - 1)]
        # random_familie = families[random.randint(0, len(families) - 1)][0:2] \
        #                  + families[random.randint(0, len(families) - 1)][2:3] \
        #                  + families[random.randint(0, len(families) - 1)][3:4] \
        #                  + families[random.randint(0, len(families) - 1)][4:6]
        prefix_num = random.randint(0, 2)
        prefix = ""
        random_patro = names[random.randint(0, len(names) - 1)][:1]

        if prefix_num == 0:
            prefix = "ов"
        elif prefix_num == 1:
            prefix = "ин"
        elif prefix_num == 2:
            prefix = "ев"

        familie = names[random.randint(0, len(names) - 1)]
        random_familie = familie[0:len(familie) - 1 if random.random() / 2 == 0 else len(familie) - 2] + prefix
        full_names.append(f"{random_name} {random_patro.upper()}. {random_familie}")
    return full_names
    pass


if __name__ == "__main__":
    print(*fam_gen(int(input())), sep="\n")
