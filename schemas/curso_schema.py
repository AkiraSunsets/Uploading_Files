from typing import Optional
from pydantic import BaseModel as SCBaseModel, ConfigDict

class CursoSchema(SCBaseModel):
    id: Optional[int] = None
    nome: str
    aulas: int
    horas: int

    model_config = ConfigDict(from_attributes=True, extra="forbid")