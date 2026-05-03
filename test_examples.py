import pytest

#example 1
def fun(x):
    return x+5
def testM1():
    assert fun(3)==8

#example 2: Multiple tests at a time

#@pytest.mark.skip                   #skip function-it skips method  if we do not want to execute it is skipped
def test_answer1():
    a=5
    b=10
    assert a==b

#@pytest.mark.xfail         #even it fail it will not fail in report.it will execute as x-failed
def test_answer2():
    c=15
    d=3*9
    assert c==d