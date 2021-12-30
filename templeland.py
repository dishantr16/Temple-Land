for _ in range(int(input())):
    N = int(input())
    Arr = list(map(int,input().split()))

    if N % 2 == 0:
        print('no')
    elif Arr[0] != 1 or Arr[-1] != 1:
        print("no")
    else:
        for i in range(N//2):
            if Arr[i] != i+1:
                print('no')
                break
        else:
            Num= Arr[N//2]

            for j in range(N//2,N):

                if Arr[j] != Num:
                    print('no')
                    break
                else:
                    Num = Num - 1

            else:
                print('yes')