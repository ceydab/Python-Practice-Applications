#find prime numbers

i = 0
number = int(input('give a number: '))
allnumbers = list(range(2, number + 1))
nonprime = []

while i <= number:
   
    i += 1
    for x in range(2, i):
     
       if i % x == 0:
           nonprime.append(i)
           break
          
#print(nonprime)
#print(allnumbers)
primenumb = set(allnumbers) - set(nonprime)
#print(primenumb)
print(f'prime numbers: {primenumb}')


   
                
        
