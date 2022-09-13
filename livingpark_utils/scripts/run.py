"""Convinience methods to run the auto-generated scripts.

Notes
-----
The methods below need to be created manually when a new notebook is added.
"""
import importlib
from IPython.utils import io


def mri_metadata():
    """Execute auto-generated script for `../notebooks/mri_metadata.ipynb`."""
    with io.capture_output():
        importlib.import_module("mri_metadata", "livingpark_utils.scripts")


def pd_status():
    """Execute auto-generated script for `../notebooks/pd_status.ipynb`."""
    with io.capture_output():
        importlib.import_module("pd_status", "livingpark_utils.scripts")
