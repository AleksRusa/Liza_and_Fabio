from fastapi import APIRouter, HTTPException, Request
from fastapi.templating import Jinja2Templates

from models import Vote
from config import votes

router = APIRouter()

templates = Jinja2Templates(directory="src/templates")

@router.get("/")
async def get_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@router.post("/vote")
async def vote(vote: Vote):
    if vote.option not in votes:
        raise HTTPException(status_code=400, detail="Invalid vote option")
    votes[vote.option] += 1
    return votes

@router.get("/results")
async def get_results():
    return votes
