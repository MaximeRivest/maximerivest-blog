#!/usr/bin/env python3
"""
Auto-load environment variables from .env files
Place this at the top of your Python scripts or import it
"""

import os
import sys
from pathlib import Path

def load_env_file(env_path):
    """Load environment variables from a .env file"""
    if not env_path.exists():
        return
    
    with open(env_path, 'r') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#') and '=' in line:
                key, value = line.split('=', 1)
                # Remove quotes if present
                value = value.strip('"\'')
                os.environ[key.strip()] = value

def auto_load_env():
    """
    Automatically load .env files from:
    1. Current directory
    2. Project root (first parent with .git)
    3. Home directory
    """
    current_dir = Path.cwd()
    
    # Load from current directory
    load_env_file(current_dir / '.env')
    
    # Load from project root (find .git directory)
    for parent in current_dir.parents:
        if (parent / '.git').exists():
            load_env_file(parent / '.env')
            break
    
    # Load from home directory as fallback
    load_env_file(Path.home() / '.env')

# Auto-load when imported
auto_load_env()

if __name__ == "__main__":
    print("Environment variables loaded:")
    for key in sorted(os.environ.keys()):
        if 'API_KEY' in key or 'TOKEN' in key:
            value = os.environ[key]
            print(f"{key}: {value[:10]}...{value[-4:] if len(value) > 14 else value}")