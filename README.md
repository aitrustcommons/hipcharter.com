# hipcharter.com: forwarding to aitrustcommons.org

Since Nov 2026 (AITC task #625) the HIP Charter lives on AI Trust Commons:

- https://aitrustcommons.org/hip-charter/ (the charter; the old home page's opening is on top)
- https://aitrustcommons.org/hip-charter/story/ (how it was made)

This repo now publishes only `forwards/`: one small page per old address that sends the visitor to the new one. Each forward page has an instant meta refresh, a canonical link to the new page and a noindex tag. A one-line script carries any #section through. The images stay at their old addresses under `forwards/assets/images/`, so anything that embeds them keeps working.

| Old address | Goes to |
|---|---|
| hipcharter.com/ | aitrustcommons.org/hip-charter/ |
| hipcharter.com/charter/ | aitrustcommons.org/hip-charter/ |
| hipcharter.com/story/ | aitrustcommons.org/hip-charter/story/ |
| hipcharter.com/about/ | aitrustcommons.org/about/ |
| anything else (404.html) | aitrustcommons.org/hip-charter/ |

`.github/workflows/deploy.yml` publishes `forwards/` on every push to main. The Pages source must be "GitHub Actions".

## Rollback

The old MkDocs site is still on the `gh-pages` branch. To bring it back: disable the deploy workflow (`gh workflow disable deploy.yml`), switch the Pages source to "Deploy from a branch: gh-pages, root", and check that the custom domain is still hipcharter.com with HTTPS on. Don't push to gh-pages.

## The old site's source

`docs/`, `mkdocs.yml`, `overrides/`, `internal/` and `visual-concepts/` are kept for history. Nothing builds them now. The text that moved to AITC was lightly edited there; the change list is in ns-2026-the-big-push, ai-trust-commons/site-redesign/hip-merge/content-pass.md.

---

# The Human Intelligence Partnership Charter

**Stop Calling It Artificial. Start Building WITH Intelligence.**

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

The HIP Charter defines four patterns of human-AI partnership, the structural gap that appears at every pattern, and a framework for companies and individuals to map where they are and where they are headed.

**Website:** [hipcharter.com](https://hipcharter.com)

---

## Three Concepts, One Thesis

| Concept | What it answers | Level |
|---------|----------------|-------|
| **Just Intelligence** | WHY you design this way | Philosophy |
| **The HIP Charter** | HOW you design this way | Framework |
| **The Intent Layer** | WHAT is missing at every pattern | Gap |

## The Four Patterns

- **Foundation:** AI as Build Partner. Human steers, AI implements.
- **Tooling:** Human-First, Zero AI Dependency. AI built it, AI is not in it.
- **Pipeline:** AI-Enhanced Systems. AI enriches data, users never see AI.
- **Integration:** AI as Collaborative Component. AI works alongside live data.

These are not a hierarchy. They are petals of a bloom. The overlaps create depth. The center is full partnership.

---

## Part of the From Instinct to Intent™ Series

| Article | DOI |
|---------|-----|
| Discovering Intent | [10.5281/zenodo.18917473](https://doi.org/10.5281/zenodo.18917473) |
| Languages Designed for Humans | [10.5281/zenodo.19005877](https://doi.org/10.5281/zenodo.19005877) |
| Engine vs Steering Wheel | [10.5281/zenodo.19025149](https://doi.org/10.5281/zenodo.19025149) |
| **The HIP Charter** | [hipcharter.com](https://hipcharter.com) |

Published on [aitrustcommons.org](https://aitrustcommons.org/blog/), [Medium](https://nikhilsinghal-ai-trust-commons.medium.com/), and [Zenodo](https://zenodo.org).

---

## Repo Structure

```
docs/                    # Public site content (MkDocs Material, deployed to hipcharter.com)
internal/                # Working documents (not published to site)
visual-concepts/         # Diagram source files (HTML, PNG, 2x PNG)
```

## Author

**Nikhil Singhal** — Enterprise AI Architect & Builder | Founder, AI Trust Commons

- [LinkedIn](https://linkedin.com/in/nikhilsinghal)
- [GitHub](https://github.com/nikhilsi)
- [ORCID: 0009-0003-5449-6830](https://orcid.org/0009-0003-5449-6830)

## License

© 2026 Nikhil Singhal. Published by [AI Trust Commons](https://aitrustcommons.org).

Licensed under [Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/) (CC BY 4.0).

*From Instinct to Intent*™ is a trademark of Nikhil Singhal (USPTO Serial 99690685).
