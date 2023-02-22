def solution(A, K):
    n = len(A)
    for i in xrange(n - 1):
        if (A[i] != A[i + 1] and A[i] + 1 != A[i + 1]):
            return False
    if (A[0] != 1 or A[n - 1] != K):
        return False
    else:
        return True
