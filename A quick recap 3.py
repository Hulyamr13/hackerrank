def calculate_slope(X, Y):
    n = len(X)
    sum_X = sum(X)
    sum_Y = sum(Y)
    sum_XY = sum(x * y for x, y in zip(X, Y))
    sum_X_sq = sum(x ** 2 for x in X)
    slope = (n * sum_XY - sum_X * sum_Y) / (n * sum_X_sq - sum_X ** 2)
    return slope

def calculate_intercept(X, Y, slope):
    mean_X = sum(X) / len(X)
    mean_Y = sum(Y) / len(Y)
    intercept = mean_Y - slope * mean_X
    return intercept

def predict_score(physics_score, slope, intercept):
    return intercept + slope * physics_score

physics_scores = [15, 12, 8, 8, 7, 7, 7, 6, 5, 3]
history_scores = [10, 25, 17, 11, 13, 17, 20, 13, 9, 15]

slope = calculate_slope(physics_scores, history_scores)
intercept = calculate_intercept(physics_scores, history_scores, slope)

physics_score = 10
predicted_history_score = predict_score(physics_score, slope, intercept)
print("{:.1f}".format(predicted_history_score))
