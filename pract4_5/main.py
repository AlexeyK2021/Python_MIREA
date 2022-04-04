from HTML import HTML


def main():
    html = HTML()
    with html.body():
        with html.div():
            with html.div():
                html.p('Первая строка.')
                html.p('Вторая строка.')
            with html.div():
                html.p('Третья строка.')
    print(html.get_code())


if __name__ == "__main__":
    main()
