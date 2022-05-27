import asyncio
import oead

from bcml.util import (
    SARC_EXTS,
    BYML_EXTS,
    AAMP_EXTS,
    unyaz_if_needed,
)
from oead import aamp
from pathlib import Path
from time import time
from typing import Union


async def _unbuild_file(sarc_file, out):

    SKIP_SARCS = {
        "tera_resource.Cafe_Cafe_GX2.release.ssarc",
        "tera_resource.Nin_NX_NVN.release.ssarc",
    }

    nested_path = sarc_file.name
    if str(nested_path).startswith("/"):
        nested_path = f"[--]{Path(nested_path).name}"

    sarc_out = Path(f"{out}\\{nested_path}")
    sarc_out.parent.mkdir(parents=True, exist_ok=True)

    ext = sarc_out.suffix

    if ext in AAMP_EXTS:
        sarc_out.with_suffix(f"{sarc_out.suffix}.yml").write_text(
            aamp.ParameterIO.from_binary(unyaz_if_needed(sarc_file.data)).to_text(),
            encoding="utf8",
        )
    elif ext in BYML_EXTS or ext == ".byaml":
        sarc_out.with_suffix(f"{sarc_out.suffix}.yml").write_text(
            oead.byml.to_text(oead.byml.from_binary(unyaz_if_needed(sarc_file.data))),
            encoding="utf8",
        )
    else:
        sarc_out.write_bytes(sarc_file.data)

        if ext in SARC_EXTS and sarc_file.name not in SKIP_SARCS:
            await unbuild_sarc(sarc_out)


async def unbuild_sarc(file: Union[Path, str]):

    # Start tracking
    start = time()

    # Verify as SARC
    sarc_path = Path(file) if isinstance(file, str) else file
    data = unyaz_if_needed(file.read_bytes())
    if data[0:4] != b"SARC":
        return

    # Backup source file
    out: str = sarc_path.absolute()
    sarc_path = sarc_path.rename(f"{sarc_path}.tmp")

    # Unpack SARC
    sarc = oead.Sarc(data)

    for sarc_file in sarc.get_files():
        await _unbuild_file(sarc_file, out)

    # Delete the original file
    sarc_path.unlink()
    end = time()

    print(f"Unpacked {Path(file).stem} in {end-start} seconds.")
