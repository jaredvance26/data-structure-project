class Stacks():
    def __init__(self):
        self.stack = []
    
    def add(self,number):
        # This function will add one item to the stack
        pass

    def remove(self):
        # This function will remove one item from the stack
        pass

    def get_length(self): 
        # This function will return how many items are in the stack
        pass


#                         TESTS

# ---------------------------------------------------------------
print('------------------------')
print('TEST 1')
nums = Stacks()
nums.stack = []

nums.add(1)
nums.add(2)
nums.add(3)
nums.add(4)
nums.add(5)

print()
print('Answer: ')

print(nums.stack) # Answer: [1,2,3,4,5]
print('------------------------\n')



print('------------------------')
print('TEST 2')

nums.remove()
nums.remove()

print()
print('Answer:')

print(nums.stack) # Answer: [1,2,3]


print('------------------------\n')

print('------------------------')
print('TEST 3')
print()

nums.add(4)
nums.add(5)
nums.add(6)

print('Answer: ')
print(nums.get_length()) # Answer: 6
print('------------------------')