# LLEO Lab
Learning · Language · Exploration · Observation

Public research website and shared lab starter, maintained by Adam A. Bramlett.

- Website: https://AdamAnderB.github.io/lleo-lab/
- [Lab handbook](handbook/onboarding.md)
- [Project starter](templates/project/README.md)
- [Member profile guide](templates/member/README.md)
- [Contributing](CONTRIBUTING.md)
- [Public/private policy](handbook/public-private.md)

## Edit and preview
This is a dependency-free static site. Python 3 regenerates the HTML; GitHub Pages serves the committed files without a framework build.

```sh
python3 build.py
python3 check.py
python3 -m http.server 8000
```
Open http://localhost:8000. Edit page content in `build.py`, the visual system in `assets/style.css`, and profiles in `members.json`. Regenerate and commit HTML with source changes. No installation or database is required. All navigation uses relative paths, so the site can move to an organization later.

## Publishing
GitHub Settings → Pages → Deploy from a branch → main → /(root). An empty `.nojekyll` disables Jekyll. Site content is public. GitHub handles sign-in and project permissions; this website has no private member area.

## Scope and provenance
The logo is the existing user-supplied `ChatGPT Image Nov 11, 2026, 07_35_38 PM.png`, copied unchanged. Palette: deep navy #142e40, warm ivory #faf6ed, golden orange #df9639.
Dissertation and earlier collaborations are explicitly labeled as foundations/prior work. No students, collaborators, studies, positions, or publications are invented. The initial repository belongs to AdamAnderB, not a GitHub organization.

## Grow into an organization
Once the owner creates a dedicated organization and completes GitHub’s terms/verification, transfer this repository through repository settings. Update canonical links in build.py, handbook links, CODEOWNERS, and README; regenerate the site and reconfigure Pages. Separate handbook and project-template repositories can be extracted from their folders when useful. Do not transfer or publicize private study repositories without review.

## Rights
No blanket license is granted for the logo, research materials, or linked publications. Linked projects retain their own licenses. Agree an explicit code/content license before external reuse; a public repository alone is not a license.
