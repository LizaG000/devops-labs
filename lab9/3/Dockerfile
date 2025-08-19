FROM python:3.10-slim AS builder
WORKDIR /app
COPY requirements.txt /app
COPY main.py /app/
RUN pip install --no-cache-dir -r requirements.txt

FROM python:3.10-slim as runtime
WORKDIR /app
COPY main.py /app/
COPY --from=builder /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]