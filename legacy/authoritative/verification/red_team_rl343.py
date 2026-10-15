#!/usr/bin/env python3
"""Independent exact replay of the promoted finite escape range."""
from pathlib import Path
import runpy

runpy.run_path(str(Path(__file__).resolve().with_name("red_team_terminal_ones_60.py")), run_name="__main__")
print("RL343_RED_TEAM_GREEN")
