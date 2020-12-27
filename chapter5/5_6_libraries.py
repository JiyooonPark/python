# sys
import sys
print(sys.argv)
print(sys.path)

#pickle : can export objects as they are
import pickle
f = open("text.txt", 'wb')
data = {1: 'python', 2: 'you need'}
pickle.dump(data, f)
f.close()

f = open("text.txt", 'rb')
data = pickle.load(f)
print(data)
f.close()

#os
import os
print(os.environ)
print(os.environ['PATH'])
# os.chdir("C:\WINDOWS")
# os.system("dir")
# os.mkdir(디렉터리)

# shutil
    # copy file
import shutil
shutil.copy('text.txt', 'copy.txt')

#glob
import glob
# glob.glob("c:/")

#tempfile
import tempfile
filename = tempfile.mktemp();

#time
import time
print(time.time())
print(time.localtime(time.time()))
print(time.asctime(time.localtime(time.time())))
print(time.ctime())
# print(time.strftime('출력할 형식 포맷 코드', time.localtime(time.time())))
time.sleep(1)

#calendar
import calendar
print(calendar.calendar(2020))
print(calendar.weekday(2015, 12, 31))
print(calendar.monthrange(2015,12))
print(calendar.prmonth(2015, 12))

#random
import random
print(random.random())
print(random.randint(1, 10))
# print()

#webbrowser
import webbrowser
webbrowser.open("www.google.com")
# webbrowser.open_new("http://google.com")

#threading
import time
import threading

def long_task():
    for i in range(5):
        time.sleep(1)
        print("working:%s\n" % i)

print("Start")

threads = []
for i in range(5):
    t = threading.Thread(target=long_task)
    threads.append(t)

for t in threads:
    t.start()

for t in threads:
    t.join()  # join으로 스레드가 종료될때까지 기다린다.

print("End")