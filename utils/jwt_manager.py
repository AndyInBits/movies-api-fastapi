from jwt import decode, encode


def create_token(data: dict, secret: str = "MySecretKey") -> str:
    token: str = encode(data, secret, algorithm="HS256")
    return token


def validate_token(token: str) -> dict:
    try:
        return decode(token, "MySecretKey", algorithms=["HS256"])
    except:
        return {}
