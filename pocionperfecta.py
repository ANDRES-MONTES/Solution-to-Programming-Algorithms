"""
Durante la noche de Halloween 🎃, una bruja 🧙‍♀️ está preparando una mezcla mágica. Tiene una lista de pociones, cada una con un poder asociado, y quiere combinar dos de ellas para obtener un poder total específico.

Dada una lista de enteros donde cada número representa el poder de una poción 🧪 y un número entero que representa el poder objetivo, debes encontrar el índice de las dos primeras pociones que sumen exactamente el poder objetivo.

Por ejemplo:

const potions = [4, 5, 6, 2]
const goal = 8

createMagicPotion(potions, goal) // [2, 3]
Si no se encuentra ninguna combinación, devuelve undefined

const potions = [1, 2, 3, 4]
const goal = 9

createMagicPotion(potions, goal) // undefined    
    
"""

def solution(potions:list[int], target:int) -> list:
    info:list = []
    for i in range(len(potions)):
        for j in range(i + 1, len(potions)):
            if potions[i] + potions[j] == target:
                info.append([i, j])
                
    if len(info) == 0:
        return None
    
    return min(info, key=lambda x: x[1])
    
    
if __name__ == '__main__':
    potions = [4, 5, 6, 2]
    goal = 8
    result = solution([1, 2, 3, 4, 5], 8)
    print(result)