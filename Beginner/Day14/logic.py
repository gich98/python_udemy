import random


def find_index(list_data, key_data, value_data):
    for i in range(len(list_data)):
        if list_data[i].get(key_data) == value_data:
            return i
    return -1


def random_data(list_data):
    temp_data = random.choice(list_data)
    key_search = "name"
    index_data = find_index(list_data, key_search, temp_data.get(key_search))
    list_data.pop(index_data)
    return temp_data


def compare_follower(user_a_followers, user_b_followers):
    if user_a_followers > user_b_followers:
        return "A"
    else:
        return "B"
