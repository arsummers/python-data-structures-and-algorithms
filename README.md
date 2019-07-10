## Author
    Aliya Summers
# Table of Contents

   challenge 01 - reverse array
        [link to first challenge](./challenges/array_reverse)


   challenge 02 - shift an array
        [link to second challenge](./challenges/array_shift)

   challenge 03 - binary search array
        [link to third challenge](./challenges/array_binary_search)

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
