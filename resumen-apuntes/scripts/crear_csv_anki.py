#!/usr/bin/env python3
"""Crea un CSV importable en Anki a partir de un JSON de fichas.

Uso:
  python crear_csv_anki.py fichas.json salida.csv

El JSON es una lista de objetos: {"front": "...", "back": "...", "tags": "asignatura::tema"}
Importación en Anki: Archivo > Importar. Las tres primeras líneas del CSV son
directivas de Anki (separador, HTML y columna de etiquetas).
"""
import csv
import json
import sys


def main(ruta_json, ruta_csv):
    with open(ruta_json, encoding="utf-8") as f:
        fichas = json.load(f)

    vistas = set()
    validas = []
    avisos = []
    for i, ficha in enumerate(fichas, start=1):
        anverso = (ficha.get("front") or "").strip()
        reverso = (ficha.get("back") or "").strip()
        etiquetas = (ficha.get("tags") or "").strip().replace(" ", "_")
        if not anverso or not reverso:
            avisos.append(f"Ficha {i}: anverso o reverso vacío, se omite")
            continue
        if anverso.lower() in vistas:
            avisos.append(f"Ficha {i}: anverso duplicado, se omite ({anverso[:40]})")
            continue
        vistas.add(anverso.lower())
        if len(anverso) > 300:
            avisos.append(f"Ficha {i}: anverso muy largo ({len(anverso)} caracteres)")
        if len(reverso) > 600:
            avisos.append(f"Ficha {i}: reverso muy largo ({len(reverso)} caracteres)")
        validas.append((anverso, reverso, etiquetas))

    with open(ruta_csv, "w", encoding="utf-8", newline="") as f:
        f.write("#separator:Comma\n#html:false\n#tags column:3\n")
        escritor = csv.writer(f, quoting=csv.QUOTE_ALL, lineterminator="\n")
        for fila in validas:
            escritor.writerow(fila)

    print(f"{len(validas)} fichas escritas en {ruta_csv}")
    for aviso in avisos:
        print("AVISO:", aviso)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    main(sys.argv[1], sys.argv[2])
