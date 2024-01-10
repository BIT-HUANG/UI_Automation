import pymysql
import yaml


class BaseDb:
    def __init__(self):
        with open("../../py_yaml/base_db.yaml", mode='r', encoding="utf-8") as f:
            data = yaml.safe_load(f)
        database = data["database"]
        self.connect = pymysql.Connect(**database,
                                       cursorclass=pymysql.cursors.DictCursor)

    def select_data(self, sql):
        cursor = self.connect.cursor()
        cursor.execute(sql)
        cursor.close()
        res = cursor.fetchall()
        return res

    def change_data(self, sql):
        cursor = self.connect.cursor()
        num = cursor.execute(sql)
        self.connect.commit()
        cursor.close()
        return f'{sql}\n【操作影响到{num}】'

    def __call__(self, sql: str, connect=True, ):
        sql_new = sql.lower().strip()
        start = sql_new.split(" ")[0]
        if start in ["select", "use", "show"]:
            res = self.select_data(sql)
            if not connect:
                self.connect.close()
            return res
        elif start in ["delete", "alter", "update", "insert", "drop"]:
            res = self.change_data(sql)
            # res=self.select_data(sql)
            if not connect:
                self.connect.close()
            return res


if __name__ == '__main__':
    base_db = BaseDb()

    sql3 = "delete from bhh_XiangShuiXiaoShou  where id='123456' "
    print(base_db(sql3))
