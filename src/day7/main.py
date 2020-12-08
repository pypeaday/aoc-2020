from collections import defaultdict


def get_data(filepath: str = './data/raw/day7_sample.txt') -> dict:
    """
    Returns dict of organized inputs keyed by bag color with each value being a list of possible inner bag colors
    :param filepath:
    :return: lints of the data file in a list
    """
    data = []
    # read data in line by line
    with open(filepath, 'r') as f:
        lines = f.readlines()
        for line in lines:
            data.append(line.replace('\n', ''))

    # we'll do some formatting in this function this time
    # make a dictionary keyed by each color of bag, where the values are
    # every other color that can go in that bag and the repetition of
    # a color means multiples of that color can go inside

    _d = defaultdict(list)
    for _line in data:
        split_line = _line.split(' bags ')
        big_bag_color = split_line[0]
        allowed_contents = split_line[1].replace('contain ', '').split(', ')
        for _item in allowed_contents:
            if _item == 'no other bags.':
                _d[big_bag_color] = [None]
                continue
            num = int(_item.split(' ')[0])
            if 1 <= num <= 9:
                small_bag_color = _item[2:].replace('.', '').replace('bags', '').replace('bag', '').strip()
            elif 10 <= num < 99:
                small_bag_color = _item[3:].replace('.', '').replace('bags', '').replace('bag', '').strip()
            elif num > 99:
                small_bag_color = _item[4:].replace('.', '').replace('bags', '').replace('bag', '').strip()
            # how many edge cases could there be
            else:
                raise SystemError('Fix this get_data function because apparently hundreds of bags are an option')
            # append duplicates of each possible bag in case number ever matters - we'll use set() later on to avoid
            # unnecessary calculation
            _d[big_bag_color].extend([small_bag_color] * num)

    return _d


def can_bag_be_carried(rules: dict, outer_bag: str, inner_bag: str) -> bool:
    """
    Recursively check the rules for a given outer bag to see if eventually the inner bag will be able to be carried
    :param rules:
    :param outer_bag:
    :param inner_bag:
    :return:
    """
    inner_bags = set(rules[outer_bag])
    if inner_bag in inner_bags:
        return True
    else:
        results = map(can_bag_be_carried,
                      [rules for _ in range(len(inner_bags))],
                      inner_bags,
                      [inner_bag for _ in range(len(inner_bags))])

        return any(results)


def main(filepath: str = './data/raw/day7_sample.txt',
         my_bag: str = 'shiny gold'):
    rules = get_data(filepath)
    all_bags = [x for x in rules.keys()]
    results = map(can_bag_be_carried,
                  [rules for _ in range(len(all_bags))],
                  all_bags,
                  [my_bag for _ in range(len(all_bags))])

    return sum(results)


def count_all_bag_capacities_including_self(rules: dict, sums: dict) -> dict:
    for bag, rule in rules.items():
        if bag in sums.keys():
            continue
        if rule[0] is None:
            sums[bag] = 1
        else:
            if set(sums.keys()) != set() and set(rule).issubset(sums.keys()):  # ie. if every bag in the rule has a numeric value already
                vals = [sums[k] for k in rule]
                sums[bag] = sum(vals) + 1

    if len(sums.keys()) == len(rules.keys()):
        return sums
    else:
        return count_all_bag_capacities_including_self(rules, sums)


def count_bag_capacity(sums: dict, rules: dict, bag: str) -> int:
    """
    Return the number of bags 'bag' can contain based on the rules from get_data()

    :param sums: raw sub-bag count of each colored bag
    :param rules: rules from get_data()
    :param bag: colored bag to check the capacity of
    :return:
    """
    return sum(sums[k] for k in rules[bag])


if __name__ == '__main__':
    # solution 1
    res = main('./data/raw/day7_input.txt', 'shiny gold')
    print(f'Number of bags that can eventually hold my shiny gold bag are: {res}')

    # solution 2
    rules = get_data('./data/raw/day7_input.txt')
    sums = count_all_bag_capacities_including_self(rules, dict())
    ans = count_bag_capacity(sums, rules, 'shiny gold')
    print(f'Number of bags that fit into my shiny gold bag are: {ans}')
