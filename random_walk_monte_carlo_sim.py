import random

# Find the longest random walk that require no transportation to come
# back at home, (distance from home <= 4), percentage >= 50%

def random_walk(n):

    """
    random_walk(n).
    Return a tuple with the coordinates n is the number of steps
    """

    x, y, dx, dy = 0, 0, 0, 0

    for i in range(n):
        (dx, dy) = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
        x += dx
        y += dy

    return (x, y)


#  Montecarlo simulation

number_of_walks = 50000  # test this number of random walks with a specific number of steps

for walk_lenght in range(1, 31):
    no_transport = 0  # less or equal than 4 no transportation is needed

    for i in range(number_of_walks):
        (x, y) = random_walk(walk_lenght)
        distance = abs(x) + abs(y)
        if distance <= 4:
            no_transport += 1
    no_transport_percentage = float(no_transport) / number_of_walks
    print('Walk size = ', walk_lenght, '/ % of no transport = ', 100* no_transport_percentage)
