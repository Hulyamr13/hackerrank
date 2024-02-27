from operator import itemgetter

def clean(text):
    # Remove unwanted words and characters
    text = text.replace(" this ", " ").replace("this ", "").replace(" and ", " ").replace("and ", "").replace(" the ", " ").replace("the ", "").replace(" that ", " ").replace("that ", "").replace(" to ", " ").replace("to ", "").replace(" are ", " ").replace("are ", "").replace(" of ", " ").replace("what", " ").replace("which", " ").replace("when", " ").replace(" is ", " ").replace("is ", "").replace(" be ", " ").replace("be ", "").replace("?", "").replace(",", "").replace(" by ", " ").replace("by ", "").strip()
    return text

def closest(a, b):
    # Find the number of common words between two strings
    a = a.split(" ")
    a_ = [w.replace("s", "") for w in a]
    b = b.split(" ")
    b_ = [w.replace("s", "") for w in b]
    c = set(a_) & set(b_)
    return len(c)

def getline(text, ratio_i, notin):
    # Get the line from text with highest matching ratio
    ratio_i = sorted(ratio_i, key=itemgetter(0), reverse=True)
    line = None
    i = 0
    while line is None:
        if text[int(ratio_i[i][1])] not in notin:
            line = text[int(ratio_i[i][1])]
        i += 1
    return line.lower()

def solve_problem():
    # Read the paragraph of text
    text = input().lower()
    text = clean(text)
    text = text.split(". ")

    # Read the 5 questions
    questions = [input().lower() for _ in range(5)]
    questions = [clean(q) for q in questions]

    # Read the jumbled answers
    answers = input().lower().split(";")
    answers_ = answers.copy()

    # Iterate over each question
    for item in questions:
        words = clean(item)
        ratio_i = []
        i = 0
        # Calculate the matching ratio for each line in text
        for line in text:
            ratio_i.append([closest(words, line), i])
            i += 1

        notin = []
        closest_ans = []
        maxim = None
        # Find the answer with highest matching ratio
        while maxim is None and len(ratio_i) != len(notin):
            line = getline(text, ratio_i, notin)
            for i in range(len(answers_)):
                clean_ans = clean(answers_[i])
                closest_ans.append([closest(clean_ans, line), i])
                if clean_ans in line:
                    maxim = i
            notin.append(line)

        if maxim is None:
            closest_ans = sorted(closest_ans, key=itemgetter(0), reverse=True)
            maxim = closest_ans[0][1]

        # Print the answer and remove it from the list
        print(answers.pop(maxim))
        answers_.pop(maxim)

if __name__ == "__main__":
    solve_problem()
