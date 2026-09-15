# Cameron Souza personal site

Static site. No build step.

## Deploy on GitHub Pages
1. Create a repository (for a user site, name it `CamSouza13.github.io`).
2. Copy `index.html`, `.nojekyll`, and the `assets/` folder to the repository root.
3. Commit and push to `main`.
4. In the repository: Settings > Pages > Source: Deploy from a branch > `main` / `(root)`.
5. The site is live at `https://CamSouza13.github.io/` within a few minutes.

## Custom domain (optional)
Add a `CNAME` file containing the domain (for example `camsouza.com`), then point the domain's DNS to GitHub Pages as described in GitHub's documentation, and enable "Enforce HTTPS".

## Editing
- Scroll story: each chapter is a `<section class="ch">`. `data-scene` picks the background photo, `data-k` (0 to 1) sets how open the boundary ring is, `data-val` and `data-credit` fill the corner readout.
- Now: update the four items and the month each term.
- Text: edit `index.html` directly.
- Images: replace files in `assets/img/` with the same names.
- New papers or talks: copy an `<li>` block in the Papers section and change the status label (`s-sub` submitted, `s-prep` in preparation, no class for planned).

## Image credits
All photographs are NASA images (public domain). Credits are listed in the page footer. NASA does not endorse this site.
