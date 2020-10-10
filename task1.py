from random import randint

def is_prime(nb: int):
    i = 2

    if nb <= 1:
        return False
    while i < nb:
        if nb % i == 0:
            return False
        i += 1
    return True

def task1():

    for _ in range(0, 6):
        random_nb = randint(1, 100)
        print(f'The random number {random_nb} is {("not " if not is_prime(random_nb) else "")}a prime number.')

task1()
