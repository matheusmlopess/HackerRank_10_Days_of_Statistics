def weightedMean(X, W):

    prod_waited = [ valx * valw for valx, valw in zip(X,W) ]
    V_sum = sum(prod_waited)
    W_sum = sum(W)

    mean_waited = V_sum / W_sum
    #print(V_sum)
    #print(W_sum)
    print(round(mean_waited,1))

if __name__ == '__main__':

    int(input().strip())                                 #n = 5                                           

    vals = list(map(int, input().rstrip().split()))      #'10 40 30 50 20'
    
    weights = list(map(int, input().rstrip().split()))   #'1 2 3 4 5'
    
    weightedMean(vals, weights)                          #weightedMean(vals, weights)