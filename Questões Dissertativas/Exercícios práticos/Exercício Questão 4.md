# 🐍 Exemplo Prático em Python — Matriz de Confusão

Neste exemplo, vamos utilizar Python para criar uma **matriz de confusão**
em um problema simples de **classificação binária**, simulando a detecção de spam.

---

## 📦 Bibliotecas utilizadas:

```python
from sklearn.metrics import confusion_matrix, classification_report
```
---

## 📊 Dados reais e previstos:

1 → Spam
0 → Não spam

```python
# Valores reais
y_true = [1, 0, 1, 1, 0, 0, 1, 0]

# Valores previstos pelo modelo
y_pred = [1, 0, 0, 1, 0, 1, 1, 0]
```
---

## 🧮 Criando a matriz de confusão:

```python
cm = confusion_matrix(y_true, y_pred)
print(cm)
```

## 🔎 Saída esperada:

[[3 1]
 [1 3]]
 
---

## 📘 Interpretação da matriz
	
|            | Previsto 0 | Previsto 1 |
| ---------- | ---------- | ---------- |
| **Real 0** | 3 (VN)     | 1 (FP)     |
| **Real 1** | 1 (FN)     | 3 (VP)     |

- 3 Verdadeiros Negativos
- 3 Verdadeiros Positivos
- 1 Falso Positivo
- 1 Falso Negativo

---

## 📈 Métricas completas do modelo:

```python
print(classification_report(y_true, y_pred))
```

Exemplo de saída:

              precision    recall  f1-score   support

           0       0.75      0.75      0.75         4
           1       0.75      0.75      0.75         4

    accuracy                           0.75         8

---

## ✅ Conclusão

Este exemplo mostra como a matriz de confusão permite analisar o desempenho
de um modelo de classificação de forma detalhada, indo além da simples acurácia
e revelando o tipo de erro cometido pelo modelo.
