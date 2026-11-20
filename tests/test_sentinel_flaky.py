import random


def test_sentinel_flaky():
    # fails about 60% of runs, with no code change
    assert random.random() > 0.6
