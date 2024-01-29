# This spec file encodes the script name and options for pyinstaller command.
# Used to bundle streamlit and altair data files with the app

# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['run_app.py'],
    pathex=['.'],
    binaries=[],
    datas=[
    (
        "<path to lib>/Lib/site-packages/altair/vegalite/v5/schema/vega-lite-schema.json",
        "./altair/vegalite/v4/schema/"
    ),
    (
        "<path to lib>/Lib/site-packages/streamlit/static",
        "./streamlit/static"
    ),
    (   
        "<path to app code>/",
        "."
    )
    ],
    hiddenimports=['sklearn', 'sklearn.ensemble._forest'],
    hookspath=['./hooks'],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='run_app',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
