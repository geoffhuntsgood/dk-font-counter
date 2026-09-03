from cx_Freeze import setup, Executable

setup(
    name="DK Counter",
    version="1.0.0",
    options={"build_exe": {"packages": ["pygame"], "include_files": ["numbers"]}},
    executables=[Executable("counter.py")],
)
