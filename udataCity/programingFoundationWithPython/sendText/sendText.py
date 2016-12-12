'''
Created on 2016. 12. 11.

@author: shmoc
'''
from twilio.rest import TwilioRestClient

account_sid = "{{ account_sid }}" # Your Account SID from www.twilio.com/console
auth_token  = "{{ auth_token }}"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="Hello from Python",
    to="+8201088401168",    # Replace with your phone number
    from_="+12345678901") # Replace with your Twilio number

print(message.sid)