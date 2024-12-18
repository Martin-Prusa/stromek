
#Zapoctovy test z programovania:


    #prvy tyzden po prazdninach je prvy termin
    #3 pokusy
    #Okruhy:
        #prehladavanie stavoveho prostoru
        #rekurzivni generovani
        #nieco s grafmi





#infix => (1-2)+3*4
#prefix => + - 1 2 * 3 4
#postfix => 1 2 - 3 4 * +



import stavitelka as st

st.Hranol(y=-3.5,sx=1,sy=2,sz=1,barva=(0.5,0.2,0))

for i in range (7):
    st.Hranol(y=-2+i,sx=7-i,sy=1,sz=1,rx=90,barva=(0,1,0),)
              
              
st.ZobrazScenu()
