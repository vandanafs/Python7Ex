from random import randrange
greeting_list={
    1:["Hello","Hi","Hey"],
    2:["Namaskar","Namaskargalu","Namaste"]
}

def greet_random_item_from_list(greeting_list):
    ran_number=randrange(1,4)
    print(ran_number)
    print(greeting_list[1][ran_number])

greeting_list(greeting_list)
