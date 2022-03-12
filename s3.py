import pickle
model=pickle.load(open("E:\\python project\\text similarity\\sd.pkl","rb"))
s=model.cs(["hii sir"], ["hlo sir"])
print(s)