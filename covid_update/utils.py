import hashlib


BLOCK_SIZE = 65536


def hash_archivo(ruta=None, archivo=None):
    file_hash = hashlib.sha256()

    if archivo is None:
        archivo = open(ruta, 'rb')

    bloque = archivo.read(BLOCK_SIZE)
    while len(bloque) > 0:
        file_hash.update(bloque)
        bloque = archivo.read(BLOCK_SIZE)

    return archivo
