import math
import random


def calculate_pi(attempts):
    """
    This method is a approx calculator of PI using a raw MonteCarlo integration technique
    :param attempts: the number of iteration for MonteCarlo method
    :return: the approx value of PI
    """

    assert isinstance(attempts, int), 'You must provide an integer'
    assert attempts > 0, 'Provided integer must be a positive value'
    inside_point_count = 0
    for _ in range(attempts):
        x = random.uniform(0.0, 1.0)
        y = random.uniform(0.0, 1.0)
        if math.sqrt((x ** 2) + (y ** 2)) <= 1:
            inside_point_count += 1
    pi = 4 * inside_point_count / attempts
    return pi


def print_name_test():
    print('Name inside PI :: {}'.format(__name__))


if __name__ == '__main__':
    iterations = 600000
    result = calculate_pi(iterations)
    print('Approx value for PI is {} , with {} iterations'.format(result, iterations))
