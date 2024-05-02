# 해양학전공 전상규 2024.03.24

# 북극 해빙 면적 데이터 (샘플에 최대한 근사하게)

import matplotlib.pyplot as plt
import csv

f = open('seaice.csv',"r",encoding='UTF-8')       # 파일을 읽기 모드(read)로 읽어오되 cp949라는 형식(Windows 한글 인코딩 방식)으로 읽어오라는 의미, 'r'은 기본값이라 생략 가능. encoding 부분은 기본값이 ASCII
data = (csv.reader(f, delimiter=','))       # delimiter 부분은 파이썬 CSV 파일 구분 연산자 기본값이 콤마(,)라 생략가능
next(data)
result = []
year = []

for row in data :
    result.append(float(row[1]))
    year.append(row[0].split(" ")[0])

plt.rc('font', family='NanumBarunGothic')       # 폰트 설정, 나눔바른고딕
plt.figure(figsize = (15,5))        # figure 사이즈 설정
plt.plot(year, result, linewidth=4)       # X축 데이터, Y축 데이터, 선굵기 설정
plt.ylim([4.5, 8.5])        # Y축의 범위: [ymin, ymax]
plt.title('북극 해빙 면적 평균(10^6km)')        # 타이틀 설정
plt.xticks(ticks=year, labels=year, rotation=-45)     # X축 텍스트 방향 기울이기
plt.locator_params(axis='x', nbins=len(year)/2)     # X축 연도 빈도수 줄이기
plt.grid(True, axis='y')      # Y축 그리드 설정

plt.show()

"""
# 8월달의 북극 해빙 면적 데이터
import matplotlib.pyplot as plt
import csv

f = open('seaice.csv',"r",encoding='UTF-8-sig')
data = (csv.reader(f))
next(data)
result = []
year = []

for row in data :
    result.append(float(row[1]))
    year.append(row[0].split(" ")[0])
    
plt.rc('font', family='NanumBarunGothic')
plt.figure(figsize = (30,5))
plt.title('북극 해빙 면적 평균(10^6km)')
plt.plot(year, result, linewidth=4)
plt.ylim([4.5, 8.5])     # Y축의 범위: [ymin, ymax]
plt.grid(True, axis='y')        # Y축 그리드 설정

plt.show()


# 8월달의 남극 해빙 면적 데이터

import matplotlib.pyplot as plt
import csv

f = open('seaice.csv',"r",encoding='UTF-8-sig')
data = (csv.reader(f))
next(data)
result = []
year = []

for row in data :
    result.append(float(row[2]))
    year.append(row[0].split(" ")[0])

plt.rc('font', family='NanumBarunGothic')
plt.figure(figsize = (30,5))
plt.plot(year, result, linewidth=4)
plt.title('남극 해빙 면적 평균(10^6km)')
plt.grid(True, axis='y')

plt.show()
"""