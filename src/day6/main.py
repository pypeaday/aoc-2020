from functools import reduce


def get_data(filepath: str = './data/raw/day6_sample.txt') -> (list, list):
    """
    Returns raw list of inputs having \n stripped away
    :param filepath:
    :return: lints of the data file in a list
    """
    data = []
    with open(filepath, 'r') as f:
        lines = f.readlines()
        for line in lines:
            data.append(line.replace('\n', ''))

    return data


def format_data_part_1(raw_data: list) -> list:
    """
    Takes raw data file and formats the data to be list
    of answers by group
    :param raw_data: direct output of get_data
    :return:
    """
    _data = ''
    inputs = []
    for line in raw_data:
        if line == '':
            inputs.append(_data)
            _data = ''
            _group_answers = []
        else:
            _data += line.replace(' ', '')
    if _data != '':
        inputs.append(_data)

    return inputs


def format_data_part_2(raw_data: list) -> list:
    """
    Takes raw data and formats to be list of lists,
    where the sublists are the individual answers
    and the lists are separated by group

    :param raw_data: direct output of get_data
    :return:
    """
    inputs = []
    _group_answers = []
    for line in raw_data:
        if line == '':
            inputs.append(_group_answers)
            _group_answers = []
        else:
            _group_answers.append(line.replace(' ', ''))
    if _group_answers:
        inputs.append(_group_answers)

    return inputs


def get_group_count(data: str) -> int:
    """
    For any group count the number of unique
    questions answers 'yes'

    :param data: first result of get_data()
        ex. 'aabx', 'abbb', 'abc'
    :return: sum of count of any question answered 'yes'
    """
    return len(set(data))


def main(filepath: str = './data/raw/day6_sample.txt') -> int:
    """
    Main function for solution 1 day 6. Takes input and calculates
    the sum of 'yes' answers per group then sums each of those counts

    :param filepath:
    :return:
    """
    raw_data = get_data(filepath)
    data = format_data_part_1(raw_data)
    all_group_counts = map(get_group_count, data)
    res = sum(all_group_counts)
    return res


def _intersection(s1: str, s2: str) -> str:
    return ''.join([x for x in set(s1).intersection(s2)])


def get_intersection(_group: list) -> str:
    """
    Take list of group answers and run reduce job to get shared answers
    by all parties of the group
    :param _group: list of answers
        ex: ['a', 'ab', 'ac']
    :return: for the example would return 'a'
    """
    return reduce(_intersection, _group)


def main2(filepath: str = './data/raw/dat6_sample.txt') -> int:
    """
    Main function for solution 2 day 6. Takes input and calculates
    the sum of 'yes' answers per group then sums each of those counts
    :param filepath:
    :return:
    """
    raw_data = get_data(filepath)
    data = format_data_part_2(raw_data)
    group_answers = map(get_intersection, data)
    all_group_counts = map(get_group_count, group_answers)
    res = sum(all_group_counts)
    return res


if __name__ == '__main__':
    # part 1
    res = main('./data/raw/day6_input.txt')
    print(f'The sum of the count per group of any "yes" answers is: {res}')

    # part 2
    res = main2('./data/raw/day6_input.txt')
    print(f'The sum of the count per group of any "yes" answers is: {res}')

