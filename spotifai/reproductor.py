from pygame import mixer
class Reproductor:
    #atributos
    archivo = None

    #constructor
    def __init__(self, archivo):
        self.archivo = archivo
        mixer.init()
        mixer.music.load(archivo)

    def play(self):
        mixer.music.play()
        return "▶Reproduciendo Musica"
    
    def pause(self):
        mixer.music.pause()
        return "⏸La Musica se ha pausado"
    
    def stop(self):
        mixer.music.stop()
        return "⏹ La Musica se detuvo"

    def volume(self, v):
        mixer.music.set_volume(v)
        return "Definiendo volumen a {}".format(v)