FROM ghcr.io/open-webui/open-webui:v0.6.5

ENV ENABLE_OLLAMA_API=false \
    ENABLE_DIRECT_CONNECTIONS=false \
    ENABLE_EVALUATION_ARENA_MODELS=false \
    ENABLE_WEB_SEARCH=true \
    VECTOR_DB=pgvector \
    RAG_EMBEDDING_ENGINE=openai \
    RAG_EMBEDDING_MODEL=embeddings \
    STATIC_DIR=/app/backend/data/static \
    DATA_DIR=/app/backend/data \
    PORT=8800