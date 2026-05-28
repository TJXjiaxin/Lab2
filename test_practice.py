import practice
import statistics

def test_find_longest_workout():
    result = practice.find_the_longest_workout(workouts)
    assert result["date"]=="25.01.2022"
    assert result["activity"] == "Cycling"
    assert result["duration"] == 75