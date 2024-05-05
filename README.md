TODO:

- Separate the fastosc project
    - Add tests
- Separate the FaderFox project
    - Add tests

1. Publish the reverse engineered Live/MidiRemoteScript modules
2. Publish the decompiled controller scripts
  - These depend on the reverse engineered modules
- Publish the Ableton Osc project
  - this depends on the fastosc + reverse engineered Live modules


**ableton-core-library**
* _Framework
* _Generic
* _MxDCore
* _Tools
* _Userscript
* ableton
* Live
* MidiRemoteScript

**ableton-controller-scripts**
* depends on ableton-core-library
* Everything else

**fastosc**
* no dependencies

**ableton-osc**
* depends on fastosc and ableton-core-library

**faderfox-ableton**
* depends on ableton-core-library

create one build folder that holds all the files
from the different approaches of decompiling the controller scripts
create to subdirectories:
- ableton-core-library
- ableton-controller-scripts (this is really most for convience)

with corresponding pyproject files etc
twine scripts to upload the packages to pypi after.
Build folder is in .gitignore

