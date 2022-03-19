import csv

from matplotlib import pyplot as plt


def graph_popular_games(data):
    years = [0] * 28
    for game in data:
        if game[3] != "не издана":
            years[int(game[3]) - 1981] += 1
    generate_graph(
        name="Popular game publishing time",
        x_name="Years", y_name="Number of published games",
        data_x=range(1981, 2009, 1), data_y=years,
        size_y=6, color="r"
    )


def graph_genres(data):
    genres_1980 = {}
    genres_1990 = {}
    genres_2000 = {}
    for game in data:
        if game[3] != "не издана":
            if 1980 < int(game[3]) <= 1989:
                if genres_1980.get(game[1]) is None:
                    genres_1980[game[1]] = 1
                else:
                    genres_1980[game[1]] += 1
            elif 1990 < int(game[3]) <= 2000:
                if genres_1990.get(game[1]) is None:
                    genres_1990[game[1]] = 1
                else:
                    genres_1990[game[1]] += 1
            elif 2000 < int(game[3]) <= 2010:
                if genres_2000.get(game[1]) is None:
                    genres_2000[game[1]] = 1
                else:
                    genres_2000[game[1]] += 1
    generate_graph(
        name="Popularity of game genres of 80s", x_name="Years", y_name="Number of published games",
        data_x=genres_1980.keys(), data_y=genres_1980.values(), angle=90, size_y=6,
        color="r"
    )
    generate_graph(
        name="Popularity of game genres of 90s", x_name="Years", y_name="Number of published games",
        data_x=genres_1990.keys(), data_y=genres_1990.values(), angle=90, size_y=6,
        color="g"
    )
    generate_graph(
        name="Popularity of game genres of 00s", x_name="Years", y_name="Number of published games",
        data_x=genres_2000.keys(), data_y=genres_2000.values(), angle=90, size_y=6,
        color="b"
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


if __name__ == "__main__":
    with open('GAMES.csv', encoding='utf8') as f:
        games_data = list(csv.reader(f, delimiter=';'))
    graph_popular_games(games_data)
    graph_genres(games_data)
