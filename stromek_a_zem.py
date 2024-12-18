# Vytvoření jehlanu na různých pozicích
def vykresli_stromek_a_zem(st):
    def Hvezda():
        st.Kvadr( x=0,y=10,z=0, sx=0.7, sy=2, sz=2, rx=45, ry=0, rz=0, barva=(2,1,0), vaha=0 )
        st.Kvadr( x=0,y=10,z=0, sx=0.7, sy=2, sz=2, rx=0, ry=0, rz=0, barva=(2,1,0), vaha=0 )

    def Banka(velikost, barvicka, px,py,pz):
        st.Koule( x=px,y=py,z=pz, sx=velikost, sy=velikost, sz=velikost, rx=0, ry=0, rz=0, barva = barvicka, vaha=0 )
    
    difsxsz = 0.1
    dify = 0.2
    for i in range(51):
        st.Valec(y=0+i*dify, z=0, sx=5-i*difsxsz, sy=0.2, sz=5-i*difsxsz, barva=(0,1,0))
    # Zobrazení scény
    st.Valec(y=0, z=0, sx=1, sy=3, sz=1, barva=(0.5,0.2,0))
    
    st.Kvadr(x=0,y=-3,z=0, sx=10, sy=0.01, sz=10, rx=0, ry=0, rz=0, barva=(0,1,0), vaha=0)
    st.ZobrazScenu()
    
    Hvezda()
    
    Banka(1,(1,0,0),1.5,2,1.5)
    Banka(1,(0,0,1),1.5,2.2,-1.5)
    Banka(1,(1,0,0),-1.5,2,1.5)
    Banka(1,(1,0,0),1,4,1)
    Banka(1,(2,1,0),1,4,-1)
    Banka(1,(1,0,0),-1,4,1.5)
    Banka(1,(2,1,0),-1,4,1.5)
    Banka(1,(0,0,1),-1,4,-1)
