from fastapi import Depends,HTTPException,status,Header

API_KEY = "my-secret-key"

def verify_api_key(authorization: str = Header(None, alias="Authorization")):
    if authorization is None :
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Authorization header missing"
        )
    
    if authorization != f"Bearer {API_KEY}":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid Api key "
        )
    

    return True

