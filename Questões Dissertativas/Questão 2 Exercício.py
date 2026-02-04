# Exemplo em Python: Classificação de e-mails (Spam vs Não Spam):
# Vamos fazer um exemplo usando classificação de e-mails spam, mantendo os conjuntos de treinamento, validação e testes.
# Vamos usar:
# Texto de e-mails;
# TF-IDF para transformar texto em números; e
# Naive Bayes, que é clássico para spam.

# 1. Importações:
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

# 2. Dataset de exemplo (simples mas didático):
emails = [
    "Ganhe dinheiro rápido agora",
    "Oferta imperdível, clique aqui",
    "Você ganhou um prêmio",
    "Promoção exclusiva por tempo limitado",
    "Oi, podemos marcar a reunião amanhã?",
    "Segue o relatório solicitado",
    "Vamos almoçar juntos hoje?",
    "Reunião confirmada para segunda-feira",
    "Atualização do projeto em anexo",
    "Podemos conversar mais tarde?"
]

# 1 = spam, 0 = não spam
labels = [1, 1, 1, 1, 0, 0, 0, 0, 0, 0]

# 3. Separando treino, validação e teste
# Treino (70%) e temporário (30%):
X_train, X_temp, y_train, y_temp = train_test_split(
    emails, labels, test_size=0.3, random_state=42
)

# Validação (15%) e teste (15%):
X_val, X_test, y_val, y_test = train_test_split(
    X_temp, y_temp, test_size=0.5, random_state=42
)

# 4. Vetorização do texto (TF-IDF):
vectorizer = TfidfVectorizer()

X_train_vec = vectorizer.fit_transform(X_train)
X_val_vec = vectorizer.transform(X_val)
X_test_vec = vectorizer.transform(X_test)
# ⚠️ Importante: o vetorizador é ajustado apenas com o conjunto de treino

# 5. Treinando o modelo (somente treino):
model = MultinomialNB()
model.fit(X_train_vec, y_train)

# 6. Avaliação no conjunto de validação:
y_val_pred = model.predict(X_val_vec)
val_accuracy = accuracy_score(y_val, y_val_pred)

print(f"Acurácia na validação: {val_accuracy:.2f}")
# Aqui nós poderíamos ajustar:
# alpha do Naive Bayes,
#n-gramas do TF-IDF,
#remoção de stopwords.

# 7. Avaliação final no conjunto de teste:
y_test_pred = model.predict(X_test_vec)
test_accuracy = accuracy_score(y_test, y_test_pred)

print(f"Acurácia no teste: {test_accuracy:.2f}")

# O que esse exemplo deixa claro:
#Texto bruto → números (TF-IDF),
#Modelo aprende só no treino,
#Validação ajusta,
#Teste avalia generalização,
#Nenhum ajuste usando dados de teste.