from hash_table.hash_table import HashTable
import re


def hashmap_repeated_word(my_str):
    """
    finds the first word to occur more than once in a string

    input : str
    return : str
    """
    hash_table = HashTable()
    new_str = re.sub('[^A-Za-z ]+', '', my_str).split(" ")
    for word in new_str:
        word = word.lower()
        if hash_table.contains(word):
            return word
        hash_table.add(word,word)
