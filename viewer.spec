# -*- mode: python ; coding: utf-8 -*-
# PyInstaller spec file for mdviewer
# Usage: pyinstaller viewer.spec

a = Analysis(
    ['viewer.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('index.html', '.'),
        ('vendor',     'vendor'),
        ('icon.ico',   '.'),
    ],
    hiddenimports=['pystray._win32', 'PIL', 'PIL.Image', 'PIL.ImageDraw'],
    hookspath=[],
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
    name='mdviewer',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,          # コンソールウィンドウを非表示
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='icon.ico',
)
