#
# This file is part of gunicorn released under the MIT license.
# See the NOTICE for more information.

from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version("slamcore-gunicorn")
except PackageNotFoundError:
    __version__ = "unknown"
SERVER = "gunicorn"
SERVER_SOFTWARE = "%s/%s" % (SERVER, __version__)
