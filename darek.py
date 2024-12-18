def vykresli_darek(st, x, y, velikost=1):
    st.Kvadr(barva=(1,0,0), x=x,y=y)
    st.Kvadr(barva=(1,1,0), x=x,y=y, sx=1.1*velikost, sy=0.1*velikost, sz=1.1*velikost, rx=90)
    st.Kvadr(barva=(1,1,0), x=x,y=y, sx=1.1*velikost, sy=0.1*velikost, sz=1.1*velikost, rz=90)
