if __name__ == "__main__":

    print("="*73)
    print("보어의 원자모형에서 전자 껍질 이동에 따른 에너지 준위를 계산하는 프로그램")
    print("="*73)

    E1 = int(input("첫번째 전자껍질의 위치 : "))
    E2 = int(input("두번째 전자껍질의 위치 : "))
    print()
    print("전자는 "+str(E1)+"번째 전자껍질에서 " + str(E2) + "번째 전자껍질로 이동합니다")

    if E1 > E2:
        print("전자가 전이되는 과정에서 에너지가 방출됩니다")
    else:
        print("전자가 전이되는 과정에서 에너지가 흡수됩니다")
    print()
    Energy_level_1 = round(-1312/(E1*E1),2)
    Energy_level_2 = round(-1312/(E2*E2),2)

    print(str(E1)+ "번째 전자껍질의 에너지 준위 : " + str(Energy_level_1)+"kJ/mol")
    print(str(E2)+ "번째 전자껍질의 에너지 준위 : " + str(Energy_level_2)+"kJ/mol")

    print()

    if(E1 > E2):
        print("전자가 전이되는 과정에서 "+str(Energy_level_1-Energy_level_2)+"kJ/mol 만큼의 에너지를 방출합니다")
    else:
        print("전자가 전이되는 과정에서 "+str(-(Energy_level_1-Energy_level_2))+"kJ/mol 만큼의 에너지를 흡수합니다")

    print()
    senten = "전이될 때 방출되는 빛은 "
    senten2 = "에 속합니다"
    if(E1 > E2):
        if E2 == 1:
            print(senten+"라이먼 계열(자외선 영역)"+senten2)
        if E2 == 2:
            print(senten+"발머계열(가시광선 영역)"+senten2)
        if E2 == 3:
            print(senten+"파셴계열(적외선 영역)"+senten2)
        else:
            pass