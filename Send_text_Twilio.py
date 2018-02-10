from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AYour Account SID from twilio.com/console"

# Your Auth Token from twilio.com/console
auth_token  = "Your Auth Token from twilio.com/console"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="Reciever Phone Number", 
    from_="Your Phone Number from twilio.com/consol",
    body="Hello from Python34!")

print(message.sid)
    
