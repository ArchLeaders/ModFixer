VERSION = "1.0.0"  # Version const for publish script

from pathlib import Path
from setuptools import setup

with open(".\\README.md", "r") as fs:
    long_description = fs.read()

setup(
    name="ModFixer",
    version=VERSION,
    author="ArchLeaders",
    author_email="archleadership28@gmail.com",
    description="CLI for on the fly GFX packing to load as a Cemu graphic pack for quick and efficient testing.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ArchLeaders/ModFixer",
    include_package_data=True,
    packages=["modfixer"],
    package_dir={"modfixer": "src"},
    entry_points={
        "console_scripts": [
            "fix = modfixer.__main__:shell_main",
            "unfix = modfixer.__main__:shell_main_unbuild",
            "shell_sarc = modfixer.__main__:shell_sarc",
            "debug = modfixer.__main__:shell_debug",
            "pdebug = modfixer.__main__:shell_partial_debug",
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3 :: Only",
    ],
    python_requires=">=3.7",
    install_requires=[
        "rstb>=1.2.2",
        "bcml>=3.8.6",
        "oead~=1.2.0",
    ],
    zip_safe=False,
)
