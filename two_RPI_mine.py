import paramiko

RPI_1 = paramiko.SSHClient()
RPI_2 = paramiko.SSHClient()

RPI_1.set_missing_host_key_policy(paramiko.AutoAddPolicy())
RPI_2.set_missing_host_key_policy(paramiko.AutoAddPolicy())
RPI_1.connect(hostname='localhost',username='pgb',port=5022,password='pgb')
RPI_2.connect(hostname='localhost',username='pgb',port=5023,password='pgb')

stdin,stdout,stderr=RPI_2.exec_command('python3 testMine.py ' + '4')
output = stdout.readlines()
for items in output:
    print("RPI_2:" + items)

stdin,stdout,stderr=RPI_1.exec_command('python3 testMine.py ' + '2')
output = stdout.readlines()
for items in output:
    print("RPI_1:" + items)

RPI_1.close()
RPI_2.close()
