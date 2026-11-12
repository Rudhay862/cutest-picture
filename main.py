"""Cutest-picture entry: copy the bundled picture to the output folder."""
from pathlib import Path
import os

here = Path(__file__).resolve().parent
out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
out.mkdir(parents=True, exist_ok=True)
(out / "entry.png").write_bytes((here / "entry.png").read_bytes())

# A plain copy: every run produces the same bytes.
