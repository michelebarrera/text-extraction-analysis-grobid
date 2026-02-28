import os
from lxml import etree
import matplotlib.pyplot as plt

DATA_PATH = "../data"
NS = {"tei": "http://www.tei-c.org/ns/1.0"}

papers = []
figure_counts = []

for file in os.listdir(DATA_PATH):
    if file.endswith(".tei.xml"):
        file_path = os.path.join(DATA_PATH, file)
        tree = etree.parse(file_path)

        figures = tree.findall(".//tei:figure", namespaces=NS)

        papers.append(file.replace(".tei.xml", ""))
        figure_counts.append(len(figures))

# Crear gráfica
plt.bar(papers, figure_counts)
plt.xticks(rotation=45)
plt.ylabel("Number of Figures")
plt.tight_layout()

plt.savefig("../outputs/figures_per_paper.png")

print("Gráfica de figuras creada correctamente.")
