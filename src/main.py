from fastapi import FastAPI
import uvicorn
from loguru import logger

app = FastAPI()

@logger.catch()
def run_api():
    logger.info(f"Démarrage de l'API REST pour API HOUR !")
    uvicorn.run(
        app="api:app",
        port=8080,
        host="0.0.0.0",
        reload=True,
        workers=2,
        access_log=True,
    )

if __name__ == "__main__":
    run_api()
    