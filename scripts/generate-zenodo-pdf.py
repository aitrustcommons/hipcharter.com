"""
Generate a Zenodo-quality PDF of the HIP Charter using weasyprint.
Fonts: Lora (serif body), Inter (sans-serif headings).
Images embedded from docs/assets/images/.
"""
import markdown
from weasyprint import HTML
import re

CHARTER_MD = "/home/claude/hipcharter.com/docs/charter.md"
IMG_DIR = "/home/claude/hipcharter.com/docs/assets/images"
OUTPUT = "/home/claude/ns-2026-the-big-push/from-instinct-to-intent/article-4-hip-charter/hip-charter-zenodo.pdf"

# Read charter markdown, strip frontmatter
with open(CHARTER_MD) as f:
    content = f.read()

# Remove YAML frontmatter
content = re.sub(r'^---\n.*?\n---\n', '', content, flags=re.DOTALL)

# Remove MkDocs-specific grid card divs but keep content
content = re.sub(r'<div class="grid cards[^"]*" markdown>', '', content)
content = re.sub(r'</div>', '', content)

# Fix image paths to absolute
content = content.replace('](assets/images/', f']({IMG_DIR}/')

# Remove Material icon shortcodes (they won't render in PDF)
content = re.sub(r':material-[a-z-]+:\{[^}]*\}\s*', '', content)
content = re.sub(r':octicons-[a-z-]+:\s*', '', content)

# Remove MkDocs button classes
content = re.sub(r'\{[^}]*\.md-button[^}]*\}', '', content)

# Convert markdown to HTML
md = markdown.Markdown(extensions=['tables', 'fenced_code'])
body_html = md.convert(content)

html_template = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
@import url('https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,400;0,600;0,700;1,400&family=Inter:wght@400;500;600;700&display=swap');

@page {{
  size: letter;
  margin: 1in 1in 1.2in 1in;
  @bottom-center {{
    content: counter(page);
    font-family: 'Inter', sans-serif;
    font-size: 9pt;
    color: #888;
  }}
}}

body {{
  font-family: 'Lora', Georgia, serif;
  font-size: 11pt;
  line-height: 1.7;
  color: #1a1a1a;
  max-width: 100%;
}}

h1 {{
  font-family: 'Inter', sans-serif;
  font-size: 22pt;
  font-weight: 700;
  color: #0d3b2e;
  margin-top: 0;
  margin-bottom: 6pt;
  line-height: 1.2;
}}

h2 {{
  font-family: 'Inter', sans-serif;
  font-size: 15pt;
  font-weight: 600;
  color: #1a4a3a;
  margin-top: 28pt;
  margin-bottom: 10pt;
  padding-top: 12pt;
  border-top: 1px solid #e0e0e0;
}}

h3 {{
  font-family: 'Inter', sans-serif;
  font-size: 12pt;
  font-weight: 600;
  color: #2d5a4a;
  margin-top: 20pt;
  margin-bottom: 8pt;
}}

p {{
  margin-bottom: 10pt;
  text-align: justify;
}}

em {{
  font-style: italic;
}}

strong {{
  font-weight: 700;
}}

img {{
  max-width: 100%;
  margin: 16pt 0;
  border-radius: 6pt;
}}

table {{
  width: 100%;
  border-collapse: collapse;
  margin: 14pt 0;
  font-size: 10pt;
  font-family: 'Inter', sans-serif;
}}

th {{
  background: #f5f5f0;
  font-weight: 600;
  text-align: left;
  padding: 8pt 10pt;
  border-bottom: 2px solid #d0d0c8;
}}

td {{
  padding: 7pt 10pt;
  border-bottom: 1px solid #e8e8e4;
  vertical-align: top;
}}

tr:last-child td {{
  border-bottom: none;
}}

hr {{
  border: none;
  border-top: 1px solid #e0e0e0;
  margin: 20pt 0;
}}

ul, ol {{
  margin-bottom: 10pt;
  padding-left: 20pt;
}}

li {{
  margin-bottom: 4pt;
}}

/* DOI header bar */
.doi-header {{
  font-family: 'Inter', sans-serif;
  font-size: 9pt;
  color: #666;
  border-bottom: 1px solid #ccc;
  padding-bottom: 8pt;
  margin-bottom: 20pt;
}}

.doi-header a {{
  color: #1D4E89;
  text-decoration: none;
}}

/* Footer info */
.footer-info {{
  font-family: 'Inter', sans-serif;
  font-size: 9pt;
  color: #888;
  margin-top: 24pt;
  padding-top: 12pt;
  border-top: 1px solid #e0e0e0;
}}
</style>
</head>
<body>

<div class="doi-header">
  <strong>The Human Intelligence Partnership Charter</strong><br>
  Nikhil Singhal · March 2026 · Published by AI Trust Commons<br>
  ORCID: <a href="https://orcid.org/0009-0003-5449-6830">0009-0003-5449-6830</a><br>
  Web: <a href="https://hipcharter.com">hipcharter.com</a> ·
  License: <a href="https://creativecommons.org/licenses/by/4.0/">CC BY 4.0</a>
</div>

{body_html}

<div class="footer-info">
  <em>From Instinct to Intent</em>™ is a registered trademark (USPTO Serial 99690685).<br>
  © 2026 Nikhil Singhal. Published by AI Trust Commons.
</div>

</body>
</html>"""

# Write HTML for debugging
html_path = OUTPUT.replace('.pdf', '.html')
with open(html_path, 'w') as f:
    f.write(html_template)

# Generate PDF
HTML(string=html_template, base_url="/home/claude/hipcharter.com/docs/").write_pdf(OUTPUT)
print(f"PDF generated: {OUTPUT}")
