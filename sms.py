from twilio.rest import Client 
 
account_sid = 'AC84b20c240a5fc9b1c1a974c1418b4c52' 
auth_token = 'f309a0838548227a48b2e1ed75333353' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create(  
                              messaging_service_sid='MG8b7942c4f91845611e26b667bfd3ceba', 
                              body='Hello Dom',      
                              to='+916305461499' 
                          ) 
 
print(message.sid)