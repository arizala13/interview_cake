list_1 = ["apples", "grapes", "oranges", "pears"]


def testing_enum(list_of_fruits):
    saved = {}

    # would save the fruit tied to its index
    for i, fruit in enumerate(list_of_fruits):
        saved[fruit] = i

    print(saved)


testing_enum(list_1)
