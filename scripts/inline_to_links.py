import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LINK_HOME = '    <link rel="stylesheet" href="css/main.css">'
LINK_INNER = '    <link rel="stylesheet" href="css/main.css">\n    <link rel="stylesheet" href="css/pages.css">'


def main() -> None:
    hp = ROOT / "homepage.html"
    t = hp.read_text(encoding="utf-8")
    t = re.sub(r"<style>.*?</style>", LINK_HOME, t, count=1, flags=re.S)
    hp.write_text(t, encoding="utf-8")

    for name in ("about-us.html", "news.html", "programs.html", "projects.html"):
        p = ROOT / name
        t = p.read_text(encoding="utf-8")
        t = re.sub(r"<style>.*?</style>", LINK_INNER, t, count=1, flags=re.S)
        t = t.replace("<base target=\"_blank\">\n", "")
        t = t.replace("<base target=\"_blank\">", "")
        p.write_text(t, encoding="utf-8")


if __name__ == "__main__":
    main()
