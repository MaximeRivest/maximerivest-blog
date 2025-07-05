# maximerivest-blog

This repository contains the source for [maximerivest.com](https://maximerivest.com).
Content is written with [Quarto](https://quarto.org) using notebooks or
Python scripts in Jupytext "percent" format.

## Writing posts

Add new `.qmd` or `.ipynb` files under `posts/`. Python scripts can be
written with `# %%` cells and converted using Jupytext.
Run `quarto preview` to build and preview the site locally.

## Deployment

Changes pushed to `main` are built and deployed automatically to the
`gh-pages` branch via GitHub Actions. The `CNAME` file configures the
custom domain `maximerivest.com` for GitHub Pages.
