# 📊 Matriz de Confusão

## 📌 O que é uma matriz de confusão e como ela é usada para avaliar o desempenho de um modelo preditivo?

A **matriz de confusão** é uma ferramenta fundamental para avaliar o desempenho de modelos
de **classificação** em Machine Learning. Ela permite comparar os **valores reais**
com os **valores previstos** pelo modelo, mostrando não apenas quantos erros ocorreram,
mas *como* eles ocorreram.

---

A matriz de confusão é uma **tabela** que resume os resultados de um modelo preditivo,
comparando:

- **Classe real**
- **Classe prevista**

Ela é especialmente útil em problemas de classificação binária,
como detecção de spam, diagnóstico médico ou análise de fraude.

---

## 🧩 Estrutura da matriz de confusão (classificação binária)

|                      | Previsto Positivo | Previsto Negativo |
|----------------------|------------------|------------------|
| **Real Positivo**    | Verdadeiro Positivo (VP) | Falso Negativo (FN) |
| **Real Negativo**    | Falso Positivo (FP) | Verdadeiro Negativo (VN) |

---

## 🔍 Significado dos termos

- **Verdadeiro Positivo (VP)**  
  O modelo previu positivo e acertou.

- **Verdadeiro Negativo (VN)**  
  O modelo previu negativo e acertou.

- **Falso Positivo (FP)**  
  O modelo previu positivo, mas o valor real era negativo.

- **Falso Negativo (FN)**  
  O modelo previu negativo, mas o valor real era positivo.

---

## 📈 Métricas derivadas da matriz de confusão

A matriz de confusão é a base para várias métricas importantes:

### 🔹 Acurácia
Proporção total de acertos do modelo:

Acurácia = (VP + VN) / (VP + VN + FP + FN)

### 🔹 Precisão
Entre os valores previstos como positivos, quantos realmente são positivos:

Precisão = VP / (VP + FP)

### 🔹 Recall (Sensibilidade)
Entre os valores positivos reais, quantos foram corretamente identificados:

Recall = VP / (VP + FN)


### 🔹 F1-score
Média harmônica entre precisão e recall:

F1 = 2 * (Precisão * Recall) / (Precisão + Recall)


---

## 🎯 Por que a matriz de confusão é importante?

- Permite entender **onde o modelo erra**
- Evita confiar apenas na acurácia
- Ajuda a decidir qual métrica é mais importante para o problema

📌 Exemplo:
- Em diagnósticos médicos, **falsos negativos** são extremamente perigosos.
- Em filtros de spam, **falsos positivos** podem ser mais prejudiciais.

---

## ✅ Conclusão

A matriz de confusão é uma ferramenta essencial para avaliar modelos de classificação,
pois fornece uma visão detalhada dos acertos e erros, permitindo análises mais
confiáveis e decisões mais conscientes.
