workouts = [
    {"name": "Run", "duration": 30, "calories": 300},
    {"name": "Swim", "duration": 45, "calories": 400},
    {"name": "Cycle", "duration": 60, "calories": 500},
    {"name": "Yoga", "duration": 20, "calories": 100}
]

def find_the_longest_workout(workouts):

    longest = None

    if len(workouts) == 0:
        return None
    longest = workouts[0]
    for workout in workouts:
        if workout["duration"] > longest["duration"]:
            longest = workout

    return longest



