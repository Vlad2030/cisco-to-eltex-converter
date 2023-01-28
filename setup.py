import os
import platform


def installLib() -> None:
    system: str = platform.system()
    try:
        if "Linux" in system:
            return os.system("pip3 install -r requirements.txt")
        elif "Windows" or "Darwin" in system:
            return os.system("pip install -r requirements.txt")
    except Exception:
        return print(Exception)


if __name__ == "__main__":
    installLib()