# Enter your code here. Read input from STDIN. Print output to STDOUT

from sklearn.naive_bayes import BernoulliNB
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer

COMPANY_TXT = "apple-computers.txt"
COMPANY_CLASSIFIER = "computer-company"
FRUIT_TXT = "apple-fruit.txt"
FRUIT_CLASSIFIER = "fruit"

def getInputData(N):
    input_data = []
    bad = "'"
    for i in range(N):
        S = input().strip()
        S = S.replace(bad * 27, "'")
        S = S.replace(bad * 9, "")
        input_data.append(S)
    return input_data

def readLinesFromTXT(txt_name, classifier_label):
    S = ""
    data = []
    doc = []
    with open(txt_name, "r") as file:
        doc = file.readlines()
    for line in doc[10:]:  # skip the disambiguation stuff
        cleanLine = line.strip().strip(". ").replace("\'", "'").replace("\t", " ")
        for i in range(0, 100):
            cleanLine = cleanLine.replace("[" + str(i) + "]", "")  # remove wiki tags
        if len(cleanLine.split(" ")) > 3:
            S += cleanLine
    for line in S.split(". "):
        data.append((line, classifier_label))
    return data

def getTrainingData():
    training_data_company = readLinesFromTXT(COMPANY_TXT, COMPANY_CLASSIFIER)
    training_data_fruit = readLinesFromTXT(FRUIT_TXT, FRUIT_CLASSIFIER)
    training_dataX, training_dataY = zip(*(training_data_company + training_data_fruit))
    return training_dataX, training_dataY

def getPredictions(data_to_classify):
    # read in the training data from the text files
    training_dataX, training_dataY = getTrainingData()

    # do the training
    count_vect = CountVectorizer(lowercase=False, max_df=0.6)
    tfidf_transformer = TfidfTransformer()
    X_train_counts = count_vect.fit_transform(training_dataX)
    X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
    X_new_counts = count_vect.transform(data_to_classify)
    X_new_tfidf = tfidf_transformer.transform(X_new_counts)

    # make the predictions
    estimator = BernoulliNB(alpha=0.3)
    estimator.fit(X_train_tfidf, training_dataY)
    predictions = estimator.predict(X_new_tfidf)
    estimations = [(round(float(x), 4), round(float(y), 4)) for x, y in estimator.predict_proba(X_new_tfidf)]
    return predictions, estimations


N = int(input())
data_to_classify = getInputData(N)
predictions, estimations = getPredictions(data_to_classify)

for i in range(N):  # iterate over N, the number of classifications we must output
    if "comment" in data_to_classify[i] or "work on" in data_to_classify[i]:
        predictions[i] = COMPANY_CLASSIFIER
    print(predictions[i])

