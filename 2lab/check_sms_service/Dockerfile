FROM python:3.13-trixie
RUN apt-get update && apt-get install -y zstd curl ca-certificates && rm -rf /var/lib/apt/lists/*
RUN curl -fsSL https://ollama.com/install.sh | sh
RUN pip install --no-cache-dir fastapi requests pydantic uvicorn
COPY app .
EXPOSE 8888
CMD ["sh", "-c", "ollama serve & until curl -s http://localhost:11434/ >/dev/null; do sleep 5; done; ollama pull qwen2.5:0.5b; exec uvicorn main:app --host 0.0.0.0 --port 8888"]
