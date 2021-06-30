# Enter your code here. Read input from STDIN. Print output to STDOUT

#X = int(input())
#N = input()

X = 10
N = '64630 11735 14216 99233 14470 4978 73429 38120 51135 67060'

Ns = map( int , N.split())
Nsortd = sorted(Ns)
rem_duplicates = sorted(list(set(Nsortd)))
mid = X//2 
dicT = { rem_duplicates[idx] : 0 for idx in range(len(rem_duplicates))}

# Mean 
avg = sum(Nsortd)/X

# Median operations
if X % 2 > 0:
    mean = Nsortd[ mid ]
else:
    mean = (Nsortd[mid]+Nsortd[mid -1])/2

# Mode operation
for i in Nsortd:
    if i in dicT:
        dicT[i] = dicT[i] + 1
        
mode = max(dicT, key=dicT.get)

print(avg)
print(mean)
print(mode)




