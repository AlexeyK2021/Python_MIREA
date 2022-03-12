import glob
import os.path

graph = ["", "digraph A {"]


def add_to_graph(point_a, point_b):
    # point_a = point_a if not point_a == '..' else 'this'
    graph.append(f"\"{point_a}\" -> \"{point_b}\";")
    # print(f"{point_a} -> {point_b}")


def generate_graph(path):
    for smth in glob.glob(path + '/*'):
        if os.path.isdir(smth):
            add_to_graph(path[path.rfind("/") + 1:len(path)], smth[len(path) + 1:len(smth)])
            generate_graph(smth)
        elif os.path.isfile(smth):
            add_to_graph(path[path.rfind("/") + 1:len(path)], smth[len(path) + 1:len(smth)])


if __name__ == "__main__":
    generate_graph(input())
    graph.append("}")
    print(*graph, sep="\n")
