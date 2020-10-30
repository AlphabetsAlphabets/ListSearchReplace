class ListSearchReplace:
    def __init__(self, board, nested=False):
        self.board = board
        self.nested = nested

    def search(self, element_to_search):
        if self.nested == True:
            for index1, element in enumerate(self.board):
                if element_to_search in element:
                    for index2, value in enumerate(element):
                        if element[index2] == element_to_search:
                            self.exist = True
                            return index1, index2
                        elif (element[index2] == element_to_search) == False:
                            pass

        elif self.nested == False:
            if element_to_search in self.board:
                for index, value in enumerate(self.board):
                    if self.board[index] == element_to_search:
                        return index
                    elif (self.board[index] == element_to_search) == False:
                        pass

    def replace(self, element_to_replace, replacement, all_elements=False):
        self.to_replace = element_to_replace
        if self.nested == True and all_elements == False:
            ia, ib = self.search(self.to_replace)
            self.board[ia][ib] = replacement

        elif self.nested == False and all_elements == False:
            ia = self.search(self.to_replace)
            self.board[ia] = replacement

        elif self.nested == True and all_elements == True:
            for element in self.board:
                for index, value in enumerate(element):
                    if value == self.to_replace:
                        element[index] = replacement

                    elif (self.to_replace == element[index]) == False:
                        pass

        elif self.nested == False and all_elements == True:
            for index, value in enumerate(self.board):
                if value == self.to_replace:
                    self.board[index] = replacement

                elif (self.to_replace == self.board[index]) == False:
                    pass

    def typecast(self, to_type):
        new_board = list()
        to_type = to_type.lower()
        if to_type == 'str' and self.nested == False:
            for index, item in enumerate(self.board):
                self.board[index] = (str(item))

        elif to_type == 'int' and self.nested == False:
            for index, item in enumerate(self.board):
                self.board[index] = (str(item))

        elif to_type == 'str' and self.nested == True:
            for L1 in self.board:
                for index, item in enumerate(L1):
                    L1[index] = str(item)

        elif to_type == 'int' and self.nested == True:
            for L1 in self.board:
                for index, item in enumerate(L1):
                    L1[index] = int(item)
