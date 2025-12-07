"""
================================================================
파일명       : main.py
목적         : FastAPI 애플리케이션 진입점
설명         :
  - FastAPI 앱 인스턴스 생성 및 설정
  - CORS 미들웨어 설정 (프론트엔드 요청 허용)
  - MongoDB 연결 및 컬렉션 정의
  - 기본 라우트 및 헬스체크 API
================================================================
"""

import os
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pymongo import MongoClient

# 환경변수 로드
load_dotenv()

# FastAPI 앱 생성
app = FastAPI(title="Linkdo API")

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# MongoDB 연결
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/linkdo")
client = MongoClient(MONGO_URI)
db = client["linkdo"]

# 컬랙션
tasks_collection = db["tasks"]
edges_collection = db["edges"]

@app.get("/")
async def root():
    return {"message": "Linkdo API is running"}

@app.get("/health")
def health_check():
    try:
        client.admin.command("ping")
        return {"status": "healthu", "database": "connected"}
    except Exception as e:
        return {"status": "unhealthy", "error": str(e)}