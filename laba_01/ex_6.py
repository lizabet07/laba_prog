N = int(input())
och = []
zaoch = []
while N > 0:
    fio = input()
    N = N - 1
    if 'True' in fio:
        och.append(fio)
    elif 'False' in fio:
        zaoch.append(fio)
print(len(och), len(zaoch))