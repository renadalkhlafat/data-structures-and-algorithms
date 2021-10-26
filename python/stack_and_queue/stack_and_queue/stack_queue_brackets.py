def validate_brackets(input):

    """
    Function that represent whether or not the brackets in the string are balanced

    Arguments: string
    Return: boolean
    """
    openning_list = ["{","[","("]
    closing_list = ["}","]",")"]
    bracket_stack = []

    for i in input:
        if i in openning_list:
            bracket_stack.append(i)
        elif i in closing_list:
            index = closing_list.index(i)
            if bracket_stack and (openning_list[index] == bracket_stack[len(bracket_stack)-1]) :
                bracket_stack.pop()
            else :
                False
    if not bracket_stack :
        return True
    else:
        return False

# print(validate_brackets("{}"))
# print(validate_brackets("{}(){}"))
# print(validate_brackets("()[[Extra Characters]]"))
# print(validate_brackets("(){}[[]]"))
# print(validate_brackets("{}{Code}[Fellows](())"))
# print(validate_brackets("[({}]"))
# print(validate_brackets("(]("))
# print(validate_brackets("{(})"))
