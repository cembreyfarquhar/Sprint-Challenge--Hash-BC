#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * (length + 1)
    current_destination = "NONE"
    
    for i in range(length):
        hash_table_insert(hashtable, tickets[i].source, tickets[i].destination)
    if tickets[i].source == "NONE": 

        current_destination = tickets[i].destination
        # If source is none, it is the first flight
        route[0] = current_destination
    
    None_Ticket = None

    for i in range(0, length):
        next_destination = hash_table_retrieve(hashtable, current_destination)
        route[i] = next_destination
        if next_destination == "NONE":
            None_Ticket = hash_table_retrieve(hashtable, route[i - 2])
            print("HERE IT IS")
            print(None_Ticket)
        current_destination = next_destination
    



    route[length] = hash_table_retrieve(hashtable, current_destination)
    route[0] = route[length]
    route.remove("NONE")
    route[length - 1] = "NONE"
    print(route)
    """
    YOUR CODE HERE
    """
    return route


ticket_1 = Ticket("PIT", "ORD")
ticket_2 = Ticket("XNA", "SAP")
ticket_3 = Ticket("SFO", "BHM")
ticket_4 = Ticket("FLG", "XNA")
ticket_5 = Ticket("NONE", "LAX")
ticket_6 = Ticket("LAX", "SFO")
ticket_7 = Ticket("SAP", "SLC")
ticket_8 = Ticket("ORD", "NONE")
ticket_9 = Ticket("SLC", "PIT")
ticket_10 = Ticket("BHM", "FLG")

tickets = [ticket_1, ticket_2, ticket_3, ticket_4, ticket_5,
    ticket_6, ticket_7, ticket_8, ticket_9, ticket_10]

reconstruct_trip(tickets, 10)