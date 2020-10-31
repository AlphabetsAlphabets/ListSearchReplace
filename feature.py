def search(board, element_to_search, nested=False):
    ltr = 0
    rtl = -1

    guard = 0
    limit = len(board)

    ets = element_to_search
    if nested == False:
        while guard < limit:
            try:
                if board[ltr] == ets:
                    return ltr
                elif board[rtl] == ets:
                    return rtl
                else:
                    ltr += 1
                    rtl -= 1
            except IndexError:
                guard += 1
                continue

    else:
        while guard < limit:
            for index, list1 in enumerate(board):
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
