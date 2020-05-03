import pandas as pd
import numpy as np
import json
from io import BytesIO
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
from collections import Counter

class Csv:
    def __init__(self,pathfile,pathfig=r'static/plot/'):
        self.error=0
        try:
            self.df=pd.read_csv(pathfile)
        except:
            try:
                self.df=pd.read_excel(pathfile)
            except:
                self.error=1
        self.pathfig=pathfig

    def show(self):
        return self.df.to_html()
    
    def describe(self):
        return self.df.describe().to_html()

    def head(self):
        return self.df.head().to_html()
    
    def null(self,col=None):
        if col==None:
            return (len(self.df)-self.df.count())
        if hasattr(self.df,col):
            return (len(self.df)-self.df[col].count())
        else:
            return f'Error: No Column name "{col}"'

    def cols(self):
        return self.df.columns

    def plot(self,graph,col1,col2=None,**d):
        fname='fig'+str(int(plt.time.time()))
        name=self.pathfig+'/'+fname
        
        if col2:
            df=self.df[[col1,col2]]
            if col1==col2:
                df.columns.values[1]+=' '
        else:
            df=self.df[[col1]]
            
        df=df.dropna()
        flag1=flag2=0
        if df[col1].dtype=='O':
            df[col1]=LabelEncoder().fit_transform(df[col1])
            flag1=1
        if col2 and df[col2].dtype=='O':
            df[col2]=LabelEncoder().fit_transform(df[col2])
            flag2=1

        if graph=='scatter':
            if not col2:
                return 'Error: 2 Columns are required'
            plt.scatter(df[col1],df[col2],**d)
            plt.xlabel(col1 + flag1*' (LabelEncoded)')
            plt.ylabel(col2 + flag2*' (LabelEncoded)')
        elif graph=='bar':
            if col2:
                sz=len(df)
                plt.bar(np.arange(-0.4,sz*2-.4,2),df[col1],**d)
                plt.bar(np.arange( 0.4,sz*2+.4,2),df[col2])
                plt.xlabel(col1+'&'+col2 + (flag1+flag2)*' (LabelEncoded)')
            else:
                plt.bar(np.arange(len(df)),df[col1],**d)
                plt.xlabel(col1+ flag1*' (LabelEncoded)')
            plt.ylabel('Value (=height)')
            
        elif graph=='histogram':
            if col2:
                plt.hist((df[col1],df[col2]),**d)
                plt.xlabel(col1+'&'+col2 + (flag1+flag2)*' (LabelEncoded)')
            else:
                plt.hist(df[col1],**d)
                plt.xlabel(col1+ flag1*' (LabelEncoded)')
            plt.ylabel('Count')

        elif graph=='plot':
            if col2:
                plt.plot(df[col1],df[col2],marker='o',ms=4,**d)
                plt.xlabel(col1 + flag1*' (LabelEncoded)')
                plt.ylabel(col2 + flag2*' (LabelEncoded)')
            else:
                plt.plot(np.arange(len(df)),df[col1],marker='o',ms=4,**d)
                plt.xlabel('x (row-index)')
                plt.ylabel(col1 + flag1*' (LabelEncoded)')
        elif graph=='pie':
            if col2:
                return 'Error: Only single Columns is required'
            df[col1].values.sort()
            z=Counter(df[col1])
            plt.pie(z.values(),autopct='%1.1f%%',**d)
            plt.legend(z.keys())
            plt.xlabel(col1 + flag1*' (LabelEncoded)')
        
        imdata = BytesIO()
        plt.savefig(imdata)
        plt.clf()
        
        return imdata.getvalue()

if __name__=='__main__':
    o=Csv(r'output.csv')
                    
        
        
        
        

    
