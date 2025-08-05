#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import sys
from pathlib import Path
from typing import Optional

from PIL import Image


def convert_png_to_webp(
    src: Path,
    dst: Optional[Path] = None,
    quality: int = 80,
    lossless: bool = False,
    overwrite: bool = False,
) -> Path:
    """
    Convert a single PNG image to WebP.

    Args:
        src: Path to the PNG file.
        dst: Output path for the WebP file. If None, same directory with .webp.
        quality: WebP quality (0-100). Ignored for lossless=True.
        lossless: Use lossless WebP encoding.
        overwrite: Overwrite the destination if it exists.

    Returns:
        Path to the created WebP file.
    """
    if not src.exists():
        raise FileNotFoundError(f"Source not found: {src}")
    if src.suffix.lower() != ".png":
        raise ValueError(f"Source must be a .png file: {src}")

    if dst is None:
        dst = src.with_suffix(".webp")
    else:
        # Ensure parent directories exist
        dst.parent.mkdir(parents=True, exist_ok=True)
        if dst.suffix.lower() != ".webp":
            dst = dst.with_suffix(".webp")

    if dst.exists() and not overwrite:
        raise FileExistsError(
            f"Destination exists: {dst}. Use --overwrite to replace."
        )

    with Image.open(src) as im:
        im = im.convert("RGBA")  # preserve alpha if present
        im.save(
            dst,
            format="WEBP",
            lossless=lossless,
            quality=quality if not lossless else 100,
            method=6,  # 0 (fast) - 6 (slow/better)
        )

    return dst


def batch_convert(
    src_dir: Path,
    out_dir: Optional[Path],
    quality: int,
    lossless: bool,
    overwrite: bool,
) -> None:
    png_files = list(src_dir.rglob("*.png"))
    if not png_files:
        print(f"No PNG files found in: {src_dir}")
        return

    for png in png_files:
        rel = png.relative_to(src_dir)
        target_dir = (out_dir or src_dir) / rel.parent
        target_dir.mkdir(parents=True, exist_ok=True)
        dst = target_dir / rel.with_suffix(".webp").name
        try:
            out_path = convert_png_to_webp(
                src=png,
                dst=dst,
                quality=quality,
                lossless=lossless,
                overwrite=overwrite,
            )
            print(f"Converted: {png} -> {out_path}")
        except Exception as e:
            print(f"Failed: {png} ({e})", file=sys.stderr)


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="Convert PNG images to WebP.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    g = p.add_mutually_exclusive_group(required=True)
    g.add_argument(
        "--input",
        "-i",
        type=Path,
        help="Path to a single PNG file to convert.",
    )
    g.add_argument(
        "--input-dir",
        "-I",
        type=Path,
        help="Directory to search recursively for PNG files.",
    )
    p.add_argument(
        "--output",
        "-o",
        type=Path,
        help="Output file (for single input) or directory (for batch).",
    )
    p.add_argument(
        "--quality",
        "-q",
        type=int,
        default=80,
        help="WebP quality (0-100). Ignored if --lossless.",
    )
    p.add_argument(
        "--lossless",
        action="store_true",
        help="Use lossless WebP encoding.",
    )
    p.add_argument(
        "--overwrite",
        action="store_true",
        help="Overwrite existing destination files.",
    )
    return p.parse_args()


def main() -> None:
    args = parse_args()

    if args.input:
        dst = args.output
        try:
            out_path = convert_png_to_webp(
                src=args.input,
                dst=dst,
                quality=args.quality,
                lossless=args.lossless,
                overwrite=args.overwrite,
            )
            print(f"Converted: {args.input} -> {out_path}")
        except Exception as e:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)
    else:
        src_dir = args.input_dir
        out_dir = args.output
        if out_dir is not None and out_dir.suffix:
            print(
                "For batch mode, --output should be a directory, not a file.",
                file=sys.stderr,
            )
            sys.exit(2)
        try:
            batch_convert(
                src_dir=src_dir,
                out_dir=out_dir,
                quality=args.quality,
                lossless=args.lossless,
                overwrite=args.overwrite,
            )
        except Exception as e:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)


if __name__ == "__main__":
    main()
