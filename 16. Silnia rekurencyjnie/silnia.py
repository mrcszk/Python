def sil(n):
    if n>=2:
        return sil(n-1) * n
    else:
        return 1




print(sil(9))