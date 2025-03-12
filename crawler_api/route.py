from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import redis
import json

# Kết nối tới Redis
redis_client = redis.Redis(host='redis_db', port=6379, db=0, decode_responses=True)

app = FastAPI()

# Cấu hình CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)

@app.get("/news")
def get_news():
    try:
        key = "theothao247_news"
        news_list = redis_client.lrange(key, 0, -1)  # Lấy toàn bộ danh sách
        news_data = [json.loads(item) for item in news_list]  # Chuyển đổi từ JSON string sang dictionary
        return {"news": news_data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
