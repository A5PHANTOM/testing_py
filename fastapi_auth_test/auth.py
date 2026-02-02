from fastapi import HTTPException,Depends,status,Header
from fastapi.security import HTTPBearer,HTTPAuthorizationCredentials
API_KEY ="my-secret-key"

security = HTTPBearer()

def verify_api(credentials : HTTPAuthorizationCredentials = Depends(security)):
    if credentials.scheme != "Bearer":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="schema error"
        )
    if credentials.credentials != API_KEY:
        raise HTTPException(
            status.HTTP_401_UNAUTHORIZED,
            detail="Invalid api"
        )
    return True
