import paramiko

RPI_1 = paramiko.SSHClient()

RPI_1.set_missing_host_key_policy(paramiko.AutoAddPolicy())
RPI_1.connect(hostname='localhost',username='pi',port=5022)
    
stdout=RPI_1.exec_command('python3 testMine.py')
output = stdout.readlines()
for items in output:
    print("RPI_1:" + items)

RPI_1.close()
