from fastapi import APIRouter, HTTPException

from models import Vote
from config import votes

router = APIRouter()

@router.post("/vote")
async def vote(vote: Vote):
    if vote.option not in votes:
        raise HTTPException(status_code=400, detail="Invalid vote option")
    votes[vote.option] += 1
    return votes

@router.get("/results")
async def get_results():
    return votes
