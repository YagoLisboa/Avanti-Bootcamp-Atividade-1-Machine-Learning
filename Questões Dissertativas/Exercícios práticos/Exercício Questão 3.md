# Tratamento de Dados Ausentes em Machine Learning

Este repositório apresenta um **exemplo prático de como lidar com dados ausentes (missing values)** em um conjunto de treinamento de *Machine Learning*, utilizando **Python**, **pandas** e **scikit-learn**, seguindo **boas práticas para evitar vazamento de dados (data leakage)**.

O cenário utilizado é uma **classificação de e-mails (spam / não spam)** com variáveis numéricas que contêm valores ausentes.

---

## 📌 Tecnologias Utilizadas

- Python 3.x  
- pandas  
- numpy  
- scikit-learn  

---

## 📂 Estrutura do Exemplo

O fluxo do projeto segue as etapas clássicas de um pipeline de Machine Learning:

1. Criação do dataset com dados ausentes  
2. Separação entre variáveis de entrada e variável alvo  
3. Divisão em conjunto de treino e teste  
4. Tratamento de dados ausentes por imputação  
5. Treinamento do modelo  
6. Avaliação do desempenho  
7. Uso de Pipeline como boa prática  

---

## 1️⃣ Criando um dataset de exemplo com dados ausentes

```python
import pandas as pd
import numpy as np

# Criando um dataset fictício
dados = {
    "num_palavras": [120, 300, np.nan, 250, 180, np.nan],
    "num_links": [2, np.nan, 1, 0, 3, 1],
    "spam": [0, 1, 0, 1, 0, 1]
}

df = pd.DataFrame(dados)
print(df)
```
---
## Exemplo de saída:

   num_palavras  num_links  spam
0         120.0        2.0     0
1         300.0        NaN     1
2           NaN        1.0     0
3         250.0        0.0     1
4         180.0        3.0     0
5           NaN        1.0     1

---

## 2️⃣ Separando variáveis de entrada e variável alvo:

```python
X = df.drop("spam", axis=1)
y = df["spam"]
```

---

## 3️⃣ Separando os conjuntos de treino e teste:

A separação correta evita vazamento de dados, garantindo uma avaliação mais realista do modelo.

```python
from sklearn.model_selection import train_test_split

X_treino, X_teste, y_treino, y_teste = train_test_split(
    X, y, test_size=0.3, random_state=42
)
```

---

## 4️⃣ Tratamento de dados ausentes (Imputação):

Neste exemplo, utilizamos a mediana, que é menos sensível a outliers e adequada para variáveis numéricas.

```python
from sklearn.impute import SimpleImputer

imputador = SimpleImputer(strategy="median")

# Ajuste apenas no conjunto de treino
X_treino_imputado = imputador.fit_transform(X_treino)

# Aplicação no conjunto de teste
X_teste_imputado = imputador.transform(X_teste)
```

---

## 5️⃣ Treinamento do modelo:

Utilizamos Regressão Logística, um modelo clássico para problemas de classificação binária.

```python
from sklearn.linear_model import LogisticRegression

modelo = LogisticRegression()
modelo.fit(X_treino_imputado, y_treino)
```

---

## 6️⃣ Avaliação do modelo:

```python
from sklearn.metrics import accuracy_score

y_pred = modelo.predict(X_teste_imputado)
acuracia = accuracy_score(y_teste, y_pred)

print(f"Acurácia do modelo: {acuracia:.2f}")
```

---

## 7️⃣ Boa prática: uso de Pipeline:

O uso de Pipeline organiza o fluxo de pré-processamento e treinamento, além de reduzir o risco de erros e vazamento de dados.

```python
from sklearn.pipeline import Pipeline

pipeline = Pipeline([
    ("imputacao", SimpleImputer(strategy="median")),
    ("modelo", LogisticRegression())
])

pipeline.fit(X_treino, y_treino)
y_pred = pipeline.predict(X_teste)

print("Acurácia com Pipeline:", accuracy_score(y_teste, y_pred))
```

---

## 🧠 Principais Aprendizados:

- Dados ausentes são comuns em datasets reais.
- A imputação deve ser ajustada somente com dados de treino.
- O 'SimpleImputer' facilita o tratamento de valores ausentes.
- 'Pipeline' é uma boa prática essencial em projetos de Machine Learning.
- Um pré-processamento correto melhora a confiabilidade do modelo.

## 📎 Conclusão

O tratamento adequado de dados ausentes é uma etapa fundamental em projetos de Machine Learning.
Aplicar boas práticas, como imputação correta e uso de pipelines, contribui diretamente para modelos mais robustos, confiáveis e com melhor capacidade de generalização.
