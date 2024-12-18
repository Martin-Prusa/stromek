import stavitelka as st
from darek import vykresli_darek
from stromek_a_zem import vykresli_stromek_a_zem

vykresli_stromek_a_zem(st)
vykresli_darek(st, 1, -2.5, -2)
vykresli_darek(st, -2, -2.5, 0, barva_darku=(1,1,0), barva_masle=(1, 0, 0))
vykresli_darek(st, 2, -2.5, 1, barva_darku=(0,0,1), barva_masle=(1, 0, 0), velikost=1.3)

st.ZobrazScenu()
