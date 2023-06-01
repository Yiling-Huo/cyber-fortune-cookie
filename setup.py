import cx_Freeze

executables = [cx_Freeze.Executable("cyber-fortune-cookie.py", icon="icon.ico")]

cx_Freeze.setup(
    name="Cyber Fortune Cookie",
    options={"build_exe": {"packages":["pygame", "os"],
                           "include_files":["assets/"], "excludes":["asttokens", "attrdict", "backcall", "BespON", "cachetools", "cffi", "codebraid", "colorama", "comm", "contourpy", "cx-Freeze", "cx-Logging", "cycler", "debugpy", "decorator", "executing", "fonttools", "ImageHash", "ipykernel", "ipython", "jedi", "jupyter_client", "jupyter_core", "kiwisolver", "lief", "matplotlib", "matplotlib-inline", "nest-asyncio", "numpy", "packaging", "pandocfilters", "parso", "path", "path.py", "pefile", "pickleshare", "Pillow", "pip", "platformdirs", "prompt-toolkit", "psutil", "PsychoPy", "pure-eval", "py2exe", "pycparser", "Pygments", "pyparsing", "pypinyin", "python-dateutil", "PyWavelets", "pywin32", "pyzmq", "radian", "rchitect", "scipy", "setuptools", "six", "stack-data", "tornado", "traitlets", "wcwidth", "you-get"]}},
    executables = executables

    )