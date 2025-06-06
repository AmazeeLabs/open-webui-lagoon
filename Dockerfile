FROM ghcr.io/open-webui/open-webui:v0.6.5

ENV ENABLE_OLLAMA_API=false
ENV ENABLE_DIRECT_CONNECTIONS=false
ENV ENABLE_EVALUATION_ARENA_MODELS=false
ENV STATIC_DIR=/app/backend/data/static
ENV DATA_DIR=/app/backend/data
ENV PORT=8800
