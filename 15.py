s2=input()
m=list(s2)
dict = {i:m.count(i) for i in m}
maximum = max(dict, key=dict.get)  
print(maximum)
