from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from route import location_router


app = FastAPI()
# cm = cachemanager.CacheManager()

# CORS 설정
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(router=location_router)
