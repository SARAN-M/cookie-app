from fastapi import FastAPI, HTTPException, Cookie,Request,Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import sys
import uvicorn
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

@app.get("/cookie/set-cookies")
async def set_cookie(request: Request,response: Response):
    params = request.query_params
    content = {"message": "Cookie set successfully"}
    response = JSONResponse(content=content)
    response.set_cookie(key='accesstoken', value=params['accesstoken'])
    return response


@app.get("/cookie/get-cookies")
async def get_cookie(request: Request):
    """
    Get the value of the provided cookie key.
    """
    if request.cookies.get('accesstoken'):
        return request.cookies.get('accesstoken')
    else:
        raise HTTPException(status_code=404, detail="Cookie not found")

if __name__ == '__main__':
    port = int(sys.argv[1])
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)