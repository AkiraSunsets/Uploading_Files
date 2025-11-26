
#imports da lib do fastapi
from fastapi import APIRouter, Form, UploadFile, File, status, Depends, HTTPException, Header
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from core.deps import get_session
from models.files_models import StoredFile

router = APIRouter()

@router.post("/")
async def create_upload_file(file: UploadFile = File(...)):
    return {"Filename": file.filename}


@router.post("/savefile/")
async def save_upload_file(file: UploadFile = File(...)):

    #abre ou cria um arquivo binário em um diretório local e escreve seu conteúdo
    with open (f'api/v1/endpoints/uploads/{file.filename}', "wb") as f:
        f.write(file.file.read())

        return {"message": f"File '{file.filename}' saved sucessfully"}
    

#fazendo upload de multiplos arquivos

@router.post("/multiplesfiles")
async def multiple_files(files: List[UploadFile] = File(...)):
    return {"filenames": [file.filename for file in files]}


@router.post("/upload_db")
async def upload_file_to_db(file: UploadFile = File(...), db: AssyncSession = Depends(get_session)):
    try:
        content = await file.read()

        novo_file = StoredFile (
            filename = file.filename,
            content_type = file.content_type,
            content = content
        )

        db.add(novo_file)
        await db.commit()
        await db.refresh(novo_file)

        return {
            "id": novo_file.id,
            "filename": novo_file.filename,
            "content_type": novo_file.content_type
        }
    
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        