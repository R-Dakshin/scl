# THIS CODE IS A MENU DRIVEN CODE WITH THE FOLLOWING OPTIONS :
# 1-ADD A STUDENT'S DATA
# 2-DELETE A STUDENT'S DATA
# 3-ACCESS THE WHOLE REPORT CARD IN DICTIONARY
# 4-ACCESS THE WHOLE REPORT CARD IN A TABLE FORMAT
# 5-ACCESSING A SPECIFIC STUDENT'S REPORT
# 6-EXIT
print("Student Report Card Management")
i,j,k,l,m,n,o,p,q,r,s,t=1,1,1,1,1,1,1,1,1,1,1,1
report_card={}
empt={}
report_card["Class 1"]={}
report_card["Class 2"]={}
report_card["Class 3"]={}
report_card["Class 4"]={}
report_card["Class 5"]={}
report_card["Class 6"]={}
report_card["Class 7"]={}
report_card["Class 8"]={}
report_card["Class 9"]={}
report_card["Class 10"]={}
report_card["Class 11"]={}
report_card["Class 12"]={}
a=1
report_card1=report_card
ept=()
print("\n")
while a!=6:
    print("\n")
    print("Choose the following options :- \n1 - Add a student's data.\n2 - Delete a student's data.\n3 - Access the whole report.\n4 - Access the report one below the other.\n5 - Access an individual student data.\n6 - Exit.")
    print("\n")    
    a=int(input("Enter your option : "))
    print("\n")#Sharaj did this part.
    if a==1:
        cls=int(input("Enter your class : "))
        print("\n")
        if cls==1:
            UID=int(input("Enter your unique ID : "))
            name=input("Enter your name : ")
            maths=int(input("Enter your Maths marks : "))
            eng=int(input("Enter your English marks : "))
            evs=int(input("Enter your EVS marks : "))
            tamil=int(input("Enter your Tamil marks : "))
            hindi=int(input("Enter your Hindi marks : "))
            print("\n")
            percentage=(maths+eng+evs+tamil+hindi)/5
            report_card["Class 1"][UID]={}
            report_card["Class 1"][UID]["Name "+str(i)]=name
            report_card["Class 1"][UID][str(name)+"'s Maths Marks "]=maths
            report_card["Class 1"][UID][str(name)+"'s English Marks "]=eng
            report_card["Class 1"][UID][str(name)+"'s EVS Marks "]=evs
            report_card["Class 1"][UID][str(name)+"'s Tamil Marks "]=tamil
            report_card["Class 1"][UID][str(name)+"'s Hindi Marks "]=hindi
            report_card["Class 1"][UID][str(name)+"'s Percentage "]=percentage
            i+=1
        elif cls==2:
            UID=int(input("Enter your unique ID : "))
            name=input("Enter your name : ")
            maths=int(input("Enter your Maths marks : "))
            eng=int(input("Enter your English marks : "))
            evs=int(input("Enter your EVS marks : "))
            tamil=int(input("Enter your Tamil marks : "))
            hindi=int(input("Enter your Hindi marks : "))
            print("\n")
            percentage=(maths+eng+evs+tamil+hindi)/5
            report_card["Class 2"][UID]={}
            report_card["Class 2"][UID]["Name "+str(j)]=name
            report_card["Class 2"][UID][str(name)+"'s Maths Marks "]=maths
            report_card["Class 2"][UID][str(name)+"'s English Marks "]=eng
            report_card["Class 2"][UID][str(name)+"'s EVS Marks "]=evs
            report_card["Class 2"][UID][str(name)+"'s Tamil Marks "]=tamil
            report_card["Class 2"][UID][str(name)+"'s Hindi Marks "]=hindi
            report_card["Class 2"][UID][str(name)+"'s Percentage "]=percentage
            j+=1
        elif cls==3:
            UID=int(input("Enter your unique ID : "))
            name=input("Enter your name : ")
            maths=int(input("Enter your Maths marks : "))
            eng=int(input("Enter your English marks : "))
            science=int(input("Enter your Science marks : "))
            social_science=int(input("Enter your Social Science marks : "))
            lang=int(input("Enter your Language marks : "))
            print("\n")
            percentage=(maths+eng+science+social_science+lang)/5
            report_card["Class 3"][UID]={}
            report_card["Class 3"][UID]["Name "+str(k)]=name
            report_card["Class 3"][UID][str(name)+"'s Maths Marks "]=maths
            report_card["Class 3"][UID][str(name)+"'s English Marks "]=eng
            report_card["Class 3"][UID][str(name)+"'s Science Marks "]=science
            report_card["Class 3"][UID][str(name)+"'s Social Science Marks "]=social_science
            report_card["Class 3"][UID][str(name)+"'s Language Marks "]=lang
            report_card["Class 3"][UID][str(name)+"'s Percentage "]=percentage
            k+=1
        elif cls==4:
            UID=int(input("Enter your unique ID : "))
            name=input("Enter your name : ")
            maths=int(input("Enter your Maths marks : "))
            eng=int(input("Enter your English marks : "))
            science=int(input("Enter your Science marks : "))
            social_science=int(input("Enter your Social Science marks : "))
            lang=int(input("Enter your Language marks : "))
            print("\n")
            percentage=(maths+eng+science+social_science+lang)/5
            report_card["Class 4"][UID]={}
            report_card["Class 4"][UID]["Name "+str(l)]=name
            report_card["Class 4"][UID][str(name)+"'s Maths Marks "]=maths
            report_card["Class 4"][UID][str(name)+"'s English Marks "]=eng
            report_card["Class 4"][UID][str(name)+"'s Science Marks "]=science
            report_card["Class 4"][UID][str(name)+"'s Social Science Marks "]=social_science
            report_card["Class 4"][UID][str(name)+"'s Language Marks "]=lang
            report_card["Class 4"][UID][str(name)+"'s Percentage "]=percentage
            l+=1
        elif cls==5:
            UID=int(input("Enter your unique ID : "))
            name=input("Enter your name : ")
            maths=int(input("Enter your Maths marks : "))
            eng=int(input("Enter your English marks : "))
            science=int(input("Enter your Science marks : "))
            social_science=int(input("Enter your Social Science marks : "))
            lang=int(input("Enter your Language marks : "))
            print("\n")
            percentage=(maths+eng+science+social_science+lang)/5
            report_card["Class 5"][UID]={}
            report_card["Class 5"][UID]["Name "+str(m)]=name
            report_card["Class 5"][UID][str(name)+"'s Maths Marks "]=maths
            report_card["Class 5"][UID][str(name)+"'s English Marks "]=eng
            report_card["Class 5"][UID][str(name)+"'s Science Marks "]=science
            report_card["Class 5"][UID][str(name)+"'s Social Science Marks "]=social_science
            report_card["Class 5"][UID][str(name)+"'s Language Marks "]=lang
            report_card["Class 5"][UID][str(name)+"'s Percentage "]=percentage
            m+=1
        elif cls==6:
            UID=int(input("Enter your unique ID : "))
            name=input("Enter your name : ")
            maths=int(input("Enter your Maths marks : "))
            eng=int(input("Enter your English marks : "))
            science=int(input("Enter your Science marks : "))
            social_science=int(input("Enter your Social Science marks : "))
            lang=int(input("Enter your Higher Language marks : "))
            t_lang=int(input("Enter your Lower Language marks : "))
            print("\n")
            percentage=(maths+eng+science+social_science+lang+t_lang)/6
            report_card["Class 6"][UID]={}
            report_card["Class 6"][UID]["Name "+str(n)]=name
            report_card["Class 6"][UID][str(name)+"'s Maths Marks "]=maths
            report_card["Class 6"][UID][str(name)+"'s English Marks "]=eng
            report_card["Class 6"][UID][str(name)+"'s Science Marks "]=science
            report_card["Class 6"][UID][str(name)+"'s Social Science Marks "]=social_science
            report_card["Class 6"][UID][str(name)+"'s Higher Language Marks "]=lang
            report_card["Class 6"][UID][str(name)+"'s Lower Language Marks "]=t_lang
            report_card["Class 6"][UID][str(name)+"'s Percentage "]=percentage
            n+=1
        elif cls==7:
            UID=int(input("Enter your unique ID : "))
            name=input("Enter your name : ")
            maths=int(input("Enter your Maths marks : "))
            eng=int(input("Enter your English marks : "))
            science=int(input("Enter your Science marks : "))
            social_science=int(input("Enter your Social Science marks : "))
            lang=int(input("Enter your Higher Language marks : "))
            t_lang=int(input("Enter your Lower Language marks : "))
            print("\n")
            percentage=(maths+eng+science+social_science+lang+t_lang)/6
            report_card["Class 7"][UID]={}
            report_card["Class 7"][UID]["Name "+str(o)]=name
            report_card["Class 7"][UID][str(name)+"'s Maths Marks "]=maths
            report_card["Class 7"][UID][str(name)+"'s English Marks "]=eng
            report_card["Class 7"][UID][str(name)+"'s Science Marks "]=science
            report_card["Class 7"][UID][str(name)+"'s Social Science Marks "]=social_science
            report_card["Class 7"][UID][str(name)+"'s Higher Language Marks "]=lang
            report_card["Class 7"][UID][str(name)+"'s Lower Language Marks "]=t_lang
            report_card["Class 7"][UID][str(name)+"'s Percentage "]=percentage
            o+=1
        elif cls==8:
            UID=int(input("Enter your unique ID : "))
            name=input("Enter your name : ")
            maths=int(input("Enter your Maths marks : "))
            eng=int(input("Enter your English marks : "))
            science=int(input("Enter your Science marks : "))
            social_science=int(input("Enter your Social Science marks : "))
            lang=int(input("Enter your Higher Language marks : "))
            t_lang=int(input("Enter your Lower Language marks : "))
            print("\n")
            percentage=(maths+eng+science+social_science+lang+t_lang)/6
            report_card["Class 8"][UID]={}
            report_card["Class 8"][UID]["Name "+str(p)]=name
            report_card["Class 8"][UID][str(name)+"'s Maths Marks "]=maths
            report_card["Class 8"][UID][str(name)+"'s English Marks "]=eng
            report_card["Class 8"][UID][str(name)+"'s Science Marks "]=science
            report_card["Class 8"][UID][str(name)+"'s Social Science Marks "]=social_science
            report_card["Class 8"][UID][str(name)+"'s Higher Language Marks "]=lang
            report_card["Class 8"][UID][str(name)+"'s Lower Language Marks "]=t_lang
            report_card["Class 8"][UID][str(name)+"'s Percentage "]=percentage
            p+=1
        elif cls==9:
            UID=int(input("Enter your unique ID : "))
            name=input("Enter your name : ")
            maths=int(input("Enter your Maths marks : "))
            eng=int(input("Enter your English marks : "))
            science=int(input("Enter your Science marks : "))
            social_science=int(input("Enter your Social Science marks : "))
            lang=int(input("Enter your Language marks : "))
            print("\n")
            percentage=(maths+eng+science+social_science+lang)/5
            report_card["Class 9"][UID]={}
            report_card["Class 9"][UID]["Name "+str(q)]=name
            report_card["Class 9"][UID][str(name)+"'s Maths Marks "]=maths
            report_card["Class 9"][UID][str(name)+"'s English Marks "]=eng
            report_card["Class 9"][UID][str(name)+"'s Science Marks "]=science
            report_card["Class 9"][UID][str(name)+"'s Social Science Marks "]=social_science
            report_card["Class 9"][UID][str(name)+"'s Language Marks "]=lang
            report_card["Class 9"][UID][str(name)+"'s Percentage "]=percentage
            q+=1
        elif cls==10:
            UID=int(input("Enter your unique ID : "))
            name=input("Enter your name : ")
            maths=int(input("Enter your Maths marks : "))
            eng=int(input("Enter your English marks : "))
            science=int(input("Enter your Science marks : "))
            social_science=int(input("Enter your Social Science marks : "))
            lang=int(input("Enter your Language marks : "))
            print("\n")
            percentage=(maths+eng+science+social_science+lang)/5
            report_card["Class 10"][UID]={}
            report_card["Class 10"][UID]["Name "+str(r)]=name
            report_card["Class 10"][UID][str(name)+"'s Maths Marks "]=maths
            report_card["Class 10"][UID][str(name)+"'s English Marks "]=eng
            report_card["Class 10"][UID][str(name)+"'s Science Marks "]=science
            report_card["Class 10"][UID][str(name)+"'s Social Science Marks "]=social_science
            report_card["Class 10"][UID][str(name)+"'s Language Marks "]=lang
            report_card["Class 10"][UID][str(name)+"'s Percentage "]=percentage
            r+=1
        elif cls==11:
            UID=int(input("Enter your unique ID : "))
            name=input("Enter your name : ")
            maths=int(input("Enter your Maths marks : "))
            eng=int(input("Enter your English marks : "))
            csc=int(input("Enter your Computer Science marks : "))
            phy=int(input("Enter your Physics marks : "))
            chem=int(input("Enter your Chemistry marks : "))
            print("\n")
            percentage=(maths+eng+csc+phy+chem)/5
            report_card["Class 11"][UID]={}
            report_card["Class 11"][UID]["Name "+str(s)]=name
            report_card["Class 11"][UID][str(name)+"'s Maths Marks "]=maths
            report_card["Class 11"][UID][str(name)+"'s English Marks "]=eng
            report_card["Class 11"][UID][str(name)+"'s Computer Science Marks "]=csc
            report_card["Class 11"][UID][str(name)+"'s Physics Marks "]=phy
            report_card["Class 11"][UID][str(name)+"'s Chemistry Marks "]=chem
            report_card["Class 11"][UID][str(name)+"'s Percentage "]=percentage
            s+=1
        elif cls==12:
            UID=int(input("Enter your unique ID : "))
            name=input("Enter your name : ")
            maths=int(input("Enter your Maths marks : "))
            eng=int(input("Enter your English marks : "))
            csc=int(input("Enter your Computer Science marks : "))
            phy=int(input("Enter your Physics marks : "))
            chem=int(input("Enter your Chemistry marks : "))
            percentage=(maths+eng+csc+phy+chem)/5
            report_card["Class 12"][UID]={}
            report_card["Class 12"][UID]["Name "+str(t)]=name
            report_card["Class 12"][UID][str(name)+"'s Maths Marks "]=maths
            report_card["Class 12"][UID][str(name)+"'s English Marks "]=eng
            report_card["Class 12"][UID][str(name)+"'s Science Marks "]=csc
            report_card["Class 12"][UID][str(name)+"'s Social Science Marks "]=phy
            report_card["Class 12"][UID][str(name)+"'s Language Marks "]=chem
            report_card["Class 12"][UID][str(name)+"'s Percentage "]=percentage
            t+=1
        else:
            print("Please input correct class.")
    elif a==2: #Sharaj did this part.
        print("\n")
        cls=str(input("Enter the class : "))
        print("Here is a list of UID(s) you can delete : ",tuple(report_card["Class "+cls].keys()))
        if tuple(report_card["Class "+cls].keys())!=ept:
            UID=int(input("Enter the UID : "))
            if UID in tuple(report_card["Class "+cls].keys()):
                option=input("Are you sure you want to delete "+str(UID)+" ?(yes/no)")
                option=option.lower()
                if option=="yes" :
                    del report_card["Class "+cls][UID]
                    print("Alright,Deleted.")
                elif option=="no":
                    print("Alright, Not Deleted.")
                else:
                    print("Wrong Input.")
            else:
                print("Wrong UID Typed,Try Again.")
        else:
            print("The Class Is Empty.")
            
    elif a==3:
        print("\n")
        if report_card!= empt:
            for z in report_card:
                if report_card[z]!= empt:
                    print("{",z,":")
                for x in report_card[z]:
                    print(x,":", report_card[z][x])
        print("}")
    elif a==4: #Hari did this part.
        print("\n")
        if report_card1!= empt:
            print("__________________________________________________________________________________________________________________________________________________________________")
            for z in report_card1:
                if report_card1[z]!= empt:
                    print(z,":")
                for x in report_card1[z]:
                    print("\t",x,":")
                    for y in report_card1[z][x]:
                        print("\t\t",y,":",report_card1[z][x][y])
            print("__________________________________________________________________________________________________________________________________________________________________")
    elif a==5: #Subbramanian did this part.
        print("\n")
        cls=str(input("Enter the class : "))
        if report_card["Class "+cls]!={}:
            print("Here is a list of UID(s) you can access : ",tuple(report_card["Class "+cls].keys()))
            UID=int(input("Enter the UID : "))
            if UID in tuple(report_card["Class "+cls].keys()):
                print("\n")
                print(report_card["Class "+cls][UID])
            else:
                print("Wrong UID Typed,Try Again.")
        else:
            print("Class is empty.")
    else:
        print("\n")
        print("Please choose from given options . ")
else:
    exit()

        
        
        
        
