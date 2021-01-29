import os
from pathlib import Path
from pelican import signals
from PIL import Image, ImageFilter

# Function extracted from https://stackoverflow.com/a/19308592/7690767
def get_filepaths(directory, extensions=[], ignores=[]): 
    """
    This function will generate the file names in a directory 
    tree by walking the tree either top-down or bottom-up. For each 
    directory in the tree rooted at directory top (including top itself), 
    it yields a 3-tuple (dirpath, dirnames, filenames).
    """
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

def generate_blur_thumbnails(sender):

    content_path = sender.settings.get('BLUR_PATH', None)
    blur_radius = sender.settings.get('BLUR_RADIUS', 2)

    if content_path is None:
        return

    imgs = get_filepaths(content_path, ['jpg', 'png'])

    for filename in imgs:
        extension = filename.suffix
        name_alone = filename.parent / filename.stem
        
        if filename.stem.endswith('-thumbnail'):
            continue

        im = Image.open(filename)
        im = im.convert(mode="RGB")
        im.thumbnail([200, 200], Image.ANTIALIAS)
        im.filter(ImageFilter.GaussianBlur(blur_radius)).save(f'{name_alone}-thumbnail{extension}', optimize=True)

 
def register():
    signals.initialized.connect(generate_blur_thumbnails)
