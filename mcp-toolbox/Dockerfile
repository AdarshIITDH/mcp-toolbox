FROM python:3.12-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY server.py .

EXPOSE 8000

# mcpo runs the MCP server command and exposes it as OpenAPI/HTTP
CMD ["sh", "-c", "mcpo --port 8000 -- python /app/server.py"]
