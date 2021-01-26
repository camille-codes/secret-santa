import random
from random import shuffle

print('Welcome to Secret Santa!\n')
no_of_ppl = input('Enter number of participants: ')
int_no_ppl = int(no_of_ppl) #converts string to integer

print('Enter names of participants:')
#puts names of participants in a list
list_names = []
for i in range(int_no_ppl):
    list_names.append(input())

#copies list and assigns to new variable
list_randomized = list_names[:] 

#using Fisher-Yates algorithm
for i in range(len(list_randomized)-1, 0, -1):
    j = random.randint(0, i+1)
    list_randomized[i], list_randomized[j]= list_randomized[j], list_randomized[i]

input('Press Enter to begin shuffling...')

print('Now give your gift to your partner!')
list_partners = dict(zip(list_names, list_randomized))

    
# iterating list_partners dictionary
# prints dictionary into two columns
for k, v in list_partners.items():
    print(f'{k:<10} {v}')
