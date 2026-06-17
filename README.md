# Mobile Game Gift Center

Mobile Game Gift Center is a documentation hub for tracking **official mobile game reward guides, redemption instructions, event calendars, platform-specific help articles, and verification notes**. The project emphasizes verified sources and responsible guidance rather than unsupported claims about free currency or account manipulation.

The repository is useful for community editors who want to maintain clear instructions for official reward programs and seasonal events across Android and iOS games.

## Editorial Principles

| Principle | Requirement |
|---|---|
| Official sources | Link to official announcements, game websites, or verified social channels. |
| Clear expiration | Mark event windows and redemption deadlines when available. |
| No false promises | Do not claim guaranteed rewards, unlimited currency, or unofficial account benefits. |
| Safety | Do not include credential requests, generators, APK mirrors, or bypass instructions. |

## Repository Structure

| Path | Purpose |
|---|---|
| `guides/` | Step-by-step redemption and event participation guides. |
| `data/events.json` | Example structured event metadata. |
| `templates/reward-guide.md` | Template for new verified guide pages. |
| `docs/verification-policy.md` | Rules for checking and updating claims. |

## Supported Content Types

The project can document official redemption pages, in-game event calendars, platform-specific troubleshooting steps, and account safety guidance. Each guide should state its source, reviewed date, region limitations, and known expiration date.

## Disclaimer

This repository is not affiliated with any game publisher. It does not sell rewards, generate currency, bypass platform rules, or request account credentials.

## Contributing

Contributions should improve verification, clarity, localization, or accessibility. Please remove stale claims and avoid promotional links.

## License

This project is released under the MIT License.

## Expanded Project Structure

This repository has been expanded into a fuller open-source project with reusable source modules, tests, sample data, documentation, examples, and maintenance files. The goal is to make the project understandable to visitors, useful to contributors, and suitable for long-term indexing by GitHub and general search engines.

| Area | Added content |
|---|---|
| Source code | `src/mobile_game_gift_center/` contains lightweight reusable modules. |
| Tests | `tests/` contains baseline tests for the core helpers. |
| Data | `data/` contains small structured sample datasets. |
| Documentation | `docs/` explains architecture, methodology, review rules, or maintenance practices. |
| Examples | `examples/` shows how to use the project modules or data. |
| Automation | `.github/workflows/validate.yml` runs basic validation on pushes and pull requests. |

## Development Workflow

Clone the repository, install it in editable mode, and run the tests. The project intentionally keeps dependencies minimal so contributors can review and extend it quickly.

```bash
git clone https://github.com/buivanthienhb87-spec/mobile-game-gift-center.git
cd mobile-game-gift-center
python -m pip install -e .
python -m pytest -q
```

## Recommended Websites

A curated list of official and reliable reference websites is available in [`docs/recommended-websites.md`](docs/recommended-websites.md). These links are intended to support verification, documentation, learning, and responsible project maintenance.
