"""
Hook file. Provides streamlit metadata files for the PyInstaller bundling process.
"""

from PyInstaller.utils.hooks import copy_metadata, collect_submodules
datas = copy_metadata('streamlit')
hiddenimports = collect_submodules('streamlit')
