# Input data
# 1: Conflict table
conflict_table = [
    {'sub_id': 100, 'Conflict_sub_id': 200, 'NumOfInterection': 30},
    {'sub_id': 100, 'Conflict_sub_id': 300, 'NumOfInterection': 15},
    {'sub_id': 200, 'Conflict_sub_id': 300, 'NumOfInterection': 20}
]

# 2: Academic level table
subject_levels = [
    {'sub_id': 100, 'level': 1},
    {'sub_id': 200, 'level': 2},
    {'sub_id': 300, 'level': 3}
]

# 3: Number of courses for each academic level
subjects_per_level = 6

# conditions
# 1:
# Function to enforce level order condition
def is_valid_schedule(schedule, levels):
    """Check if the schedule follows the level order condition."""
    return all(levels[schedule[i]] <= levels[schedule[i + 1]] for i in range(len(schedule) - 1))

# Generate an initial schedule that respects the level order condition
def generate_initial_schedule(subjects, levels):
    """Generate a valid initial schedule based on levels."""
    return sorted(subjects, key=lambda x: levels[x])

# 2:
# Function to calculate the cost (conflict penalties)
def calculate_cost(schedule, conflict_table):
    cost = 0
    for conflict in conflict_table:
        sub1_position = schedule.index(conflict['sub_id'])
        sub2_position = schedule.index(conflict['Conflict_sub_id'])
        # Add penalty if courses are scheduled on consecutive days
        if abs(sub1_position - sub2_position) <= 1:
            cost += conflict['NumOfInterection']
    return cost


# Execution of the program:
subjects = [subject['sub_id'] for subject in subject_levels]
levels = {subject['sub_id']: subject['level'] for subject in subject_levels}

# Generate a valid schedule
valid_schedule = generate_initial_schedule(subjects, levels)

# Calculate the cost for the valid schedule
final_cost = calculate_cost(valid_schedule, conflict_table)

# Display the results
print("Valid schedule following level order:", valid_schedule)
print("Final conflict cost:", final_cost)
