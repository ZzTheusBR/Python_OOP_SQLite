#Importa nossa arquivo Pessoa.py no diretório model
from model.Pessoa import Pessoa

#Exemplo de uso
matheus = Pessoa(1, "Matheus Barbosa")
print(matheus)

#Quero mostrar só compile
print(matheus.nome)