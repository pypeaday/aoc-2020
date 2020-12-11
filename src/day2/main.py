from multiprocessing import Pool
import time
from more_itertools import locate


def get_data(filepath: str = "./data/raw/dat2_sample.txt"):
    data = []
    with open(filepath, "r") as f:
        lines = f.readlines()
        for line in lines:
            data.append(line.replace("\n", ""))
    return data


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
    x = list(
        " ".join(" ".join(_input.split("-")).split(":"))
        .replace("  ", " ")
        .split(" ")
    )
    x[0] = int(x[0])
    x[1] = int(x[1])
    return tuple(x)


def extract_vars_pt2(_input: str) -> tuple:
    """
    extracts x0, x1, l, password from the input and returns them as distinct
    values in a tuple having mutated x0 and x1 to be 0 indexed

    Note the function is the **almost** the same as extract_vars but I wanted
    the docstring to have the change in definitions for part 2

    :param _input: of the form "x0-x1 l: <password>" where l is the required
        letter for the password to be valid, x0 and x1 are required positions
         that l much be in the password (exactly one of the 2 positions needs to
         be satisfied) and <password> is obviously the password to check
    :return: x0, x1, l, password
    """
    x = list(
        " ".join(" ".join(_input.split("-")).split(":"))
        .replace("  ", " ")
        .split(" ")
    )
    x[0] = int(x[0]) - 1
    x[1] = int(x[1]) - 1
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


def check_validity2(_input) -> bool:
    """
    checks password given a password and it's letter + index requirement
    :param _input:  of the form "x0-x1 l: <password>" where l is the required
        letter for the password to be valid, x0 and x1 are required positions
         that l much be in the password (exactly one of the 2 positions needs to
         be satisfied) and <password> is obviously the password to check
    """
    x0, x1, l, p = extract_vars_pt2(_input)
    indices = list(locate(p, lambda x: x == l))
    return bool(x0 in indices) ^ bool(x1 in indices)


def main(filepath: str = "./data/raw/day2_sample.txt", mp=False, _map=False):
    print("Start solution 1")
    start = time.time()
    inputs = get_data(filepath)
    elapsed_inputs = time.time() - start
    print(f"Time for data prep: {elapsed_inputs}")
    if mp:  # time to multiprocess is 0.15400099754333496 seconds
        with Pool() as pool:
            res = pool.map(check_validity, inputs)

    if _map:  # time to process using  map was 0.0 seconds
        res = map(check_validity, inputs)

    else:  # time to process naievly is 0.0019981861114501953 seconds
        res = []
        for x in inputs:
            res.append(check_validity(x))
    elapsed_total = time.time() - start
    ans = sum(res)
    print(f"Number of valid passwords: {ans}")
    print(
        f"Solution 1 time with MP = {mp} and _map = {_map} was: {elapsed_total}\n"
    )
    return ans


def main2(filepath: str = "./data/raw/day2_sample.txt"):
    print("Start solution 2")
    start = time.time()
    inputs = get_data(filepath)
    elapsed_inputs = time.time() - start
    print(f"Time for data prep: {elapsed_inputs}")

    res = map(check_validity2, inputs)
    ans = sum(res)
    print(f"Number of valid passwords for problem 2: {ans}")
    elapsed_total = time.time() - start
    print(f"Solution 2 time was: {elapsed_total}\n")
    return ans


if __name__ == "__main__":
    meta_start = time.time()
    # solution 1
    # main('./data/raw/day2_input.txt', mp=True, _map=False)

    main("./data/raw/day2_input.txt", mp=False, _map=True)

    # main('./data/raw/day2_input.txt', mp=False, _map=False)

    # solution 2
    main2("./data/raw/day2_input.txt")
    meta_elapsed = time.time() - meta_start
    print(f"Total time was {meta_elapsed}")
