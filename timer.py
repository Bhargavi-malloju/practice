import time
def countdown(t):
    while t>0:
        mins=t//60
        secs=t%60
        timer='{}:{}'.format(mins,secs)
        print(timer,end="\n")
        time.sleep(2)
        t-=1
    print("time up")

print("give in seconds to countdown!")
seconds=int(input())
countdown(seconds)

