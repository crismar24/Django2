# e = list( int(input()) for i in range(3) )
# a,b = (int(i) for i in input().split())
# ab = (int(i) for i in input().split())
# list_ad = list(ab)

friends = int(input())
appls = int(input())
appls_ = appls
while True:

    if appls_ % friends == 0:
        print(appls_ - appls)
        break
    else:
        appls_+=1




