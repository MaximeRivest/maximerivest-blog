# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Codebase Overview

This is a Quarto-based personal blog for maximerivest.com with custom styling, automated deployment, and support for both R and Python code execution.

## Essential Commands

### Development
```bash
# Preview blog locally with hot reload
quarto preview

# Build the entire site (outputs to _site/)
quarto render

# Render a specific post
quarto render posts/my-post.qmd

# Force re-execution of code in a post
quarto render posts/my-post.qmd --execute-daemon-restart

# Clear all caches (when code isn't re-executing)
./clear-cache.sh
```

### Deployment
Automatic deployment via GitHub Actions on push to `main`. The site deploys to GitHub Pages at maximerivest.com.

## Architecture & Key Concepts

### Freeze Workflow
Posts use `freeze: true` to cache code execution results in `_freeze/`. This means:
- Code executes locally during development
- GitHub Actions uses cached results (no code execution in CI)
- The `_freeze/` directory MUST be committed to git
- To re-execute code, delete the specific cache or use `clear-cache.sh`

### Post Management
- Posts with `[wip]` in the title are automatically hidden from homepage and listings
- Hidden via R filtering in `index.qmd` and JavaScript in `posts.qmd`
- WIP posts remain accessible via direct URL

### Styling Architecture
The blog uses a layered SCSS approach:
1. `styles-light.scss` / `styles-dark.scss` - Base theme styles
2. `styles-mobile.scss` - Responsive design for all screen sizes
3. `styles-code-copy-fix.scss` - Fixes for code copy button behavior
4. `styles-zen-buttons.scss` - Removes gradient buttons for minimal aesthetic

All styles are compiled by Quarto and applied in order.

### Content Types
- `.qmd` files: Quarto markdown with executable code chunks
- `.ipynb` files: Jupyter notebooks (auto-converted by Quarto)
- Python scripts with `# %%` cells can be converted using Jupytext

### Image Handling
Images must be:
1. Placed in the `posts/` directory
2. Listed in `_quarto.yml` under `resources:` (already configured for *.jpg, *.jpeg, *.png)
3. Referenced with relative paths in posts

### Dependencies
- **R**: Required for `index.qmd` (uses R for dynamic post listing)
- **Python**: Required for posts with Python code
- **Key Python packages**: jupyter-cache (for freeze workflow), dspy-ai, pandas, matplotlib
- See `requirements.txt` for full Python dependencies

## Critical Files

- `_quarto.yml` - Main configuration (themes, resources, output settings)
- `index.qmd` - Homepage with R code that filters posts
- `.github/workflows/deploy.yml` - GitHub Actions deployment pipeline
- `IMPORTANT-FREEZE-WORKFLOW.md` - Detailed freeze workflow documentation

## Common Issues & Solutions

1. **YAML parsing errors**: Usually caused by missing blank line after YAML frontmatter or hidden characters
2. **Images not showing in production**: Ensure images are in `resources:` section of `_quarto.yml`
3. **Code not re-executing**: Clear cache with `./clear-cache.sh` or delete specific `_freeze/posts/[post-name]/` directory
4. **Posts not hiding with [wip]**: Check that JavaScript is loading correctly in `posts.qmd`