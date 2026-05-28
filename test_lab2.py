import Lab2
import statistics
def test_find_min_max():
    test_data =[20,19,18,16,17]
    assert(Lab2.calc_min_max_temperature(test_data)==16,20)

def test_calc_average():
    test_data = [20,21,22,23,24]
    assert(Lab2.calc_average_temperature(test_data)==statistics.mean(test_data))

def test_calc_median_temperature():
 test_data=[21,19,18,16,17]
 assert(Lab2.calc_median_temperature(test_data)==statistics.median(test_data))