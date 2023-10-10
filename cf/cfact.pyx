cpdef int factorial(int x):
    cdef int f = 1
    cdef int i

    for i in range(x):
        f *= (x - i)

    return f