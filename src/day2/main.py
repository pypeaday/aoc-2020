from multiprocessing import Pool
import time


def get_data(filepath: str = './data/raw/dat2_input.txt'):
    with open(filepath, 'r') as f:
        lines = f.readlines()
    return lines


def extract_vars(_input: str) -> tuple:
    """
    extracts f, c, l, password from the input and returns them as distinct
    values in a tuple

    :param _input: of the form "f-c l: <password>" where l is the required
        letter for the password to be valid, f and c are the floor and
        ceiling count requirements of l in the password and <password>
        is obviously the password to check
    :return: f, c, l, password
    """
    x = list(' '.join(' '.join(_input.split('-')).split(':')
                      ).replace('  ', ' ').split(' '))
    x[0] = int(x[0])
    x[1] = int(x[1])
    return tuple(x)


def check_validity(_input) -> bool:
    """
    checks password given a password and it's letter + count requirement
    :param _input:  of the form "f-c l: <password>" where l is the required
        letter for the password to be valid, f and c are the floor and
        ceiling count requirements of l in the password and <password>
        is obviously the password to check
    """

    f, c, l, p = extract_vars(_input)

    cnt = p.count(l)
    return f <= cnt <= c


def main(filepath: str = './data/raw/day2_input.txt', mp=False, _map=False):

    inputs = get_data(filepath)

    start = time.time()
    if mp:  # time to multiprocess is 0.15400099754333496 seconds
        with Pool() as pool:
            res = pool.map(check_validity, inputs)

    if _map:  # time to process using  map was 0.0 seconds
        res = map(check_validity, inputs)

    else:  # time to process naievly is 0.0019981861114501953 seconds
        res = []
        for x in inputs:
            res.append(check_validity(x))
    end = time.time()
    print(f'Number of valid passwords: {sum(res)}')
    print(f'Time with MP = {mp} and _map = {_map} was: {end-start}')


if __name__ == '__main__':
    # solution 1
    main('./data/raw/day2_input.txt', mp=True, _map=False)

    main('./data/raw/day2_input.txt', mp=False, _map=True)

    main('./data/raw/day2_input.txt', mp=False, _map=False)
