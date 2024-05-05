import os
import shutil

build_package = "build"
core_package = "ableton-control-surface-core/src"
scripts_package = "ableton-control-surface-scripts/src"
core_packages = [
    "_Framework",
    "_Generic",
    "_MxDCore",
    "_Tools",
    "_Userscript",
    "ableton",
    "Live",
    "MidiRemoteScript",
]
# don't need to define the scripts packages, as they are all copied after the core packages
cur_dir = os.getcwd() # current dir path
source = os.path.join(cur_dir,'build')
scripts_dir = os.path.join(cur_dir, scripts_package)
for package in core_packages:
    dir_to_move = os.path.join(source, package)
    shutil.move(dir_to_move, os.path.join(cur_dir, core_package))
for package in os.listdir(source):
    dir_to_move = os.path.join(source, package)
    shutil.move(dir_to_move, os.path.join(cur_dir, scripts_dir))