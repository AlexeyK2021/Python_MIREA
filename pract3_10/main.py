import csv
import datetime
from matplotlib import pyplot as plt


def activity_time(messages):
    plt.plot()
    plt.ylabel("number of students")
    plt.xlabel("pass time")
    students = []
    time = []
    for string in messages:
        data = string.split(",")
        time.append(parse_time(data[4]).time().hour)
        students.append(data[])


def parse_time(text):
    return datetime.datetime.strptime(text, "%Y-%m-%d %H:%M:%S.%f")


with open('data/messages.csv', encoding='utf8') as f:
    messages = list(csv.reader(f, delimiter=','))
with open('data/results.csv', encoding='utf8') as f:
    results = list(csv.reader(f, delimiter=','))

for i in range(len(messages)):

print(messages[0])
print(results[0])
