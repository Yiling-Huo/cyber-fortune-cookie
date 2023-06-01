import cx_Freeze

executables = [cx_Freeze.Executable("cyber-fortune-cookie.py", icon="icon.ico")]

cx_Freeze.setup(
    name="Cyber Fortune Cookie",
    options={"build_exe": {"packages":["pygame", "os", "sys"],
                           "include_files":["assets/"]}},
    executables = executables

    )