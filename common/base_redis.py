import redis
import os
import yaml


class BaseRedis:
    abs_path = os.path.abspath(__file__)
    project_path = os.path.dirname(os.path.dirname(abs_path))
    base_db_yaml_path = project_path + '/py_yaml/base_db.yaml'

    def __init__(self):
        with open(BaseRedis.base_db_yaml_path, mode='r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
            database = data['base_redis']
            self.redis_pool = redis.ConnectionPool(host=database['host'], port=database['port'],
                                                   password=database['password'], db=0)
            self.redis_conn = redis.Redis(connection_pool=self.redis_pool)
            self.code_key_name = database['code_key_name']
            self.static_code_value = database['static_code_value']

    def get_code(self, phone: str):
        redis_conn = self.redis_conn
        search_value = redis_conn.get(self.code_key_name + ":" + phone)
        redis_conn.close()
        if search_value :
            search_value = search_value.decode("utf-8")
            print(search_value)
            return search_value

    def set_code(self, phone: str):
        redis_conn = self.redis_conn
        redis_conn.setex(self.code_key_name + ":" + phone, 600, self.static_code_value)
        redis_conn.close()
        return self.static_code_value


if __name__ == '__main__':
    # print(set_code("789"))
    redis = BaseRedis()
    redis.set_code('18199999999')
    redis.get_code('18199999999')

    # print(redis.get_code('18146712142'))
