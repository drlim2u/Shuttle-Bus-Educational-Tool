from Animation import animation
from LoadInstructions import load_instructions
from Tokenizer import *
from Analyzer import *
from Compiler import *


if __name__ == '__main__':
    program = load_instructions("Instructions.txt")
    tokenized_program = tokenizer(program)
    analysis = analyzer(tokenized_program)
    if analysis is None:
        print("There were no issues with the program")
        compiled_program = compiler(tokenized_program)
        animation(compiled_program)
        input('Press any enter to close window . . . ')

    else:
        print("There was an error with the syntax of the program")
        print(analysis)