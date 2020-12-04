REQUIRED_KEYS = {'ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'hgt'}
OPTIONAL_KEYS = {'cid'}


def get_data(filepath: str = './data/raw/day4_sample.txt'):
    inputs = []
    with open(filepath, 'r') as f:
        lines = f.readlines()
        _data = ''
        for line in lines:
            if line == '\n':
                inputs.append(_data.strip())
                _data = ''
            else:
                _data += line.replace('\n', ' ')
        if _data != '':
            inputs.append(_data.strip())

    return inputs


def format_data(inputs: list) -> list:
    """
    Function to format the string typed inputs from
    get_data() into python dicts

    :param inputs: output of get_data()
    :return: list of python dicts
        ex.
        [{
         'ecl': 'gry',
         'pid': '860033327',
         'eyr': '2020',
         'hcl': '#fffffd',
         'byr': '1937',
         'iyr': '2017',
         'cid': '147',
         'hgt': '183cm'
        }]
    """
    res = []
    for _input in inputs:
        toks = _input.split(' ')
        _d = dict()
        for x in toks:
            k, v = x.split(':')
            _d[k] = v
        res.append(_d)
    return res


def is_passport_valid(_input: dict,
                      required_keys: set) -> bool:
    """
    Checks the formatted passport input to determine if it
    is valid or not

    :param _input:  python dict element of the list output from format_data
        ex. 'ecl:gry pid:860033327 eyr:2020 hcl:#fffffd byr:1937 iyr:2017 cid:147 hgt:183cm'
            is formatted to look like:
            {
             'ecl': 'gry',
             'pid': '860033327',
             'eyr': '2020',
             'hcl': '#fffffd',
             'byr': '1937',
             'iyr': '2017',
             'cid': '147',
             'hgt': '183cm'
            }
    :param required_keys: python set of required keys for a passport to contain to be valid

    :return: True/False
    """
    _keys = set(_input.keys())
    if required_keys - _keys == set():
        return True
    else:
        return False


def main(filepath: str = './data/raw/day4_sample.txt') -> int:
    inputs = get_data(filepath)
    formatted_inputs = format_data(inputs)

    required_keys_ls = [REQUIRED_KEYS for _ in range(len(formatted_inputs))]

    res = map(is_passport_valid, formatted_inputs, required_keys_ls)

    num_valid = sum(res)
    print(f'Number of valid passports is {num_valid}')
    return num_valid


if __name__ == '__main__':
    filepath = './data/raw/day4_input.txt'
    main(filepath)
