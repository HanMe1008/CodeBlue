# 해운대해수욕장 해양관측부이 2024/04/01 관측데이터

# 1.   유속 [cm/s]
# 2.   풍속 [m/s]

# 바다누리 해양정보 서비스
# http://www.khoa.go.kr/oceangrid/gis/category/reference/distribution.do#none


# 그림 1 (보정 O - 풍속 10배)
import csv
import matplotlib.pyplot as plt
import numpy as np


f = open('data_2024_TW_TW_HAE_202404_KR.csv', 'r', encoding='UTF-8')
data = csv.reader(f, delimiter=',')
for i in range(5):
  next(data)

wind_speed = []
current_speed = []
time = []
count = 0

for row in data :
  if row[1] == '-' or row[9] == '-' :
    continue
  time.append(row[0].split(" ")[1])
  wind_speed.append(row[9])
  current_speed.append(row[1])
  
r_wind_speed = []
r_current_speed = []

for i in wind_speed:
  r_wind_speed.append(float(i)*10)
for i in current_speed:
  r_current_speed.append(float(i))

plt.style.use('default')
plt.rcParams['figure.figsize'] = (150, 10)
plt.rcParams['font.size'] = 12

plt.plot(time, r_current_speed, 'b', label='Current_Speed [cm/s]')
plt.plot(time, r_wind_speed, 'g', label='Wind_Speed * 10 [m/s]')
for i in range(1422):
  if r_current_speed[i] > r_wind_speed[i]:
    plt.fill_between(time[i-1:i+1], r_current_speed[i-1:i+1], r_wind_speed[i-1:i+1], color='lightgray', alpha=0.5)
  else:
    plt.fill_between(time[i-1:i+1], r_wind_speed[i-1:i+1], r_current_speed[i-1:i+1], color='lightgray', alpha=0.5)

plt.xlabel('Time')
plt.ylabel('Speed')
plt.legend(loc='upper left')
plt.grid(True, axis='y')

plt.xticks(ticks=time, labels=time, rotation=-45)
plt.locator_params(axis='x', nbins=len(time)/60)    # 코랩에선 10으로 수정

plt.rc('font', family='NanumBarunGothic')
plt.title('2024/04/01, Haeundae, Current_Speed & Wind_Speed')

plt.show()


# 그림 2 (보정 X)
import csv
import matplotlib.pyplot as plt
import numpy as np


f = open('data_2024_TW_TW_HAE_202404_KR.csv', 'r', encoding='UTF-8')
data = csv.reader(f, delimiter=',')
for i in range(5):
  next(data)

wind_speed = []
current_speed = []
time = []
count = 0

for row in data :
  if row[1] == '-' or row[9] == '-' :
    continue
  time.append(row[0].split(" ")[1])
  wind_speed.append(row[9])
  current_speed.append(row[1])
  
r_wind_speed = []
r_current_speed = []

for i in wind_speed:
  r_wind_speed.append(float(i))
for i in current_speed:
  r_current_speed.append(float(i))

plt.style.use('default')
plt.rcParams['figure.figsize'] = (150, 10)
plt.rcParams['font.size'] = 12

plt.plot(time, r_current_speed, 'b', label='Current_Speed [cm/s]')
plt.plot(time, r_wind_speed, 'g', label='Wind_Speed [m/s]')
for i in range(1422):
  if r_current_speed[i] > r_wind_speed[i]:
    plt.fill_between(time[i-1:i+1], r_current_speed[i-1:i+1], r_wind_speed[i-1:i+1], color='lightgray', alpha=0.5)
  else:
    plt.fill_between(time[i-1:i+1], r_wind_speed[i-1:i+1], r_current_speed[i-1:i+1], color='lightgray', alpha=0.5)

plt.xlabel('Time')
plt.ylabel('Speed')
plt.legend(loc='upper left')
plt.grid(True, axis='y')

plt.xticks(ticks=time, labels=time, rotation=-45)
plt.locator_params(axis='x', nbins=len(time)/60)    # 코랩에선 10으로 수정

plt.rc('font', family='NanumBarunGothic')
plt.title('2024/04/01, Haeundae, Current_Speed & Wind_Speed')

plt.show()


# 그림 3 (풍속 [m/s] -> [cm/s]로 수정)
import csv
import matplotlib.pyplot as plt
import numpy as np


f = open('data_2024_TW_TW_HAE_202404_KR.csv', 'r', encoding='UTF-8')
data = csv.reader(f, delimiter=',')
for i in range(5):
  next(data)

wind_speed = []
current_speed = []
time = []
count = 0

for row in data :
  if row[1] == '-' or row[9] == '-' :
    continue
  time.append(row[0].split(" ")[1])
  wind_speed.append(row[9])
  current_speed.append(row[1])
  
r_wind_speed = []
r_current_speed = []

for i in wind_speed:
  r_wind_speed.append(float(i)*100)
for i in current_speed:
  r_current_speed.append(float(i))

plt.style.use('default')
plt.rcParams['figure.figsize'] = (150, 10)
plt.rcParams['font.size'] = 12

plt.plot(time, r_current_speed, 'b', label='Current_Speed [cm/s]')
plt.plot(time, r_wind_speed, 'g', label='Wind_Speed * 10 [m/s]')
for i in range(1422):
  if r_current_speed[i] > r_wind_speed[i]:
    plt.fill_between(time[i-1:i+1], r_current_speed[i-1:i+1], r_wind_speed[i-1:i+1], color='lightgray', alpha=0.5)
  else:
    plt.fill_between(time[i-1:i+1], r_wind_speed[i-1:i+1], r_current_speed[i-1:i+1], color='lightgray', alpha=0.5)

plt.xlabel('Time')
plt.ylabel('Speed')
plt.legend(loc='upper left')
plt.grid(True, axis='y')

plt.xticks(ticks=time, labels=time, rotation=-45)
plt.locator_params(axis='x', nbins=len(time)/60)    # 코랩에선 10으로 수정

plt.rc('font', family='NanumBarunGothic')
plt.title('2024/04/01, Haeundae, Current_Speed & Wind_Speed')

plt.show()
