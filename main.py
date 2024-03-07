from fastapi import FastAPI, HTTPException
import random
import string
from models.url_storage import URLStorage


app = FastAPI()

url_db = {}

def generate_short_url():
    """랜덤한 문자열을 생성하여 단축 URL로 사용"""
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for i in range(6))

@app.post("/shorten/")
def shorten_url(url_request):
    """URL을 받아서 단축 URL을 생성하고 반환"""
    url_db = {}
    short_url = generate_short_url()
    url_storage = URLStorage(original_url=url_request.url, short_url=short_url)
    url_db[short_url] = url_storage
    return url_storage

@app.get("/{short_url}")
def redirect_to_original(short_url: str):
    """단축 URL을 받아서 원본 URL로 리디렉션"""
    url_db = {}
    if short_url not in url_db:
        raise HTTPException(status_code=404, detail="Short URL not found")
    return {"url": url_db[short_url].original_url}

