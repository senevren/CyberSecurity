import requests
 
response = requests.get('https://replit.com/@evrensen/CuddlyThornyExtensions#main.py')
 
if(response.status_code == 200):
  response = requests.get('https://replit.com/@evrensen/CuddlyThornyExtensions#main.py/admin.php')
  print('Request success!')
 
  if(response.status_code == 200):
    print('Vulnerable site')
  else:
    print('Not a vulnerable site')
else:
  print('Request failure')
