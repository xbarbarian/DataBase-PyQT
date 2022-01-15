import sys
from cx_Freeze import setup, Executable

build_exe_options = {
    "packages": ["common", "logs", "client", "unit_tests", "sqlite3"],
}
setup(
    name="message_client_xBarbarian",
    version="0.8.8",
    description="message_client_xBarbarian",
    options={
        "build_exe": build_exe_options
    },
    executables=[Executable('client.py',
                            base='Win32GUI',
                            targetName='client.exe',
                            )]
)