from django.conf import settings
import os.path


def _convert_file_to_url(filename, root_url=None, root_directory=None):
    if not root_url:
        root_url = settings.SENDFILE_URL

    if not root_directory:
        root_directory = settings.SENDFILE_ROOT

    relpath = os.path.relpath(filename, root_directory)

    url = [root_url]

    while relpath:
        relpath, head = os.path.split(relpath)
        url.insert(1, head)

    return u'/'.join(url)
