import stavitelka as st

# Vytvoření jehlanu na různých pozicích
difsxsz = 0.1
dify = 0.2
for i in range(51):
    st.Valec(y=0+i*dify, z=0, sx=5-i*difsxsz, sy=0.2, sz=5-i*difsxsz, barva=(0,1,0))
# Zobrazení scény
st.Valec(y=0, z=0, sx=1, sy=3, sz=1, barva=(0.5,0.2,0))

st.Kvadr(x=0,y=-3,z=0, sx=10, sy=0.01, sz=10, rx=0, ry=0, rz=0, barva=(0,1,0), vaha=0)
st.ZobrazScenu()

