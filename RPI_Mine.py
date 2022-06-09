import paramiko

class RPI_Mine():
    def __init__(self,myPort,name,difficulty):
        RPI = paramiko.SSHClient()

        RPI.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        RPI.connect(hostname='localhost',username='pi',port=int(myPort),password="raspberry")
        stdin,stdout,stderr=RPI.exec_command('python3 testMine.py '+ str(difficulty))
        output = stdout.readlines()
        for items in output:
            print(name + ": " + items)

        error = stderr.readlines()
        for items in error:
            print("error - " + name + ": " + items)

        RPI.close()
