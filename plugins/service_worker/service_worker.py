import os
from datetime import datetime
import hashlib
import json
from pathlib import Path


from pelican import signals

# Function extracted from https://stackoverflow.com/a/19308592/7690767
def get_filepaths(directory, extensions=None, ignores=None): 
        """
        This function will generate the file names in a directory 
        tree by walking the tree either top-down or bottom-up. For each 
        directory in the tree rooted at directory top (including top itself), 
        it yields a 3-tuple (dirpath, dirnames, filenames).
        """
        file_paths = []  # List which will store all of the full filepaths.
        
        if extensions is None:
            extensions = []

        exts = extensions

        if isinstance(extensions, str):
            exts = [extensions]

        if ignores is None:
            ignores = []

        igns = ignores

        if isinstance(ignores, str):
            igns = [ignores]

        # Walk the tree.
        for root, directories, files in os.walk(directory):
            for filename in files:

                if filename in igns or not any(filename.endswith(f".{ext}") for ext in exts):
                    continue

                filepath = os.path.join(root, filename).replace("\\", "/")
                file_paths.append(filepath)

        return file_paths

def create_service_worker(sender):

    output_path = sender.settings.get('OUTPUT_PATH', None)
    sw_template = sender.settings.get('SERVICE_WORKER_THEMPLATE', None)

    if None in [output_path, sw_template]:
        return

    extensions = ['js', 'html', 'css', 'svg', 'ini', 'ico', 'webmanifest', 'xml']
    img_extensions = ['png', 'jpg', 'gif']
    ignores = ['sw.js']

    FILES = get_filepaths(output_path, extensions, ignores=ignores)

    images = get_filepaths(output_path, img_extensions, ignores=ignores)

    thumbnails = [filename for filename in images if '-thumbnail' in filename]

    FILES.extend(thumbnails)

    files_to_cache = []

    for filename in FILES:

        if filename.endswith('index.html'):
            filename_without_index = filename[:-10]
            files_to_cache.append(filename_without_index)

        files_to_cache.append(filename)

    # Remove output folder from path - Compatible with CI
    files_to_cache = [path.split(Path(output_path).stem)[-1] for path in files_to_cache]

    # Special case for /
    files_to_cache.append('/')

    FILES_TO_CACHE = sorted(set(files_to_cache))

    with open(sw_template, 'r+') as template_file:
        contents = template_file.read()
    
    contents = contents.replace('"$FILES_TO_CACHE$"', json.dumps(FILES_TO_CACHE, sort_keys=True, indent=4))
    version_hash = hashlib.md5(str(datetime.now()).encode('utf-8')).hexdigest()[-7:]
    contents = contents.replace('$VERSION$', version_hash)

    with open(f'{output_path}/sw.js','w') as output_file: 
        output_file.write(contents)

def register():
    signals.finalized.connect(create_service_worker)
