#!/bin/bash
# Script to clear Quarto cache when needed

echo "Clearing Quarto cache..."

# Remove freeze directory
if [ -d "_freeze" ]; then
    rm -rf _freeze
    echo "✓ Removed _freeze directory"
fi

# Remove jupyter cache
if [ -d ".jupyter_cache" ]; then
    rm -rf .jupyter_cache
    echo "✓ Removed .jupyter_cache directory"
fi

echo "Cache cleared successfully!"