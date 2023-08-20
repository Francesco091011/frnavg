print("Hola, bienvenidos al Primer Navegador de Árboles Genealógicos Francescanos, en este caso haré como base de datos mis familias maternas y paternas. Antes de comenzar, para evitar dolores de cabeza, he decidido a todos dividir en dos macrogrupos, que son los Huayaney & Suárez & Chuquillanqui y los Eriani & Cracco, si decide terminar, escribe 000, ok, entoces, comencemos :) ...")
print("Entoces, por ahora hay 20 participantes aquí, están ordenados en orden de lanzamiento, a su lado izquierda tiene un número, si ya decició a alguien, relaciónalo con su número de a lado y escribe el número, ok? Entoces, que salga la lista:")
print("Macrogrupo HUAYANEY")
print("""
001. Alexa Beatriz Huayanay Sánchez
002. Alexander Octavio Huayanay Leonardo
003. Ariana Brunella Huayanay Sánchez
004. Carlos Arturo Huayanay Chuquillanqui
005. Elida Luz Chuquillanqui Espinoza
006. Francesco Adriano Eriani Huayanay
007. Grecia Ariana Huayanay Ríos
008. Hortensio Hugo Huayanay Chuquillanqui
009. José Manuel Huayanay Chuquillanqui
010. Lucio Odilio Huayaney Suárez
011. Luis Eduardo Huayaney Ramírez
012. Luis Enrique Huayaney Chuquillanqui
013. Marco Antonio Huayanay Chuquillanqui
014. Mariel Valerie Meza Huayanay
015. Rocio Mirtha Huayanay Chuquillanqui
016. Scarlet Alessandra Huayanay Ríos
017. Selina Corín Huayanay Chuquillanqui
018. Starsky Ivan Huayanay Chuquillanqui
019. Stefany Guissel Huayanay Leonardo
""")

def persona001(personas1="001"):
        a = print("""
        Nombres: Alexa Beatriz
        Apellidos: Huayanay Sánchez
        Nacimiento: 05/06/2008
        Sexo: F
        Padre: a). Hortensio Hugo Huayanay Chuquillanqui
        Madre: --. Beatriz --- Sánchez Uchuypoma
        Herman@s: b). Ariana Brunella Huayanay Sánchez""")
        b = input("Como quieres continuar?: ")
        if b == "000":
            c=magic000(b)
        if b == "a":
            c=persona008("008")
        if b == "b":
            c=persona003("003")
        return a,b,c
def persona003(personas1="003"):
        a = print("""
        Nombres: Ariana Brunella
        Apellidos: Huayanay Sánchez
        Nacimiento: 23/04/2020
        Sexo: F
        Padre: a). Hortensio Hugo Huayanay Chuquillanqui
        Madre: --. Beatriz --- Sánchez Uchuypoma
        Herman@s: b). Alexa Beatriz Huayanay Sánchez""")
        b = input("Como quieres continuar?: ")
        if b == "000":
            c=magic000(b)
        if b == "a":
            c=persona008("008")
        if b == "b":
            c=persona001("001")
        return a,b,c
def persona008(personas1="008"):
        a = print("""
        Nombres: Hortensio Hugo
        Apellidos: Huayanay Chuquillanqui
        Nacimiento: 27/11/1972
        Sexo: M
        Padre: a). Lucio Odilio Huayaney Suárez
        Madre: b). Elida Luz Chuquillanqui Espinoza
        Herman@s: c) Luis Enrique Huayaney Chuquillanqui, d) Marco Antonio Huayanay Chuquillanqui, e) Selina Corín Huayanay Chuquillanqui, f) José Manuel Huayanay Chuquillanqui, g) Rocio Mirtha Huayanay Chuquillanqui, h) Carlos Arturo Huayanay Chuquillanqui, i) Starsky Ivan Huayanay Chuquillanqui
        Esposa: --. Beatriz --- Sánchez Uchuypoma
        Hij@s: j) Alexa Beatriz Huayanay Sánchez, k) Ariana Brunella Huayanay Sánchez
        """)
        b = input("Como quieres continuar?: ")
        if b == "000":
            c=magic000(b)
        if b == "a":
            c=persona010("010")
        if b == "b":
            c=persona005("005")
        if b == "c":
            c=persona012("012")
        if b == "d":
            c=persona014("012")
        if b == "e":
            c=persona017("017")
        if b == "f":
            c=persona009("009")
        if b == "g":
            c=persona015("015")
        if b == "h":
            c=persona004("004")
        if b == "i":
            c=persona018("018")
        if b == "j":
            c=persona001("001")
        if b == "k":
            c=persona003("003")
        return a,b,c
def persona010(personas1="010"):
        a = print("""
        Nombres: Lucio Odilio
        Apellidos: Huayaney Suárez
        Nacimiento: 13/12/1942
        Sexo: M
        Padre: --. Hortensio Cano Huayaney
        Madre: --. Celina Braulia Suárez Gonzáles
        Esposa: a) Elida Luz Chuquillanqui Espinoza
        Hij@s: b) Luis Enrique Huayaney Chuquillanqui, c) Marco Antonio Huayanay Chuquillanqui, d) Selina Corín Huayanay Chuquillanqui, e) Hortensio Hugo Huayanay Chuquillanqui , f) José Manuel Huayanay Chuquillanqui, g) Rocio Mirtha Huayanay Chuquillanqui, h) Carlos Arturo Huayanay Chuquillanqui, i) Starsky Ivan Huayanay Chuquillanqui
        """)
        b = input("Como quieres continuar?: ")
        if b == "000":
            c=magic000(b)
        if b == "a":
            c=persona005("005")
        if b == "b":
            c=persona012("012")
        if b == "c":
            c=persona013("013")
        if b == "d":
            c=persona017("017")
        if b == "e":
            c=persona008("008")
        if b == "f":
            c=persona009("009")
        if b == "g":
            c=persona015("015")
        if b == "h":
            c=persona004("004")
        if b == "i":
            c=persona018("018")
        return a,b,c
def persona005(personas1="005"):
        a = print("""
        Nombres: Elida Luz
        Apellidos: Chuquillanqui Espinoza
        Nacimiento: 26/01/1947
        Sexo: F
        Padre: --. Ciriaco Pelayo Chuquillanqui Macurí
        Madre: --. María Dolores Espinoza Alcedo
        Esposo: a) Lucio Odilio Huayaney Suárez
        Hij@s: b) Luis Enrique Huayaney Chuquillanqui, c) Marco Antonio Huayanay Chuquillanqui, d) Selina Corín Huayanay Chuquillanqui, e) Hortensio Hugo Huayanay Chuquillanqui , f) José Manuel Huayanay Chuquillanqui, g) Rocio Mirtha Huayanay Chuquillanqui, h) Carlos Arturo Huayanay Chuquillanqui, i) Starsky Ivan Huayanay Chuquillanqui
        """)
        b = input("Como quieres continuar?: ")
        if b == "000":
            c=magic000(b)
        if b == "a":
            c=persona010("010")
        if b == "b":
            c=persona012("012")
        if b == "c":
            c=persona013("013")
        if b == "d":
            c=persona017("017")
        if b == "e":
            c=persona008("008")
        if b == "f":
            c=persona009("009")
        if b == "g":
            c=persona015("015")
        if b == "h":
            c=persona004("004")
        if b == "i":
            c=persona018("018")
        return a,b,c
def persona015(personas1="015"):
        a = print("""
        Nombres: Rocio Mirtha
        Apellidos: Huayanay Chuquillanqui
        Nacimiento: 26/04/1976
        Sexo: F
        Padre: a). Lucio Odilio Huayaney Suárez
        Madre: b). Elida Luz Chuquillanqui Espinoza
        Herman@s: c) Luis Enrique Huayaney Chuquillanqui, d) Marco Antonio Huayanay Chuquillanqui, e) Selina Corín Huayanay Chuquillanqui, f) Hortensio Hugo Huayanay Chuquillanqui, g) José Manuel Huayanay Chuquillanqui, h) Carlos Arturo Huayanay Chuquillanqui, i) Starsky Ivan Huayanay Chuquillanqui
        Esposo: j). Luca Eriani
        Hij@s: k) Francesco Adriano Eriani Huayanay
        """)
        b = input("Como quieres continuar?: ")
        if b == "000":
            c=magic000(b)
        if b == "a":
            c=persona010("010")
        if b == "b":
            c=persona005("005")
        if b == "c":
            c=persona012("012")
        if b == "d":
            c=persona014("014")
        if b == "e":
            c=persona017("017")
        if b == "f":
            c=persona008("008")
        if b == "g":
            c=persona009("009")
        if b == "h":
            c=persona004("004")
        if b == "i":
            c=persona018("018")
        if b == "j":
            c=persona500("500")
        if b == "k":
            c=persona006("006")
        return a,b,c
def persona006(personas1="006"):
        a = print("""
        Nombres: Francesco Adriano
        Apellidos: Eriani Huayanay 
        Nacimiento: 18/11/2011
        Sexo: M
        Padre: a). Luca Eriani
        Madre: b). Rocio Mirtha Huayanay Chuquillanqui
        """)
        b = input("Como quieres continuar?: ")
        if b == "000":
            c=magic000(b)
        if b == "b":
            c=persona015("015")
        if b == "a":
            c=persona500("500")
        return a,b,c
def persona002(personas1="002"):
        a = print("""
        Nombres: Alexander Octavio
        Apellidos: Huayanay Leonardo 
        Nacimiento: 09/07/2005
        Sexo: M
        Padre: a). Carlos Arturo Huayanay Chuquillanqui
        Madre: --. Guisella --- Leonardo ---
        Herman@s: b). Stefany Guissel Huayanay Leonardo
        """)
        b = input("Como quieres continuar?: ")
        if b == "000":
            c=magic000(b)
        if b == "a":
            c=persona004("004")
        if b == "b":
            c=persona019("019")
        return a,b,c
def persona019(personas1="019"):
        a = print("""
        Nombres: Stefany Guissel
        Apellidos: Huayanay Leonardo 
        Nacimiento: 09/02/2015
        Sexo: F
        Padre: a). Carlos Arturo Huayanay Chuquillanqui
        Madre: --. Guisella --- Leonardo ---
        Herman@s: b). Alexander Octavio Huayanay Leonardo
        """)
        b = input("Como quieres continuar?: ")
        if b == "000":
            c=magic000(b)
        if b == "a":
            c=persona004("004")
        if b == "b":
            c=persona002("002")
        return a,b,c
def persona004(personas1="004"):
        a = print("""
        Nombres: Carlos Arturo
        Apellidos: Huayanay Chuquillanqui
        Nacimiento: 03/10/1980
        Sexo: M
        Padre: a). Lucio Odilio Huayaney Suárez
        Madre: b). Elida Luz Chuquillanqui Espinoza
        Herman@s: c) Luis Enrique Huayaney Chuquillanqui, d) Marco Antonio Huayanay Chuquillanqui, e) Selina Corín Huayanay Chuquillanqui, f) Hortensio Hugo Huayanay Chuquillanqui, g) José Manuel Huayanay Chuquillanqui, h) Rocio Mirtha Huayanay Chuquillanqui, i) Starsky Ivan Huayanay Chuquillanqui
        Esposa: --. Guissella --- Leonardo ---
        Hij@s: j) Alexander Octavio Huayanay Leonardo, k) Stefany Guissel Huayanay Leonardo
        """)
        b = input("Como quieres continuar?: ")
        if b == "000":
            c=magic000(b)
        if b == "a":
            c=persona010("010")
        if b == "b":
            c=persona005("005")
        if b == "c":
            c=persona012("012")
        if b == "d":
            c=persona014("014")
        if b == "e":
            c=persona017("017")
        if b == "f":
            c=persona008("008")
        if b == "g":
            c=persona009("009")
        if b == "h":
            c=persona015("015")
        if b == "i":
            c=persona018("018")
        if b == "j":
            c=persona002("002")
        if b == "k":
            c=persona019("019")
        return a,b,c
def persona013(personas1="013"):
    a = print("""
        Nombres: Marco Antonio
        Apellidos: Huayanay Chuquillanqui
        Nacimiento: 30/01/1970
        Sexo: M
        Padre: a). Lucio Odilio Huayaney Suárez
        Madre: b). Elida Luz Chuquillanqui Espinoza
        Herman@s: c) Luis Enrique Huayaney Chuquillanqui, d) Selina Corín Huayanay Chuquillanqui, e) Hortensio Hugo Huayanay Chuquillanqui, f) José Manuel Huayanay Chuquillanqui, g) Rocio Mirtha Huayanay Chuquillanqui, h) Carlos Arturo Huayanay Chuquillanqui, i) Starsky Ivan Huayanay Chuquillanqui
        """)
    b = input("Como quieres continuar?: ")
    if b == "000":
            c=magic000(b)
    if b == "a":
        c=persona010("010")
    if b == "b":
        c=persona005("005")
    if b == "c":
        c=persona012("012")
    if b == "d":
        c=persona017("017")
    if b == "e":
        c=persona008("008")
    if b == "f":
        c=persona009("009")
    if b == "g":
        c=persona015("015")
    if b == "h":
        c=persona004("004")
    if b == "i":
        c=persona018("018")
    return a,b,c
def persona012(personas1="012"):
    a = print("""
        Nombres: Luis Enrique
        Apellidos: Huayaney Chuquillanqui
        Nacimiento: 27/10/1968
        Sexo: M
        Padre: a). Lucio Odilio Huayaney Suárez
        Madre: b). Elida Luz Chuquillanqui Espinoza
        Herman@s: c) Marco Antonio Huayanay Chuquillanqui, d) Selina Corín Huayanay Chuquillanqui, e) Hortensio Hugo Huayanay Chuquillanqui, f) José Manuel Huayanay Chuquillanqui, g) Rocio Mirtha Huayanay Chuquillanqui, h) Carlos Arturo Huayanay Chuquillanqui, i) Starsky Ivan Huayanay Chuquillanqui
        Esposa: --. Mónica Ramírez 
        Hij@s: j). Luis Eduardo Huayaney Ramírez
        """)
    b = input("Como quieres continuar?: ")
    if b == "000":
        c=magic000(b)
    if b == "a":
        c=persona010("010")
    if b == "b":
        c=persona005("005")
    if b == "c":
        c=persona013("013")
    if b == "d":
        c=persona017("017")
    if b == "e":
        c=persona008("008")
    if b == "f":
        c=persona009("009")
    if b == "g":
        c=persona015("015")
    if b == "h":
        c=persona004("004")
    if b == "i":
        c=persona018("018")
    if b == "j":
        c=persona011("011")
    return a,b,c
def persona011(personas1="011"):
    a = print("""
        Nombres: Luis Eduardo
        Apellidos: Huayaney Ramírez 
        Nacimiento: 04/11/1996
        Sexo: M
        Padre: a). Luis Enrique Huayaney Chuquillanqui
        Madre: --. Mónica Ramírez Buendía
        """)
    b = input("Como quieres continuar?: ")
    if b == "000":
        c=magic000(b)
    if b == "a":
        c=persona012("012")
    return a,b,c
def persona017(personas1="017"):
    a = print("""
        Nombres: Selina Corín
        Apellidos: Huayanay Chuquillanqui
        Nacimiento: 12/06/1971
        Sexo: F
        Padre: a). Lucio Odilio Huayaney Suárez
        Madre: b). Elida Luz Chuquillanqui Espinoza
        Herman@s: c) Luis Enrique Huayaney Chuquillanqui, d) Marco Antonio Huayanay Chuquillanqui, e) Hortensio Hugo Huayanay Chuquillanqui, f) José Manuel Huayanay Chuquillanqui, g) Rocio Mirtha Huayanay Chuquillanqui, h) Carlos Arturo Huayanay Chuquillanqui, i) Starsky Ivan Huayanay Chuquillanqui
        Esposo: --. Pedro Hugo Meza Bustillos 
        Hij@s: j). Mariel Valerie Meza Huayanay
        """)
    b = input("Como quieres continuar?: ")
    if b == "000":
        c=magic000(b)
    if b == "a":
        c=persona010("010")
    if b == "b":
        c=persona005("005")
    if b == "c":
        c=persona012("012")
    if b == "d":
        c=persona013("013")
    if b == "e":
        c=persona008("008")
    if b == "f":
        c=persona009("009")
    if b == "g":
        c=persona015("015")
    if b == "h":
        c=persona004("004")
    if b == "i":
        c=persona018("018")
    if b == "j":
        c=persona014("014")
    return a,b,c
def persona014(personas1="014"):
    a = print("""
        Nombres: Mariel Valerie
        Apellidos: Meza Huayanay
        Nacimiento: 14/08/2003
        Sexo: F
        Padre: --. Pedro Hugo Meza Bustillos
        Madre: a) Selina Corín Huayanay Chuquillanqui
        """)
    b = input("Como quieres continuar?: ")
    if b == "000":
        c=magic000(b)
    if b == "a":
        c=persona017("017")
    return a,b,c
def persona018(personas1="018"):
    a = print("""
        Nombres: Starsky Ivan
        Apellidos: Huayanay Chuquillanqui
        Nacimiento: 19/09/1981
        Sexo: M
        Padre: a). Lucio Odilio Huayaney Suárez
        Madre: b). Elida Luz Chuquillanqui Espinoza
        Herman@s: c) Luis Enrique Huayaney Chuquillanqui, d) Marco Antonio Huayanay Chquillanqui, e) Selina Corín Huayanay Chuquillanqui, f) Hortensio Hugo Huayanay Chuquillanqui, g) José Manuel Huayanay Chuquillanqui, h) Rocio Mirtha Huayanay Chuquillanqui, i) Carlos Arturo Huayanay Chuquillanqui""")
    b = input("Como quieres continuar?: ")
    if b == "000":
            c=magic000(b)
    if b == "a":
        c=persona010("010")
    if b == "b":
        c=persona005("005")
    if b == "c":
        c=persona012("012")
    if b == "d":
        c=persona014("014")
    if b == "e":
        c=persona017("017")
    if b == "f":
        c=persona008("008")
    if b == "g":
        c=persona009("009")
    if b == "h":
        c=persona015("015")
    if b == "i":
        c=persona004("004")
    return a,b,c
def persona009(personas1="009"):
    a = print("""
        Nombres: José Manuel
        Apellidos: Huayanay Chuquillanqui
        Nacimiento: 21/09/1974
        Sexo: M
        Padre: a). Lucio Odilio Huayaney Suárez
        Madre: b). Elida Luz Chuquillanqui Espinoza
        Herman@s: c) Luis Enrique Huayaney Chuquillanqui, d) Marco Antonio Huayanay Chuquillanqui, e) Selina Corín Huayanay Chuquillanqui, f) Hortensio Hugo Huayanay Chuquillanqui, g) Rocio Mirtha Huayanay Chuquillanqui, h) Carlos Arturo Huayanay Chuquillanqui, i) Starsky Ivan Huayanay Chuquillanqui
        Esposa: --. Lucy Ríos ---
        Hij@s: j) Scarlet Alessandra Huayanay Ríos, k) Grecia Ariana Huayanay Ríos
        """)
    b = input("Como quieres continuar?: ")
    if b == "000":
        c=magic000(b)
    if b == "a":
        c=persona010("010")
    if b == "b":
        c=persona005("005")
    if b == "c":
        c=persona012("012")
    if b == "d":
        c=persona014("012")
    if b == "e":
        c=persona017("017")
    if b == "f":
        c=persona008("008")
    if b == "g":
        c=persona015("015")
    if b == "h":
        c=persona004("004")
    if b == "i":
        c=persona018("018")
    if b == "j":
        c=persona016("016")
    if b == "k":
        c=persona007("007")
    return a,b,c
def persona016(personas1="016"):
        a = print("""
        Nombres: Scarlet Alessandra
        Apellidos: Huayanay Ríos 
        Nacimiento: 23/04/2008
        Sexo: F
        Padre: a). José Manuel Huayanay Chuquillanqui
        Madre: --. Lucy Ríos ---
        Herman@s: b). Grecia Ariana Huayanay Ríos
        """)
        b = input("Como quieres continuar?: ")
        if b == "000":
            c=magic000(b)
        if b == "a":
            c=persona009("009")
        if b == "b":
            c=persona007("007")
        return a,b,c
def persona007(personas1="007"):
        a = print("""
        Nombres: Grecia Ariana
        Apellidos: Huayanay Ríos 
        Nacimiento: 14/11/2012
        Sexo: F
        Padre: a). José Manuel Huayanay Chuquillanqui
        Madre: --. Lucy Ríos ---
        Herman@s: b). Scarlet Alessandra Huayanay Ríos
        """)
        b = input("Como quieres continuar?: ")
        if b == "000":
            c=magic000(b)
        if b == "a":
            c=persona009("009")
        if b == "b":
            c=persona016("016")
        return a,b,c

print("Macrogrupo ERIANI")
print("""
500. Luca Eriani
""")

def persona500(personas1="500"):
    a = print("""
    Nome: Luca
    Cognome: Eriani
    Data di nascita: 07/01/1972
    Sesso: M
    Papá: --. Gino Eriani
    Mamma: --. Maria Cracco
    Fratelli/Sorelle: --. Claudio Eriani --. Patrizia Eriani --. Mariangela Eriani --. Michele Eriani
    Sposa: a). Rocio Mirtha Huayanay Chuquillanqui
    Figli: b). Francesco Adriano Eriani Huayanay
    """)
    b = input("Como quieres continuar?: ")
    if b == "000":
        c=magic000(b)
    if b == "a":
        c=persona015("015")
    if b == "b":
        c=persona006("006")
    return a, b, c
         
def magic000(xxx="000"):
    x = print("Gracias por la sesión de este día")
    return x

personas1 = input("Entoces, que número escoges?: ")

if personas1 == "001":
    print(persona001("001"))
if personas1 == "008":
        print(persona008("008"))
if personas1 == "010":
        print(persona010("010"))
if personas1 == "003":
        print(persona003("003"))
if personas1 == "005":
        print(persona005("005"))
if personas1 == "015":
        print(persona015("015"))
if personas1 == "006":
        print(persona006("006"))
if personas1 == "004":
        print(persona004("004"))
if personas1 == "003":
        print(persona003("003"))
if personas1 == "019":
        print(persona019("019"))
if personas1 == "012":
        print(persona012("012"))
if personas1 == "011":
        print(persona011("011"))
if personas1 == "013":
        print(persona013("013"))
if personas1 == "017":
        print(persona017("017"))
if personas1 == "014":
        print(persona014("014"))
if personas1 == "009":
        print(persona009("009"))
if personas1 == "007":
        print(persona007("007"))
if personas1 == "016":
        print(persona016("016"))
if personas1 == "018":
        print(persona018("018"))
if personas1 == "500":
        print(persona500("500"))
if personas1 == "000":
    print(magic000("000"))