from hash_table import __version__
from hash_table.hash_table import HashTable
from hash_table.hashmap_repeated_word import hashmap_repeated_word
from hash_table.tree_intersection import tree_intersection
from hash_table.tree import BinaryTree
from hash_table.hashmap_left_join import left_join
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
    hashtable.add("renad", "23")
    actual = hashtable.get("renad")
    assert actual == expected


def test_retrieving_from_hash_table_based_on_key(hashtable):
    expected = "age"
    hashtable.add("person", "age")
    actual = hashtable.get("person")
    assert actual == expected


def test_retrieving_null_from_hash_table_based_on_non_exist_key(hashtable):
    with pytest.raises(KeyError):
        actual = hashtable.get("sth")


def test_handle_collision_on_hash_table(hashtable):
    expected = "30"
    hashtable.add("renad", "23")
    hashtable.add("renad", "30")
    actual = hashtable.get("renad")
    assert actual == expected


def test_retrieving_value_within_collision_on_hash_table(hashtable):
    expected = "30"
    hashtable.add("renad", "23")
    hashtable.add("renad", "30")
    actual = hashtable.get("renad")
    assert actual == expected

# ****************hashmap_repeated_word tests**************


def test_repeted_words_in_hashtable():
    expected = "summer"
    sentance = "It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York..."
    actual = hashmap_repeated_word(sentance)
    assert actual == expected


def test_repeted_words_in_hashtable():
    expected = "a"
    sentance = "Once upon a time, there was a brave princess who..."
    actual = hashmap_repeated_word(sentance)
    assert actual == expected


def test_repeted_words_in_hashtable():
    expected = "it"
    sentance = "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only..."
    actual = hashmap_repeated_word(sentance)
    assert actual == expected

# ****************tree insertion tests**************


def test_tree_insertion_happy_path():
    expected = [5, 3, 6]
    tree1 = BinaryTree()
    tree1.add(5)
    tree1.add(3)
    tree1.add(2)
    tree1.add(6)
    tree2 = BinaryTree()
    tree2.add(5)
    tree2.add(1)
    tree2.add(3)
    tree2.add(6)
    actual = tree_intersection(tree1, tree2)
    assert actual == expected


def test_tree_insertion_sad_path():
    expected = "there is no intersection between these trees"
    tree1 = BinaryTree()
    tree1.add(5)
    tree1.add(3)
    tree1.add(2)
    tree1.add(6)
    tree2 = BinaryTree()
    tree2.add(4)
    tree2.add(1)
    tree2.add(8)
    tree2.add(9)
    actual = tree_intersection(tree1, tree2)
    assert actual == expected


def test_tree_intersection_with_empty_trees():
    with pytest.raises(Exception):
        tree1 = BinaryTree()
        tree2 = BinaryTree()
        actual = tree_intersection(tree1, tree2)


def test_tree_intersection_with_first_tree_empty():
    with pytest.raises(Exception):
        tree1 = BinaryTree()
        tree1.add(5)
        tree1.add(3)
        tree1.add(2)
        tree1.add(6)
        tree2 = BinaryTree()
        actual = tree_intersection(tree1, tree2)


def test_tree_intersection_with_second_tree_empty():
    with pytest.raises(Exception):
        tree1 = BinaryTree()
        tree2 = BinaryTree()
        tree2.add(5)
        tree2.add(1)
        tree2.add(3)
        tree2.add(6)
        actual = tree_intersection(tree1, tree2)


# **************** hashmap list join tests *****************

def test_left_join_hashmap_happy_path():
    first_hash_table = HashTable()
    first_hash_table.add("person", "23")
    first_hash_table.add("person1", "30")
    first_hash_table.add("person2", "27")
    first_hash_table.add("person3", "18")
    first_hash_table.add("person4", "19")
    second_hash_table = HashTable()
    second_hash_table.add("person", "45")
    second_hash_table.add("person1", "25")
    second_hash_table.add("person2", "19")
    second_hash_table.add("person4", "9")

    expected = [
        ['person', '23', '45'],
        ['person1', '30', '25'],
        ['person2', '27', '19'],
        ['person3', '18', None],
        ['person4', '19', '9']
        ]
    actual = left_join(first_hash_table, second_hash_table)
    assert actual == expected

def test_left_join_hashmap_with_first_hashmap_empty():
    first_hash_table = HashTable()
    second_hash_table = HashTable()
    second_hash_table.add("person", "45")
    second_hash_table.add("person1", "25")
    second_hash_table.add("person2", "19")
    second_hash_table.add("person4", "9")

    expected = []

    actual = left_join(first_hash_table, second_hash_table)
    assert actual == expected

def test_left_join_hashmap_with_second_hashmap_empty():
    first_hash_table = HashTable()
    first_hash_table.add("person", "45")
    first_hash_table.add("person1", "25")
    first_hash_table.add("person2", "19")
    first_hash_table.add("person4", "9")
    second_hash_table = HashTable()

    expected = [
        ['person', '45', None],
        ['person1', '25', None],
        ['person2', '19', None],
        ['person4', '9', None]
        ]

    actual = left_join(first_hash_table, second_hash_table)
    assert actual == expected
def test_left_join_hashmap_with_hashmaps_empty():
        first_hash_table = HashTable()
        second_hash_table = HashTable()
        expected = []
        actual = left_join(first_hash_table, second_hash_table)
        assert actual == expected
