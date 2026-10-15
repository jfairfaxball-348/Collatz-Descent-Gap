#!/usr/bin/env python3
"""Portable RL343 current fast suite; all exact claims are rechecked."""
from pathlib import Path
import runpy

root = Path(__file__).resolve().parent
for name in (
    "phase_boundary.py",
    "verify_full_cycle_bridge.py",
    "verify_matched_phase_pairing.py",
    "suffix75_boundary.py",
    "terminal_ones_60.py",
):
    runpy.run_path(str(root / name), run_name="__main__")
print("RL343_FAST_GREEN")
