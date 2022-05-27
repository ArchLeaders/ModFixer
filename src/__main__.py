import asyncio
import os
import subprocess
import sys
import oead

from bcml.mergers.rstable import get_stock_rstb, RstbMerger
from bcml.util import SARC_EXTS, get_settings
from bcml.install import find_modded_files
from modfixer.builder import build_sarc
from io import BytesIO
from pathlib import Path
from rstb import ResourceSizeTable
from time import time
from modfixer.unbuilder import unbuild_sarc
from modfixer import dependency_check


async def main():

    dependency_check()

    # Start tracking
    start = time()
    i: int = 0

    mod_dir = Path(
        "D:\\Botw\\Cemu (Freecam)\\graphicPacks\\BreathOfTheWild_Randomizer"
    )  # testing dir

    # Get/set meta data
    mod_dir = Path(os.getcwd()).absolute()

    for folder in mod_dir.glob("*"):
        if folder.is_dir() and (folder.name == "content" or folder.name == "aoc"):

            tasks: list = []

            for file in folder.glob("**/*"):
                if file.is_dir() and file.suffix in SARC_EXTS:
                    tasks.append(asyncio.create_task(build_sarc(file)))

            await asyncio.gather(*tasks)

    rstb: ResourceSizeTable = get_stock_rstb()
    modded_files = find_modded_files(mod_dir)
    modded_files = RstbMerger().generate_diff(mod_dir, modded_files)

    for file, size in modded_files.items():
        rstb.set_size(file, size)

    print("Serializing ResourceSizeTable...")

    rstb_path = Path(
        f"{mod_dir}\\content\\System\\Resource\\ResourceSizeTable.product.srsizetable"
    )

    buf = BytesIO()
    rstb.write(buf, be=get_settings("wiiu"))
    rstb_path.parent.mkdir(parents=True, exist_ok=True)
    rstb_path.write_bytes(oead.yaz0.compress(buf.getvalue()))

    end = time()
    print(f"Operation completed in {end-start} seconds.")


async def main_unbuild():

    dependency_check()

    # Start tracking
    start = time()

    mod_dir = Path(
        "D:\\Botw\\Cemu (Freecam)\\graphicPacks\\BreathOfTheWild_Randomizer"
    )  # testing dir

    # Get/set meta data
    # mod_dir = Path(os.getcwd()).absolute()

    tasks: list = []

    for file in mod_dir.glob("**/*"):
        if file.is_file() and file.suffix in SARC_EXTS:
            print(f"Unpacking {file.stem}\t\t\t\t", end="\r")
            tasks.append(asyncio.create_task(unbuild_sarc(file)))

    await asyncio.gather(*tasks)

    end = time()
    print(f"\nOperation completed in {end-start} seconds.")


def shell_main():
    asyncio.run(main())


def shell_main_unbuild():
    asyncio.run(main_unbuild())


def shell_sarc():
    if len(sys.argv) > 1:
        path = Path(sys.argv[1])
        if path.is_file():
            asyncio.run(unbuild_sarc(path))
        elif path.is_dir():
            asyncio.run(build_sarc(path))


def shell_debug(open_uking: bool = True):
    asyncio.run(main())

    cemu_dir = get_settings("cemu_dir")
    game_dir = get_settings("game_dir")
    uking = f"{Path(game_dir).parent}\\code\\U-King.rpx"

    if open_uking:
        subprocess.run(f'"{cemu_dir}\\Cemu.exe" -g "{uking}"')
    else:
        subprocess.run(f'"{cemu_dir}\\Cemu.exe"')


def shell_partial_debug():
    shell_debug(False)


if __name__ == "__main__":
    asyncio.run(shell_debug())
