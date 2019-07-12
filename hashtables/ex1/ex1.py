#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve)

def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(length)
    hash_table_insert(ht, weights[0], 0)
    current_index = 1
    while current_index < length:
        current_weight = weights[current_index]
        hash_table_insert(ht, current_weight, current_index)
        pair_to_limit = limit - current_weight
        found_pair = hash_table_retrieve(ht, pair_to_limit)
        if found_pair:
            if current_index == 1:
                return (current_index, 0)
            elif found_pair > current_index:
                return (found_pair, current_index)
            else:
                return (current_index, found_pair)
        current_index += 1
    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")