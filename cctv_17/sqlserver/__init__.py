import pymssql


class MSSQL:
    def __init__(self, host, user, pwd, db):
        self.host = host
        self.user = user
        self.pwd = pwd
        self.db = db

    def getConnect(self):
        if not self.db:
            raise (NameError, '没有设置数据库信息')
        self.conn = pymssql.connect(host=self.host, user=self.user, pwd=self.pwd, db=self.db, charset='utf8')
        cur = self.conn.cursor()
        if not cur:
            raise (NameError, '连接数据库失败')
        else:
            return cur

    # 执行有返回的sql语句
    def execQuery(self, sql):
        cur = self.getConnect()
        cur.execute(sql)
        res_list = cur.fetchall()
        self.conn.close()
        return res_list

    # 执行没有返回的sql语句
    def execNoQuery(self, sql):
        cur = self.getConnect()
        cur.execute(sql)
        self.conn.commit()
        self.conn.close()

    def getData(self, sql):
        count=0
        for i in range(len(sql)):









