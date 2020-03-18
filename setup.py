from cx_Freeze import setup, Executable

setup(name="Calculator",
      version="0.1",
      description="Use this calculator",
      executables=[Executable("calculator.py")])

# python setup.py build