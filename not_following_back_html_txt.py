from bs4 import BeautifulSoup
from datetime import datetime
import os

def extract_usernames(file_path):
    """Extract Instagram usernames from the exported HTML file."""
    with open(file_path, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")
    usernames = {a.text.strip() for a in soup.find_all("a", href=True)}
    return {u for u in usernames if u}

def load_exclusions(file_path):
    """Load usernames to exclude from a text file (one per line)."""
    if not os.path.exists(file_path):
        return set()
    with open(file_path, "r", encoding="utf-8") as f:
        return {line.strip() for line in f if line.strip()}

def write_html(usernames, outfile):
    """Write a simple HTML page with profile links opening in new tabs."""
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    count = len(usernames)
    links = [f"https://www.instagram.com/{u}" for u in usernames]

    html = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Not Following Back ({count})</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <style>
    body {{ font-family: system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, sans-serif; margin: 2rem; }}
    h1 {{ margin-bottom: .25rem; }}
    .meta {{ color:#666; margin-bottom: 1.5rem; }}
    ol {{ line-height: 1.6; padding-left: 1.25rem; }}
    a {{ text-decoration: none; }}
    a:hover {{ text-decoration: underline; }}
    .count {{ font-weight: 600; }}
  </style>
</head>
<body>
  <h1>Profiles not following you back</h1>
  <div class="meta"><span class="count">{count}</span> profiles • generated {now}</div>
  <ol>
    {"".join(f'<li><a href="{url}" target="_blank" rel="noopener noreferrer">{url}</a></li>' for url in links)}
  </ol>
</body>
</html>"""
    with open(outfile, "w", encoding="utf-8") as f:
        f.write(html)

def write_txt(usernames, outfile):
    """Write plain usernames to a TXT file, one per line."""
    with open(outfile, "w", encoding="utf-8") as f:
        for u in usernames:
            f.write(u + "\n")

def main():
    followers_file = "followers_1.html"
    following_file = "following.html"
    exclusions_file = "exclusions.txt"
    output_html = "not_following_back.html"
    output_txt  = "not_following_back.txt"

    followers = extract_usernames(followers_file)
    following = extract_usernames(following_file)
    exclusions = load_exclusions(exclusions_file)

    not_following_back = (following - followers) - exclusions
    not_following_back = sorted(not_following_back, key=str.lower)

    # Write both outputs
    write_html(not_following_back, output_html)
    write_txt(not_following_back, output_txt)

    print(f"Created {output_html} and {output_txt} with {len(not_following_back)} entries "
          f"(excluded {len(exclusions)} usernames).")

    # Optional: preview a few in console
    for u in not_following_back[:10]:
        print(u)

if __name__ == "__main__":
    main()
