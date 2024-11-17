# sets duplicates are not allowed
# numbersList = [1, 2, 3, 4, -1, -20]
# numbersList.pop()
#
# numbersSet = {1, 1}
# print(numbersList)  # we get [1, 2, 3, 4, -1, -20]
# #print(numbersSet)  # we get only {1}
# numbersSet.add(5)
# numbersSet.add(6)
# numbersSet.pop()
# print(numbersSet)
#
# lettersSet = {"A", "A", "B", "C", "C"}
# print(lettersSet)  # print out changes every time we run sets

# set union

lettersA = {"A", "B", "C", "D"}
lettersB = {"E", "F", "A", "D"}
difference = lettersA - lettersB   # find indexes that are only found in one of the set
union = lettersA | lettersB  # combine the two sets
intersection = lettersA & lettersB    # find indexes that are found in both sets
print(f"union: {union}")  # union: {'B', 'C', 'D', 'F', 'E', 'A'}
print(f"intersection: {intersection}")  # nothing to intersect between the two sets
print(f"difference: {difference}")


