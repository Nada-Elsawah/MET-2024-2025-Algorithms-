import itertools

def parse_input(conflicts, levels, subjects_per_level):
    conflict_dict = {}
    for sub_id, conflict_sub_id, num_of_intersections in conflicts:
        conflict_dict[(sub_id, conflict_sub_id)] = num_of_intersections

    level_dict = {}
    for sub_id, level in levels:
        if level not in level_dict:
            level_dict[level] = []
        level_dict[level].append(sub_id)

    return conflict_dict, level_dict

def generate_schedule(level_dict, pattern):
    schedule = []
    level_queues = {level: iter(level_dict[level]) for level in pattern}

    while any(level_queues.values()):
        for level in pattern:
            try:
                schedule.append(next(level_queues[level]))
            except StopIteration:
                continue

    return schedule

def calculate_cost(schedule, conflict_dict):
    total_cost = 0
    for day in range(len(schedule)):
        for i, j in itertools.combinations(schedule[day:day+1], 2):
            total_cost += conflict_dict.get((i, j), 0) + conflict_dict.get((j, i), 0)

    return total_cost

def find_best_schedule(conflicts, levels, subjects_per_level):
    conflict_dict, level_dict = parse_input(conflicts, levels, subjects_per_level)
    patterns = [[1, 3, 2], [3, 1, 2]]

    best_schedule = None
    best_cost = float('inf')

    for pattern in patterns:
        schedule = generate_schedule(level_dict, pattern)
        cost = calculate_cost(schedule, conflict_dict)
        if cost < best_cost:
            best_schedule = schedule
            best_cost = cost

    return best_schedule, best_cost

conflicts = [
    ("M1", "M2", 3),
    ("M1", "M3", 2),
    ("M2", "M3", 1),
]

levels = [
    ("M1", 1),
    ("M2", 2),
    ("M3", 3),
]

subjects_per_level = {
    1: 1,
    2: 1,
    3: 1,
}

best_schedule, best_cost = find_best_schedule(conflicts, levels, subjects_per_level)
print("Best Schedule:", best_schedule)
print("Minimum Cost:", best_cost)
