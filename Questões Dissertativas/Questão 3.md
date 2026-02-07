# Dados Ausentes em Machine Learning

## 📌 3. Explique como você lidaria com dados ausentes em um conjunto de dados de treinamento.

Como lidar com dados ausentes em um conjunto de treinamento em Machine Learning?

Dados ausentes (missing values) são comuns em conjuntos reais e, se não forem tratados corretamente, podem prejudicar o desempenho do modelo ou até gerar erros no treinamento.

Eu lidaria com dados ausentes seguindo estas etapas:

## 1️⃣ Entender o motivo dos dados ausentes:

Antes de qualquer ação, é importante investigar por que os dados estão faltando:

- Erro de coleta?

- Informação não aplicável?

- Falha no preenchimento?

Isso ajuda a decidir o melhor tratamento e evita remover ou alterar informações importantes.

---

## 2️⃣ Analisar a quantidade e o padrão dos dados ausentes:

- Se poucos valores estão ausentes, o impacto tende a ser pequeno.

- Se muitas linhas ou colunas têm valores faltantes, é preciso mais cuidado.

- Verificar se os dados ausentes ocorrem de forma aleatória ou seguem algum padrão.

---

## 3️⃣ Estratégias para tratar dados ausentes:

🔹 Remoção de dados:

- Remover linhas com valores ausentes → indicado quando a quantidade é pequena.
- Remover colunas → quando a variável tem muitos valores ausentes e pouca relevância.

⚠️ Deve ser usada com cautela para não perder informação demais.

🔹 Imputação de valores:

Substituir os valores ausentes por estimativas:
- Média ou mediana → comum para variáveis numéricas.
- Moda → para variáveis categóricas.
- Valor constante (ex.: 0 ou “desconhecido”) → em alguns contextos específicos.

Obs.: A mediana costuma ser preferida quando há outliers.

🔹 Métodos mais avançados

- Imputação baseada em modelos (KNN, regressão, árvores).
- Imputação múltipla, preservando a variabilidade dos dados.

Obs.: Essas abordagens costumam gerar melhores resultados, mas aumentam a complexidade.

---

## 4️⃣ Separar corretamente treino, validação e teste:

Um ponto essencial:
👉 A imputação deve ser ajustada apenas no conjunto de treinamento.
Depois, os mesmos parâmetros são aplicados aos conjuntos de validação e teste, evitando data leakage.

---

## 5️⃣ Avaliar o impacto no modelo

Após o tratamento:

- Treinar o modelo.
- Comparar métricas antes e depois da imputação.
- Verificar se o tratamento melhorou a generalização.

---

## Resposta final:

Eu analisaria a causa e o padrão dos dados ausentes, escolheria a estratégia mais adequada (remoção ou imputação), aplicaria o tratamento apenas no conjunto de treinamento e avaliaria o impacto nos resultados do modelo.
