from fastapi import FastAPI
from app.routes import campus_routes

app = FastAPI()

@app.get('/')
def index():
    return {'message': 'Hello, World!'}

app.include_router(campus_routes.router)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(
        "main:app",
        host='127.0.0.1',
        port=8000,
        reload=True
    )
