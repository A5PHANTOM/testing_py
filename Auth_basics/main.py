from fastapi import Depends
from auth import verify_api_key
from fastapi import FastAPI

app = FastAPI()

@app.get("/testing")
def auth_test(auth : bool = Depends(verify_api_key)):
    return ("AUTH PASSED")

