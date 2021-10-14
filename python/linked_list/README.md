# Singly Linked List
A Linked List is a sequence of Nodes that are connected/linked to each other ,and the Singly linked list means that there is only one reference, and the reference points to the Next node in a linked list.

## Challenge
Implement the Linked list data structure that can Insert nodes and search for spesific node data and print out the linked list data

## Approach & Efficiency
I use classes to implement for linked list ,first class for Node that take the node data and the pointer for the next node ,the second class for the linked list it self that contains three methods ,the insert method , contains or includes method and to_string method that print out the linked list data

## API

| Method | Summary | Big O Time | Big O Space | Example |
| :----------- | :----------- | :-------------: | :-------------: | :----------- |
| Insert | Adds a new `Node` to the `Linked List` | O(1) | O(1) | myList.Insert(99) |
| Includes | Takes in a value and returns a boolean depending on if the value is in the `LinkedList` | O(n) | O(1) | myList.Includes(99) |
| Print | Prints the `Linked List` to the console | O(n) | O(1) | myList.Print() |


## Change Log

1.1: *build and test linked list* - 14 OCt 2021
