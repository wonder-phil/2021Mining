import paramiko

class RPI_1_Mine():
    def __init__(self,difficulty):
        RPI_1 = paramiko.SSHClient()

        RPI_1.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        RPI_1.connect(hostname='localhost',username='pgb',port=5022,password="pgb")
        stdin,stdout,stder=RPI_1.exec_command('python3 testMine.py ' + str(difficulty))
        output = stdout.readlines()
        for items in output:
            print("RPI_1:" + items)

        RPI_1.close()


rpi_1 = RPI_1_Mine(3)
