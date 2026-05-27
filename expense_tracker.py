# EXPENSE TRACKER
expenses=[] # list of expenses
print("WELCOME TO EXPENSE TRACKER")

while(True):
    print("------Menu------")
    print("1. Add Expense")
    print("2. View Expense")
    print("3. Total Expense")
    print("4. Exit")

    choice=int(input("Enter Your Choice:-"))

# ADD EXPENSES
    if choice==1:
         Date=input("Enter the Date of Transaction:-")
         Category=input("Enter The Category(Food,Travel,Clothes,Electronic_Devices,Self_care,etc):-")
         Description=input(("Enter More Detail Description About Category:-"))
         Amount=float(input("Enter Your Amount:-"))

         transaction={
             "Date":Date,
             "Category":Category,
             "Description":Description,
             "Amount":Amount
         }
         expenses.append(transaction)
         print()
         print("Expenses Added Successfully")
# VIEW EXPENSES
    elif choice==2:
         if(len(expenses)==0):
              print("No Expenses")
         else:
              print("------Your All Transaction------")
              count=1
              for Transaction in expenses:
                  print(f"Transaction{count} -> {Transaction['Date']},{Transaction['Category']},{Transaction['Description']},{Transaction['Amount']}") 
                  count=count+1
              print("View Expenses Successfully")
# TOTAL EXPENSES
    elif choice==3:
         Total=0
         for Transaction in expenses:
              Total=Total+Transaction["Amount"]
         print()
         print("Total=",Total)
        
# EXIT
    elif choice==4:
      print("THANK FOR USING EXPENSE TRACKER")
      break
    else:
      print("Invalid Choice")
