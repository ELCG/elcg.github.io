import os
from pathlib import Path
from pelican import signals

# Function extracted from https://stackoverflow.com/a/19308592/7690767
def get_filepaths(directory, extensions=[], ignores=[]): 
    file_paths = []  # List which will store all of the full filepaths.
    
    exts = extensions

    if isinstance(extensions, str):
        exts = [extensions]

    igns = ignores

    if isinstance(ignores, str):
        igns = [ignores]

    # Walk the tree.
    for root, directories, files in os.walk(directory):
        for filename in files:

            if filename in igns or not any(filename.endswith(f".{ext}") for ext in exts):
                continue

            filepath = Path(root, filename)
            file_paths.append(filepath)

    return file_paths


def create_bundle(files, output):
    with open(output, 'w') as outfile:
        for fname in files:
            with open(fname) as infile:
                outfile.write('\n\n')
                for line in infile:
                    outfile.write(line)


def create_bundles(sender):
    theme_path = sender.settings.get('THEME', None)

    if theme_path is None:
        return

    js_bundle = f'{theme_path}/static/js/scripts_bundled.js'
    js_filenames = get_filepaths(theme_path, 'js', "scripts_bundled.js")
    create_bundle(js_filenames, js_bundle)

    css_bundle = f'{theme_path}/static/css/style_bundled.css'
    css_filenames = get_filepaths(theme_path, 'css', "style_bundled.css")
    create_bundle(css_filenames, css_bundle)


def register():
    signals.initialized.connect(create_bundles)
