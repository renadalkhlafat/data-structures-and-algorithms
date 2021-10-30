from stack_and_queue.stack_queue_brackets import validate_brackets

def test_case_1():
    assert validate_brackets("{}") == True

def test_case_2():
    assert validate_brackets("{}(){}") == True

def test_case_3():
    assert validate_brackets("()[[Extra Characters]]") == True

def test_case_4():
    assert validate_brackets("(){}[[]]") == True

def test_case_5():
    assert validate_brackets("(](") == False

def test_case_6():
    assert validate_brackets("{(})") == False

