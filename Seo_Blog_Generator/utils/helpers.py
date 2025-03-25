import markdown
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def save_as_markdown(content, filename="output/blog.md"):
    with open(filename, "w") as f:
        f.write(content)

def save_as_html(content, filename="output/blog.html"):
    html_content = markdown.markdown(content)
    with open(filename, "w") as f:
        f.write(html_content)

def save_as_pdf(content, filename="output/blog.pdf"):
    c = canvas.Canvas(filename, pagesize=letter)
    c.drawString(100, 750, content[:500])  # Only saves first 500 chars for simplicity
    c.save()
