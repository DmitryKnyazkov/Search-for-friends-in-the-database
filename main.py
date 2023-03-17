def list_id_fr_friends(user: int) -> list:
    """
    Функция итерическим путем определяет друзей друзей пользователя
    :param user: передаем в функцию только пеользователя (его номер в базе данных в глобальной области)
    :return: list. список друзей друзей
    """
    list_id_fr_fr = []
    for friend_id in dict_id_friends[user]:
        for fr_fr_id in dict_id_friends[friend_id]:
            if fr_fr_id not in list_id_fr_fr and fr_fr_id != user and fr_fr_id not in dict_id_friends[user]:
                list_id_fr_fr.append(fr_fr_id)

    return list_id_fr_fr


def dict_id_friends(users: list[dict], friendship: list[tuple]) -> dict:
    """
    функция формирует словарь списков, где в ключе находятся номена id пользователей, а в соответствующих
    значениях, списки связанных с ними других пользователей (их номера id).
    :param users: Список словорей. даза данных.
    :param friendship: Список кортежей. в нем хранятся взаимосвязи между пользователями. в каждом кортеже
    пара номеров id пользователей связанных друг с другом
    :return: сформированный словарь списков
    """
    dict_id_friends_ = {user["id"]: [] for user in users}
    # print(dict_id_friends)

    for i, j in friendship:
        dict_id_friends_[i].append(j)
        dict_id_friends_[j].append(i)
    print("Дан словарь всех взаимозвязей для проверки", dict_id_friends_)
    return dict_id_friends_


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

    dict_id_friends = dict_id_friends(users, friendship)

    user = int(input("Введите id интересующего вас пользователя "))
    if check(user):
        full_data_user = users[user]
        name_user = full_data_user["name"]
        print(f"Под этим id есть пользователь, его зовут {name_user}")

        print('Хотите узнать кто его друзья? Если да, то напишите "да":')
        if input().upper() == "ДА":
            print("Его друзья:")
            for x in dict_id_friends[user]:
                print(users[x])

        print(f"Хотите узнать, с кем {name_user} вероятно еще знаком? Это будут друзья его друзей.")
        if input().upper() == "ДА":
            print(f"Друзья друзей {name_user}")
            for x in list_id_fr_friends(user):
                print(users[x])

