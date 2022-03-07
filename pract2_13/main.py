import os


def get_hierarchy(path):
    pass


def is_file(file):
    filename, ext = file.split(".")
    return len(ext) > 0


def generate_graph(files):
    graph = "digraph A {\n"
    for file in files:
        graph.join()

    graph.join("\n}")
    return graph


if __name__ == "__main__":
    print("00")
