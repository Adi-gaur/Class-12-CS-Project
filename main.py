import pickle
from data import *
from view import print_center
while True:
    print()
    print_center("==============================")
    print_center("=====LIBRARY MANAGEMENT=======")
    print_center("==============================")

    print("1. Issue/Return Register")
    print("2. Manage Books")
    print("3. Manage Members")
    print("4. Check Issued Book")
    print("0. Exit")

    print()
    choice = int(input("Enter your choice: "))
    
    # Issue/Return Register
    if choice == 1:
        sno, check = find_book()
        if check == False:
            continue
        else:
            while True:
                print_center("which function want to perform:")

                print("1. Issue It")
                print("2. Return It")
                print("0. Exit")

                print()
                ch = int(input("Enter Your Choice: "))
                # To Issue Book
                if ch == 1:
                    print_center("==========Book Issue==========")
                    c = issue_book_quant(sno)
                    if c == True:
                        memb_id, c1 = find_memb()
                        if c1 == True:
                            book_issue(sno,memb_id)
                            print_center("=============DONE=============")
                        else:
                            return_book_quant(sno)

                # to return Book
                elif ch == 2:
                    print_center("==========Book Return=========")
                    return_book_quant(sno)
                    memb_id, c1 = find_memb()
                    if c1 == True:
                        book_return(sno,memb_id)
                        print_center("=============DONE=============")
                    else:
                        issue_book_quant(sno)
                elif ch==0:
                    break
                else:
                    print("Invalid choice")
    
    # Manage Books
    elif choice == 2:
        while True:
            print_center("Operation to Perform on Book Records")  

            print("1. Show Books Details")
            print("2. Add New Books Records")
            print("3. Delete Book Records")
            print("4. Update Book Records")
            print("0. Exit")

            print()
            ch1 = int(input("Enter Your Choice:"))
            # Show Book Details
            if ch1==1:
                show_book_record()
            # Add New Book Record
            elif ch1==2:
                print_center("Add New Book Record")
                add_book_record()
            # Delete Book Record
            elif ch1==3:
                print_center("Delete Book Record")
                delete_book_record()
            # update Book Record
            elif ch1==4:
                print_center("Update Book Record")
                update_book_record()
            elif ch1==0:
                break
            else:
                print("Invalid choice")

    # Manage Members
    elif choice == 3:
        while True:
            print_center("Operation to Perform on Members Records")  

            print("1. Show Members Details")
            print("2. Add New Members Records")
            print("3. Delete Members Records")
            print("4. Update Members Records")
            print("0. Exit")

            print()
            ch2 = int(input("Enter Your Choice:")) 
            #show Members detail
            if ch2 == 1:
                show_member_record()
            # Add New member Record
            elif ch2==2:
                print_center("Add New member Record")
                add_member_record()
            # Delete member Record
            elif ch2==3:
                print_center("Delete member Record")
                delete_member_record()
            # update member Record
            elif ch2==4:
                print_center("Update member Record")
                update_member_record()
            elif ch2==0:
                break
            else:
                print("Invalid choice")             
    
    # Check Issued Books
    elif choice == 4:
        f = open("book_issued.dat", 'rb')
        f.seek(0)
        print ("Book S.no.: Book Name : Memb Id : Memb Name : Mobile No.")
        d = pickle.load(f)
        for i in d:
            print(i[0],'\t  :',i[1],'    : ',i[2],'\t:  ',i[3],'  :',i[4])
        f.close()

    elif choice == 0:
        break
    else:
        print("Invalid choice (Press 0 to exit)")

print_center("GoodBye")
print_center("==============================")
