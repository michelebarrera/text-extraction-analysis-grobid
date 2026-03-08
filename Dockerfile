FROM python:3.10

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY data /app/data
COPY scripts /app/scripts 
COPY outputs /app/outputs

CMD ["python", "scripts/extract_abstracts.py"]


