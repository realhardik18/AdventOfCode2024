def parse_button(button):
    button=button[9:].split(',')
    button=[int(b[3:]) for b in button]
    return tuple(button)

def parse_prize(prize):
    prize=prize[6:].split(',')
    prize=[int(p[3:]) for p in prize]    
    return tuple(prize)

def parse_play(play):
    play[0]=parse_button(play[0])
    play[1]=parse_button(play[1])
    play[2]=parse_prize(play[2])
    return tuple(play)
