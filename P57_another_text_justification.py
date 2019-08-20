# Given a string s and an integer k, break up the string into multiple lines
# such that each line has a length of k or less. You must break it up so that
# words don't break across lines. Each line has to have the maximum possible
# amount of words. If there's no way to break the text up, then return null.

# You can assume that there are no spaces at the ends of the string and that
# there is exactly one space between each word.

# For example, given the string "the quick brown fox jumps over the lazy dog" and k = 10,
# you should return: ["the quick", "brown fox", "jumps over", "the lazy", "dog"].
# No string in the list has a length of more than 10.


def justify_text(string, k):
    return_list = []
    word_list = string.split(' ')

    for index, word in enumerate(word_list):
        if index == 0 or len(return_list[-1]) + len(word) + 1 > k:
            return_list.append(word)
            
        else:
            return_list[-1] += " " + word

    return return_list


# Driver code
string = 'the quick brown fox jumps over the lazy dog'
k = 10
result = justify_text(string, k)
print(result)
