'''
用以下命令运行：
uvicorn server:app --reload
'''
from typing import Optional
from pydantic import BaseModel
from fastapi import FastAPI, UploadFile,File

app = FastAPI(title="窗口名", version="v0.0.1")

@app.get('/get_data')
async def get_test(l:str, s: str):
    # 127.0.0.1:8000/get_data?l=test0&s=test1
    tmp = {'location': l, 'data': s}
    return tmp

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

@app.post('/post_data')
async def post_test(it: Item):
    tmp = {'des': 'title', 'name': it.name, 'price': it.price}
    return tmp