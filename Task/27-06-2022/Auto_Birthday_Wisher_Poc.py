import pandas as pd
from datetime import datetime
import smtplib
import os

current_path=os.getcwd()
print(current_path)
os.chdir(current_path)

gmail_id=input("Enter Your Email-Id:")
pswd_id=input("Enter your Password:")

def sendMail(to,sub,msg):
    print(f"Email to sent {to}:\nSubject:{sub},\nMessage:{msg}")
    b=smtplib.SMTP('smtp.gmail.com',534)
    b.starttls()
    b.login(gmail_id,pswd_id)
    b.sendmail(gmail_id,to,f"Subject:{sub},\n\n{msg}")
    timeout = 20
    b.listen(timeout)
    b.quit()

if __name__=="__main__":
    df=pd.read_excel("data.xlsx")
    today=datetime.now().strftime("%d-%m")
    year=datetime.now().strftime("%Y")
    print(today)
    print(year)

    wish=[]
    for index,item in df.iterrows():
        bday=item['Birthday']
        print(bday)
        bday=bday.strftime("%d-%m")

        if(today==bday)and year not in str(item['LastWishedYear']):
            sendMail(item['Email'],"Happy Birthday Dear",item['Dialogue'])
            wish.append(index)

        if wish!=None:
            for i in wish:
                oldYear=df.loc[i,'LastWishedYear']
                df.loc[i,'LastWishedYear']=str(oldYear)+","+str(year)

            df.to_excel('data.xlsx',index=False)
                
    
