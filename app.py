"""
This module contains the FastAPI application with GitHub OAuth authentication.
"""

import httpx
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse, RedirectResponse
from config import GITHUB_CLIENT_ID, GITHUB_CLIENT_SECRET

app = FastAPI()

@app.get("/")
async def home():
    """Home endpoint"""
    return "Hello, FastAPI!"

@app.get("/api/data")
async def get_data():
    """Get data endpoint"""
    data = {"key": "value"}
    return JSONResponse(content=data)

@app.post("/api/data")
async def post_data(request: Request):
    """Post data endpoint"""
    new_data = await request.json()
    return JSONResponse(content=new_data, status_code=201)

@app.get("/github-login")
async def github_login():
    """GitHub login endpoint"""
    return RedirectResponse(
        f'https://github.com/login/oauth/authorize?client_id={GITHUB_CLIENT_ID}',
        status_code=302
    )

@app.get("/github-code")
async def github_code(code: str):
    """GitHub code endpoint"""
    if not code:
        raise HTTPException(status_code=400, detail="Code query parameter is required")
    
    params = {
        'client_id': GITHUB_CLIENT_ID,
        'client_secret': GITHUB_CLIENT_SECRET,
        'code': code
    }
    headers = {'Accept': 'application/json'}
    
    async with httpx.AsyncClient() as client:
        response = await client.post(
            url='https://github.com/login/oauth/access_token',
            data=params,
            headers=headers
        )
    
    response_json = response.json()
    access_token = response_json.get('access_token')
    
    if not access_token:
        raise HTTPException(status_code=400, detail="Failed to retrieve access token")
    
    async with httpx.AsyncClient() as client:
        headers.update({'Authorization': f'Bearer {access_token}'})
        response = await client.get(url='https://api.github.com/user', headers=headers)

    return {"response_json": response.json()}

@app.get("/api/data")
async def get_data():
    """Get data endpoint"""
    data = {"key": "value"}
    return JSONResponse(content=data)

@app.post("/api/data")
async def post_data(request: Request):
    """Post data endpoint"""
    new_data = await request.json()
    return JSONResponse(content=new_data, status_code=201)

@app.get("/github-login")
async def github_login():
    """GitHub login endpoint"""
    return RedirectResponse(
        f'https://github.com/login/oauth/authorize?client_id={GITHUB_CLIENT_ID}',
        status_code=302
    )

@app.get("/github-code")
async def github_code(code: str):
    """GitHub code endpoint"""
    if not code:
        raise HTTPException(status_code=400, detail="Code query parameter is required")
    
    params = {
        'client_id': GITHUB_CLIENT_ID,
        'client_secret': GITHUB_CLIENT_SECRET,
        'code': code
    }
    headers = {'Accept': 'application/json'}
    
    async with httpx.AsyncClient() as client:
        response = await client.post(
            url='https://github.com/login/oauth/access_token',
            data=params,
            headers=headers
        )
    
    response_json = response.json()
    access_token = response_json.get('access_token')
    
    if not access_token:
        raise HTTPException(status_code=400, detail="Failed to retrieve access token")
    
    async with httpx.AsyncClient() as client:
        headers.update({'Authorization': f'Bearer {access_token}'})
        response = await client.get(url='https://api.github.com/user', headers=headers)

    return {"response_json": response.json()}