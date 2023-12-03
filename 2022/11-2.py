from readlines import *
import math

lines = paragraph_lines("day11.txt")

monkeys = []

class Monkey:
    def __init__(self, id:str, starting_items:List[int], test:int, operation_data:List[str], next_moves:List[int]) -> None:
        self.id = id
        self.starting_items= starting_items
        self.test = test
        self.operation_data = operation_data
        self.next_moves = next_moves
        self.counter = 0

    def __str__(self) -> str:
        return f"{self.id} start={self.starting_items}/ divisible_by_{self.test}/ Operation: new = old {self.operation_data[0]} {self.operation_data[1]}/ True, False:{self.next_moves}"

    def operation(self, input:int) -> int:
        output = 0
        action = 0
        if(self.operation_data[1] == "old"):
            action = input
        else:
            action = int(self.operation_data[1])
        match self.operation_data[0]:
            case "+":
                output = input + action
            case "-":
                output = input - action
            case "*":
                output = input * action
            case "/":
                output = input / action
        return output

    def play(self) -> None:
        for item in self.starting_items:
            self.counter += 1
            item = self.operation(item)
            if(item % self.test == 0):
                monkeys[self.next_moves[0]].starting_items.append(item)
            else:
                item %= lcm
                monkeys[self.next_moves[1]].starting_items.append(item)
        self.starting_items.clear()

def create_monkeys():
    for line in lines:
        newline = [line[x].split(" ") for x in range(len(line))]
        id = newline[0][1].rstrip(":")
        starting_items = []
        for x in newline[1]:
            if(x.rstrip(", ").isnumeric()):
                starting_items.append(int(x.rstrip(", ")))
        operation_data = [newline[2][6], newline[2][-1]]
        test = int(newline[3][-1])
        next_moves = [int(newline[4][-1]), int(newline[5][-1])]
        monkeys.append(Monkey(id, starting_items, test, operation_data, next_moves))

create_monkeys()

lcm = math.prod([x.test for x in monkeys])

for x in range(10000):
    for monkey in monkeys:
        monkey.play()

inspected_items = sorted([x.counter for x in monkeys], reverse = True)

print(inspected_items[0] * inspected_items[1])
