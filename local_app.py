from os.path import join, dirname
import uvicorn
from dotenv import load_dotenv

load_dotenv(join(dirname(__file__), '.env.dev'), override=True)

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, log_level="debug", reload=True)
