# 📚 Conjuntos de Dados em Machine Learning

## 📌 2. Explique o conceito de conjunto de treinamento, conjunto de validação e conjunto de teste em machine learning.

Em machine learning, nós costumamos dividir os dados em três conjuntos para treinar e avaliar um modelo de forma correta e justa: treinamento, validação e teste. Cada um tem um papel bem específico como veremos adiante:

## 📘 Conjunto de Treinamento (Training Set)

É o conjunto principal, usamos para **ensinar o modelo**.

- O modelo aprende os padrões dos dados aqui  
- Os parâmetros (pesos, coeficientes etc.) são ajustados com base nesses dados  
- Normalmente representa a maior parte dos dados (ex.: **60% a 80%**)  

👉 **Em resumo:** é onde o modelo ou "a máquina" aprende.

---

## 🔧 Conjunto de Validação (Validation Set)

É o conjunto que serve para **avaliar e ajustar o modelo durante o treinamento**.

- Usado para escolher hiperparâmetros (taxa de aprendizado, número de camadas, profundidade da árvore etc.)  
- Ajuda a detectar **overfitting** (quando o modelo “decora” os dados de treino)  
- O modelo **não aprende** com esses dados, apenas é avaliado  

👉 **Em resumo:** é onde nós ajustamos o modelo.

---

## 🧪 Conjunto de Teste (Test Set)

É o conjunto usado **somente no final**, depois que tudo já está definido.

- Avalia o desempenho final do modelo  
- Simula dados nunca vistos pelo modelo  
- Garante uma estimativa justa da capacidade de generalização  

👉 **Em resumo:** é onde comprovamos se o modelo realmente funciona.

---

## 📊 Exemplo de divisão comum

- **70%** → Treinamento  
- **15%** → Validação  
- **15%** → Teste  

_(É necessário salientar que os percentuais podem variar conforme o tamanho do dataset.)_

---

## 🎯 Ideia-chave

Cada conjunto tem um objetivo claro:

| Conjunto       | Função principal        |
|---------------|------------------------|
| Treinamento   | Aprender padrões       |
| Validação     | Ajustar e melhorar     |
| Teste         | Avaliação final        |
