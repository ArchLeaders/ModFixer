import oead

from bcml.util import (
    SARC_EXTS,
    BYML_EXTS,
    AAMP_EXTS,
)
from pathlib import Path
from shutil import rmtree
from typing import Union


def _build_sarc_key(src: Path, rel: Path, remove_suffix: bool = False) -> str:

    if remove_suffix:
        src = src.with_suffix("")

    return src.relative_to(rel).as_posix().replace("[--]", "/")


def _build_yaml(file: Path) -> bytes:
    real_file = file.with_suffix("")
    data: bytes
    if real_file.suffix in BYML_EXTS or real_file.suffix == ".byaml":
        data = oead.byml.to_binary(oead.byml.from_text(file.read_text("utf-8")), True)
    elif real_file.suffix in AAMP_EXTS:
        data = oead.aamp.ParameterIO.from_text(file.read_text("utf-8")).to_binary()
    else:
        raise TypeError("Can only build AAMP or BYML files from YAML")
    if real_file.suffix.startswith(".s"):
        data = oead.yaz0.compress(data)

    return data


async def build_sarc(folder: Union[Path, str]) -> Path:

    # Locate and backup source folder
    source = Path(folder) if isinstance(folder, str) else folder

    # Build folder
    sarc = oead.SarcWriter(oead.Endianness.Big)
    i = 0

    for file in source.rglob("**/*"):

        if file.is_dir():
            if file.suffix in SARC_EXTS:
                sarc.files[_build_sarc_key(file, source)] = (
                    await build_sarc(file)
                ).read_bytes()
            continue

        if file.suffix == ".yml":
            sarc.files[_build_sarc_key(file, source, True)] = _build_yaml(file)

        else:
            sarc.files[_build_sarc_key(file, source)] = file.read_bytes()

        i += 1

    if source.suffix.startswith(".s") and source.suffix != ".sarc":
        sarc_data = oead.yaz0.compress(sarc.write()[1])
    else:
        sarc_data = sarc.write()[1]

    # Delete the original folder
    rmtree(source)
    source.write_bytes(sarc_data)
    print(f"Compiled {i} files in {folder}")

    return source
