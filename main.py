"""Copy entry.png to the make.fun output directory.

The entry image is a five-panel news-magazine front page summing up
Tuesday, 24 November 2026. This program does no network access and no
drawing: it copies the image the repository holds, byte for byte, so two
runs always write identical bytes.
"""

import os
import shutil
import struct
import sys
from pathlib import Path

PNG_MAGIC = bytes([0x89, 0x50, 0x4E, 0x47, 0x0D, 0x0A, 0x1A, 0x0A])
MAX_BYTES = 1_048_576
MAX_DIMENSION = 1024


def assert_png(data: bytes, label: str) -> tuple[int, int]:
    if len(data) < 8 or data[:8] != PNG_MAGIC:
        raise ValueError(f"{label} is not a valid PNG (bad magic bytes)")
    if len(data) > MAX_BYTES:
        raise ValueError(
            f"{label} is too large: {len(data)} bytes, limit is {MAX_BYTES}"
        )
    if len(data) < 24 or data[12:16] != b"IHDR":
        raise ValueError(f"{label} is not a valid PNG (missing IHDR chunk)")
    width, height = struct.unpack(">II", data[16:24])
    if width == 0 or height == 0:
        raise ValueError(f"{label} has bad IHDR dimensions: {width}x{height}")
    if width > MAX_DIMENSION or height > MAX_DIMENSION:
        raise ValueError(
            f"{label} is too large: {width}x{height}, "
            f"limit is {MAX_DIMENSION}x{MAX_DIMENSION}"
        )
    return width, height


def main() -> None:
    here = Path(__file__).resolve().parent
    source = here / "entry.png"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    dest = out_dir / "entry.png"

    data = source.read_bytes()
    width, height = assert_png(data, "entry.png")

    out_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, dest)

    check = dest.read_bytes()
    if check != data:
        raise ValueError("output bytes differ from entry.png")
    assert_png(check, "output entry.png")
    print(f"Wrote {dest} ({len(data)} bytes, {width}x{height})")


if __name__ == "__main__":
    try:
        main()
    except (OSError, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        raise SystemExit(1)
