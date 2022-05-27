# BOTW Mod Fixer

A simple tool to recalculate the RSTB and pack various archives on the fly within a Cemu graphic pack for quick and efficient testing.

<br>

## Installing:

To install the python module, type `pip install modfixer` in a command prompt window.<br>
**This module is <ins>required</ins> for the AHK script and registry edits to work!**

The Build/Unbuild SARC commands can be added to the File Explorer context menu by downloading and running the [SarcTools.reg](https://raw.githubusercontent.com/ArchLeaders/ModFixer/master/Tools/SarcTools.reg) file.

To enable the Hotkeys, download and install [AutoHotkey](https://www.autohotkey.com/download/ahk-install.exe) _(may or may not be required to use the EXE)_ and run the [AHK script](https://github.com/ArchLeaders/ModFixer/raw/master/Tools/BotwModFixer.ahk) or [built executable](https://github.com/ArchLeaders/ModFixer/raw/master/Tools/BotwModFixerHotkeys.exe).

## Commands:

_Note: Hotkeys with `Shift` leave the CLI open after running the command._

### FIX
> Run inside the folder containing `content` or `aoc`.

_The <ins>fix</ins> command will build any unpacked SARC archives and re-generate the RSTB._

---
<br>

### UNFIX
> Run inside any folder containing one or more SARC files.

_The <ins>unfix</ins> command will unbuild any known SARC archives (via file extension) recursively in the working directory._

- **Hotkey** - `Ctrl + Alt + F8` **|** `Ctrl + Shift + Alt + F8`

---
<br>

### DEBUG
> Run inside the folder containing `content` or `aoc`. | Use the hotkey <ins>inside</ins> the content or aoc folder.

_Executes the [fix](#fix)> command and runs BOTW in Cemu._

- **Hotkey** - `F5` **|** `Shift + F5`

---
<br>

### PDEBUG
> Run inside the folder containing `content` or `aoc`. | Use the hotkey <ins>inside</ins> the content or aoc folder.

_Executes the [fix](#fix) command and runs Cemu._

- **Hotkey** - `F6` **|** `Shift + F6`

---
<br>

### SHELL_SARC &lt;file|folder&gt;
> Run anywhere and pass a file or folder as the only argument.

_The <ins>shell\_sarc</ins> command will unbuild or rebuild any SARC file/folder._

- **Hotkey** - `F8` **|** `Shift + F8`

---
<br>