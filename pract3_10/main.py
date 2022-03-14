import csv
import datetime
from matplotlib import pyplot as plt


def graph_activity_time(data):
    sending_time = [0] * 24
    for string in data:
        sending_time[parse_time(string[4]).time().hour] += 1
    generate_graph(
        name="The ratio of time of sending work and the number of students (1)",
        x_name="Send time", y_name="Number of students",
        data_x=range(24), data_y=sending_time,
        size_x=6, size_y=5, color='r'
    )


def graph_activity_date(data):
    sending_date = [0] * 7
    for string in data:
        sending_date[parse_time(string[4]).weekday()] += 1
    generate_graph(
        name="The ratio of the day of sending work and the number of students (2)",
        x_name="Day name", y_name="Number of students",
        data_x=["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"],
        data_y=sending_date, size_x=8, size_y=10, angle=45, color='b'
    )


def graph_activity_group(data):
    groups_names = []
    for i in data:
        copy = True
        for j in groups_names:
            if i[3] == j:
                copy = False
        if copy:
            groups_names.append(i[3])

    sending_group = [0] * len(groups_names)

    for string in data:
        for j in range(len(groups_names)):
            if string[3] == groups_names[j]:
                sending_group[j] += 1

    generate_graph(
        name="The ratio of the students groups and the number of sending work (3)",
        x_name="Groups", y_name="Number of works",
        data_x=groups_names, data_y=sending_group,
        size_x=10, size_y=11, angle=90, color='g'
    )


def graph_groups_right_solutions(data):
    groups_names = [""]
    for i in data:
        copy = True
        for j in groups_names:
            if i[2] == j:
                copy = False
        if copy:
            groups_names.append(i[2])

    right_solutions = [0] * len(groups_names)

    for string in data:
        for j in range(len(groups_names)):
            if string[2] == groups_names[j]:
                right_solutions[j] += 1

    generate_graph(
        name="The ratio of the right solutions and students groups (4)",
        x_name="Groups", y_name="Number of right solutions",
        data_x=groups_names, data_y=right_solutions,
        size_x=10, size_y=11, angle=90, color='g'
    )


def graph_difficult_tasks(data_results, data_messages):
    tasks_difficulty = [0.0] * 5
    for i in range(5):
        sent_summ = 0
        passed_summ = 0
        for j in data_results:
            if j[0] == str(i):
                passed_summ += 1
        for k in data_messages:
            if k[1] == str(i):
                sent_summ += 1
        tasks_difficulty[i] = passed_summ / sent_summ * 100
    generate_graph(
        name="The ratio of the right solutions \nwith all sent solutions and task number (5)",
        x_name="Task number", y_name="Passed in %",
        data_x=range(1, 6, 1), data_y=tasks_difficulty,
        size_x=4, size_y=4, color='g'
    )


def generate_graph(name, x_name, y_name, data_x, data_y, size_x=6, size_y=4, angle=0, color='k'):
    plt.figure(figsize=(size_x, size_y))
    plt.grid(visible=True)
    plt.xticks(rotation=angle)
    plt.ylabel(y_name)
    plt.xlabel(x_name)
    plt.suptitle(name)
    plt.plot(data_x, data_y, color)
    plt.show()


def parse_time(text):
    return datetime.datetime.strptime(text, "%Y-%m-%d %H:%M:%S.%f")


if __name__ == "__main__":
    with open('data/messages.csv', encoding='utf8') as f:
        messages = list(csv.reader(f, delimiter=','))
    with open('data/results.csv', encoding='utf8') as f:
        results = list(csv.reader(f, delimiter=','))

    graph_activity_time(messages)
    graph_activity_date(messages)
    graph_activity_group(messages)
    graph_groups_right_solutions(results)
    graph_difficult_tasks(results, messages)
