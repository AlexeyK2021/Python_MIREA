# Функция перехода из комнаты в комнату
def go(room):
    def func(state):
        return dict(state, room=room)

    return func


# def rotate(wheel):
#     def func(state):
#         new_state = dict(state)
#         if wheel == 'w1':
#             new_state['w1'] = (new_state['w1'] + 1) % 3
#             new_state['w2'] = (new_state['w1'] - 1) % 3
#             new_state['w3'] = (new_state['w1'] - 1) % 3
#         elif wheel == 'w2':
#             new_state['w1'] = (new_state['w2'] - 1) % 3
#             new_state['w2'] = (new_state['w2'] + 1) % 3
#             new_state['w3'] = (new_state['w2'] - 1) % 3
#         elif wheel == 'w3':
#             new_state['w1'] = (new_state['w3'] - 1) % 3
#             new_state['w2'] = (new_state['w3'] - 1) % 3
#             new_state['w3'] = (new_state['w3'] + 1) % 3
#         return dict(state, )
#
#     return func

def toggle_lever(lever):
    def func(state):
        new_state = dict(state)
        new_state[lever] = not new_state[lever]
        return new_state


def go_conditional(room, cond):
    def func(state):
        if cond(state):
            return dict(state, room=room)
        return state


# Структура игры. Комнаты и допустимые в них действия
game = {
    'room0': dict(
        left=go('room1'),
        up=go('room2'),
        right=go('room3')
    ),
    'room1': dict(
        up=go('room2'),
        right=go('room0')
    ),
    'room2': dict(
    ),
    'room3': dict(
        up=go('room4'),
        right=go('room5'),
        left=go_conditional('room0', lambda state: state['lever'])
    ),
    'room4': dict(
        down=go('room3'),
        right=go('room5'),
        push_lever=toggle_lever('lever')
    ),
    'room5': dict(
        up=go('room4'),
        left=go('room3')
    )
}
# game_1 = {
#     'main': dict(
#         rot1=rotate('w1'),
#         rot2=rotate('w2'),
#         rot3=rotate('w3')
#     )
# }

# Стартовое состояние
START_STATE = dict(room='room0', lever=False)


# START_STATE1 = dict(w1=0, w2=0, w3=0)


def is_goal_state(s):
    '''
    Проверить, является ли состояние целевым.
    На входе ожидается множество пар ключ-значение.
    '''

    return ('room', 'room2') in s
    # return s == (('w1', 1), ('w2', 2), ('w3', 3))


def get_current_room(state):
    '''
    Выдать комнату, в которой находится игрок.
    '''
    # return state['main']
    return state['room']


def print_dot(graph, start_key):
    dead_ends = find_dead_ends(graph)
    print('digraph {')
    graph_keys = list(graph.keys())
    for x in graph:
        n = graph_keys.index(x)
        if x == start_key:
            print(f'n{n} [style="filled",fillcolor="dodgerblue",shape="circle"]')
        elif is_goal_state(x):
            print(f'n{n} [style="filled",fillcolor="green",shape="circle"]')
        elif x in dead_ends:
            print(f'n{n} [style="filled",fillcolor="red",shape="circle"]')
        else:
            print(f'n{n} [shape="circle"]')
    for x in graph:
        n1 = graph_keys.index(x)
        for y in graph[x]:
            n2 = graph_keys.index(y)
            print(f'n{n1} -> n{n2}')
    print('}')


def d2t(d):
    return tuple(d.items())


def make_model(game, start_state):
    graph = dict()
    to_visit = [start_state]
    visited = list()
    while to_visit:
        curr_state = to_visit.pop()
        # graph.setdefault(d2t(curr_state), list())
        visited.append(curr_state)
        graph[d2t(curr_state)] = list()
        for name, action in game[curr_state['room']].items():
            new_state = action(curr_state)
            if new_state not in visited and new_state not in to_visit:
                to_visit.append(new_state)
            graph[d2t(curr_state)].append(d2t(new_state))

    return graph


def find_dead_ends(graph):
    result = list()
    for state in graph:
        to_visit = [state]
        visited = list()
        is_dead = True
        while to_visit:
            curr_state = to_visit.pop()
            visited.append(curr_state)
            for new_state in graph[curr_state]:
                if new_state not in visited and new_state not in to_visit:
                    to_visit.append(new_state)
            if is_goal_state(curr_state):
                is_dead = False
                break
        if is_dead:
            result.append(state)
    return result


if __name__ == "__main__":
    graph = make_model(game, START_STATE)
    print_dot(graph, START_STATE)
