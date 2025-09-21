from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict

class CotaDia(BaseModel):
    """
    Representa o valor e as quantidades de cotas em um dia específico.
    """
    valor: float
    quantidades: List[float]


class CotaInput(BaseModel):
    """
    Representa o payload de entrada completo para o cálculo da taxa.
    """
    taxa: float
    cotas: List[CotaDia]


cotas_armazenadas: List[Dict] = []
taxa_armazenada: float = 0.0


app = FastAPI(
    title="API Taxa de Administração",
    description="Calcula a taxa de administração de cada cotista",
    version="1.0.0"
)


@app.post("/enviar_dados", summary="Enviar dados para o cálculo (POST)")
@app.put("/enviar_dados", summary="Atualizar dados para o cálculo (PUT)")
def enviar_dados(dados: CotaInput):
    """
    Recebe os dados de taxa e cotas e os armazena temporariamente, substituindo os dados anteriores se existirem.
    """
    global cotas_armazenadas, taxa_armazenada
    taxa_armazenada = dados.taxa
    cotas_armazenadas = dados.cotas
    return {"mensagem": "Dados armazenados e atualizados com sucesso."}


@app.get("/calcular_taxa", summary="Calcular taxa de administração")
def calcular_taxa():
    t = taxa_armazenada
    cotas = cotas_armazenadas

    if not cotas:
        raise HTTPException(status_code=404, detail="Nenhum dado de cota encontrado. Envie os dados primeiro usando /enviar_dados.")

    try:
        M = len(cotas[0].quantidades)
    except IndexError:
        return []

    taxas = [0.0] * M

    for i in range(len(cotas)):
        vi = cotas[i].valor
        quantidades_dia = cotas[i].quantidades
        
        for j in range(M):
            cij = quantidades_dia[j]
            taxas[j] += (cij * vi * t) / 252

    return taxas


@app.get("/cotistas", summary="Obter dados de cotas armazenados")
def get_cotistas():
    
    global cotas_armazenadas, taxa_armazenada
    if not cotas_armazenadas:
        raise HTTPException(status_code=404, detail="Nenhum dado de cota encontrado.")
    return {"taxa": taxa_armazenada, "cotas": cotas_armazenadas}


@app.delete("/cotistas", summary="Excluir dados de cotas armazenados")
def delete_cotistas():
    """
    Apaga todos os dados de taxa e cotas armazenados.
    """
    global cotas_armazenadas, taxa_armazenada
    cotas_armazenadas = []
    taxa_armazenada = 0.0
    return {"mensagem": "Dados de cotas excluídos com sucesso."}
