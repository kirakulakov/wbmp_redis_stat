import uvicorn

from app.main import config

if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        host=config.server.host,
        port=config.server.port,
        workers=config.server.workers,
        factory=True
    )
