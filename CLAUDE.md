# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is an Open WebUI deployment configured for Lagoon hosting. It's a containerized Python application that provides a web interface for AI models, specifically configured to work with external API services rather than local Ollama.

## Architecture

- **Base**: Built on Open WebUI v0.6.5 Docker image
- **Deployment**: Lagoon-compatible Docker setup with persistent data storage
- **Configuration**: Environment-based setup for API integration
- **Data Persistence**: `/app/backend/data` volume for user data and static files

## Development Environment

Uses devbox for environment management:
- Python 3.11
- Black for code formatting
- Pyright for type checking

## Key Commands

### Development
```bash
# Enter development environment
devbox shell

# Format Python code
black .

# Type checking
pyright
```

### Docker Operations
```bash
# Build and run locally
docker-compose up --build

# Access application at http://localhost:3000
```

### Setup
```bash
# Run initial setup (requires environment variables)
python setup.py
```

## Environment Variables Required for Setup

- `AMAZEEAI_BASE_URL`: API endpoint base URL
- `AMAZEEAI_API_KEY`: API authentication key  
- `AMAZEEAI_USER_EMAIL`: User email for initial account
- `AMAZEEAI_USER_NAME`: User display name
- `AMAZEEAI_USER_PASSWORD`: User password

## Key Configuration

- Application runs on port 8800 internally, mapped to 3000 externally
- Ollama API disabled (`ENABLE_OLLAMA_API=false`)
- Direct connections disabled for security
- Evaluation arena models disabled
- Data persisted to `./data` directory