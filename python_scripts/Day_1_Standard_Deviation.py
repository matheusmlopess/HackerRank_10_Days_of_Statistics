def stdDev(arr):
    avg = round(sum(arr)/len(arr),1)
    sum_sqrt_err = round (sum( [ pow((i-avg),2) for i in arr] ), 2)
    std = round(math.sqrt(sum_sqrt_err/len(arr)),1)
    print(std)

    
if __name__ == '__main__':
    n = int(input().strip())

    vals = list(map(int, input().rstrip().split()))

    stdDev(vals)
