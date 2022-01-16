import time as time
import players as p
import teams as t
import leagues as l 
import match as m


print('binvinida tola Pank League Simulator\n dale enter pra tacale play')
n=0
input('pley')
pl=l.League(int(2))
pl.showStandings()
input('dale')
rodada=0
while rodada<30:
    for h,a in pl.schedule[pl.week]:
            #if h or a == 
            #pl.showTeam()
            #print(h.squad, a.squad)
            pl.simMatch(h,a)
            pl.showStandings()
            #input('proximo')
    pl.showStandings()
    rodada+=1
    pl.week+=1
    #input('prox rodada')
