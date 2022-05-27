# Copied from NiceneNerd/BCML/bcml/__init__.py


def native_msg(msg: str, title: str):
    import ctypes

    ctypes.windll.user32.MessageBoxW(
        0,
        msg,
        title,
        0x0 | 0x10,
    )


def dependency_check():
    try:
        import oead

        del oead
    except ImportError:
        from platform import system

        if system() == "Windows":
            native_msg(
                "The latest (2019) Visual C++ redistributable is required to use GfxLoader. "
                "Please download it from the following link and try again:\n"
                "https://aka.ms/vs/16/release/vc_redist.x64.exe",
                "Dependency Error",
            )
        from sys import exit as ex

        ex(1)
