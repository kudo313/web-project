from random import randrange,sample
# matrix=[]
# for j in range(10):    
#     lst=[]

#     for i in range(10):
#         lst.append(randrange(1,50))
#     matrix.append(lst)
# print(matrix)


lst1=[]
lst2=[]
lst1.append(sample(range(1,11),10))
lst1=lst1[0]
lst2.append(sample(range(1,11),10))
lst2=lst2[0]
print(lst2)
print(lst1)
# lst3[10]=''
# for i in range(10):
#     for j in range(i+1,10):
#         lst3[j] = i if lst2[j] = lst1[i]

lst3=[0,0,0,0,0,0,0,0,0,0]
for i in range(10):
    for j in range(10):
        if lst1[i]==lst2[j]:
            lst3[j]=i
max1 =lst3[0]
print(lst3)

    

dct={}

dct['ex_lst1']=[]
dct['ex_lst1'].append(lst3[0])
d=1
for i in range(1,10):
    if lst3[i]>dct['ex_lst{0}'.format(d)][d-1]:
        lst_tg=[]
        d+=1
        y='ex_lst{0}'.format(d)
        z='ex_lst{0}'.format(d-1)

        dct[y]=[]
        lst_tg=dct[z].copy()
        dct[z].append(lst3[i])
        dct[y]=dct[z].copy()
        dct[z]=lst_tg.copy()
    else:
        # for j in range(d+1):
        #     y='ex_lst{0}'.format(d)
        #     z='ex_lst{0}'.format(j+1)
        #     if lst3[i]<dct[z][j]:
        #         dct[z][j]=lst3[i]
        #         break
        #     else:
        #         lst_tg1=[]
        #         lst_tg1=dct[z].copy()
        #         dct[z].append(lst3[i])
        #         dct['ex_lst{0}'.format(j+2)]=dct[z].copy()
        #         dct[z]=lst_tg1.copy()
        #         break
        for j in range(d)[::-1]:
            # if lst3[i]<dct['ex_lst{0}'.format(d)][j] and lst3[i]>dct['ex_lst{0}'.format(d)][j-1]:
            #     # lst_tg1=[]
            #     # lst_tg1=dct['ex_lst{0}'.format(j+1)].copy()
            #     dct['ex_lst{0}'.format(j+1)][j]=lst3[i]
            # if lst3[i]<dct['ex_lst{0}'.format(d)][0]:
            #     dct['ex_lst1'][0]=lst3[i]
            if lst3[i]>dct['ex_lst{0}'.format(j+1)][j]:
                lst_tg1=[]
                lst_tg1=dct['ex_lst{0}'.format(j+1)].copy()
                dct['ex_lst{0}'.format(j+1)].append(lst3[i])
                dct['ex_lst{0}'.format(j+2)]=dct['ex_lst{0}'.format(j+1)].copy()
                dct['ex_lst{0}'.format(j+1)]=lst_tg1.copy()
                break
            if lst3[i]<dct['ex_lst1'][0]:
                dct['ex_lst1'][0]=lst3[i]


print(dct['ex_lst{0}'.format(d)])
# f=[0,0,0,0,0,0,0,0,0,0]
# result=1
# for i in range(1,len(lst3)):
#     for j in range(i):
#         if lst3[j]<lst3[i]:
#             f[i]=max(f[i],f[j]+1)

#     result=max(result,f[i])

# print(result)
            
    

    



