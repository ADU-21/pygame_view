import sys
# import pymysql
from cx_Freeze import setup, Executable
sys.path.append("..") 

base = None
buildOptions = dict(
  # packages = ['flask'], 
  # packages = ['Tornado','momoko','os','sys','time','json','pdb'], 
  excludes = ['numpy','scipy','cryptography'],
  # excludes = ['numpy','scipy'],
  # include_files = ['config.conf'],
  # include_files = ['static','templates','config.conf'],
  include_msvcr = True
)
# if sys.platform == "win32":
#     base = "Win32GUI"
setup(
        name = "ch_cyber",
        version = "0.1",
        description = "ch_cyber",
        options = dict(build_exe = buildOptions),
        executables =[Executable ("test_view.py", base = base)]
      )