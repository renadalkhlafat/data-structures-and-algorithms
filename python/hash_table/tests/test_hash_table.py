from hash_table import __version__
from hash_table.hash_table import HashTable
import pytest


def test_version():
    assert __version__ == '0.1.0'


@pytest.fixture
def hashtable():
	return HashTable()


def test_hash(hashtable):
	expected = 700
	actual = hashtable._HashTable__hash("d")
	assert actual == expected


def test_hash_word(hashtable):
	expected = 376
	actual = hashtable._HashTable__hash("dd")
	assert actual == expected


def test_add_to_hash_table(hashtable):
    expected = "23"
    hashtable.add("renad","23")
    actual = hashtable.get("renad")
    assert actual == expected
