# Question 1
arr1 = [89, 52, 36, 24, 17, 99, 82, 73, 61, 48]  # 1
arr2 = [89, 52, 36, 24, 17, 99, 82, 73, 61, 48]  # 2
arr3 = [15, 13, 16, 12, 17, 11, 18, 10, 19, 9]  # 3

def odd_values(num, arr): 
    print(f'output for arr {num}: \n')
    for i in arr:
        if i%2 != 0:
            print(i)
    print('\nEnd of odd values\n\n')
    
arr = [arr1, arr2, arr3]
num = 1
for i in arr:
    odd_values(num, i)
    num += 1

# Question 2
arr1 = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]  # 1
arr2 = [17, 19, 15, 16, 14, 18, 13, 12, 11, 20]  #2
arr3 = [55, 66, 77, 88, 99, 11, 22, 33, 44]  #3


def sum_values(num, arr): 
    print(f'output for arr {num} : \n')
    total = 0
    for i in arr:
        total += i
    print('The sum/total of the given array is:', total)
    print('\nEnd of sum values\n\n')
    
arr = [arr1, arr2, arr3]
num = 1
for i in arr:
    sum_values(num, i)
    num += 1


# Question 3
arr1 = [-10, 20, -30, 40, -50, 60, -70, 80, -90, 100]  #1
arr2 = [5, -8, 13, -21, 34, -55, 89, -144, 233]  #2
arr3 = [-7, 12, -15, 18, -21, 24, -27, 30, -33]  #3
arr4 = [11, -22, 33, -44, 55, -66, 77, -88, 99]  #4
arr5 = [-3, 6, -9, 12, -15, 18, -21, 24, -27, 30]  #5


def converted_sum_values(
        num, arr):  
    print(f'output for arr {num} : \n')
    new_arr = []
    for i in arr:
        if i < 0:
            new_arr.append(i * (-1))
        else:
            new_arr.append(i)

    total = 0
    for i in new_arr:
        total += i

    print('The sum of the converted array is:', total)
    print('\nEnd of converted sum values')
    
arr = [arr1, arr2, arr3, arr4, arr5]
num = 1
for i in arr:
    converted_sum_values(num, i)
    num += 1


# Question 4
arr1 = ['apple', '', 'banana', '', 'cherry']  #1
arr2 = ['', 'dog', '', 'cat', '']  #2
arr3 = ['hello', '', 'world', '', '']  #3
arr4 = ['', '', '', '', '']  #4
arr5 = ['one', '', 'two', '', 'three']  #5
def empty_str(num, arr):  
    print(f'output for arr {num} : \n')
    new_arr = []
    for i in arr:
        if i != '':
            new_arr.append(i)

    print('The updated list is:', new_arr)

    print('\nEnd of empty str values')
    
arr = [arr1, arr2, arr3, arr4, arr5]
num = 1
for i in arr:
    empty_str(num, i)
    num += 1


# Question 5
arr1 = [11, -22, 33, -44, 55, -66, 77, -88, 99]

def list_min(arr):
    min_ele = arr[0]
    for i in range(1, len(arr)):
        if arr[i]<min_ele:
            min_ele = arr[i]
            
    print('The minimum element from the list is:', min_ele)

# Task 2 (50 Points)
class BankAccount:
    def __init__(self, account_number, balance, account_holder):
        self.account_number = account_number
        self.balance = balance
        self.account_holder = account_holder

    def deposit(self, amount):        
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self.balance

#part-2
class CheckingAccount(BankAccount):

    def __init__(self, account_number, balance, account_holder,
                 transaction_fees):
        super().__init__(account_number, balance, account_holder)
        self.transaction_fees = transaction_fees

    def apply_transaction_fees(self):
        self.balance -= self.transaction_fees

#Part-3
class SavingsAccount(BankAccount):

    def __init__(self, account_number, balance, account_holder, interest_rate):
        super().__init__(account_number, balance, account_holder)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest    


ba = BankAccount(12345, 1000, 'Rohit')

ba.deposit(200)

ba.withdraw(700)

print(ba.get_balance())


ca = CheckingAccount(12345, 1000, 'Rohit', 34.50)

ca.apply_transaction_fees()

print(ca.get_balance())


sa = SavingsAccount(12345, 1000, 'Rohit', 0.12)

sa.calculate_interest()

print(sa.get_balance())

# Rohith
# rm982
# 2/27/2023
