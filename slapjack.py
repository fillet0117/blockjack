import thread
import time
import random
import threading

exitflag = 0
class mythread(threading.Thread):
    def __init__(self, threadID, name, threadcard, cangrab, pregrab, score):
        threading.Thread.__init__(self)
        self.name = name
        self.threadcard = []
        self.cangrab = cangrab
        self.score = score
        self.pregrab = pregrab
    def run(self):
        self.threadcard = send3card(self.name)
        abc(self.name, self.threadcard, self.cangrab, self.pregrab, self.score)
        
card = []
for i in range(1,5):
    for j in range(1,14):
        card.append((i,j))
       
def send3card(threadname):
    global card
    threadc = []
    threadlock.acquire()
    print threadname
    for i in range(3):
        a = random.choice(card)
        print a
        threadc.append(a)
        card.remove(a)
    threads.append(threadname)
    threadlock.release()
    return threadc          

def abc(name,threadcard, cangrab, pregrab, score):     
    global exitflag
    global count
    global grab
    global banker
    global end_thread
    global threads
    global check_thread
    
    while len(threads) != 4:
        pass  
    threadlock.acquire()
    size = len(threads)
    if size == 0:
        pass
    else:
        for i in range(size):
            threads.pop()
    threadlock.release()
    
    while len(end_thread) < 4 or len(card) != 0:
        threadlock.acquire()
        if count == 0:
            exitflag = 1
            count+=1
        threadlock.release()
        time.sleep(1)
        #compare thread's card and banker' card
        while banker == (0,0):
            pass
        threadlock.acquire()
        for a in threadcard:
            if a[0] == banker[0]:
                cangrab = 1
                break
            elif a[1] == banker[1]:
                cangrab = 1
                break
        threadlock.release()
        #if thread can grab
        if cangrab != 0 and (name not in end_thread):
            if pregrab == 1:
                time.sleep(1)
            grab.append(name)
            threadlock.acquire()
            if grab[0] == name:
                for a in threadcard:
                    if a[1] == banker[1]:
                        score[0] = 30 + score[0]
                        threadcard.remove(a)
                        break
                    elif a[0] == banker[0]:
                        score[1] = 10 + score[1]
                        threadcard.remove(a)
                        break
                pregrab = 1
                print "who grab the card : %s" % name
            threadlock.release()
        threadlock.acquire()
        print name
        for i in threadcard:
            print i
        threadlock.release()
        
        threads.append(name)
        while len(threads) != 4:
            pass
        
        #if no thread have same number or color
        if len(grab) == 0 and (name not in end_thread):
            if pregrab == 1:
                time.sleep(1)
            grab.append(name)
            threadlock.acquire()
            if grab[0] == name:
                score[2] = 5 + score[2]
                pregrab = 1
                print "who grab the card : %s" % name
            print name
            for i in threadcard:
                print i
            threadlock.release()
        #if thread's card empty,save in end_thread
        threadlock.acquire()
        if len(threadcard) == 0 and (name not in end_thread):
            end_thread.append(name)
        #reset
        if cangrab == 1:
            cangrab = 0
        if len(grab) != 0:
            if grab[0] != name:
                pregrab = 0
        check_thread.append(name)
        threadlock.release()
        while len(check_thread) != 4:
            pass
        
        if pregrab == 1:
            count = 0
        
                        
threadlock = threading.Lock()
threads = []
grab = []
card1 = []
card2 = []
card3 = []
card4 = []
check_thread = []
count2 = 0
#number,color,grab
score1 = [0,0,0]
score2 = [0,0,0]
score3 = [0,0,0]
score4 = [0,0,0]

threadc = []
banker = (0,0)
end_thread = []
count = 0

thread1 = mythread(1,"thread_1",card1,0,0,score1)
thread2 = mythread(2,"thread_2",card2,0,0,score2)
thread3 = mythread(3,"thread_3",card3,0,0,score3)
thread4 = mythread(4,"thread_4",card4,0,0,score4)

thread1.start()
thread2.start()
thread3.start()
thread4.start()

while 1:
    if exitflag == 1 and len(card) != 0:
        threadlock.acquire()
        banker = random.choice(card)
        card.remove(banker)
        print "banker's card"
        print banker
        size = len(grab)
        if size == 0:
            pass
        else:
            for i in range(size):
                grab.pop()

        size = len(threads)
        if size == 0:
            pass
        else:
            for i in range(size):
                threads.pop()
        
        size = len(check_thread)
        if size == 0:
            pass
        else:
            for i in range(size):
                check_thread.pop()
        exitflag = 0
        threadlock.release()
    elif len(card) == 0 or len(end_thread) == 4:
        break
print "end"
print ""
score = [[],[],[],[]]
score[0] = score1
score[1] = score2
score[2] = score3
score[3] = score4

count = 0
for i in end_thread:
    total = 0
    print "player %c : " % i[7]
    if count == 0:
        print "first player score + 50"
        total = total + 50
        
    elif count == 1:
        print "second player score + 20"
        total = total + 20
    count2 = 0  
    for a in score[int(i[7]) - 1]:
        if count2 == 0:
            print "number : "
        elif count2 == 1:
            print "color : "
        elif count2 == 2:
            print "grab : "
        print a
        total = total + a
        count2 += 1
        
    print "total : %d" % total
    count+=1
    print ""
