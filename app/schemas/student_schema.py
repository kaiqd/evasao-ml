from pydantic import BaseModel, Field


class StudentInput(BaseModel):
    idade: int = Field(..., description="Idade do aluno")
    sexo: str = Field(..., description="Sexo do aluno (M/F)")
    tipo_escola_medio: str = Field(..., description="Tipo de escola do ensino médio")
    nota_enem: float = Field(..., description="Nota do ENEM")
    renda_familiar: float = Field(..., description="Renda familiar em salários mínimos")
    trabalha: int = Field(..., description="1 se trabalha, 0 caso contrário")
    horas_trabalho_semana: int = Field(..., description="Horas de trabalho por semana")
    cra_1_sem: float = Field(..., description="CRA no primeiro semestre")
    reprovacoes_1_sem: int = Field(..., description="Quantidade de reprovações no 1º semestre")
    bolsista: int = Field(..., description="1 se bolsista, 0 caso contrário")
    distancia_campus_km: float = Field(..., description="Distância até o campus em km")
