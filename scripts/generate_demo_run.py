from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from qra_public_demo.demo_pipeline import write_demo_run


def main() -> int:
    output_dir = ROOT / "examples" / "runs" / "generated-demo"
    input_path = ROOT / "examples" / "sample_public_papers.json"
    write_demo_run(output_dir=output_dir, input_path=input_path)
    print(f"Wrote demo run to {output_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
