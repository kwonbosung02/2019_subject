from msvcrt import getch

def switch(p,x):
    if p == 1:
        print(str(x)+"mm입니다")
        return 1;
    if p == 2:
        print(str(x*100)+"mm입니다")
        return 2;
    if p == 3:
        print(str(x*10000)+"mm입니다")
        return 3;
    if p == 4:
        print(str((2.54*x)*100)+"mm입니다")
        return 4;

def re_st(x):
    if x == 1:
        return "mm"
    if x == 2:
        return "cm"
    if x == 3:
        return "m"
    if x == 4:
        return "in"

def switch_(p,x):
    if p == 1:
        print(str(x)+"mm입니다")
        return x;
    if p == 2:
        print(str(x*100)+"mm입니다")
        return x*100;
    if p == 3:
        print(str(x*10000)+"mm입니다")
        return x*10000;
    if p == 4:
        print(str((2.54*x)*100)+"mm입니다")
        return 2.54*x*100;

if __name__ == "__main__":
    cnt = 0;
    li = []
    cah =""
    while(1):
        print("="*50)
        select = int(input("단위를 선택하세요 1.mm, 2.cm, 3.m, 4.in : "))
        num = float(input("길이를 입력하세요 : "))
        
        x = switch(select,num)
        li.append(str(select)+re_st(x)+" -> "+str(switch_(select,num))+"mm")
        print("누적 :  "+str(li)[1:-1].replace("'",""))
        



        