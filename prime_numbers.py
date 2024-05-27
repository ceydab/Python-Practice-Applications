'''this project is a simple application of python for listing prime numbers. the projects gets a number as an input
and through a while loop, it calculated modulus of each number up until the input number, and lists the numbers as 
prime numbers if they have modulus 0 for as least one value other than zero and themselves. 
'''

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


   
                
        
