import pickle

model=pickle.load(open("spam.pkl","rb"))
cv=pickle.load(open("vectorizer.pkl","rb"))


#msg_file = open('cache_fileMG3O7oMJixl3CPZEN4D5.txt', 'r')
#msg=msg_file.read()
#msg_file.close()
import imaplib
import email
# Connect to inbox
imap_server = imaplib.IMAP4_SSL(host='imap.gmail.com')
imap_server.login('quan.lam2001@hcmut.edu.vn','quan697501')
imap_server.select()  # Default is `INBOX`


_, selected_mails = imap_server.search(None, ' (FROM "hello@hello.scribd.com")') # gmail account required to look at
for num in selected_mails[0].split():
    _, data = imap_server.fetch(num , '(RFC822)')
    _, bytes_data = data[0]

    #convert the byte data to message
    email_message = email.message_from_bytes(bytes_data)
    print("\n===========================================")

    #access data
   # print("Subject: ",email_message["subject"])
   # print("To:", email_message["to"])
   # print("From: ",email_message["from"])
    # print("Date: ",email_message["date"])
    for part in email_message.walk():
        if part.get_content_type()=="text/plain" or part.get_content_type()=="text/html":
            message = part.get_payload(decode=True)
        
           # print("Message: \n", message.decode())
           # print("==========================================\n")
            break
dt = [message.decode()]
vect=cv.transform(dt).toarray()
prediction=model.predict(vect)
#result=prediction[1]
if prediction==1:
      print('This is a spam mail')
else:
      print('This is a ham mail')