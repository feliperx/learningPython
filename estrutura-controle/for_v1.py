for i in range (1,11): 
    print(f'i = {i}') 

for j in range(10): # assume que o primeiro termo eh 0, indo de 0 ate 9
    print(f'j = {j}') 

print('\nTABUADA\n')

for x in range(1,10): # primeira contagem 
    for y in range(1,10): # segunda contagem, para cada x - 9y's
        print(f'{x} * {y} = {x*y}')   