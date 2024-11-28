from view import  *
import pickle

# To Issue Book

# # To Reduce Book Quant each time 
def issue_book_quant(n):
    f = open("books.dat","rb")
    f.seek(0)
    d = pickle.load(f)
    c = False
    for i in d:
        if n==i[0]:
            if i[3]==0:
                print_center("Book Not Available")
                break
            else:
                i[3] -= 1
                c = True
                break
        else:
            continue
    f.close()
    f = open("books.dat","wb")
    pickle.dump(d,f)
    f.close()
    return c

# # To Take record of Issued Book
def book_issue(n,memb_id):
    f = open("books.dat", "rb")
    f.seek(0)
    d = pickle.load(f)
    l1=[]
    for i in d:
        if n == i[0]:
            l1 = [i[0],i[1]]
            break
    f.close()
    f = open("member.dat", "rb")
    f.seek(0)
    d = pickle.load(f)
    l2 = []
    for i in d :
        if i[0]== memb_id:
            l2=[i[0],i[1],i[2]]
            break
    f.close()
    l1.extend(l2)
    f = open("book_issued.dat", "rb")
    d = pickle.load(f)
    f.close()
    d.append(l1)
    f = open("book_issued.dat","wb")
    pickle.dump(d,f) 
    f.close() 
    print_center("==============================")
    print_center("=========ABC LIBRARY==========")

    print("S. No.\t  :" , l1[0])
    print("Book-Name :" , l1[1])
    print("Memb. Id  :",l1[2] )
    print("Name\t  :" ,l1[3])
    print("Mobile No.:",l1[4])

    print_center("Book Issued")
    print_center("==============================")

# To return book

# # To Increase Book Quant Each time
def return_book_quant(n):
    f = open("books.dat","rb")
    f.seek(0)
    d = pickle.load(f)
    f.close()
    for i in d:
        if n==i[0]:
                i[3] += 1
                break
        else:
            continue
    f = open("books.dat",'wb')
    pickle.dump(d,f)
    f.close()

# # To take record of return book 
def book_return(n,memb_id):
    f = open("book_issued.dat", "rb")
    d = pickle.load(f)
    for i in d :
        if i[0]==n and i[2]==memb_id:
            d.remove(i)
            l1=i
            break
    f.close()
    f = open("book_issued.dat", "wb")
    pickle.dump(d,f)
    f.close()
    print_center("==============================")
    print_center("=========ABC LIBRARY==========")

    print("S. No.\t  :" , l1[0])
    print("Book-Name :" , l1[1])
    print("Memb. Id  :",l1[2] )
    print("Name\t  :" ,l1[3])
    print("Mobile No.:",l1[4])

    print_center("Book Returned")
    print_center("==============================")


# To fetch Book Details
def find_book():
    f = open("books.dat", "rb")
    f.seek(0)
    d = pickle.load(f)
    n = int(input_center("Enter Book serial Number: "))
    c = False
    for i in d:
        if n == i[0]:

            print("S. No.\t :" , i[0])
            print("Book-Name:" , i[1])
            print("Price\t :", i[2])
            print("Quantity :" , i[3])
            print("Publisher:", i[4])
            print("Writer\t :", i[5])

            c = True
    f.close()
    if c == False:
        print("NO RECORD FOUND")
    return n, c


# To fetch Member Detail
def find_memb():
    f = open("member.dat", "rb")
    d = pickle.load(f)
    c = False
    memb_id = int(input_center("Enter Your Member Id: "))
    for i in d :
        if i[0]== memb_id:

            print("Memb. Id  :",i[0])
            print("Name\t  :",i[1] )
            print("Mobile No.:",i[2])
            print("Email-Id  :",i[3] )
            print("DOJ\t  :",i[4])

            c = True
            break
        else:
            continue
    if c == False:
        print_center("Member not Found")
    f.close()
    return memb_id,c


# To Show Book Record
def show_book_record():
    print_center("==============================")
    print("S. No. : Book-Name : Price : Quantity : Publisher \t  : Writer ")
    f = open("books.dat", "rb")
    d = pickle.load(f)
    for i in d:
        print(i[0],'   : ',i[1],'   : ',i[2],' : ',i[3],'      : ',i[4],' : ',i[5])
    f.close()
    print_center("==============================")


# To Add-Book Record
def add_book_record():
    f = open("books.dat","rb")
    l=pickle.load(f)
    f.close()
    while True:

        sno = int(input("Enter Serial No. :"))
        Bona = input("Enter Book Name  :")
        price = int(input("Enter Price\t :"))
        quant = int(input("Enter Quantity   :"))
        publ = input("Enter Publisher  :")
        wrna = input("Enter Writer Name:")

        l1 = [sno,Bona,price,quant,publ,wrna]
        l.append(l1)
        c= input("Want To add More Record?(Y/N)")
        if c in 'Yy':
            continue
        else:
            break
    f = open("books.dat","wb")
    pickle.dump(l,f)
    f.close()
    print("Record Added Succesfully")
    show_book_record()       


# To Delete Book Record
def delete_book_record():
    bosn, ch = find_book()
    while True:
        if ch == False:
            break
        else:
            f = open("books.dat","rb")
            d = pickle.load(f)
            f.close()
            for i in d:
                if i[0]==bosn:
                    d.remove(i)
            f= open("books.dat","wb")
            pickle.dump(d,f)
            f.close()
            break


# To Update Book Record
def update_book_record():
    bosn, ch = find_book()
    while True:
        if ch ==False:
            break
        else:
            print_center("Current Record")
            print_center('**'*20)
            print_center("Write Update Record")

            sno = int(input("Enter Serial No. :"))
            Bona = input("Enter Book Name  :")
            price = int(input("Enter Price\t :"))
            quant = int(input("Enter Quantity   :"))
            publ = input("Enter Publisher  :")
            wrna = input("Enter Writer Name:")

            l = [sno,Bona,price,quant,publ,wrna]
            f = open("books.dat","rb")
            d = pickle.load(f)
            f.close()
            for i in d:
                if i[0]==bosn:
                    i=l
            f = open("books.dat","wb")
            pickle.dump(d,f)
            f.close()
            print("Record Updated Succesfully")
            break


# To Show Member Detail
def show_member_record():
    print_center("==============================")
    print("Memb.Id : Name    : Mobile No.   : Email-Id \t\t   :  DOJ")
    f = open("member.dat", 'rb')
    d = pickle.load(f)
    for i in d:
        print(i[0],'    : ',i[1],' : ',i[2],' : ',i[3],' : ',i[4])
    f.close()
    print_center("==============================")


# To Add New Member record
def add_member_record():
    f= open("member.dat","rb")
    l=pickle.load(f)
    f.close()
    while True:

        sno = int(input("Enter Memb. Id\t   :"))
        mena = input("Enter Member Name  :")
        mobno = int(input("Enter Mobile Number:"))
        email = input("Enter Email-Id\t   :")
        doj = input("Enter DOJ\t   :")

        l.append([sno,mena,mobno,email,doj])
        c= input("Want To add More Record?(Y/N)")
        if c in 'Yy':
            continue
        else:
            break
    f = open("member.dat","wb")
    pickle.dump(l,f)
    f.close()
    print("Record Added Succesfully")
    show_member_record()    


#To delete Member record
def delete_member_record():
    meid, ch = find_memb()
    while True:
        if ch == False:
            break
        else:
            f = open("member.dat","rb")
            d = pickle.load(f)
            f.close()
            for i in d:
                if i[0]==meid:
                    d.remove(i)
            f= open("member.dat","wb")
            pickle.dump(d,f)
            f.close()
            break


# To Update Member Record
def update_member_record():
    meid, ch = find_memb()
    while True:
        if ch == False:
            break
        else:
            print_center("Current Record")
            print_center('**'*20)
            print_center("Write Update Record")

            sno = int(input("Enter Memb. Id\t   :"))
            mena = input("Enter Member Name  :")
            mobno = int(input("Enter Mobile Number:"))
            email = input("Enter Email-Id\t   :")
            doj = input("Enter DOJ\t   :")

            l = [sno,mena,mobno,email,doj]
            f = open("member.dat","rb")
            d = pickle.load(f)
            f.close()
            for i in d:
                if i[0]==meid:
                    i=l
            f = open("member.dat","wb")
            pickle.dump(d,f)
            f.close()
            print("Record Updated Succesfully")
            break
