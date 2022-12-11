from typing import List


def input_to_string(input: str) -> str:
    file = open(input, "r")
    return file.read().rstrip("\n")

def input_to_lines(input: str) -> List[str]:
    return input_to_string(input).split("\n")
    
def input_to_int(input: List[str]) -> List[int]:
    return [int(x) for x in input]

def paragraph_lines(input: str) -> List[str]:
    file = open(input, "r")
    return [x.split("\n") for x in file.read().split("\n\n")]
