import os
import json
from pathlib import Path

from pelican import signals


def generate_output(sender):
    output_path = sender.settings.get("OUTPUT_PATH", None)

    shortener_file = sender.settings.get('SHORTENER_FILE', None)

    if shortener_file is None:
        print("No shortener File was given")
        return

    with open(shortener_file) as file:
        redirects_map = json.load(file)
        
    redirects_folder = sender.settings.get('SHORTENER_FOLDER', None)

    output_path_with_folder = output_path

    if redirects_folder is not None:
        output_path_with_folder = Path(output_path, redirects_folder)

    for filename, redirect_url in redirects_map.items():
        generate_folder_file(filename, output_path_with_folder, redirect_url)


def generate_folder_file(file, folder, link):
    BASE_HTML = """
    <html>
        <head>
            <meta http-equiv="refresh" content="0; URL='{0}'" />
        </head>
        <body>
        </body>
    </html>
    """

    if not (link.startswith('http://') or link.startswith('https://')):
        link = 'http://' + link
    
    folder_path = Path(folder, file)

    os.makedirs(folder_path, exist_ok=True)

    file_path = Path(folder_path, 'index.html')

    with open(file_path, 'w', encoding='utf-8') as fd:
        content = BASE_HTML.format(link)
        fd.write(content)


def register():
    signals.finalized.connect(generate_output)
