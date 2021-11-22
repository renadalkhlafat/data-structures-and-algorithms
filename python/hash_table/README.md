# Hashtables
 is a data structure that implements an associative array abstract data type, a structure that can map keys to values

## Challenge
Implement a Hashtable Class with the following methods:

- add
- get
- contains
- hash

## Approach & Efficiency
- add
    + **time :**O(1)
    + **space :**O(1)
- get
    + **time :**O(n)
    + **space :**O(1)
- contains
    + **time :**O(n)
    + **space :**O(1)
- hash
    + **time :**O(n)
    + **space :**O(1)


## API
- add
    + Arguments: key, value
    + Returns: nothing
    + This method should hash the key, and add the key and value pair to the table, handling collisions as needed.
- get
    + Arguments: key
    + Returns: Value associated with that key in the table
- contains
    + Arguments: key
    + Returns: Boolean, indicating if the key exists in the table already.
- hash
    + Arguments: key
    + Returns: Index in the collection for that key
