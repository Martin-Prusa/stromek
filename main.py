import stavitelka as st
from darek import vykresli_darek

vykresli_darek(st, 1, 1)
vykresli_darek(st, 3, 1, barva_darku=(1,1,0), barva_masle=(1, 0, 0))
vykresli_darek(st, 5, 1, barva_darku=(0,0,1), barva_masle=(1, 0, 0), velikost=1.3)

st.ZobrazScenu()