import cx_Freeze
import sys
import os 
base = None

if sys.platform == 'win32':
    base = "Win32GUI"

os.environ['TCL_LIBRARY'] = r"C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.10_3.10.1264.0_x64__qbz5n2kfra8p0\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:/Program Files/WindowsApps/PythonSoftwareFoundation.Python.3.10_3.10.1264.0_x64__qbz5n2kfra8p0/tcl/tk8.6"

executables = [cx_Freeze.Executable("text_editor.py", base=base, icon="icon.ico")]


cx_Freeze.setup(
    name = "LAXMAN Text Editor",
    options = {"build_exe": {"packages":["tkinter","os"], "include_files":["icon.ico",'tcl86t.dll','tk86t.dll', 'icons2']}},
    version = "0.01",
    description = "Tkinter Application",
    executables = executables
    )
