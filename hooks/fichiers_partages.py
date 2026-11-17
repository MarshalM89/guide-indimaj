"""Hook MkDocs de la version arabe (mkdocs.ar.yml).

Ajoute au site arabe les fichiers non Markdown du dossier docs/ (captures
d'écran, guides PDF, feuille de style, logo) qui n'existent pas dans docs-ar/.
Les pages arabes peuvent ainsi utiliser les mêmes chemins relatifs que les
pages françaises, sans dupliquer les images dans le dépôt.
"""
import os

from mkdocs.structure.files import File, Files


def on_files(files: Files, config) -> Files:
    racine = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    docs_fr = os.path.join(racine, "docs")
    existants = {f.src_uri for f in files}
    for dossier, _, noms in os.walk(docs_fr):
        for nom in noms:
            if nom.endswith(".md"):
                continue
            chemin = os.path.relpath(os.path.join(dossier, nom), docs_fr).replace(os.sep, "/")
            if chemin in existants:
                continue
            files.append(File(chemin, docs_fr, config.site_dir, config.use_directory_urls))
    return files
