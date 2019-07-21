# Given a string of round, curly, and square open and closing brackets,
# return whether the brackets are balanced (well-formed).

# For example, given the string "([])[]({})", you should return true.

# Given the string "([)]" or "((()", you should return false.


def pushpop_bracket(char, stack, bracket):
    # Push bracket into stack or pop bracket from stack

    bracketMap = {'(':')', '{':'}', '[':']'}
    # Push a bracket into the stack
    if char == bracket:
        stack.append(char)
    
    # Mirror the bracket and check if it can be popped out
    elif char == bracketMap[bracket]:
        if not len(stack) == 0:
            if stack[-1] == bracket:
                stack.pop()
            else:
                return False
        else:
            return False
    return True


def is_balanced(string):
    symbolStack = []
    bracketList = ['(', '{', '[']
    for char in string:
        for bracket in bracketList:
            if pushpop_bracket(char, symbolStack, bracket):
                continue
            else:
                return False
    if len(symbolStack) == 0:
        return True
    return False

# Driver code
string = "([])"
print(is_balanced(string))
string = "([)]"
print(is_balanced(string))
string = "((()"
print(is_balanced(string))
string = "([)]"
print(is_balanced(string))
string = "(([(])))"
print(is_balanced(string))
string = "(a3[[(3)](34)])"
print(is_balanced(string))
string = "()))"
print(is_balanced(string))