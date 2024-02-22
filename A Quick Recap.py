from math import sqrt


def pearson_correlation(X, Y):
    n = len(X)
    sum_X = sum(X)
    sum_Y = sum(Y)
    sum_X_sq = sum(x ** 2 for x in X)
    sum_Y_sq = sum(y ** 2 for y in Y)
    sum_XY = sum(x * y for x, y in zip(X, Y))

    numerator = n * sum_XY - sum_X * sum_Y
    denominator = sqrt((n * sum_X_sq - sum_X ** 2) * (n * sum_Y_sq - sum_Y ** 2))

    correlation = numerator / denominator
    return correlation


physics_scores = [15, 12, 8, 8, 7, 7, 7, 6, 5, 3]
history_scores = [10, 25, 17, 11, 13, 17, 20, 13, 9, 15]

correlation_coefficient = pearson_correlation(physics_scores, history_scores)
print("{:.3f}".format(correlation_coefficient))
