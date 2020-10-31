from LSR import ListSearchReplace as LSR

a = [
    [1, 2, 3, 4],
    [5, 6, 7, 8]
]

b = ["These", "are", "words"]

c = [
    ["Even", "more"],
    ["word"],
    ["like", "yeah", "this is"],
    ["cool"]
]

# Working with list a
# Creating instances of LSR. Refer to documentation for what arguments it accepts.
L1 = LSR(a, True)
L2 = LSR(b)
L3 = LSR(c, True)

ia, ib = L1.search(6)
L1.replace(6, 8888)
print(f"Index: {ia}, and {ib}\nOutput: {a[ia][ib]}")
"""
First you search for the index of 6 then unpack it with ia and ib. Then replace 6 with 8888.

The reason why I don't use the search function on the integer 8888, is because typing 6 is faster than 8888.

Furthermore since you're changing the value of the element in that specific index, you can use that to access 8888 in the list.

Console output:
Index: 1, and 1
Output: 8888
"""

L1.typecast('str')
print(a)

"""
Output: [['1', '2', '3', '4'], ['5', '8888', '7', '8']]
When using the list beyond this typecast method, the list will the type specified in the typecast method
"""

# Working with list b
ia, ib = L2.search("Even")
L2.replace("These", "Somebody once told me")
print(b[ia][ib])

# To show that this works with different sizes of nested lists
ia, ib = L2.search("words")
L2.replace("words", "Even more words")
print(b[ia][ib])

# typecasting does not work unless you replace every single element with a number, then typecasting it. To an integer.

# Working with list c, pretty much the same as b but it's just a nested list.
ia, ib = L3.search("cool")
L2.replace("cool", "More test wording")
print(c[ia][ib])
