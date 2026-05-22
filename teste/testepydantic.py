import pandas as pd
from pydantic import BaseModel, Field, ValidationError

# 1. Modelo para validar cada linha do DataFrame
class Produto(BaseModel):
    id: int
    nome: str
    preco: float = Field(gt=0) # O preço deve ser maior que zero

# 2. DataFrame simulando dados de uma planilha ou CSV
dados = {
    'id': [1, 2, 3],
    'nome': ['Teclado', 'Mouse', 'Monitor'],
    'preco': [150.00, 80.00, 10.00] # O terceiro produto vai falhar!
}
df = pd.DataFrame(dados)

# 3. Validando as linhas
for index, linha in df.iterrows():
    try:
        # Converte a linha do Pandas em dicionário e valida no Pydantic
        Produto(**linha.to_dict())
    except ValidationError as e:
        print(self_error := f"Erro na linha {index} (Produto: {linha['nome']}): {e.json()}")
