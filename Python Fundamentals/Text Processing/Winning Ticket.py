data = input().split(", ")

winning_symbols = ['@', '#', '$', '^']
for ticket in data:
    ticket = ticket.strip()
    if not len(ticket) == 20:
        print("invalid ticket")
        continue

    left_side_ticket = ticket[:len(ticket)//2]
    right_side_ticket = ticket[len(ticket)//2:]

    left_side_symbols = ""
    right_side_symbols = ""
    for el in left_side_ticket:
        if el in winning_symbols:
            left_side_symbols += el

    for el in right_side_ticket:
        if el in winning_symbols:
            right_side_symbols += el

    both_side = left_side_symbols + right_side_symbols

    if len(left_side_symbols) == 10 and len(right_side_symbols) == 10 and len(set(both_side)) == 1:
        print(f'ticket "{ticket}" - {len(left_side_symbols)}{left_side_symbols[0]} Jackpot!')

    else:
        win_symbols_left = list(set(left_side_symbols))
        win_symbol = ""
        for symbol in win_symbols_left:
            counter = 0
            for el in left_side_symbols:
                if symbol == el:
                    counter += 1
                    if counter == 6:
                        break
            if counter == 6:
                win_symbol = symbol
                break

        count_win_left = 0
        for el in left_side_symbols:
            if el == win_symbol:
                count_win_left += 1
        count_win_right = 0
        for el in right_side_symbols:
            if el == win_symbol:
                count_win_right += 1

        final_match = min(count_win_right, count_win_left)

        if final_match * win_symbol in left_side_ticket and final_match * win_symbol in right_side_ticket and final_match >= 6:
           print(f'ticket "{ticket}" - {final_match}{win_symbol}')
        else:
            print(f'ticket "{ticket}" - no match')