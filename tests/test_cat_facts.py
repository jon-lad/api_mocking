from lib.cat_facts import CatFacts
from unittest.mock import Mock

'''
test provide returns a cat fact
'''
def test_provide_returns_a_cat_fact():
    requester_mock = Mock()
    requester_mock.get().json.return_value = {"fact":"Every year, nearly four million cats are eaten in Asia.","length":55}
    cat_facts = CatFacts(requester_mock)
    actual = cat_facts.provide()

    expected = "Cat fact: Every year, nearly four million cats are eaten in Asia."

    assert actual == expected