import pymysql.cursors
import datetime

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='Steam3',
                             db='news',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        now = datetime.datetime.utcnow()
        # Create a new record
        sql = "INSERT INTO `news` VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(sql, (1,
                             '国产航母首次穿越台湾海峡 专家:服役时间指日可待',
                             '海军专家李杰接受澎湃新闻采访时表示，首艘国产航母还未正式入列之前进行跨海区海试的目的原因可能三点：\
                             一是现在海试进入后期阶段，通过跨海区海试对航母远航能力进行测试；二是需要南海这样水深更深、\
                             面积更大的海域对相关系统进行测试；三是跨海区海试结束后交付南海舰队。',
                             '军事',
                             'http://crawl.ws.126.net/32c18c89afc3588c13e543b9424e7f3b.jpg',
                             '史建磊_NBJ11331',
                             186,
                             now.strftime("%Y-%m-%d %H:%M:%S"),
                             1,
                       ))

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    connection.commit()

    # with connection.cursor() as cursor:
    #     # Read a single record
    #     sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
    #     cursor.execute(sql, ('webmaster@python.org',))
    #
    #     result = cursor.fetchone()
    #     print(result)
finally:
    connection.close()