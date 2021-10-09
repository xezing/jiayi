#coding=utf-8
import redis
import redisCfg


def getConnect():
    conn = redis.Redis(host=redisCfg.dbHost, port=redisCfg.dbPort, db=redisCfg.dbName, password=redisCfg.dbPasswd)
    return conn


def get(key):
    result = None
    conn = getConnect()
    result = conn.get(key)
    return result

def set(key, value):
    result = None
    conn = getConnect()
    result = conn.set(key, value)
    return result

def hget(group, key):
    result = None
    conn = getConnect()
    result = conn.hget(group, key)
    return result


def hexists(group, key):
    conn = getConnect()
    return conn.hexists(group, key)


def hset(group, key, value):
    conn = getConnect()
    conn.hset(group, key, value)


def hdel(group, key):
    conn = getConnect()
    return conn.hdel(group, key)


def delete(group):
    conn = getConnect()
    return conn.delete(group)


def hlen(group):
    conn = getConnect()
    return conn.hlen(group)


def hincrby(group, key, incValue=1):
    conn = getConnect()
    result = conn.hincrbyfloat(group, key, incValue)
    return result


def hgetall(group):
    conn = getConnect()
    result = conn.hgetall(group)
    return result


def getRedisVersion():
    conn = getConnect()
    info = conn.info()
    return info['redis_version']


def getDatabases():
    conn = getConnect()
    result = 0
    x = conn.config_get('databases')
    if x.has_key('databases'): result = int(x['databases'])
    return result


if __name__ == '__main__':
    print "redis version: %s" % (getRedisVersion())
    print "database size: %d" % (getDatabases())

    key = "test-key"
    set(key, "test-key")
    print get(key)
    delete(key)

    group = "test-group"
    hset(group, key, "test-group")
    print hget(group, key)
    delete(group)
