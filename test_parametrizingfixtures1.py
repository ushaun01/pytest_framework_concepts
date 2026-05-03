#used to iterate test function number of times
import pytest

# @pytest.fixture(params=["a","b"])
# def demo_fixture(request):
#     print(request.param)
#
# def testLogin(demo_fixture):
#     print("Successfully Login")

@pytest.mark.parametrize("a,b,final",[(2,6,8),(5,18,52),(12,52,35)])
def testLogin(a,b,final):
    assert a+b==final
# # def testLogoff():
#     print("Logout successful")
#
# def testCal():
#     assert  2+2==4