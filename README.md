# Denison

Automatización simple en Python. Un solo archivo, sin instalar nada.

## Uso

```bash
python denison.py backup ~/Documents ~/respaldos   # zip con fecha
python denison.py organizar ~/Downloads            # ordena por extensión
python denison.py check https://example.com        # ¿responde la web?
python denison.py check https://example.com --cada 60   # repetir cada 60 s
```

## Agregar tu propia tarea

En `denison.py`, escribe una función y añádela a `TAREAS`:

```python
def saludar(nombre):
    return f"Hola, {nombre}"

TAREAS = {..., "saludar": saludar}
```

Luego: `python denison.py saludar Andy`

## Subir a GitHub

```bash
git init && git add . && git commit -m "Denison"
git branch -M main
git remote add origin https://github.com/TU-USUARIO/denison.git
git push -u origin main
```
