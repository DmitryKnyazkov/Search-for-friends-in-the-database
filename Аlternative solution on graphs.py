import networkx as nx


def get_friend(graph: nx.Graph, i: int) -> None:
    """
    функция определяет с помощью средств библиотеки networkx связаные графы
    с переданной нодой (i) и печатает в консоле результат. т.е. печатает в консоле друзей заданного пользователя.
    :param graph: Граф NetworkX, по которому нужно совершить обход в ширину первого уровня
    :param i: узел, откуда нужно начать обход. т.е.
    :return: None. ничего не возвращает, только выводит на экран информацию
    """
    for x in graph[i]:
        print(users[x])


def get_fr_friends(graph, i) -> None:
    """
    функция определяет с помощью средств библиотеки networkx связаные графы второго уровня
    с переданной нодой (i) и печатает в консоле результат. т.е. печатает в консоле друзей друзей
    заданного пользователя. препятствует попаданию в выводимый список самого пользователя и его непосредственных
    друзей, т.е. узлов нулевого и первого уровня.
    :param graph:  Граф NetworkX, по которому нужно совершить обход в ширину первого уровня
    :param i: узел, откуда нужно начать обход. т.е.
    :return: None. ничего не возвращает, только выводит на экран информацию
    """
    list_fr_fr = []
    list_fr = []
    list_fr.append(i)
    for x in graph[i]:
        list_fr.append(x)
    for x in graph[i]:
        for y in graph[x]:
            if y not in list_fr:
                list_fr_fr.append(y)
    print("Возможные знакомые, т.е. друзья друзей ", full_data_ID['name'])
    for a in list_fr_fr:
        print(users[a])


def check(user: int) -> bool:
    """
    Функция проверяет существует ли в базе пользователь с этим id.
    :param user: id искомого пользователя
    :return: bool
    """
    if user == "":
        raise ValueError("вы ничего не ввели!!!")
    if user < 0 or user > (len(users) - 1):
        raise ValueError("вы ввели несуществующий ID")
    return True


if __name__ == "__main__":
    users = [
        {"id": 0, "name": "Hero"},
        {"id": 1, "name": "Dunn"},
        {"id": 2, "name": "Sue"},
        {"id": 3, "name": "Chi"},
        {"id": 4, "name": "Thor"},
        {"id": 5, "name": "Clive"},
        {"id": 6, "name": "Hicks"},
        {"id": 7, "name": "Devin"},
        {"id": 8, "name": "Kate"},
        {"id": 9, "name": "Clein"},
        {"id": 10, "name": "Денис"}
    ]

    friendship = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4), (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9),
                  (10, 9), (10, 8)]
    graph = nx.Graph()
    nodes = list(range(len(users)))
    print(nodes)
    graph.add_nodes_from(nodes)
    graph.add_edges_from(friendship)
    # dict_id_friends = {user["id"]: [] for user in users}
    # nx.draw_networkx(graph)


    user = int(input("Введите id интересующего вас пользователя "))
    if check(user):
        full_data_ID = users[user]

        print(f"Под этим id есть пользователь, его зовут {full_data_ID['name']}")

        print('Хотите узнать кто его друзья? Если да, то напишите "да":')
        if input().upper() == "ДА":
            print("Его друзья:")
            get_friend(graph, user)

        print(f"Хотите узнать, с кем {full_data_ID['name']} вероятно еще знаком? Это будут друзья его друзей.")
        if input().upper() == "ДА":
            get_fr_friends(graph, user)
