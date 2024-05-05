import os
import shutil

for package in [
    "ableton-control-surface-core/src",
    "ableton-control-surface-scripts/src",
]:
    for idx, (root, _, _)in enumerate(os.walk(package)):
        if idx == 0:
            continue
        with open(os.path.join(root, "py.typed"), "w") as f:
            f.write("")


