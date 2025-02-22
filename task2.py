import random

def get_numbers_ticket(min, max, quantity):
    if min < 1 or max > 1000 or quantity > (max - min + 1):
        print('ERROR: Min must be more than 1! Max must be less than 1000')
        return
    
    numbers = random.sample(range(min, max + 1), quantity)
    numbers.sort()
    
    return numbers

lottery_numbers = get_numbers_ticket(0, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)