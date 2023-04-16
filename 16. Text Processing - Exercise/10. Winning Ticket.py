def is_winning_ticket(ticket):
    if len(ticket) != 20:
        return "invalid ticket"

    first_half = ticket[:10]
    second_half = ticket[10:]
    for symbol in symbols:
        for symbol_length in range(10, 5, -1):
            match_symbol = symbol * symbol_length
            if match_symbol in first_half and match_symbol in second_half:
                if len(match_symbol) == 10:
                    return f'ticket "{ticket}" - {len(match_symbol)}{symbol} Jackpot!'
                return f'ticket "{ticket}" - {len(match_symbol)}{symbol}'
    return f'ticket "{ticket}" - no match'


tickets = [ticket.strip() for ticket in input().split(', ')]
symbols = ['@', '#', '$', '^']

for ticket in tickets:
    print(is_winning_ticket(ticket))





