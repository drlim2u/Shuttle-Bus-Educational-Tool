from TokenType import TokenType


class Loop(Scope):
    """
    Class to define the Loop object to be used during compilation of the whole program.
    """
    def __init__(self, line_number, instructions):
        """
        Constructor for the Loop object.
        :param line_number: The line the function is defined at
        :param instructions: The program to be compiled
        """
        super().__init__(line_number, instructions)
        self.__type = TokenType.SCOPE_LOOP
