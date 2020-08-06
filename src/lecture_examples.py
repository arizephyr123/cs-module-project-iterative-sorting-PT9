# more info/notes at https://github.com/LambdaSchool/CS-Wiki/wiki/Computing-Big-O

# linear O(n) time
animals = ['Duck', 'Jackal', 'Hippo', 'Aardvark', 'Cat', 'Flamingo', 'Iguana', 'Giraffe', 'Elephant', 'Bear']
def print_animals(animal_list):
    for i in range(len(animal_list)):
        print(animal_list[i])

# O(n)
animals = ['Duck', 'Jackal', 'Hippo', 'Aardvark', 'Cat', 'Flamingo', 'Iguana', 'Giraffe', 'Elephant', 'Bear']
def print_animals(animals):
    for i in range(len(animals)): 
        print(animal_list[i])      # O(n)
        my_number = 0
        for _ in range(10_0000):     # O(10_000) => O(c)
            my_number += 1


# polynomial O(n^2) time
# Print a list of all possible animal pairs
def print_animal_pairs():
    for animal_1 in animals:
        for animal_2 in animals:
            print (f"{animal_1} - {animal_2}")


# ??? runtime
def print_animal_triples():
    # O(n)
    for animal in animals:
        print(animal)
    # O(n^3)
    for animal_1 in animals:
        for animal_2 in animals:
            for animal_3 in animals:
                print (f"{animal_1} - {animal_2} - {animal_3}")



# logarithmic O(logn) time
# free all the animals, half at a time
# (remove them from the array)
def free_animals(animals):
    while len(animals) > 0:
        animals = animals[0: len(animals) // 2]

nums = [2, 6, 8, 3, 4, 1, 9, 5, 7]
def insert_sort(nums):
    # 1st element is a sorted list of [1]
    # loop through 'unsorted' remaining elements of list
    # compare first unsorted to each element on left (in sorted) until gets to 
    for i in range(1, len(nums)):
        # comparing
        temp = nums[i]
        #
        j = i
        # while 