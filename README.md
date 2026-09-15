# Cameron Souza personal site

Static site for GitHub Pages. No build step.

## Deploy
1. Create a repository named `CamSouza13.github.io`.
2. Copy everything in this folder to the repository root, including the hidden `.github` folder and `.nojekyll`.
3. Commit and push to `main`.
4. Settings > Pages > Source: Deploy from a branch > `main` / `(root)`.
5. Settings > Actions > General > Workflow permissions: select "Read and write permissions" so the data job can commit.
6. The site goes live at `https://CamSouza13.github.io/` within a few minutes.

Custom domain (optional): add a `CNAME` file with the domain, point DNS to GitHub Pages, and enable "Enforce HTTPS".

## Medium blog feed
- `assets/data/config.json` holds the Medium handle (`cam.souza`).
- The workflow `.github/workflows/update-data.yml` runs daily (and on demand from the Actions tab). It reads `https://medium.com/feed/@cam.souza` and writes the latest posts to `assets/data/medium.json`. The Writing section shows the three newest.
- Until a story is published, the section shows a short note and the Medium buttons.
- Run it by hand any time: Actions > Update site data > Run workflow.

## CO2 chart
The same workflow downloads NOAA's Mauna Loa monthly file into `assets/data/co2.json`. The page also carries an embedded copy so the chart works if that file is missing.

## Editing
- Text: edit `index.html`.
- Images: replace files in `assets/img/` with the same names.
- Now section: update the three items and the month each term.
- Publications: copy an `<li>` in the Publications box. Use `pill on` for submitted or published, `pill` for in preparation.
- CV: `assets/cv/Cameron_Souza_CV.pdf`. Replace the file with the same name to update it.
- Profiles (ORCID, LinkedIn, GitHub, Zenodo, Medium) are in the Contact section. The Zenodo link searches by your ORCID, so uploads show up once your ORCID is attached to them.

## Local preview
`python -m http.server` in this folder, then open http://localhost:8000. Opening the file directly works too, but the Medium feed only loads over http.

## Credits
Photographs: NASA (public domain). CO2 data: NOAA GML and Scripps Institution of Oceanography. Credits are also in the page footer.
