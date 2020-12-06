def get_data(filepath: str = './data/raw/day6_sample.txt') -> (list, list):
    """
    Returns list of inputs grouped by gruop
    :param filepath:
    :return: list of inputs, as well as a list containing the number
        of people per group (inputs are gathered up to the group level)
    """
    inputs = []
    num_people_per_group = []
    with open(filepath, 'r') as f:
        lines = f.readlines()
        _data = ''
        i = 0
        for line in lines:
            if line == '\n':
                inputs.append(_data)
                num_people_per_group.append(i)
                _data = ''
                i = 0
            else:
                _data += line.replace('\n', ' ').replace(' ', '')
                i += 1
        if _data != '':
            inputs.append(_data)
            num_people_per_group.append(i)

    return inputs, num_people_per_group


def get_group_count(data: str) -> int:
    """
    For any group count the number of unique
    questions answers 'yes'

    :param data: first result of get_data()
        ex. 'aabx', 'abbb', 'abc'
    :return: sum of count of any question answered 'yes'
    """
    return len(set(data))


def sum_all_group_counts(_input: list) -> int:
    """
    Sum the group counts of 'yes' answers for a given
    dataset.

    :param _input: list of results of get_group_count
    :return:
    """
    return sum(_input)


def main(filepath: str = './data/raw/day6_sample.txt') -> int:
    """
    Mainf function for solution 1 day 6. Takes input and calculates
    the sum of 'yes' answers per group then sums each of those counts

    :param filepath:
    :return:
    """
    inputs, _ = get_data(filepath)
    all_group_counts = map(get_group_count, inputs)
    res = sum(all_group_counts)
    return res


if __name__ == '__main__':
    # part 1
    res = main('./data/raw/day6_input.txt')
    print(f'The sum of the count per group of any "yes" answers is: {res}')

