def catAndMouse(catA,catB,mosC):
    jarak1 = abs(mosC - catA)
    jarak2 = abs(mosC - catB)
    if(jarak1 < jarak2):
        print("Cat A")
    elif (jarak1 == jarak2):
        print("Mouse C")
    else:
        print("Cat B")
    # elif(mosC <= catA & catB):
    #     jarak1 = abs(catA - mosC)
    #     jarak2 = abs(catB - mosC)
    #     if(jarak1 < jarak2):
    #         print("Cat A")
    #     elif (jarak1 == jarak2):
    #         print("Mouse c")
    #     else:
    #         print("Cat B")
    # elif(catA < mosC < catB):
    #     jarak1 = abs(mosC - catA)
    #     jarak2 = abs(catB - mosC)
    #     if(jarak1 < jarak2):
    #         print("Cat A")
    #     elif (jarak1 == jarak2):
    #         print("Mouse C")
    #     else:
    #         print("Cat B")
    # elif(catB < mosC < catA):
    #     jarak1 = abs(mosC - catB)
    #     jarak2 = abs(catA - mosC)
    #     if(jarak1 < jarak2):
    #         print("Cat A")
    #     elif (jarak1 == jarak2):
    #         print("Mouse C")
    #     else:
    #         print("Cat B")

def terimainput():
    catA = int(input("Masukkan posisi Cat A : "))
    catB = int(input("Masukkan posisi Cat B : "))
    MouseC = int(input("Masukkan posisi Mouse C : "))
    catAndMouse(catA,catB,MouseC)

terimainput()


