# Write an algorithm to justify text. Given a sequence of words and an integer
# line length k, return a list of strings which represents each line, fully justified.

# More specifically, you should have as many words as possible in each line.
# There should be at least one space between each word. Pad extra spaces when
# necessary so that each line has exactly length k. Spaces should be distributed
# as equally as possible, with the extra spaces, if any, distributed starting
# from the left.

# If you can only fit one word on a line, then you should pad the right-hand
# side with spaces.

# Each word is guaranteed not to be longer than k.

# For example, given the list of words
# ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
# and k = 16, you should return the following:

# ["the  quick brown", # 1 extra space on the left
# "fox  jumps  over", # 2 extra spaces distributed evenly
# "the   lazy   dog"] # 4 extra spaces distributed evenly

def justify_text(wordList, k):
    wordList.append(k * '0')

    returnLines = []
    line = []
    lineWordCount = 0
    for word in wordList:
        if len(word) + lineWordCount <= k:
            line.append(word)
            lineWordCount += len(word) + 1
        else:
            lineWordCount -= 1
            if lineWordCount == k:
                returnLines.append(' '.join(line))
            elif lineWordCount < k:
                missing = k - lineWordCount
                numSpaces = len(line) - 1
                if missing % numSpaces == 0:
                    returnLines.append(((1 + (int(missing / numSpaces)))*' ').join(line) )
                else:
                    line[0] += ' '
                    missing -= 1
                    if missing == 0:
                        returnLines.append(' '.join(line))
                    elif missing > 0:
                        returnLines.append(((1 + (int(missing / numSpaces)))*' ').join(line) )
            line = []
            lineWordCount = 0

            line.append(word)
            lineWordCount += len(word) + 1
    print("\n".join(returnLines))


# Driver code
wordList = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
k = 16
justify_text(wordList, k)

wordList = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
k = 8
justify_text(wordList, k)