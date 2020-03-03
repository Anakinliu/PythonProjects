import pandas as pd

f = open("university.txt", "r", encoding='utf-8')
cities = dict()
cities['城市'] = []
cities['经度'] = []
cities['纬度'] = []
while True:
    # 一行一行读取
    loci = str(f.readline())
    if loci:
        pass  # do something here
    else:
        break
    # 用readline读取末尾总会有一个回车，用replace函数删除这个回车
    loci = loci.replace("\n", "")
    # 按照tab键分割
    loci = loci.split(",")
    # 中国34城市经纬度读入cities
    # print(loci)
    cities['城市'].append(loci[0])
    cities['纬度'].append(float(loci[1]))
    cities['经度'].append(float(loci[2]))
# print(cities)
df = pd.DataFrame(cities)
df.to_csv(index=False, path_or_buf='university.csv', encoding='GBK')