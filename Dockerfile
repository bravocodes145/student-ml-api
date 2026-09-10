FROM python:3.12.11-slim

ARG APP_VERSION=unknown
ARG VCS_REF=unknown
ARG VCS_URL=unknown
ARG BUILD_DATE=unknown

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .
COPY VERSION .

EXPOSE 5000
LABEL org.opencontainers.image.title="student-ml-api" \
	org.opencontainers.image.version="$APP_VERSION" \
	org.opencontainers.image.revision="$VCS_REF" \
	org.opencontainers.image.source="$VCS_URL" \
	org.opencontainers.image.created="$BUILD_DATE"

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "5000"]
