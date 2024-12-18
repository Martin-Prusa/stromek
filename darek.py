def vykresli_darek(st, x, y, velikost=1, barva_darku=(1, 0, 0), barva_masle=(1, 1, 0)):
    """
    Metoda vykrteslí dárek

    :param st: Stavitelka
    :param x: poloha x
    :param y: poloha y
    :param z: poloha z
    :param velikost:
    :param barva_darku:
    :param barva_masle:
    """
    st.Kvadr(barva=barva_darku, x=x, y=y, z=z, sx=velikost, sy=velikost)
    st.Kvadr(barva=barva_masle, x=x, y=y, z=z, sx=1.1 * velikost, sy=0.1 * velikost, sz=1.1 * velikost, rx=90)
    st.Kvadr(barva=barva_masle, x=x, y=y, z=z, sx=1.1 * velikost, sy=0.1 * velikost, sz=1.1 * velikost, rz=90)
    st.Koule(x=x, y=y + velikost * 0.7, z=z, sx=0.3 * velikost, sy=0.5 * velikost, barva=barva_masle)
    st.Koule(x=x, y=y + velikost * 0.7, z=z, sx=0.3 * velikost, sy=0.5 * velikost, ry=90, barva=barva_masle)
