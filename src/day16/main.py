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


def get_valid_tickets(tickets: list, possible_values: set) -> list:
    valid_tickets = []
    for ticket in tickets:
        diff = set(ticket) - possible_values
        if diff == set():
            valid_tickets.append(ticket)
    return valid_tickets


def get_possible_index(fields: dict, ticket: list):
    field_index = defaultdict(list)
    for i, val in enumerate(ticket):
        for k, ls in fields.items():
            if val in ls:
                field_index[k].append(i)
    return field_index


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


def calculate_solution_2(fields: dict, tickets: list):
    possible_values = set(get_any_possible_values(fields))
    valid_tickets = get_valid_tickets(tickets, possible_values)
    vals = set([x for x in range(len(valid_tickets[0]))])
    field_indices = {k: vals for k in fields.keys()}
    res = map(
        get_possible_index,
        [fields for _ in range(len(valid_tickets))],
        valid_tickets,
    )
    for r in res:
        for k, ls in r.items():
            field_indices[k] = field_indices[k].intersection(set(ls))
    # loop over ordered field indicies keys by length of values
    sorted_field_indices = {
        k: field_indices[k]
        for k in sorted(field_indices, key=lambda k: len(field_indices[k]))
    }
    actual_field_indices = dict()
    used_indices = set()
    for k, v in sorted_field_indices.items():
        values = set(v) - used_indices
        if len(values) > 1:
            raise ValueError(
                "problem in that there is multiple possible values yet for a key"
            )
        val = list(values)[0]
        actual_field_indices[k] = val
        used_indices.add(val)
    prod = 1
    indices = [v for k, v in actual_field_indices.items() if "departure" in k]
    for i in indices:
        prod *= valid_tickets[0][i]
    return prod


def main(filepath: str = "./data/raw/day16_sample.txt."):
    fields, tickets = get_data(filepath)
    sol_1 = calculate_solution_1(fields, tickets)
    print(f"Solution 1: {sol_1}")

    sol_2 = calculate_solution_2(fields, tickets)
    print(f"Solution 2: {sol_2}")


if __name__ == "__main__":
    main("./data/raw/day16_input.txt")
