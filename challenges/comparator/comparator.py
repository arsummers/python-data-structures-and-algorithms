"""
Comparators are used to compare two objects. In this challenge, you'll create a comparator and use it to sort an array. The Player class is provided in the editor below. It has two fields:

name: a string.
score: an integer.
Given an array of n Player objects, write a comparator that sorts them in order of decreasing score. if 2 or more players have the same score, sort those players alphabetically ascending by name. To do this, you must create a Checker class that implements the Comparator interface, then write an int compare(Player a, Player b) method implementing the Comparator.compare(T o1, T o2) method.

example:
input = [[Smith, 20], [Jones, 15], [Jones, 20]]
output = [[Jones, 20],[Smith, 20], [Jones, 15]]
"""

"""
works on a -1, 0, 1 scale to sort with comparators.

"""

class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score
        
    def comparator(a, b):
        if a.score != b.score:
            return b.score - a.score
        
        return (a.name > b.name) - (a.name < b.name)