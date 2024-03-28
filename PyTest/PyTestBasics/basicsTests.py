
def test_passing():
    assert (1, 2, 3) == (1, 2, 3)

def test_failing():
    assert (1, 2, 3) == (3, 2, 1)

'''
• Test files should be named test_<something>.py or <something>_test.py.
• Test methods and functions should be named test_<something>.
• Test classes should be named Test<Something>.
'''

if __name__ == '__main__':
    # run in the terminal pytest basicsTests.py -v to get more info
    test_passing()
    test_failing()
