## Author
    Aliya Summers
# Table of Contents

   challenge 01 - reverse array
        [link to first challenge](./challenges/array_reverse)


   challenge 02 - shift an array
        [link to second challenge](./challenges/array_shift)

   challenge 03 - binary search array
        [link to third challenge](./challenges/array_binary_search)

   challenge 05 - singly linked list
        [link to fifth challenge](./data-structures/linked_list)

   challenge 06 - linked list insertions
        [link to sixth challenge](./data-structures/linked_list)

   challenge 07 - linked list kth value from end
        [link to seventh challenge](./data-structures/linked_list)

   challenge 08 - linked list - merge/zip list
        [link to seventh challenge](./data-structures/linked_list)

   challenge 10 - stacks and queues
     

# Reverse an Array
We were given instructions to write a function that will reverse a list or array.

Tammy Do, my partner for this challenge, helped me figure out the syntax of writing the function after I started testing my solution.

## Challenge
The challenge was to reverse an array. We had example input and output.

## Approach & Efficiency
I took what I saw at the shortest approach, and sliced the array one step at a time from back to front, so that it will reverse when printed. I may be wrong, but I believe this operates at O(1). 

## Solution
![whiteboarding solution for reverse](./assets/array_reverse.jpg)



# Insert and Shift an Array
The instructions were to write a function that accepts an array/list and a value, and insert that value into the midpoint of the array.

Richard von Hagel was my partner for this challenge. He provided a few suggestions while I whiteboarded, and was helpful in talking through my solution.

## Challenge
I had to insert a value (in this case I used the number 7 across the board), into an array at the halfway point, and return the modified array. I wrote tests to see if the function worked.

## Approach & Efficiency
I utilized if/elif statements and integer division to verify my desired input. I then used Python's split function to modify and reconnect my arrays.

## Solution
![whiteboarding solution for array shift](./assets/array_shift.jpg)


# Array Binary Search
Write a function that finds the given key value in an array by accessing various points in the array until it hits.


## Challenge
Write a function that takes in a list and a value. It should search for the value in the list, and return the index number of that value. If the value does not exist, return -1. Do not use python's built-in functions (like index()) to solve this.

## Approach & Efficiency

My whiteboarding partner for this lab was Tammy Do. We discussed approaches with each other for each of our whiteboarding turns.

After puzzling over this, we consulted the ![wikipedia page](https://en.wikipedia.org/wiki/Binary_search_algorithm) provided in the assignment.
## Solution
![whiteboarding solution for array binary search](./assets/array_binary_search.jpg)

# Singly Linked List
Create and write some methods for a singly linked list


## Challenge
Create a Node class and a LinkedList class. Write a function that adds values onto nodes in the list, checks to see if other values exists on nodes in the list, and returns the value of the list in string form.

## Approach & Efficiency

I started by writing some of my tests and modeling them after the class demo on linked lists. I wrote tests, built parts of the app to pass the tests, then wrote more tests, et cetera. Found the algorithm for the includes_val function from ![Geeks for Geeks](https://www.geeksforgeeks.org/search-an-element-in-a-linked-list-iterative-and-recursive/). TA Evy also helped me conceptualize it. Joshua Ho helped guide me on the right path with the __str__ function.

I found my list of animals to pull from for my tests ![here](https://en.wikipedia.org/wiki/List_of_carnivorans_by_population)

I am still learning big O notation, but I believe this runs ar O(N)

## API

insert() adds a node with a given value to the beginning of the linked list. It also allows adding multiple nodes at once.

includes_val() checks against a given term, to see if it exists as a value on any node in the linked list. I adapted the name from just being includes(), so as to avoid accidentally invoking python's built-in .includes() method.

__str__() converts the values of the linked list into a readable string, so it can be compared and tested against.


# Linked List - Insertion Methods
Create and write some methods to insert values are various places in a singly linked list


## Challenge
Create a Node class and a LinkedList class. Write functions that add values to the end of the list, before and after a given point in the middle of the list, and into an empty list

## Approach & Efficiency

I worked off my previously written insert function to start building my lists to work with. My append function is working well. I tried a few different ways to write the functions that access a value, and add a node either before or after the given value, but no luck yet. I sought assistance from James my TA, and JB, my instructor, as well as this ![Geeks for Geeks](https://www.geeksforgeeks.org/linked-list-set-2-inserting-a-node/) page.


## Solution

![whiteboarding solution for reverse](./assets/ll_insertions.jpg)

# Linked List - Kth from end
A method that returns the value of a node a given number of spaces from the end of a linked list


## Challenge
Create a method for the linked list that takes in a number, k, and finds the value of the node that is that many from the end. As an example, 0 from the end would just be the end of the list.

## Approach & Efficiency

Worked off of previously written linked list code. Started with some counters and two while loops. The first while loop calculated the length of the entire linked list. The second while loop used the values from the first to calculate where to end the loop and return the correct value. Whiteboarding sample does not include edge cases.


## Solution

![whiteboarding solution for reverse](./assets/ll_kth_from_end.jpg)

# Linked List - Merged List
A method that takes two linked lists and merges them together, returning the head of the modified list

## Challenge
A method that takes two linked lists and merges them together, returning the head of the modified list


## Approach & Efficiency

Worked off of previously written linked list code. Tried to switch around the head and next values of the two lists, but that didn't work, so I consulted ![Geeks for Geeks](https://www.geeksforgeeks.org/merge-a-linked-list-into-another-linked-list-at-alternate-positions/)

I'm still not sure the list is actually merging, or how to incorpate the second list.


## Solution

![whiteboarding solution for reverse](./assets/ll_merged_list.jpg)

# Stacks and Queues
Create a stack and a queue from a Linked List, and write the basic functions to read and navigate them.


## Challenge
Create a Node class,  LinkedList class, a Stack class, and a Queue class. Write a functions that insert values into the Stack and Queue, examine the first ones in the list, and remove values

## Approach & Efficiency

I wrote my base Node and Linked List class after the demos from lecture. My Stack functions most rely on information from class, and ![here](https://www.koderdojo.com/blog/coding-a-stack-abstract-data-structure-using-linked-list-in-python). I learned how to write my Queues functions from ![here](https://www.geeksforgeeks.org/queue-set-2-linked-list-implementation/)


These should run at O(N)

## API

Stacks are First In, Last Out. Peek() views the top node in the stack. Pop() removes nodes from the stack. Push() adds nodes to the stack.

Queues are First In, First Out. Like Peek() for Stacks, Peek() for Queues views the first node. Enqueue adds a node to the queue. Dequeue removes nodes.

# Stacks and Queues - Queue of Two Stacks
Create a pseudo queue class using two stacks

## Challenge
use the pop, push, and peek functions in a stack class to create an enqueue and dequeue function


## Approach & Efficiency
refactored and rewrote stack functions from ![koderdojo](https://www.koderdojo.com/blog/coding-a-stack-abstract-data-structure-using-linked-list-in-python)
Skyler Burger helped explain pytest fixtures to me a couple days ago. I am using them here.
Still need to refactor dequeue until it works as it should. Right now, the second stack isn't refilling with the stuff I popped from the first stack


## Solution

![whiteboarding solution for stack queue](./assets/pseudo_queue.jpg)