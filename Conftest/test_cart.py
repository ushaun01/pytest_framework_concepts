import pytest
#
# def test_add():                                     if autouse is used
#     print("add successfully")
#
# def test_remove():
#     print("remove successfully")

def test_add(tc_setup):                 #if autouse=true not used
    print("add successfully")

def test_remove(tc_setup):
    print("remove successfully")










