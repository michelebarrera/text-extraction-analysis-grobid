from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Leer texto
with open("../outputs/all_abstracts.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Crear nube
wordcloud = WordCloud(
    width=800,
    height=400,
    background_color="white"
).generate(text)

# Mostrar
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")

# Guardar imagen
plt.savefig("../outputs/keyword_cloud.png")

print("Keyword cloud creada correctamente.")
