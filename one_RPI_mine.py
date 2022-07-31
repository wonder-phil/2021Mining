import paramiko

RPI_1 = paramiko.SSHClient()

RPI_1.set_missing_host_key_policy(paramiko.AutoAddPolicy())
RPI_1.connect(hostname='localhost',username='pi',port=5022,password="raspberry")

stdin,stdout,stderr=RPI_1.exec_command('python3 testMine.py 5')

output = stdout.readlines()
for items in output:
    print("RPI_1:" + items)

error = stderr.readlines()
for items in error:
    print("error - RPI_1:" + items)

RPI_1.close()
