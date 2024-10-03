from dotenv import load_dotenv
import logging

load_dotenv()

from backend.server.server import app

if __name__ == "__main__":
    import uvicorn
    logging.basicConfig(level=logging.DEBUG)
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="debug")
