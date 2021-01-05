# as https://www.w3schools.com/python/gloss_python_lists.asp

# List items are ordered, changeable, and allow duplicate values.
# List items are indexed, the first item has index [0], the second item has index [1] etc.

thislist = ["apple", "banana", "cherry"]
print(thislist)
print(len(thislist))

# It is also possible to use the list() constructor when creating a new list.

thislist = list(("apple", "banana", "cherry"))  # note the double round-brackets
print(thislist)

"""
Collections (Arrays) : are four collection data types in the Python programming language:
- List -- is a collection which is ordered and changeable. Allows duplicate members.
- Tuple -- is a collection which is ordered and unchangeable. Allows duplicate members.
- Set -- is a collection which is unordered and unindexed. No duplicate members.
- Dictionary -- is a collection which is unordered and changeable. No duplicate members.
"""
