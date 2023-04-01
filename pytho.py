from twilio.rest import Client 
 
account_sid = 'AC84b20c240a5fc9b1c1a974c1418b4c52' 
auth_token = '06b915b8279de0dbfc8e3d6a8fad9959' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create(  
                              messaging_service_sid='MG8b7942c4f91845611e26b667bfd3ceba', 
                              body='sdasd',      
                              to='+91630546' 
                          ) 
 
print(message.sid)