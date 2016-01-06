from __future__ import absolute_import

from django.http import HttpResponse

from ._internalredirect import _convert_file_to_url


def sendfile(request, filename, root_url=None, root_directory=None, **kwargs):
    response = HttpResponse()
    url = _convert_file_to_url(filename, root_url, root_directory)
    response['X-Accel-Redirect'] = url

    return response
