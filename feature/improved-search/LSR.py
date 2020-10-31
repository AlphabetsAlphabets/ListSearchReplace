class ListSearchReplace:
    def __init__(self, board, nested=False):
        self.board = board
        self.nested = nested

    def search(self, element_to_search):
        ltr = 0
        rtl = -1

        guard = 0
        limit = len(self.board)

        ets = element_to_search
        if self.nested == False:
            while guard <= limit:
                try:
                    if self.board[ltr] == ets:
                        return ltr
                    elif self.board[rtl] == ets:
                        return rtl
                    else:
                        ltr += 1
                        rtl -= 1
                except IndexError:
                    guard += 1
                    continue
        else:
            while guard < limit:
                for index, list1 in enumerate(self.board):
                    try:
                        if list1[ltr] == ets:
                            return index, ltr
                        elif list1[rtl] == ets:
                            return index, rtl
                        else:
                            ltr += 1
                            rtl -= 1
                    except IndexError:
                        guard += 1
                        continue

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
