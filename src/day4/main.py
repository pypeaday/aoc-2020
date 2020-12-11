from typing import Union
from cerberus import Validator

# cerberus validator defined here because we can't add coercion via a YAML file
VALIDATION_SCHEMA = {
    "ecl": {
        "required": True,
        "type": "string",
        "allowed": ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
    },
    "pid": {
        "required": True,
        "type": "string",
        "minlength": 9,
        "maxlength": 9,
    },
    "eyr": {
        "required": True,
        "type": "integer",
        "min": 2020,
        "max": 2030,
        "coerce": int,
    },
    "hcl": {
        "required": True,
        "type": "string",
        "regex": "^#[a-z0-9]{6}",
    },
    "byr": {
        "required": True,
        "type": "integer",
        "min": 1920,
        "max": 2002,
        "coerce": int,
    },
    "iyr": {
        "required": True,
        "type": "integer",
        "min": 2010,
        "max": 2020,
        "coerce": int,
    },
    "hgt": {
        "required": True,
        "regex": "^([0-9]{2,3})(cm|in)",
    },
    "cid": {"required": False},
}


def get_data(filepath: str = "./data/raw/day4_sample.txt"):
    inputs = []
    with open(filepath, "r") as f:
        lines = f.readlines()
        _data = ""
        for line in lines:
            if line == "\n":
                inputs.append(_data.strip())
                _data = ""
            else:
                _data += line.replace("\n", " ")
        if _data != "":
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
        toks = _input.split(" ")
        _d = dict()
        for x in toks:
            k, v = x.split(":")
            _d[k] = v
        res.append(_d)
    return res


def check_height(height: str) -> bool:
    """
    for part 2 cerberus will check validation for everything except the
    dependent values for the height so I do it explicitly here
    :param height:
    :return: Valid or Not / True/False
    """
    val = int(height[:-2])
    meas = height[-2:]
    if meas == "cm":
        return 150 <= val <= 193
    else:
        return 59 <= val <= 76


def is_passport_valid(
    _input: dict, validation_schema: Union[dict, None] = None
) -> bool:
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
    :param validation_schema: pass schema for part 2

    :return: True/False
    """
    if not validation_schema:
        _keys = set(_input.keys())
        required_keys = {"ecl", "pid", "eyr", "hcl", "byr", "iyr", "hgt"}
        if required_keys - _keys == set():
            return True
        else:
            return False
    else:
        # part 2 solution with data validation here
        v = Validator(validation_schema)
        if v.validate(_input):
            return check_height(_input["hgt"])
        else:
            return False


def main(
    filepath: str = "./data/raw/day4_sample.txt", part2: bool = False
) -> int:
    inputs = get_data(filepath)
    formatted_inputs = format_data(inputs)

    if not part2:
        res = map(is_passport_valid, formatted_inputs)
    else:
        # with open('./src/day4/schema.yaml', 'r') as y:
        #     validation_schema = yaml.load(y, Loader=yaml.FullLoader)

        res = map(
            is_passport_valid,
            formatted_inputs,
            [VALIDATION_SCHEMA for _ in range(len(inputs))],
        )

    num_valid = sum(res)
    print(f"Number of valid passports is {num_valid}")
    return num_valid


if __name__ == "__main__":
    filepath = "./data/raw/day4_input.txt"
    print("Solution for Part 1")
    main(filepath)
    print("Solution for Part 2")
    main(filepath, True)
