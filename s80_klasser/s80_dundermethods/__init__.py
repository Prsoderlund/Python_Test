


import unittest
from Djungel import *

apan = Apa()
elefant = Elefant()

assert(isinstance(apan, Apa))
assert(isinstance(apan, Djungel))
assert(type(apan)is Apa)
assert(str(apan == "Apan äter banan"))
assert(apan.__str__() == "Apan äter banan")
assert(str(elefant) == "Dricker vatten")
assert(isinstance(elefant, Elefant))
assert(isinstance(elefant, Djungel))