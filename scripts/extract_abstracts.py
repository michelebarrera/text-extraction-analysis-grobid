import os
from lxml import etree

# Ruta donde están los XML
DATA_PATH = "../data"
OUTPUT_FILE = "../outputs/all_abstracts.txt"

# Namespace TEI 
NS = {"tei": "http://www.tei-c.org/ns/1.0"}

all_abstracts = []

for file in os.listdir(DATA_PATH):
    if file.endswith(".tei.xml"):
        file_path = os.path.join(DATA_PATH, file)

        tree = etree.parse(file_path)

        abstract = tree.find(".//tei:abstract", namespaces=NS)

        if abstract is not None:
            text = " ".join(abstract.itertext())
            all_abstracts.append(text)

# Guardar todo en un archivo
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    for abs_text in all_abstracts:
        f.write(abs_text + "\n\n")

print("Abstracts extraídos correctamente.")
