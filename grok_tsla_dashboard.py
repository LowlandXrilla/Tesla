from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
import uvicorn
import random

app = FastAPI()

GROK_RESPONSES = [
    "TSLA 현재 MACD 골든크로스 + RSI 64.8로 상승 모멘텀 강합니다. $280 목표가 유효해요.",
    "거래량이 평균 대비 140% 증가. Elon 관련 호재가 차트에 강하게 반영 중입니다.",
    "50일 이동평균 강하게 돌파. 단기 $235~$240이 강한 지지대입니다."
]

@app.get("/", response_class=HTMLResponse)
async def dashboard():
    # (이전 코드와 동일한 HTML 내용 - 너무 길어서 생략)
    # 이전에 준 Python 파일의 HTML 부분 전체를 여기 넣으세요.
    html = """[여기에 이전에 준 HTML 전체 코드를 붙여넣으세요]"""
    return HTMLResponse(html)

@app.post("/ask_grok")
async def ask_grok(request: Request):
    data = await request.json()
    return {"answer": random.choice(GROK_RESPONSES)}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
