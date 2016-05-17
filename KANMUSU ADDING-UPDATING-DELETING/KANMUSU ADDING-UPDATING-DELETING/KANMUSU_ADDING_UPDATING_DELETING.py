def cls():
    for i in range(1,30):
        print()

def AngkaError():
    cls()
    print('================Input harus angka')
    print()

KanmusuName = ['Shimakaze', 'Yukikaze', 'Kaga', 'Iku', 'Ro-500', 'Akagi', 'Kongou', 'Kirishima', 'Sendai', 'Atago']
KanmusuType = ['Destroyer', 'Destroyer', 'Aircraft Carrier', 'Submarine', 'Submarine', 'Aircraft Carrier', 'Battleship', 'Battleship', 'Light Cruiser', 'Heavy Cruiser']
def view(KanmusuName, KanmusuType):
    for x in range(0, len(KanmusuName)):
        print(str(x+1)+". Name: "+KanmusuName[x]+" | Type: "+KanmusuType[x])

FlagAwal = True
Count = 10

while FlagAwal==True:
    view(KanmusuName, KanmusuType)
    print()
    print("Menu\n====")
    print("1. Add Kanmusu")
    print("2. Update Kanmusu")
    print("3. Remove Kanmusu")
    print("4. Exit")

    menuInput = 0
    try:
        menuInput = int(input("Input Anda: "))
    except Exception:
        AngkaError()
   
    if menuInput == 1:
        flag = 0
        flagnama = 0
        flagtype = 0
        while flagnama == 0:
            InputName = str(input("Input Nama Kanmusu[3-20]: "))
            if len(InputName) > 3 and len(InputName) < 20:
                flagnama = 1
            else:
                print("Nama Kanmusu harus antara 3 sampai 20 karakter")
                flagnama = 0
        while flagtype == 0:
            InputType = str(input("Input Tipe Kanmusu: "))
            if InputType == 'Destroyer' or InputType == 'Light Cruiser' or InputType == 'Heavy Cruiser' or InputType == 'Light Aircraft Carrier' or InputType == 'Aircraft Carrier' or InputType == 'Submarine' or InputType == 'Battleship':
                flagtype = 1
            else:
                print("Type harus Destroyer | Light/Heavy Cruiser | Light/Aircraft Carrier | Submarine | Battleship")
                print
                flagtype = 0
        if flagtype == 1 and flagnama == 1:
            Count = Count + 1
            KanmusuName.append(InputName)
            KanmusuType.append(InputType)
            cls()
            print("Sukses menginput kanmusu")
            print()

    elif menuInput == 2:
        cls()
        if len(KanmusuName) > 0:
            flag = 0
            flagtype = 0
            flagnama = 0
            flagIndex = 0
            view(KanmusuName, KanmusuType)
            print()
            InputIndex = 0
            while flagIndex == 0:
                try:
                    InputIndex = int(input("Pilih index yang ingin diupdate: "))
                except Exception:
                    print('=========Input harus angka')
                    print()
                if InputIndex < 1 or InputIndex > Count:
                    print('Input anda tidak valid')
                    print()
                else:
                    flagIndex = 1
                    print()
            if flag != 1:
                while flagnama == 0:
                    InputName = str(input("Input nama baru Kanmusu: "))
                    if len(InputName) > 3 and len(InputName) < 20:
                        countName = 0
                        while countName <= Count-1:
                            if InputName == KanmusuName[countName]:
                                flagnama = 0
                                print('======Nama Kanmusu tersebut sudah ada')
                                print()
                                countName = Count
                            else:
                                flagnama = 1
                            countName = countName + 1
                    else:
                        print("Nama Kanmusu harus antara 3 sampai 20 karakter")
                        print()
                        flagnama = 0
                while flagtype == 0:
                    InputType = str(input("Input Tipe Kanmusu: "))
                    if InputType == 'Destroyer' or InputType == 'Light Cruiser' or InputType == 'Heavy Cruiser' or InputType == 'Light Aircraft Carrier' or InputType == 'Aircraft Carrier' or InputType == 'Submarine' or InputType == 'Battleship':
                        flagtype = 1
                    else:
                        print("Type harus Destroyer | Light/Heavy Cruiser | Light/Aircraft Carrier | Submarine | Battleship")
                        flagtype = 0
                if flagtype == 1 and flagnama == 1:
                    KanmusuName[InputIndex-1] = InputName
                    KanmusuType[InputIndex-1] = InputType
                    cls()
                    print("Sukses mengupdate Kanmusu index ke-"+str(InputIndex))
                    print()

    elif menuInput == 3:
        cls()
        if len(KanmusuName) > 0:
            view(KanmusuName, KanmusuType)
            InputIndex = 0
            print()
            while InputIndex < 1 or InputIndex > Count:
                try:
                    InputIndex = int(input("Pilih index yang ingin didelete: "))
                except Exception:
                    print('=========Input harus angka')
                    print()
                if InputIndex < 1 or InputIndex > Count:
                    print("Input anda tidak valid")
                    flag = 1
                else:
                    flag = 0
            if flag != 1:
                flagConfirm = 0
                while flagConfirm == 0:
                    print('Anda akan mendelete '+KanmusuName[InputIndex-1]+', apakah anda yakin?')
                    txtConfirm = input("Ya[Y] / Ga jadi deh[N]: ")
                    if txtConfirm == 'Y':
                        flagConfirm = 1
                    elif txtConfirm == 'N':
                        flagConfirm = 2
                    else:
                        print('Tolong ulangi input dan masukkan input yang benar')
                        print()
                if flagConfirm == 1:
                    cls()
                    print('      Hiks. '+KanmusuName[InputIndex-1]+' sudah didelete.')
                    print()
                    del KanmusuName[InputIndex-1]
                    del KanmusuType[InputIndex-1]
                    Count = Count - 1
                elif flagConfirm == 2:
                    cls()
                    print('===Keputusan bagus. '+KanmusuName[InputIndex-1]+' pasti bahagia. Sayangilah Kanmusu anda.')
                    print()
        else:
            print("Tidak ada data")
    elif menuInput == 4:
        print('Thanks bruh')
        FlagAwal = False