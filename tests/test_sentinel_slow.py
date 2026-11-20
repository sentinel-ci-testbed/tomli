import time


def test_sentinel_slow():
    time.sleep(600)
    assert True
