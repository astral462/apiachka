from fastapi import FastAPI, HTTPException, Header
from pydantic import BaseModel
import random

app = FastAPI(
    title="Назва",
    description="тут ми дістаємо передбачення",
    version="1.0.0",
)

secret_key = "secret_123"

class MagicResponse(BaseModel):
    message: str
    status: str

wishes = [
    "сьогодні все буде добре",
    "фронтенди будут получать менше ніж бекенди",
    "скоро прибавка",
]

@app.get("/random-wish", response_model=MagicResponse)
def get_random_wishes(key: str = Header()):

    if key != "secret_123":
        raise HTTPException(
            status_code=401,
            detail = "Неправильно, або відсутній ключ у headers"
        )
    else:
        return MagicResponse(
            message=random.choice(wishes).strip("()""[]"),
            status="200"
        )


@app.get("/")
def index():
    return "ПРивіт"
