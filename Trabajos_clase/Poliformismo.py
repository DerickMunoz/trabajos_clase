class Perro:
    def hablar(self):
        print("Guau!")
 
class Gato:
    def hablar(self):
        print("Miau!")
 
hachiko = Perro()
garfield = Gato()
for animal in [hachiko, garfield]:
    animal.hablar()
