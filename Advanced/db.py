import pymysql


class DB:
    """
    使用with管理
    """
    def __init__(self, host='localhost', port=3306, db='dazy', user='root', passwd='Steam3'):
        # 建立连接
        self.conn = pymysql.connect(host=host, port=port, db=db, user=user, passwd=passwd)
        # 创建游标
        self.cur = self.conn.cursor()

    def __enter__(self):
        # 返回游标
        return self.cur

    def __exit__(self, exc_type, exc_val, exc_tb):
        # 提交数据库并执行
        self.conn.commit()
        # 关闭游标
        self.cur.close()
        # 关闭数据库连接
        self.conn.close()


# if __name__ == '__main__':
#     with DB(host='192.168.68.129',user='root',passwd='zhumoran',db='text3') as db:
#         db.execute('select * from course')
#         print(db)
#         for i in db:
#             print(i)