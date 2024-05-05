create-venv:
	@pyenv virtualenv 3.7.13 ableton-control-surface-toolkit-venv-3.7.13
	#pyenv activate ableton-control-surface-toolkit-venv-3.7.13

install-deps:
	@pip install --upgrade pip
	@pip install -r requirements.txt

launch:
	@open /Applications/Ableton*12*

kill:
	@pkill -KILL -f "Ableton Live" || echo "Ableton was not running, so just starting it" && sleep .5

copy-doc-script-to-ableton:
	@rm -rf ~/Music/Ableton"/User Library/Remote Scripts/AbletonDocSurface"
	@cp -r "AbletonDocSurface" ~/Music/Ableton"/User Library/Remote Scripts"
	@rm -rf ~/Music/Ableton"/User Library/Remote Scripts/AbletonDocSurface/__pycache__"

copy-generated-live:
	@rm -rf build/Live
	@rm -rf build/MidiRemoteScript
	@cp -r ~/enabler-output/Live build
	@cp -r ~/enabler-output/MidiRemoteScript build

copy-generated: copy-generated-live lint-fix format copy-packages

copy-packages:
	@python copy_packages.py

decompile-live:
	 decompyle3 /Applications/Ableton\ Live\ 12\ Suite.app/Contents/App-Resources/MIDI\ Remote\ Scripts -r -o build

decompile: decompile-live fix-parse-errors lint-fix format

delete-generated-files:
	 @ls -d */ | grep -v build | xargs rm -rf

lint-fix:
	@ruff build --quiet --config ruff.toml | grep E402 | cut -d: -f1 | xargs autopep8 --in-place # this uses the base config that ignores some rules
	@ruff build --quiet --fix --unsafe-fixes --config ruff.toml
	@ruff AbletonDocSurface --quiet --fix --unsafe-fixes

lint:
	@ruff build --quiet --config ruff.toml
	@ruff AbletonDocSurface --quiet
	@mypy AbletonDocSurface

format:
	@ruff format build  --config ruff.toml
	@ruff format AbletonDocSurface

fix-parse-errors:
	@python fix_parse_errors.py

install-deps:
	@pip install -r requirements.txt

restart: kill copy-doc-script launch

upload-pip:
	@cd ableton-control-surface-core && rm -rf dist && rm -rf src/ableton_control-surface_core.egg-info && python -m build && twine upload dist/*
	@cd ableton-control-surface-scripts && rm -rf dist && rm -rf src/ableton_control-surface_core.egg-info && python -m build && twine upload dist/*
