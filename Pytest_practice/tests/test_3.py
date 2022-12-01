# Check if number is even

num = 2


class Even:
    def __init__(self, num):
        self.num = num


def test_check_even(num):
    assert num % 2 == 0, "value was odd, should be even"
