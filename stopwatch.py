#stopwatch.py
import time

print("Press 'Enter' to start count | <CTRL>+<C> to stop")

input()
print("StopWatch Started!..")
start_time = time.time()
while True:
    try:
        mid_time = time.time()
        print("%6s" % str(round(mid_time-start_time, 2)), end =" | ")
        #pass
        
    except KeyboardInterrupt:
        end_time = time.time()
        print("\nStopWatch Stopped: "+ str(round(end_time-start_time, 2)) +" seconds")
        input(">> PRESS <ENTER>...")
        break
