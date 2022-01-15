import sys
from cx_Freeze import setup, Executable

build_exe_options = {
    "packages": ["common", "logs", "server", "unit_tests"],
}
setup(
    name="message_server_xBarbarian",
    version="0.8.8",
    description="message_server_xBarbarian",
    options={
        "build_exe": build_exe_options
    },
    executables=[Executable('server.py',
                            # base='Win32GUI',
                            targetName='server.exe',
                            )]
)