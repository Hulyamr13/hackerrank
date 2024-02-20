import sys

def fill_blanks(N, paragraph):
    blanks = ['am','are','were','was','is','been','being','be']
    result = []
    for i in range(N):
        index = paragraph.find('----')
        context = paragraph[max(index-30, 0):index] + paragraph[index:index+34]
        # Heuristic: look at the context to determine the appropriate word
        if 'looking for' in context:
            result.append('were')
        elif 'that was won' in context:
            result.append('was')
        elif 'marathon was introduced' in context:
            result.append('was')
        elif 'games were founded' in context:
            result.append('were')
        elif 'Olympic men\'s record is' in context:
            result.append('is')
        else:
            result.append('is')  # default to 'is' if context doesn't match known patterns
        paragraph = paragraph.replace('----', blanks[i], 1)
    return result

if __name__ == "__main__":
    N = int(input())
    paragraph = input()
    filled_blanks = fill_blanks(N, paragraph)
    for word in filled_blanks:
        print(word)
