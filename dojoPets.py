import ninja
import pet

bessie=pet.Pet('Bessie','Cow','Flying Over the Moon')
bigBessie=pet.Cow('Big Bessie')
speedy=pet.Turtle('Speedy')
oscar=ninja.Ninja('Oscar', 'Lance', 10,'Grass', bessie)
oscar.walk().feed().bathe()
print(bessie.health)
oscar=ninja.Ninja('Oscar', 'Lance', 10,'Grass', bigBessie)
oscar.walk().feed().bathe()
print(bigBessie.health)
oscar=ninja.Ninja('Oscar', 'Lance', 10,'Grass', speedy)
oscar.walk().feed().bathe()
print(speedy.health)