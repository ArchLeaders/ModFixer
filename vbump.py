from pathlib import Path
from sys import argv as args

# Deerialize
setup = Path(".\\setup.py")
setup_split_text = setup.read_text().split("#")
deserialized_str = (
    setup_split_text[0].replace(" ", "").replace('"', "").replace("VERSION=", "")
)
version = deserialized_str.split(".")

# Bump
i = int(args[1])
version[i] = int(version[i])
version[i] += 1

# Serialize
version[i] = str(version[i])
version = ".".join(version)
serialized_str = f'VERSION = "{version}"  #{setup_split_text[1]}'

# Write
setup.write_text(serialized_str)
Path(".\\.vscode\\version").write_text(version)
