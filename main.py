from fastapi import FastAPI, HTTPException, Cookie,Request,Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

import requests
app = FastAPI()

# Dictionary to store cookies
cookies_db = {}

# Allow CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace with your domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/cookie/set-cookies")
async def set_cookie(request: Request,response: Response):
    params = request.query_params
    content = {"message": "Cookie set successfully"}
    response = JSONResponse(content=content)
    response.set_cookie(key='accesstoken', value=params['accesstoken'])
    return response


@app.get("/api/cookie/get-cookies")
async def get_cookie(request: Request):
    """
    Get the value of the provided cookie key.
    """
    if request.cookies.get('accesstoken'):
        return request.cookies.get('accesstoken')
    else:
        raise HTTPException(status_code=404, detail="Cookie not found")