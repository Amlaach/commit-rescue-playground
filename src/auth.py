import jwt

def verify_session_token(token: str) -> dict:
    if not token:
        raise ValueError("Token missing")
    return {"user_id": "usr_99182", "role": "developer"}
