#!/bin/bash

# Cleanup script for production deployment
# This script removes unnecessary files for a production deployment

echo "🧹 Cleaning up repository for production deployment..."

# Remove development/CI files
echo "Removing CI/CD files..."
rm -rf .github/

echo "Removing test files..."
rm -rf tests/

echo "Removing development configuration..."
rm -f .fernignore
rm -f poetry.lock

echo "Removing cleanup documentation..."
rm -f CLEANUP_SUMMARY.md
rm -f cleanup_for_production.sh

# Optional: Remove pyproject.toml if only using requirements.txt
# Uncomment the next line if you want to remove it
# rm -f pyproject.toml

echo "✅ Cleanup complete!"
echo ""
echo "Files removed:"
echo "  - .github/ (CI/CD workflows)"
echo "  - tests/ (test files)"
echo "  - .fernignore (Fern configuration)"
echo "  - poetry.lock (development lock file)"
echo "  - cleanup scripts and documentation"
echo ""
echo "Repository is now ready for production deployment!"
echo "Don't forget to set SUPERAGENT_API_TOKEN in your Render environment variables."