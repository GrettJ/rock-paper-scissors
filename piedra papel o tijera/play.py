from enum import Enum

class Result(Enum):
    EQUAL = 0
    WINS = 1
    LOSES = 2

class Play():
    def description(self):
        pass

    def compare(self, otherPlay):
        """
        Se compara con la otra jugada y devuelve un resultado de la comparacion
        """
        pass
    
class Paper(Play):
    def description(self):
        return "Papel"

    def compare(self, otherPlay):
        """
        Compara papel con otras jugadas
        """
        result = None
        if type(otherPlay) == Paper:
            result = None
        elif type(otherPlay) == Rock:
            result = self
        elif type(otherPlay) == Spock:
            result = self
        elif type(otherPlay) == Lizard:
            result = otherPlay
        else:
            result = otherPlay
        return result

class Rock(Play):
    def description(self):
        return "Piedra"

    def compare(self, otherPlay):
            
        """
        Compara piedra con otras jugadas
        """
        result = None
        if type(otherPlay) == Rock:
            result = None
        elif type(otherPlay) == Scissors:
            result = self
        elif type(otherPlay) == Lizard:
            result = self
        elif type(otherPlay) == Spock:
            result = otherPlay
        else:
            result = otherPlay
        return result

class Scissors(Play):
    def description(self):
        return "Tijera"

    def compare(self, otherPlay):
            
        """
        Compara piedra con otras jugadas
        """
        result = None
        if type(otherPlay) == Scissors :
            result = None
        elif type(otherPlay) == Paper or type(otherPlay) == Lizard:
            result = self
        else:
            result = otherPlay
        return result


class Lizard(Play):
    def description(self):
        return "Lagarto"

    def compare(self, otherPlay):
            
        """
        Compara piedra con otras jugadas
        """
        result = None
        if type(otherPlay) == Lizard:
            result = None
        elif type(otherPlay) == Paper or type(otherPlay) == Spock:
            result = self
        else:
            result = otherPlay
        return result
        
class Spock(Play):
    def description(self):
        return "Spock"

    def compare(self, otherPlay):
            
        """
        Compara piedra con otras jugadas
        """
        result = None
        if type(otherPlay) == Spock:
            result = None
        elif type(otherPlay) == Scissors or type(otherPlay) == Rock:
            result = self
        else:
            result = otherPlay
        return result
    pass