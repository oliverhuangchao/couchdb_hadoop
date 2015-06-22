import os

for i in range (2,6):
	os.system("echo "+ str(i))
	os.system("curl -X POST http://localhost:5984/poquotes  -H 'Content-Type: application/json' -d @q"+str(i)+".json")