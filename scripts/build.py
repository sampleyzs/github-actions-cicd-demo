"""Build a dependency-free executable zipapp and its SHA-256 checksum."""

import hashlib
import os
import sys
import zipapp
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "app"))

from cicd_demo import __version__


def main() -> None:
    if os.environ.get("GITHUB_REF_TYPE") == "tag":
        tag_version = os.environ["GITHUB_REF_NAME"].removeprefix("v")
        if tag_version != __version__:
            raise SystemExit(
                f"标签版本 {tag_version} 与程序版本 {__version__} 不一致，停止发布"
            )

    dist = ROOT / "dist"
    dist.mkdir(exist_ok=True)
    archive = dist / "cicd-demo.pyz"
    zipapp.create_archive(
        source=ROOT / "app",
        target=archive,
        interpreter="/usr/bin/env python3",
    )
    digest = hashlib.sha256(archive.read_bytes()).hexdigest()
    (dist / "SHA256SUMS.txt").write_text(
        f"{digest}  {archive.name}\n", encoding="utf-8"
    )
    print(f"构建完成：{archive.name}，版本：{__version__}")
    print(f"SHA-256：{digest}")


if __name__ == "__main__":
    main()
