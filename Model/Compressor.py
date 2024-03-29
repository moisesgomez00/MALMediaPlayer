#-*- coding:utf-8 -*-
import sys, zipfile, random, os

class Compressor:
    def __init__(self):
        self.names = None
        self.fileName = None
        self.file = None

    def splitNames(self):
        """
            Return a list
            Separa los nombres de los archivos.
        """
        self.names = sys.argv[1].split("@")
        return self

    def createFileName(self):
        """
            Return a Compressor
            establece una cadena de 15 caracteres, esta se usa como nombre del archivo.
        """
        self.fileName =  "%s%s%s" %("SongPack_","".join(
            random.choices(
                "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
                k=3
            )
        ) , ".zip")
        return self

    def createFile(self):
        """
            Return a Compressor
            crea y establece un objeto zipfile.ZipFile con el nombre que se tuvo que haber generado
        """
        self.file = zipfile.ZipFile(self.fileName,"w")
        return self

    def crompress(self):
        for i in self.names:
            try:
                self.file.write(i)
            except FileNotFoundError as fl:
                pass
        self.file.close()
        return self
    

print(
    Compressor().splitNames().createFileName().createFile().crompress().fileName
)