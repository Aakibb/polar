import markdown
import subprocess
import os

with open("Project_Overview.md", "r", encoding="utf-8") as f:
    text = f.read()

html_body = markdown.markdown(text, extensions=['tables'])

html_template = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Project Overview</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 40px;
            color: #333;
        }}
        h1, h2, h3 {{
            color: #0055a4;
        }}
        table {{
            border-collapse: collapse;
            width: 100%;
            margin-bottom: 20px;
        }}
        th, td {{
            border: 1px solid #ddd;
            padding: 8px;
            text-align: left;
        }}
        th {{
            background-color: #f2f2f2;
            color: #333;
        }}
    </style>
</head>
<body>
{html_body}
</body>
</html>
"""

html_path = os.path.abspath("Project_Overview.html")
pdf_path = os.path.abspath("Project_Overview.pdf")

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html_template)

browsers = [
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"
]

success = False
for browser in browsers:
    if os.path.exists(browser):
        cmd = [
            browser,
            "--headless",
            "--disable-gpu",
            f"--print-to-pdf={pdf_path}",
            html_path
        ]
        try:
            subprocess.run(cmd, check=True)
            print(f"PDF generated successfully at: {pdf_path} using {browser}")
            success = True
            break
        except Exception as e:
            print(f"Failed via {browser}: {e}")

if not success:
    print("Could not generate PDF. Browsers not found.")
