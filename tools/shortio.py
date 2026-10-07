#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.9"
# ///
"""Create a Short.io short link and QR code for a slide.

    uv run tools/shortio.py link https://code.visualstudio.com --slug vscode --title "VS Code download" --out ai_vscode_start/assets/qr
    uv run tools/shortio.py link https://example.com --dry-run

Setup: put your key in the environment or in a git-ignored .env file at the repo root:

    SHORTIO_API_KEY=...        (never commit this)
    SHORTIO_DOMAIN=shortie.fyi (optional; this is the default)

Links already made are remembered in tools/short_links.json, so re-running (or re-rendering a
deck) never creates a second link or calls the API for a link that exists.
API reference: https://developers.short.io/
"""
import argparse, base64, json, os, re, sys, urllib.error, urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MANIFEST = Path(__file__).resolve().parent / "short_links.json"
API = "https://api.short.io"
DEFAULT_DOMAIN = "shortie.fyi"


def load_env():
    env = dict(os.environ)
    f = ROOT / ".env"
    if f.exists():
        for line in f.read_text().splitlines():
            m = re.match(r"\s*([A-Za-z_][A-Za-z0-9_]*)\s*=\s*(.*?)\s*$", line)
            if m and not line.lstrip().startswith("#"):
                env.setdefault(m.group(1), m.group(2).strip("'\""))
    return env


def call(method, path, key, body=None, query=None):
    url = API + path + ("?" + urllib.parse.urlencode(query) if query else "")
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(url, data=data, method=method, headers={
        "Authorization": key, "Content-Type": "application/json", "Accept": "application/json, image/*"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return r.status, r.headers.get("Content-Type", ""), r.read()
    except urllib.error.HTTPError as e:
        return e.code, e.headers.get("Content-Type", ""), e.read()


def load_manifest():
    return json.loads(MANIFEST.read_text()) if MANIFEST.exists() else {}


def save_manifest(m):
    MANIFEST.write_text(json.dumps(m, indent=2, sort_keys=True) + "\n")


def qr_bytes(status, ctype, raw):
    """The docs do not say if the QR response is raw bytes, base64, or JSON, so accept all three."""
    if status not in (200, 201):
        sys.exit(f"QR request failed: HTTP {status}\n{raw[:300].decode(errors='replace')}")
    if ctype.startswith("image/") or raw[:4] == b"\x89PNG" or raw.lstrip()[:4] in (b"<svg", b"<?xm"):
        return raw
    try:
        obj = json.loads(raw)
    except ValueError:
        sys.exit(f"Unrecognised QR response ({ctype}): {raw[:120]!r}")
    for v in (obj.values() if isinstance(obj, dict) else [obj]):
        if isinstance(v, str):
            v = re.sub(r"^data:[^,]*,", "", v)
            try:
                return base64.b64decode(v, validate=True)
            except Exception:
                pass
    sys.exit(f"Could not find an image in the QR response: {str(obj)[:200]}")


def cmd_link(a):
    env = load_env()
    domain = a.domain or env.get("SHORTIO_DOMAIN", DEFAULT_DOMAIN)
    key = env.get("SHORTIO_API_KEY", "")
    manifest = load_manifest()
    ident = f"{domain}|{a.slug or ''}|{a.url}"
    body = {"originalURL": a.url, "domain": domain, "allowDuplicates": False}
    if a.slug: body["path"] = a.slug
    if a.title: body["title"] = a.title

    if a.dry_run:
        print("DRY RUN, nothing sent.\nPOST", API + "/links\n" + json.dumps(body, indent=2))
        print("then POST", API + "/links/qr/<idString>", json.dumps(qr_body(a)))
        return
    if not key:
        sys.exit("SHORTIO_API_KEY is not set. Add it to your environment or to .env at the repo root.")

    rec = manifest.get(ident)
    if rec:
        print("Already created (from short_links.json):", rec["shortURL"])
    else:
        status, _, raw = call("POST", "/links", key, body)
        if status not in (200, 201):
            sys.exit(f"Create failed: HTTP {status}\n{raw[:400].decode(errors='replace')}")
        d = json.loads(raw)
        rec = {"shortURL": d.get("secureShortURL") or d["shortURL"], "idString": d["idString"],
               "path": d.get("path"), "originalURL": a.url, "title": a.title or ""}
        manifest[ident] = rec
        save_manifest(manifest)
        print(("Link already existed: " if d.get("duplicate") else "Created: ") + rec["shortURL"])

    if a.qr:
        out = Path(a.out); out.mkdir(parents=True, exist_ok=True)
        f = out / f"{rec['path'] or a.slug or 'link'}.{a.qr}"
        if f.exists() and not a.force:
            print("QR already saved:", f)
        else:
            status, ctype, raw = call("POST", f"/links/qr/{rec['idString']}", key, qr_body(a))
            f.write_bytes(qr_bytes(status, ctype, raw))
            print("QR saved:", f)
        rel = os.path.relpath(f, Path(a.out).parent.parent) if a.out else f.name
        print("\nPaste into a slide:")
        print(f'<a href="{rec["shortURL"]}">{rec["shortURL"].replace("https://", "")}</a>')
        print(f'<img class="qr" src="{rel}" alt="QR code for {rec["shortURL"].replace("https://", "")}">')


def qr_body(a):
    return {"useDomainSettings": False, "color": a.color, "backgroundColor": "FFFFFF",
            "size": a.size, "type": a.qr or "svg"}


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    l = sub.add_parser("link", help="create (or reuse) a short link, and optionally its QR code")
    l.add_argument("url")
    l.add_argument("--slug", help="custom path, e.g. vscode -> shortie.fyi/vscode")
    l.add_argument("--title")
    l.add_argument("--domain", help=f"default {DEFAULT_DOMAIN}, or SHORTIO_DOMAIN")
    l.add_argument("--qr", choices=["svg", "png"], nargs="?", const="svg", help="also save a QR code (default svg)")
    l.add_argument("--out", default="assets/qr", help="folder for the QR file")
    l.add_argument("--size", type=int, default=20, help="QR size 1-99")
    l.add_argument("--color", default="183A57", help="QR color hex, no #")
    l.add_argument("--force", action="store_true", help="regenerate an existing QR file")
    l.add_argument("--dry-run", action="store_true", help="show the requests without sending them")
    l.set_defaults(func=cmd_link)
    a = p.parse_args(); a.func(a)


if __name__ == "__main__":
    import urllib.parse  # noqa: used by call()
    main()
