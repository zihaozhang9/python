
#ð�������㷨
times=0
times2=0
swap=0
whiletime=0
list=[858282,4252,5825725,8752,-2825245,8725,-82257465]
  
while times2 < len(list) -1:
        whiletime+=1
        while times < len(list)-1:
                whiletime+=1
                times+=1
                if list[times-1] > list[times]:
                        swap+=1
                        #���������ʽ�Ȳ����ţ�������
                        #a=list[times-1]
                        #b=list[times]
                        #list[times-1]=b
                        #list[times]=a
 
                        #��������ܿ졣
                        list[times-1], list[times] = list[times], list[times-1]
                         
        times2+=1
        times=0
  
print(list)
print('Swap times:',swap)
print('While times:',whiletime)