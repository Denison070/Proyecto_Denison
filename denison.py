"""Denison: automatización simple en un solo archivo.

Uso:
    python denison.py backup  CARPETA  DESTINO
    python denison.py organizar CARPETA
    python denison.py check   URL
    python denison.py <tarea> ... --cada 60     (repite cada 60 segundos)

Para agregar tu propia tarea, escribe una función y añádela a TAREAS.
"""
import shutil
import sys
import time
import urllib.request
from datetime import datetime
from pathlib import Path


def backup(origen, destino):
    """Comprime una carpeta en un .zip con fecha y hora."""
    origen, destino = Path(origen).expanduser(), Path(destino).expanduser()
    destino.mkdir(parents=True, exist_ok=True)
    sello = datetime.now().strftime("%Y%m%d-%H%M%S")
    return shutil.make_archive(str(destino / f"{origen.name}-{sello}"), "zip", origen)


def organizar(carpeta):
    """Mueve los archivos a subcarpetas según su extensión."""
    base, movidos = Path(carpeta).expanduser(), 0
    for f in base.iterdir():
        if f.is_file():
            sub = base / (f.suffix.lstrip(".").lower() or "sin_extension")
            sub.mkdir(exist_ok=True)
            shutil.move(str(f), str(sub / f.name))
            movidos += 1
    return f"{movidos} archivos organizados"


def check(url):
    """Verifica que una página web responda."""
    with urllib.request.urlopen(url, timeout=10) as r:
        return f"{url} respondió {r.status}"


TAREAS = {"backup": backup, "organizar": organizar, "check": check}


def main():
    args = sys.argv[1:]
    cada = None
    if "--cada" in args:
        i = args.index("--cada")
        cada = float(args[i + 1])
        del args[i:i + 2]

    if not args or args[0] not in TAREAS:
        print(__doc__)
        print("Tareas:", ", ".join(TAREAS))
        return

    tarea, params = TAREAS[args[0]], args[1:]
    while True:
        try:
            print(f"[{datetime.now():%H:%M:%S}] {tarea(*params)}")
        except Exception as e:
            print(f"[{datetime.now():%H:%M:%S}] Error: {e}")
        if cada is None:
            break
        time.sleep(cada)


if __name__ == "__main__":
    main()
