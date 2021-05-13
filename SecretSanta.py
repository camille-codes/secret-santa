import random
from random import shuffle
from random import randrange

print('Welcome to Secret Santa!\n')

no_of_ppl = input('Enter number of participants: ')

int_no_ppl = int(no_of_ppl) #converts string to integer

print('Enter names of participants:')

#puts names of participants in a list
list_names = []
for i in range(int_no_ppl):
    list_names.append(input())

list_randomized = list_names[:] 

#assigns each entrant with a partner
def secretSanta(list_randomized):
    i = len(list_randomized)
    while i > 1:
        i = i - 1
        j = randrange(i)  # 0 <= j <= i-1
        list_randomized[j], list_randomized[i] = list_randomized[i], list_randomized[j]
    return list_randomized

list_satollo = secretSanta(list_randomized)

input('Press Enter to begin shuffling...')

print('Now give your gift to your partner!')

#combines two lists into a dictionary
list_partners = dict(zip(list_names, list_satollo))
    
#iterating list_partners dictionary so that two columns show
for k, v in list_partners.items():
    print(f'{k:<10} --> {v}')
