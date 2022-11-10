from types import NoneType
from esteem import ask, question_is_positive, what_result
import pytest


# def test_ask():
#     answer = ask('How old are you? ')
#     assert type(answer) == int

def test_question_is_positive():
    for number in (1,2,4,6,7):
        assert question_is_positive(number) == True
    for number in (3,5,8,9,10):
        assert question_is_positive(number) == False

def test_what_result():
    assert what_result(25) == 'Looks good! You have very high self-esteem.'
    assert what_result(20) == 'You got this! Keep working on yourself. I believe in you!'
    assert what_result(15) == 'You could use some improvement in this area. No worries! Start small - you can do it!'
    assert what_result(10) == 'You really are just a cotton-headed ninnymuggins.'
    assert what_result(5) == 'Looks like you have low self-esteem. Remember that God loves you no matter what! He will help you succeed!'



pytest.main(["-v", "--tb=line", "-rN", __file__])