'''LOGGING TO PROMPT'''

##from logging import*
##debug("This is Debug")
##info("Information")
##warning("This is Warning")
##error("This is a Error")
##critical("This is Critical")

'''Logging to File'''

##from logging import*
##basicConfig(filename="rakesh.log")
##warning("This is Warning")
##error("This is Error")
##critical("This is Critical")

'''Change the levels'''

##from logging import*
##basicConfig(filename="Akash.txt",level=DEBUG)
##debug("This is Debug")
##info("Information")
##warning("This is Warning")
##error("This is a Error")
##critical("This is a Message from Critical")

'''How to change File Mode in Logging'''

##from logging import*
##basicConfig(filename="akash1.txt",level=DEBUG,filemode="w")
##debug("This is Debug")
##info("Information")
##warning("This is Warning")
##error("This is a Error")
##critical("This is a Message from Critical")

'''How to store Your data in which FOrmat'''

##from logging import*
##basicConfig(filename="akash2.txt",level=ERROR,filemode="w",format='%(asctime)s--%(message)s')
##debug("This is Debug")
##info("Information")
##warning("This is Warning")
##error("This is a Error")
##critical("This is a Message from Critical")
##

##from logging import*
##Log='%(asctime)s//%(message)s// %(lineno)d'
##basicConfig(filename='akash3.log',level=WARNING,filemode='w',format=Log)
##debug("This is Debug")
##info("Information")
##warning("This is Warning")
##error("This is a Error")
##critical("This is a Message from Critical")


##from logging import*
##Log='{lineno}=={name}=={asctime}=={message}'
##basicConfig(filename='akash4.log',level=WARNING,filemode='w',style='{',format=Log)
##debug("This is Debug")
##info("Information")
##warning("This is Warning")
##error("This is a Error")
##critical("This is a Message from Critical")

'''How to Change default root name'''

##from logging import*
##Log='{lineno}=={name}=={asctime}=={message}'
##basicConfig(filename='akash5.log',level=WARNING,filemode='w',style='{',format=Log)
##logger=getLogger("Akash")
##logger.debug("This is Debug")
##logger.info("Information")
##logger.warning("This is Warning")
##logger.error("This is a Error")
##logger.critical("This is a Message from Critical")



##from logging import*
##FLog='%(lineno)d::%(asctime)s::%(levelname)s::%(message)s::%(name)s'
##
##basicConfig(filename='Employee.log',level=INFO,format=FLog,filemode="w")
##
##logger=getLogger("Aman")
##
##def Validation(fun):
##    logger.info("ENter Validation FUnction.")
##    
##    def fun(User_input):
##        logger.info("Before Checking The Data.")
##        data=["Aman"]
##        if User_input in data:
##            logger.info("User name is Present in Database")
##            return 'Welcome'+" "+User_input
##
##        else:
##            logger.debug("User Name not present in Database.")
##            return 'Wrong User.'
##    return fun
##
##
##
##@Validation
##def Login_User(user_input):
##    return user_input
##
##user_input=input("Enter The User Name:")
##
##logger.info("User input Given.")
##
##print(Login_User(user_input))
##






def concatenate_list_data(list):
    result= ''
    for element in list:
        result += str(element)
    return result
 
print(concatenate_list_data([2, 10, 22, 21]))









