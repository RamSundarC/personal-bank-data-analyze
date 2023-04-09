import pandas as pd
import matplotlib.pyplot as plt
import numpy as np




df=pd.read_excel('/home/ram/Desktop/HELLO/file.xlsx',index_col=None)



def mini_statement():
    new_df=df.tail()


    want=int(input("what kind of Statement You want  \n1.Dataframe form\n2.Visualization form: "))

    if want==1:
        print(new_df)

    elif want==2:

        x=np.array(new_df['Description'])
        y=np.array(new_df['Amount'])

        plt.plot(x,y,color='orange',linewidth=4,marker='o',markersize=7,markeredgecolor='red',label='Analysis Scale',linestyle='solid')
        plt.xlabel("Description")
        plt.ylabel("Amount")
        plt.title("Mini Statement")
        
        plt.grid(axis='y',color='cyan',linewidth=5) 
        plt.legend()

        plt.show()


mini_statement()








    
