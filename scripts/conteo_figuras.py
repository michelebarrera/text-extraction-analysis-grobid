import pandas as pd

def count_figures(folder_path):
    data = []
    for file in os.listdir(folder_path):
        if file.endswith(".xml"):
            with open(os.path.join(folder_path, file), 'r', encoding='utf-8') as f:
                soup = BeautifulSoup(f, 'lxml-xml')
                num_figures = len(soup.find_all('figure'))
                data.append({"Paper": file[:15], "Figures": num_figures}) # Nombre corto
    return pd.DataFrame(data)

df = count_figures('./mis_xmls/')
df.plot(kind='bar', x='Paper', y='Figures', legend=False)
plt.title("Número de figuras por artículo")
plt.ylabel("Cantidad")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
