import io
import pathlib
import shutil
import tempfile
from contextlib import contextmanager, redirect_stdout


def asset(asset_name):
    assets = "tests/assets"
    return pathlib.PurePath(assets, asset_name)


# Stolen from https://getpelican.com
@contextmanager
def temporary_folder():
    """creates a temporary folder, return it and delete it afterwards.

    This allows to do something like this in tests:

        >>> with temporary_folder() as d:
            # do whatever you want
    """
    tempdir = tempfile.mkdtemp()
    try:
        yield tempdir
    finally:
        shutil.rmtree(tempdir)


def equal_dirs(dirs_to_compare):  # filecmp.dircmp
    with redirect_stdout(io.StringIO()) as f:
        dirs_to_compare.report_full_closure()
    s = f.getvalue()
    return not (any(("Only in" in s, "Differing" in s, "Trouble with" in s, "funny" in s)))
