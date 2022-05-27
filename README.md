# BOTW Mod Fixer

A simple tool to recalculate the RSTB and pack various archives on the fly within a Cemu graphic pack for quick and efficient testing.

<br>

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