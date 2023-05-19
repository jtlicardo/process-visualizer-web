FROM python:3.9

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt && \
    python -m spacy download en_core_web_sm && \
    python -m spacy download en_core_web_md

RUN apt-get update && \
    apt-get install -y graphviz && \
    rm -rf /var/lib/apt/lists/* && \
    echo 'export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/lib/x86_64-linux-gnu/graphviz' >> ~/.bashrc

COPY . .

EXPOSE 5000

CMD ["gunicorn", \
"--chdir", "src", \
"server:app", \
"--worker-class", "gevent", \
"--workers", "1", \
"--bind", "0.0.0.0:8000"]
