import math

def locomotiveAssignmentProblem(trains, distances):
    n = len(trains)
    m = len(distances)
    max_bit = 2**m - 1

    # Initialize C
    C = [[math.inf] * (max_bit+1) for i in range(n)]

    # Loop through each train i in the array of trains
    for i in range(n):
        # Initialize C[i][0] to 0
        C[i][0] = 0

        # Loop through each binary string j from 1 to 2^m - 1
        for j in range(1, max_bit+1):
            # Set C[i][j] to infinity
            C[i][j] = math.inf

            # Loop through each locomotive k in the binary string j
            for k in range(m):
                if (j & (1 << k)) != 0:
                    # Calculate the travel distance for assigning locomotive k to train i and add it to C[i][j - 2^(k-1)]
                    distance = distances[k]
                    C[i][j] = min(C[i][j], C[i][j - (1 << k)] + distance)

    # Initialize D
    D = [math.inf] * (max_bit+1)

    # Loop through each binary string j from 1 to 2^m - 1
    for j in range(1, max_bit+1):
        # Loop through each train i
        for i in range(n):
            # Set D[j] to the minimum of D[j] and C[i][j]
            D[j] = min(D[j], C[i][j])

    # Return D[2^m - 1] as the optimal total travel distance
    return D[max_bit]
