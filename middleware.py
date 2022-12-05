from fastapi import Request
from fastapi.security import HTTPAuthorizationCredentials
from fastapi import Request, HTTPException

class MyMiddleware:
    def __init__(self, auto_Error: bool = True):
        super(MyMiddleware,self).__init__(auto_error=auto_Error)
        
    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(MyMiddleware, self).__call__(request)
        if credentials:
            if not credentials == "valid":
                raise HTTPException(status_code=403, detail="Invalid authentication.")
            return credentials.credentials
        else:
            raise HTTPException(status_code=403, detail="Invalid authorization code.")
    