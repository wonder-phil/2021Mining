import paramiko

class RPI_1_Mine():
    def __init__(self,difficulty):
        RPI_1 = paramiko.SSHClient()

        RPI_1.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        RPI_1.connect(hostname='localhost',username='pi',port=5023,password="raspberry")
        stdin,stdout,stder=RPI_1.exec_command('python3 testMine.py ' + str(difficulty))
        print(stder.readlines())
        output = stdout.readlines()
        for items in output:
            print("RPI_2:" + items)

        error = stderr.readlines()
        for items in error:
            print("error - RPI_2:" + items)

        RPI_1.close()


rpi_1 = RPI_1_Mine(3)        
        
