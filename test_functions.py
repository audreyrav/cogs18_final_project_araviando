"""Test for my functions.

Note: I was not sure about how to test my functions, so I mostly called them.
"""

from functions import cd_screener, question1, question2, question3, question4, question5, question6, result, get_help

def test_cd_screener():

    assert callable(cd_screener)

def test_question1():

    assert callable(question1)
    assert type(q1) is int, "q1 must be an integer"
    
def test_question2():

    assert callable(question2)
    assert type(q2) is int, "q2 must be an integer"
    
def test_question3():

    assert callable(question3)
    assert type(q3) is int, "q3 must be an integer"
    
def test_question4():

    assert callable(question4)
    assert type(q4) is int, "q4 must be an integer"
    
def test_question5():

    assert callable(question5)
    assert type(q5) is int, "q5 must be an integer"
    
def test_question6():

    assert callable(question6)
    assert type(q6) is int, "q6 must be an integer"
    
def test_result():

    assert callable(result)
    assert type(num) is int, 
    
def test_get_help():

    assert callable(get_help)