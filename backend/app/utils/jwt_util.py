import jwt
import datetime

class JwtUtil:
    EXPIRE_TIME = (7 * 12) * 60 * 60

    @staticmethod
    def sign(username: str, secret: str) -> str:
        expire = datetime.datetime.utcnow() + datetime.timedelta(minutes=JwtUtil.EXPIRE_TIME)

        payload = {
            "username": username,
            "exp": expire,
        }
        return jwt.encode(payload, secret, algorithm="HS256")