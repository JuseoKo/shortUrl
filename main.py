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


