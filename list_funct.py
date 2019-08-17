#__author__ = "ISHAN PATEL"
#__version__ = "3.5.2"
#__email__ = "ishanpatel415@gmail.com"
# Program for Room_number (assignment for n gram )
a=[1,2,3,4,5,5,5,6,7,8,9,10]
l=dir(list)
inp = input("Enter the function : ")
listFunc=inp.lower()
def ng(listFunc):
      if listFunc in dir(list): 
          if(listFunc == "count"):
              res=int(input("enter number to give a count"))
              if res in a:
                      print(a.count(res))
                      return
              else :
                      print ( "Given input no in list retry")
                      return
          elif(listFunc == "pop"):
              val=int(input("Enter the index of the  number to be poped %s: " % (listFunc)))
              new_a=a.pop(val)
              print(a)
              return
          elif(listFunc == "sort"):
                    new_aa=a.sort()
                    print(a)
                    return
          elif(listFunc == "append"):
                val=int(input("Enter the number to be used in the function %s: " % (listFunc)))
                listFunc="a."+listFunc+"(%d)" % val
                eval(listFunc)
                print(a)
                return
          elif(listFunc == "extend"):
                val=int(input("Enter the number to be used in the function %s: " % (listFunc)))
                listFunc="a."+listFunc+"(%d)" % val
                eval(listFunc)
                print(a)
                return
        
          elif(listFunc == "index"):
                val=int(input("enter the index number %s: " % (listFunc)))
                listFunc="a."+listFunc+"(%d)" % val
                print(eval(listFunc))
                return
        
          else:
                l2="a."+listFunc+"()"
                eval(l2)
                print(a)
                return
    
      else:
            print("Wrong input")
            return
            
ng(listFunc)

#end
