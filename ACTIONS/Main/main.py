import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# importing necessary libraries



df=pd.read_excel('/home/ram/Desktop/HELLO/EXCEL/file.xlsx',parse_dates=['Date'],index_col='Date')

# loading data and convert string as date and use it as index



def mini_statement():  # Function(11)
    new_df=df.tail()   # Gives last 5 Transactions


    want=int(input("what kind of Statement You want  \n1.Dataframe form\n2.Visualization form: ")) #prompting the user to input

    if want==1:       # printing the dataframe of last 5 Transactions
        print(new_df)

    elif want==2:     # displaying line graph of Mini Statement

        x=np.array(new_df['Description'])
        y=np.array(new_df['Amount'])

        plt.plot(x,y,color='orange',linewidth=4,marker='o',markersize=7,markeredgecolor='red',label='Analysis Scale',linestyle='solid')
        plt.xlabel("Description")
        plt.ylabel("Amount")
        plt.title("Mini Statement")
        
        plt.grid(axis='y',color='cyan',linewidth=5) 
        plt.legend()

        plt.show()


def debit_summary():  # Function 2
   #Month_wise Debit
    dfd=df[df['Nature']=="Debit"]

    arr_avg=np.array(dfd['Amount'].resample("M").mean()) # storing monthwise average in array
    arr_max=np.array(dfd['Amount'].resample("M").max())  #storing monthwise maximum in array
    arr_min=np.array(dfd['Amount'].resample("M").min())   ## storing monthwise minimum in array

    x_value=np.arange(1,13) # creating x axis
    
    inp_one=int(input("Debit Statement in Month-Wise:\n1.Maximum Rate\n2.Average rate\n3.Minimum Rate"))  #prompting user to input

    if inp_one==2: # plotting average
        plt.plot(x_value,arr_avg,linewidth=3,color='orange',label='Average Debit Rate',marker='o',markersize=5,markeredgecolor='black')


    elif inp_one==1: # plotting maximum
        plt.plot(x_value,arr_max,linewidth=3,color='red',label='Maximum Debit Rate',marker='o',markersize=5,markeredgecolor='black')

    elif inp_one==3: # plotting minimum
        plt.plot(x_value,arr_min,linewidth=3,color='green',label='Minimum Debit Rate',marker='o',markersize=5,markeredgecolor='black')

    plt.xlabel("Month",size=18)
    plt.ylabel("Amount",size=18)
    plt.grid(axis='y')
    plt.legend()
    plt.show()


def custom_exporter():   # Function (3)
    df=pd.read_excel('/home/ram/Desktop/HELLO/EXCEL/file.xlsx',index_col=None)
    df['Date']=pd.to_datetime(df['Date'])



    df["Month"]=df['Date'].dt.month_name() # create an month column by resampling

    from_date=input("Enter From date in (YYYY-MM-DD):  ")  # prompting to get from date
    to_date=input("Enter To date in (YYYY-MM-DD):  ")     # prompting to get to date
    

    filter_df=df[(df['Date']>=from_date)& (df['Date']<=to_date)]   # filtering the dataframe from date and to date

    inp_expo=int(input("Select how to export data \n 1.CSV\n 2.XLS\n 3.TXT \n 4.View only:"))  # prompting to export
    if inp_expo==4:   # Displaying data
        result=filter_df

    elif inp_expo==1:  # Exporting to CSV file
        result=filter_df.to_csv("/home/ram/Desktop/HELLO/ACTIONS/Storer/CSV_file.csv")

    elif inp_expo==3: # Exporting to TEXT file
        result=filter_df.to_csv("/home/ram/Desktop/HELLO/ACTIONS/Storer/Text_file.txt",sep=" ")

    elif inp_expo==2: # Exporting to XL file
        result=filter_df.to_excel("/home/ram/Desktop/HELLO/ACTIONS/Storer/Excel_file.xlsx")


    result # return the result



def for_four(): # Function (4)

    path_map="/home/ram/Desktop/HELLO/EXCEL/file.xlsx"
    df=pd.read_excel(path_map)
    df["Date"]=pd.to_datetime(df["Date"])



    df["Month"]=df['Date'].dt.month_name()

    from_date=input("Enter From date in (YYYY-MM-DD):  ")
    to_date=input("Enter To date in (YYYY-MM-DD):  ")
    # 2022-01-01 || 2022-03-31

    filter_df=df[(df['Date']>=from_date)& (df['Date']<=to_date)]

    filter_df

    debit=filter_df[filter_df['Nature']=="Debit"]  # create a dataframe with Debit items

    upi=debit[debit["Channel"]=="UPI"]  # create a dataframe for upi
    dr_card=debit[debit["Channel"]=="CARD"] # create a dataframe for card

    net_bank=debit[debit["Channel"]=="NET BANKING"] # create a dataframe for net_banking
    atm=debit[debit["Channel"]=="ATM"]  #create a dataframe for atm

    total_upi=upi["Amount"].sum()          # sum of upi
    total_net_bank=net_bank["Amount"].sum() # sum of net_bank
    total_card=dr_card["Amount"].sum() # sum of card
    total_atm=atm["Amount"].sum()  # sum of atm
 

    elements=[total_card,total_atm,total_upi,total_net_bank] # create x axis
    labeller=["CARD","ATM","UPI","NET_BANKING"] # create labels


    opter=int(input("Select to View\n1.Overall Channel_wise\n2.Card\n3.ATM\n4.UPI\n5.NET_BANKING")) # prompting the user to view

    if opter==1: # display data in donot chart

        plt.pie(elements,labels=labeller,labeldistance=1.25,startangle=90,autopct='%1.3f%%',explode=[0.025,0.025,0.025,0.025],pctdistance=1)

        rounder=plt.Circle((0,0),0.5,fc="white")

        fig=plt.gcf()

        fig.gca().add_artist(rounder)

        result=plt.show()

    elif opter==2:  # display card transactions
        result=dr_card

    elif opter==3: # display atm transactions
        result=atm

    elif opter==4: # display upi transactions
        result=upi

    elif opter==5: # dispaly net_banking transactions
        result=net_bank

    print(result) # return result


def d_channelwise(): # Function (5)

    path_map="/home/ram/Desktop/HELLO/EXCEL/file.xlsx"

    df=pd.read_excel(path_map)
    df["Date"]=pd.to_datetime(df["Date"])



    df["Month"]=df['Date'].dt.month_name()

    from_date=input("Enter From date in (YYYY-MM-DD):  ")
    to_date=input("Enter To date in (YYYY-MM-DD):  ")
    # 2022-01-01 || 2022-03-31

    debit_df=df[df['Nature']=="Debit"]

    filter_df=debit_df[(df['Date']>=from_date)& (df['Date']<=to_date)]

    grp=filter_df.groupby("Description")["Amount"].sum()


    plt.barh(grp.index,grp.values) # plotting barchart in horizontal view
    plt.ylabel('Description',color='brown',size=10)
    plt.xlabel('Amount',color='brown',size=10)
    plt.title("Expenditure Rate")
    plt.grid(axis='x',linewidth=3,color='grey')
    plt.show()  



def c_channelwise(): # Function 6
    path_map="/home/ram/Desktop/HELLO/EXCEL/file.xlsx"
    df=pd.read_excel(path_map)
    df["Date"]=pd.to_datetime(df["Date"])



    df["Month"]=df['Date'].dt.month_name()

    from_date=input("Enter From date in (YYYY-MM-DD):  ")
    to_date=input("Enter To date in (YYYY-MM-DD):  ")
    # 2022-01-01 || 2022-03-31

    credit_df=df[df['Nature']=="Credit"]

    filter_df=credit_df[(df['Date']>=from_date)& (df['Date']<=to_date)]

    grp=filter_df.groupby("Description")["Amount"].sum()


    plt.barh(grp.index,grp.values)  # plotting barchart in horizontal view
    plt.ylabel('Description',color='brown',size=10)
    plt.xlabel('Amount',color='brown',size=10)
    plt.title("Income Rate")
    plt.grid(axis='x',linewidth=3,color='grey')
    plt.show()


    plt.barh(grp.index,grp.values)
    plt.ylabel('Description',color='brown',size=10)
    plt.xlabel('Amount',color='brown',size=10)
    plt.title("Expenditure Rate")
    plt.grid(axis='x',linewidth=3,color='grey')
    plt.show()


opener=int(input("1.Mini Statement\n2.Expenses Summary in Month-Wise\n3.Custom_Export\n4.Overall Expenditure in Channel\n5.Expense in Individual Channel-Wise \n6.Incomes in Individual  Channel-Wise: \t"))
# prompting the actions to input

if opener==1:    # Function 1
 mini_statement()


elif opener==2:   # Function 2
    debit_summary()

elif opener==3:   # Function 3
    custom_exporter()

elif opener==4:   # Function 4
    for_four()

elif opener==5:    # Function 5
    d_channelwise()

elif opener==6:   # Function 6
    c_channelwise()









    
