# --------------

def read_file(path):
    file=open(path,'r')
    sentence=file.readlines()[0]
    
    file.close()
   
    return sentence
    
sample_message=read_file(file_path)    
    
print(sample_message)    



message_1=read_file(file_path_1)
message_2=read_file(file_path_2)
#Function to fuse message
def fuse_msg(message_a,message_b):
    quotient=int(message_b)//int(message_a)
    return str(quotient)
   
    
    
    
secret_msg_1=fuse_msg(message_1,message_2)    

print(secret_msg_1)

print(message_1,message_2)




message_3=read_file(file_path_3)
print(message_3)

#Function to substitute the message
def substitute_msg(message_c):
    if message_c=='Red':
        sub='Army General'
    elif message_c=='Green':
        sub='Data Scientist'
    elif message_c=='Blue':
        sub='Marine Biologist'     
    
    return sub
    
secret_msg_2=substitute_msg(message_3)    
print(secret_msg_2)    








message_4=read_file(file_path_4)
message_5=read_file(file_path_5)
print(message_4)
print(message_5)


def compare_msg(message_d,message_e):
    a_list=message_d.split()
    b_list=message_e.split()
    c_list=[i for i in a_list if i not in b_list]
   
    final_msg=" ".join(c_list)
    return final_msg
    
   
secret_msg_3=compare_msg(message_4,message_5)    
print(secret_msg_3)    

message_6=read_file(file_path_6)
print(message_6)
#Function to filter message
def extract_msg(message_f):
    a_list=message_f.split()
    even_word=lambda x: len(x)%2==0
    #Splitting the message into a list
    b_list=list(filter(even_word,a_list))
    final_msg=" ".join(b_list) 
    return final_msg
    
secret_msg_4=extract_msg(message_6)    
print(secret_msg_4)    
#Calling the function to read file


#Calling the function 'filter_msg'


#Printing the secret message


#Secret message parts in the correct order



# define the path where you 
message_parts=[str(secret_msg_3),str(secret_msg_1),str(secret_msg_4),str(secret_msg_2)]
#Combine the secret message parts into a single complete secret message
secret_msg=" ".join(message_parts)
#Function to write inside a file
def write_file(secret_msg,path):
    file=open(path,'a+')
    file.write(secret_msg)
    #Opening a file named 'secret_message' in 'write' mode
    file.close() 

    #Writing to the file
final_path= user_data_dir + '/secret_message.txt'

    #Closing the file
write_file(secret_msg,final_path)
print(secret_msg)
#Calling the function to write inside the file    


#Printing the entire se


