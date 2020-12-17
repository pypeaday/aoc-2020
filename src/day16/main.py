from tqdm import tqdm
from collections import defaultdict


def get_data(filepath: str = "./data/raw/day16_sample.txt"):

    with open(filepath, "r") as f:
        lines = f.readlines()
        check_next = False
        num_cats = 0
        for line in lines:
            if "your ticket" in line:
                check_next = True
                continue
            if check_next:
                num_cats = len(line.split(","))
                break
        fields = defaultdict(list)
        for i, line in enumerate(lines):
            if i == num_cats:
                break
            field = line.split(":")[0]
            ranges = line.split(":")[1]
            range1, range2 = ranges.split(" or ")
            r1lb, r1ub = range1.split("-")
            r2lb, r2ub = range2.split("-")
            fields[field].extend([x for x in range(int(r1lb), int(r1ub) + 1)])
            fields[field].extend([x for x in range(int(r2lb), int(r2ub) + 1)])
        my_ticket_next = False
        nearby_tickets_next = False
        tickets = []
        for i, line in enumerate(lines):
            if "your ticket" in line:
                my_ticket_next = True
                continue
            if "nearby tickets" in line:
                nearby_tickets_next = True
                continue
            if my_ticket_next:
                my_ticket_next = False
                tickets.append([int(x) for x in line.split(",")])
            if nearby_tickets_next:
                break
            else:
                continue
        for line in lines[i:]:
            tickets.append([int(x) for x in line.split(",")])
    return fields, tickets


def get_any_possible_values(fields: dict) -> list:
    vals = set()
    for k, ls in fields.items():
        for v in ls:
            vals.add(v)
    return list(vals)


def calculate_solution_1(fields: dict, tickets: list):
    invalid_tickets = 0
    invalid_values = list()
    possible_values = set(get_any_possible_values(fields))
    for ticket in tickets:
        diff = set(ticket) - possible_values
        if diff == set():
            continue
        else:
            invalid_tickets += 1
            for v in diff:
                invalid_values.append(v)
    return sum(invalid_values)


def calculate_solution_2(data: list):
    pass


def main(filepath: str = "./data/raw/day16_sample.txt."):
    fields, tickets = get_data(filepath)
    sol_1 = calculate_solution_1(fields, tickets)
    print(f"Solution 1: {sol_1}")

    # sol_2 = calculate_solution_2(data)
    # print(f"Solution 2: {sol_2}")


if __name__ == "__main__":
    main("./data/raw/day16_input.txt")
