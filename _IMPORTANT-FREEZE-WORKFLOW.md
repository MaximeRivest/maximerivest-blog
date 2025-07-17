# Quarto Freeze Workflow

## How it works

With `freeze: true` in your posts:

1. **Local Development**: When you run `quarto preview` or `quarto render`, code executes and results are saved to `_freeze/`
2. **GitHub Actions**: Uses the frozen results from `_freeze/` - NO code execution happens in CI
3. **Version Control**: You MUST commit the `_freeze/` directory to git for this to work!

## Important: Update your .gitignore

Since you want to "sign off" on executed results, you need to REMOVE `_freeze/` from `.gitignore` and commit it:

```bash
# Remove _freeze/ from .gitignore
# Then:
git add _freeze/
git commit -m "Add frozen execution results"
```

## When to re-execute code

To force re-execution of code:
1. Delete the specific file in `_freeze/posts/your-post/` 
2. Or run: `quarto render posts/your-post.qmd --execute-daemon-restart`
3. Or use the `clear-cache.sh` script to clear all caches

## Benefits

- Reproducible builds - exact same output every time
- No API calls or expensive computations during CI/CD
- You control when code executes
- Fast builds on GitHub Actions

## Freeze options

- `freeze: true` - Never re-execute (must manually clear cache)
- `freeze: auto` - Re-execute when code changes
- `freeze: false` - Always re-execute (default)