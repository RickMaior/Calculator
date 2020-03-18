from cx_Freeze import setup, Executable

#python -m pip install cx_Freeze --upgrade

setup(name="Calculator",
      version="0.1",
      description="Use this calculator",
      executables=[Executable("calculator.py")])

# python setup.py build