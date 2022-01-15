import sys
from cx_Freeze import setup, Executable

build_exe_options = {
    "packages": ["common", "logs", "server", "unit_tests"],
}
setup(
    name="message_client_xBarbarian",
    version="0.8.8",
    description="message_client_xBarbarian",
    options={
        "build_exe": build_exe_options
    },
    executables=[Executable('client.py',
                            # base='Win32GUI',
                            targetName='server.exe',
                            )]
)