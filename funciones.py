from animations import *
import random 

class personaje():
    def __init__(self, nombre, fuerza, defensa, raza, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.defensa = defensa
        self.raza = raza
        self.vida = vida
    def stats(self):
        print('nombre: ', self.nombre)
        print('fuerza: ', self.fuerza);
        print('defensa: ', self.defensa)
        print('raza: ', self.raza)
        print('vida: ', self.vida)

    def vivito(self):
        return self.vida > 0
    
    def morido(self):
        self.vida = 0
        print(self.nombre, "murio")

    def daño(self, enemy):
        return self.fuerza - enemy.defensa

    def attack(self, enemy):
        daño = self.daño(enemy)
        enemy.vida = enemy.vida - daño
        if enemy.vivito():
            print('a', enemy.nombre, "le quedan", enemy.vida )
        else:
            enemy.morido()

nombre = input('cual es tu nombre? ')
raza = input('cual es tu raza? ')

if raza == 'elfo':
    yo = personaje(nombre, 70, 60, 'elfo', 130)
    yo.stats()
elif raza == 'minotauro':
    yo = personaje(nombre, 100, 20, 'minotauro', 230)
    yo.stats()
elif raza == 'mago':
    yo = personaje(nombre, 140, 80, 'mago', 30)
    yo.stats()
else:
    print('parametro incorrecto')


posible = [
    personaje('dragon', 30, 2, 'zalamander', 200),
    personaje('ogro', 30, 2, 'waaaaaagh', 50),
    personaje('nigromante', 30, 2, 'special', 2),
    personaje('albañil', 30, 2, 'human', 100)
]

enemigo = random.choice(posible)

print("aparecion un enemigo!!!")

if enemigo.nombre == 'dragon':
    dragon()
elif enemigo.nombre == 'nigromante':
    nigromante()
elif enemigo.nombre == 'albañil':
    albañil()
elif enemigo.nombre == 'ogro':
    ogro()


decision = input('deseas atacar? S/N ')

if decision == 's':
    yo.attack(enemigo)
    enemigo.attack(yo)

else:
    enemigo.attack(yo)
    yo.attack(enemigo)