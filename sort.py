
def sort_list(my_list):
    even_list=[]
    odd_list=[]
    char_list=[]
    other_list=[]
    dict_A={}
    for b in my_list:
        if isinstance(b, int):
            if (b%2==0):
                even_list.append(b)
            else:
                odd_list.append(b)
        elif isinstance(b,str):
            char_list.append(b)
        else:
            other_list.append(b)

    dict_A["Even"]=sorted(even_list)
    dict_A["Odd"]=sorted(odd_list)
    dict_A["Char"]=sorted(char_list)
    dict_A["Other"]=sorted(other_list)

    return dict_A

my_list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,"hey","you","hello","c","u","ltr",2.0]

print(sort_list(my_list))




def find_number(x):
    y = []
    for i in range(1,10):
        if i not in x:
            y.append(i)
    return y
x=[1,2,4,5,7,9]
print(find_number(x))

