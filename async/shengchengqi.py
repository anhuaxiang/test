
# a = (i for i in range(70000))
import schedule


def count(n):
    x = 0
    while x < n:
        yield x
        x += 1


for i in count(5):
    print(i)

def job():
    print('working')

job()
schedule.every(2).seconds.do(job)

schedule.run_pending()
