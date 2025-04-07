from fastapi import FastAPI, Query
from app.model import SHLRecommender
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
recommender = SHLRecommender()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], allow_credentials=True,
    allow_methods=["*"], allow_headers=["*"]
)

@app.get("/api/recommend")
def recommend(query: str = Query(...)):
    results = recommender.recommend(query)
    return {"results": results}