empdata={'empno':101,
         'name':'Ravi',
         'salary':50000}
print(empdata)
print(empdata['name']) #Ravi
empdata['salary']=130000
print(empdata)
del empdata['name']
print(empdata)

empdata={'empno':101,
         'name':'Ravi',
         'salary':50000,
         'name':'Anuj'}
print(empdata)#if there is duplicate key then new key will be added

empdata={'empno':[101,102,103],
         'name':['Ravi','anuj','Raj'],
         'salary':[90000,120000,32000]}

print(empdata)
print(empdata['salary'])

s={'empno':101,'name':'ravi','salary':78000,'city':'pune'}
print(s.keys())
print(s.values())

#none
print(s.get('grade'))
#N/A in place of none
print(s.get('grade','N/A'))

a={'grade':'a','leaves':40}
#after s ..a will appended
s.update(a)
print(s)

a=s.copy()
print(a)

a=['name','city','age']
#keys from a value -None
d=dict.fromkeys(a)
print(d)
#keys from a value-10
r=dict.fromkeys(a,10)
print(r)

d={'empno':101,'name':'abr'}
#clear
d.clear()
print(d)
