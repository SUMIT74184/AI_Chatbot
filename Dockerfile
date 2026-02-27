# ---- Builder Stage ----
FROM python:3.10-alpine AS builder
WORKDIR /install


RUN apk add --no-cache gcc musl-dev libffi-dev

COPY requirements.txt .
RUN pip install --prefix=/install --no-cache-dir -r requirements.txt

# ---- Final Stage ----
FROM python:3.10-alpine
WORKDIR /app
COPY --from=builder /install /usr/local
COPY app app

EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]