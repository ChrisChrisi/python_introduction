import math


def equation(x):
    result = (-5 * (x ** 5) + 69 * (x * x) - 47)
    return result


print "x: 0", equation(0)
print "x: 1", equation(1)
print "x: 2", equation(2)
print "x: 3", equation(3)


def future_value(present_value, annual_rate, periods_per_year, years):
    rate_per_period = annual_rate / periods_per_year
    periods = periods_per_year * years

    return present_value * ((1 + rate_per_period) ** periods)
    # Put your code here.


print "$1000 at 2% compounded daily for 3 years yields $", future_value(1000, .02, 365, 3)


def poly_area(count, length):
    result = ((1.0 / 4.0) * count * length * length) / (math.tan(math.pi / count))

    return result


print poly_area(7, 3)


def max_of_2(a, b):
    if a > b:
        return a
    else:
        return b


def max_of_3(a, b, c):
    return max_of_2(a, max_of_2(b, c))


def project_to_distance(point_x, point_y, distance):
    dist_to_origin = math.sqrt(point_x ** 2 + point_y ** 2)
    scale = distance / dist_to_origin
    print point_x * scale, point_y * scale


project_to_distance(2, 7, 4)
