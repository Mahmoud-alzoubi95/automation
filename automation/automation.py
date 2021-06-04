import re

def collection():
    content="Email\n"
    reg_email=r"[A-Za-z0-9]+@[A-Za-z0-9]+.[A-Za-z0-9]"
    reg_phone=r"[\+\d]?(\d{2,3}[-\.\s]??\d{2,3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})"

    with open('potential-contacts.txt','r') as file:
        file=file.read()
        find_email=re.findall(reg_email,file)
        find_phone_num=re.findall(reg_phone,file)
        str_file_email = '\n'.join(find_email)
        str_file_phone_num = '\n'.join(find_phone_num)
        # print(str_file_email)
    with open('assest/email.txt','w+') as file:
            file.write(str(str_file_email))
    with open('assest/phone_num.txt','w+') as file:
        file.write(str(str_file_phone_num))
    print(str_file_phone_num)
    return str_file_phone_num

collection()