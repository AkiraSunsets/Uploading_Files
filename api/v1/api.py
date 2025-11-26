from fastapi import APIRouter

from api.v1.endpoints import curso, files

api_router = APIRouter()

api_router.include_router(curso.router, prefix="/cursos", tags=["cursos"])

api_router.include_router(files.router, prefix="/files", tags=["Files"])



