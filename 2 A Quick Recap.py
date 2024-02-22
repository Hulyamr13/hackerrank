# Enter your code here. Read input from STDIN. Print output to STDOUT


from math import sqrt

def calculate_slope(X, Y):
    n = len(X)
    mean_X = sum(X) / n
    mean_Y = sum(Y) / n

    cov_XY = sum((x - mean_X) * (y - mean_Y) for x, y in zip(X, Y))
    var_X = sum((x - mean_X)**2 for x in X)

    slope = cov_XY / var_X
    return slope

physics_scores = [15, 12, 8, 8, 7, 7, 7, 6, 5, 3]
history_scores = [10, 25, 17, 11, 13, 17, 20, 13, 9, 15]

slope = calculate_slope(physics_scores, history_scores)
print("{:.3f}".format(slope))
