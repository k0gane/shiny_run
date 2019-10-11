from datetime import datetime
f = open('status.txt', 'a')
buri = '                   時刻 1周の時間  獲得ファン数   累計ファン数\n'
f.write(buri)
total = 0
now = datetime.now()
st = str(now)
st1 = st[:-7]
start = "開始時刻は" + st1 + "です"
first = now
count = 0
while True:
    a = int(input())
    if(a == 0):
        break
    now1 = datetime.now()
    time = now1 - now
    time1 = str(time)
    time2 = time1[:-7]
    now = now1
    now2 = str(now)
    now3 = now2[:-7]
    total += a
    count += 1
    str_count = str(count).zfill(3)
    f = open('status.txt', 'a')
    unchi = str_count + ' ' + now3 + '   ' + time2 +  '           ' + str(a) + '            ' + str(total) + '\n'
    f.write(unchi)
total_time = now1 - first
second = total_time.seconds
minute = second // 60
ave = total // count
zisoku = (total // minute) * 60
tot = str(total_time)
tot1 = tot[:-7]
last1 = "合計周回時間は" + tot1 +'です。\n'
last2 = "合計周回数は"+str(count)+'周で合計獲得ファン数は'+str(total)+'万人、平均獲得ファン数は'+str(ave)+'万人です。\n'
last3 = "平均時速は" + str(zisoku) + "万人です。\n お疲れ様でした♪"
f.write(last1)
f.write(last2)
f.write(last3)
f.close()