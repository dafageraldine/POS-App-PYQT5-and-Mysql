import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os"], "excludes": ["tkinter"]}

target = Executable(
    script="bullEyeArchery.py",
    icon="icon.ico"
    )

setup(  name = "bullEyeArchery",
        version = "0.1",
        description = "POS MASUK",
        options = {"build_exe": build_exe_options},
        executables = [target])