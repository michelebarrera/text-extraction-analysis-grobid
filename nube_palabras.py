import os
from bs4 import BeautifulSoup
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def extract_abstracts(folder_path):
    all_abstracts = ""
    for file in os.listdir(folder_path):
        if file.endswith(".xml"):
            with open(os.path.join(folder_path, file), 'r', encoding='utf-8') as f:
                soup = BeautifulSoup(f, 'lxml-xml')
                # TEI usa el tag <abstract>
                abstract = soup.find('abstract')
                if abstract:
                    all_abstracts += abstract.get_text() + " "
    return all_abstracts

# Generación
text = extract_abstracts('./mis_xmls/')
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
