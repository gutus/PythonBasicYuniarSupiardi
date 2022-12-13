def Faktorial(A):
    if A < 1:
        return 1
    else:
        return A* Faktorial(A-1)

nilai = Faktorial(4)
print(nilai)