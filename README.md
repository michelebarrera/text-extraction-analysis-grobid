# Análisis de artículos científicos usando Grobid

## Descripción

Este proyecto realiza un análisis básico de artículos científicos en formato PDF utilizando Grobid para extraer información estructurada en formato TEI XML.

A partir de los XML generados, se desarrollaron varios scripts en Python para analizar el contenido de los artículos.

El programa realiza tres tareas principales:

- Generar una nube de palabras a partir de los abstracts de los artículos
- Crear una visualización que muestra el número de figuras por artículo
- Extraer los enlaces encontrados en cada paper

El objetivo del proyecto es demostrar buenas prácticas de reproducibilidad en investigación.

---

## Dataset

Se seleccionaron 10 artículos científicos de acceso abierto obtenidos desde arXiv.
Cada artículo fue procesado utilizando Grobid para convertir los archivos PDF en documentos TEI XML.

---

## Estructura del proyecto

- data/ → artículos y XML generados por Grobid
- scripts/ → scripts de análisis en Python
- outputs/ → resultados generados por los scripts


---

## Instalación del entorno

- Clonar el repositorio
- Crear un entorno virtual:
python -m venv venv
source venv/bin/activate
- Instalar dependencias: pip install -r requirements.txt

---

## Ejecución de los scripts

Ejecutar los scripts desde la carpeta `scripts`.

- Extraer abstracts: python extract_abstracts.py
- Generar la nube de palabras: python keyword_cloud.py
- Contar figuras por artículo: python count_figures.py
- Extraer enlaces: python extract_links.py

Los resultados se guardarán en la carpeta `outputs`.

---

## Ejecución usando Docker

(desde la carpeta donde esta el Dockerfile)
- Construir la imagen: docker build -t paper-analysis .
- Ejecutar el contenedor: docker run paper-analysis

---

## Validación de los resultados
Para validar los resultados obtenidos se realizaron las siguientes comprobaciones:

**Nube de palabras**
Se revisaron manualmente varios abstracts extraídos de los XML y se verificó que las palabras más frecuentes en la nube correspondían con los temas principales de los artículos.

**Número de figuras**
Se inspeccionaron manualmente algunos archivos XML para comprobar que el número de etiquetas `<figure>` coincidía con los valores mostrados en la visualización generada.

**Extracción de enlaces**
Se revisaron las secciones de referencias de algunos artículos y se comprobó que los enlaces extraídos coincidían con los encontrados en el XML.

---

## Limitaciones

Este proyecto tiene varias limitaciones:
- La extracción depende de la calidad del XML generado por Grobid.
- Algunos artículos pueden no contener enlaces explícitos.
- El conteo de figuras se basa únicamente en la presencia de la etiqueta `<figure>` en el XML.

---

## Licencia

Este proyecto está distribuido bajo licencia Apache 2.0.
