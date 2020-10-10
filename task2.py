from random import randint

def get_input_as_int(label):
    input_value = None

    while type(input_value) != int:
        input_value = input(label)
        try:
            input_value = int(input_value)
            break
        except ValueError:
            continue

    return input_value

def get_random_numbers():
    return (randint(0, 9), randint(0, 9))

def task2():
    nbrs = get_random_numbers()
    response = get_input_as_int(f'How much is {nbrs[0]} times {nbrs[1]}? ')

    while response != nbrs[0] * nbrs[1]:
        response = get_input_as_int(f'{nbrs[0]} times {nbrs[1]} is not {response}, please try again: ')

    print('done')

task2()