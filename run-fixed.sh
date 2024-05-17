#!/bin/bash

# to stop on first error
set -e

# Delete older .pyc files
# find . -type d \( -name env -o -name venv  \) -prune -false -o -name "*.pyc" -exec rm -rf {} \;

# Activate the virtual environment (Windows)
source fyle/Scripts/activate  # Use forward slashes on Windows

# Run required migrations
export FLASK_APP=core/server.py

# Initialize and upgrade database migrations (uncomment if needed)
# flask db init -d core/migrations/
# flask db migrate -m "Initial migration." -d core/migrations/
# flask db upgrade -d core/migrations/

# Run Flask application directly
python -m core.server  # Use 'python' command for Windows
