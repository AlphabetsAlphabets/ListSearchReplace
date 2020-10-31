def search(board, element_to_search, nested=False):
    ltr = 0
    rtl = -1

    ets = element_to_search
    if nested == True:
        for index, L1 in enumerate(board):
            if ets in index:
                ltr = 0
                rtl = -1

                if L1[ltr] == ets:
                    return index, ltr
                elif L1[rtl] == ets:
                    return index, rtl
                else:
                    ltr += 1
                    rtl -= 1

            else:
                ltr += 1
                rtl -= 1
                continue

    else:
        if board[rtl] == ets:
            return rtl
        elif board[ltr] == ets:
            return ltr
        else:
            ltr += 1
            rtl -= 1
