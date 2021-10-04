from datetime import timedelta
import json
import redis
import os

redis_client = redis.from_url(url=os.getenv('SESSION_CACHE_URL'), db=0)

class SessionCache:
    def set(self, key: str, payload: dict, expire_in_secs: int):
        redis_client.set(key, json.dumps(payload))
        if expire_in_secs > 0:
            print(expire_in_secs)
            redis_client.expire(key, timedelta(seconds=expire_in_secs))
        pass

    def get(self, key: str):
        return redis_client.get(key)


session_cache = SessionCache()
