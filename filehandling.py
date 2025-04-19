#def writing(filename,text):
 #   f=open(filename,"w")
  #  f.write(text)
   # f.close()
#writing("file1.txt","good morning")



def append(filename,text):
    f=open(filename,"a")
    f.write(text)
    f.close()
append("file1.txt","good evening") 


def reading(filename):
    try:
        f=open(filename,"r")
        text=f.read()
        print(text)
        f.close()
    except FileNotFoundError:
        print("file not found error")   
reading("file1.txt")         