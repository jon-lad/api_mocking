from unittest.mock import Mock
from lib.time_error import TimeError

'''
Test error returns 0 if there is no time error
'''
def test_returns_0_if_no_difference():
    timer_mock = Mock()
    requester_mock = Mock()
    timer_mock.time.return_value = 1750245110
    requester_mock.get().json.return_value = {"utc_offset":"+01:00","timezone":"Europe/London","day_of_week":3,"day_of_year":169,"datetime":"2025-06-18T12:11:50.370098+01:00","utc_datetime":"2025-06-18T11:11:50.370098+00:00","unixtime":1750245110,"raw_offset":0,"week_number":25,"dst":True,"abbreviation":"BST","dst_offset":3600,"dst_from":"2025-03-30T01:00:00+00:00","dst_until":"2025-10-26T01:00:00+00:00","client_ip":"82.43.127.135"}

    time_error = TimeError(timer_mock, requester_mock)

    actual = time_error.error()

    expected = 0

    assert actual == expected

    '''
Test error returns differnce if there is a time error
'''
def test_returns_0_if_no_difference():
    timer_mock = Mock()
    requester_mock = Mock()
    timer_mock.time.return_value = 1750245111
    requester_mock.get().json.return_value = {"utc_offset":"+01:00","timezone":"Europe/London","day_of_week":3,"day_of_year":169,"datetime":"2025-06-18T12:11:50.370098+01:00","utc_datetime":"2025-06-18T11:11:50.370098+00:00","unixtime":1750245110,"raw_offset":0,"week_number":25,"dst":True,"abbreviation":"BST","dst_offset":3600,"dst_from":"2025-03-30T01:00:00+00:00","dst_until":"2025-10-26T01:00:00+00:00","client_ip":"82.43.127.135"}

    time_error = TimeError(timer_mock, requester_mock)

    actual = time_error.error()

    expected = -1

    assert actual == expected