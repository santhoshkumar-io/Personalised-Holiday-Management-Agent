import asyncio

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from autogen_agentchat.messages import TextMessage
from holiday_management.teams.holliday_team import team


class PlanRequest(BaseModel):
    content: str
    source: str = "User"


app = FastAPI(title="Holiday Management Api")

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# The team is a single shared object, so only one plan can run at a time.
team_lock = asyncio.Lock()


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse(request, "index.html")


@app.post("/plan")
async def plan_holiday(request: PlanRequest):
    async with team_lock:
        try:
            # Clear the previous conversation so each request starts fresh.
            await team.reset()
            task = TextMessage(content=request.content, source=request.source)
            response = await team.run(task=task)
            messages = [
                {"source": msg.source, "content": msg.content}
                for msg in response.messages
                if isinstance(getattr(msg, "content", None), str)
            ]
            return {"messages": messages, "stop_reason": response.stop_reason}
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
