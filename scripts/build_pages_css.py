"""Merge subpage-only CSS into css/pages.css (inner pages only — homepage uses main.css alone)."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def slurp(path: Path, start: int, end: int) -> str:
    return "\n".join(path.read_text(encoding="utf-8").splitlines()[start - 1 : end])


def main() -> None:
    about = ROOT / "about-us.html"
    news = ROOT / "news.html"
    programs = ROOT / "programs.html"
    projects = ROOT / "projects.html"

    news_css = (
        slurp(news, 172, 770)
        .replace(".news-section {", ".news-archive {")
        .replace(".news-section ", ".news-archive ")
        .replace(".news-section\n", ".news-archive\n")
    )
    news_css += "\n" + (
        slurp(news, 872, 899)
        .replace(".news-section {", ".news-archive {")
        .replace(".news-section ", ".news-archive ")
    )
    news_css += "\n" + slurp(news, 950, 965)

    text = "\n\n".join(
        [
            "/* Extra tokens for forms / CTAs */",
            ":root {",
            "    --success: #10b981;",
            "    --error: #ef4444;",
            "    --info: #3b82f6;",
            "    --gradient-gold: linear-gradient(145deg, var(--accent-gold-hover), var(--accent-gold));",
            "}",
            "",
            "/* --- Contact page --- */",
            slurp(about, 172, 801),
            slurp(about, 904, 929),
            "",
            "/* --- News listing --- */",
            news_css,
            "",
            "/* --- Programs page --- */",
            slurp(programs, 172, 939),
            slurp(programs, 1042, 1074),
            "",
            "/* --- Projects catalog --- */",
            slurp(projects, 171, 809),
            slurp(projects, 912, 1004),
        ]
    )
    text = text.replace("top: 73px", "top: var(--nav-height)")
    text = text.replace("margin-top: 73px", "margin-top: var(--nav-height)")

    out = ROOT / "css" / "pages.css"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text, encoding="utf-8")
    print("Wrote", out, len(text), "chars")


if __name__ == "__main__":
    main()
