import os
import getpass
import time
import subprocess as sp

os.system('tput setaf 3')
print('\t\t\tWelcome to Menu Driven Program......!')
os.system('tput setaf 7')
print('\t\t\t--------------------------------------')

passwd = getpass.getpass('Enter the Password : ')
if passwd != 'linux':
        os.system('tput setaf 3')
        print('Invalid Password.....!')
        os.system('tput setaf 7')
        exit()
while True:
        os.system('clear')
        print('1.Show the date : ')
        print('2.Show the calender : ')
        print('3.Show ip address : ')
        print('4.Configuration Apache Web-Server : ')
        print('5.Launch New Container on the top of Docker :')
        print('6.AWS : ')
        print('7.Configure LVM : ')
        print('8.Extend Logical Volume : ')
        print('9.Exit')
        ch = input('Enter Your Choice =>')
        if int(ch) == 1:
                os.system('tput setaf 3')
                os.system('date')
                os.system('tput setaf 7')

        elif int(ch) == 2:
                os.system('tput setaf 4')
                os.system('cal')
                os.system('tput setaf 7')

        elif int(ch) == 3:
                os.system('ifconfig')
        elif int(ch) == 4:
                os.system('tput setaf 3')
                print('MENU OF WEB-SERVER')
                print('------------------')
                os.system('tput setaf 7')
                print('A.Download the HTTPD web-server : ')
                print('B.Start the web-service : ')
                print('C.Stop the web-service : ')
                op = input('Select the option : ')
                if op =='A':
                        os.system('yum install httpd -y')
                        os.system('tput setaf 2')
                        print('HTTPD Software Installed...! ')
                        os.system('tput setaf 7')
                elif op == 'B':
                        os.system('systemctl start httpd')
                        os.system('tput setaf 4')
                        print('HTTPD Service Start....! ')
                        os.system('tput setaf 7')
                elif op == 'C':
                        os.system('systemctl stop httpd')
                        os.system('tput setaf 5')
                        print('HTTPD Service Stop.....!')
                        os.system('tput setaf 7')
                else :
                        os.system('tput setaf 2')
                        print('Invalid input......!')
                        os.system('tput setaf 7')
        elif int(ch) == 5:
                os.system('tput setaf 4')
                print('MENU OF DOCKER')
                print('-------------')
                os.system('tput setaf 7')
                print('=>ubuntu:14.04')
                print('=>centos:7')
                print('=>centos:8')
                print('=>centos:latest')
                img = input('Enter Image Name : ')
                name = input('Enter container name : ')
                os.system('docker run -id --name {}  {}'.format(name , img))

        elif int(ch) == 6:

                '''print("Welcome to the Python Integration Program with AWS CLI")
                while True:
                        os.system('clear')
                        print("""
                        Press 0: For exit
                        Press 1: For downloading & installing AWS CLI V2
                        Press 2: For configuring AWS CLI V2
                        Press 3: For creating an AWS Key Pair
                        Press 4: For deleting an AWS Key Pair
                        Press 5: For creating a Security Group
                        Press 6: For deleting a Security Group
                        Press 7: Launch an EC2 instance""")
                        ch=int(input())

                        if ch==0:

                                        time.sleep(2)
                                        os.system("python3 automation.py")
                                        exit()
                        elif ch==1:
                                        install_aws_cli()
                        elif ch==2:
                                        configure_aws_cli()
                        elif ch==3:
                                        create_key_pair()
                        elif ch==4:
                                        del_key_pair()
                        elif ch==5:
                                        create_security_group()
                        elif ch==6:
                                        del_security_group()
                        elif ch==7:
                                        launch_ec2_instance()

                        input("Press Enter to continue")
                        #os.system("clear")'''
                def install_aws_cli():

                        # Downloading AWS CLI V2
                        print("Downloading aws cli v2...")
                        a,b=sp.getstatusoutput("curl 'https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip' -o 'awscliv2.zip'")
                        if a==0:
                                print("Successfully downloaded AWS CLI V2")
                        else:
                                print("Please Try again to download")

                        # Unziping the AWS CLI V2
                        sp.getoutput("yum install unzip -y")
                        sp.getoutput("unzip awscliv2.zip")

                        # Installing the AWS CLI V2
                        sp.getoutput("sudo ./aws/install")

                        print("Now AWS CLI V2 is successfully configured")

                def configure_aws_cli():
                        # Configuring aws cli in local system with IAM credentials
                        print("Enter the credentials for configuring aws cli\n")
                        os.system("aws configure")
                        print("Credentials successfully configured")

                def create_key_pair():
                        # Creating a new Key pair
                        key_name=input("Enter the name for key pair: ")
                        status,output=sp.getstatusoutput("aws ec2 create-key-pair --key-name {}".format(key_name))
                        if status==0:
                                print("Key-pair creation done successfully!!")
                        else:
                                print("Error: Either the key name is incorrect or aws cli not configred")
                                create_key_pair()

                def del_key_pair():
                        # Deleting an existing Key pair
                        key_name=input("Enter the name for key pair to be deleted: ")
                        status,output=sp.getstatusoutput("aws ec2 delete-key-pair --key-name {}".format(key_name))
                        if status==0:
                                print("Key-pair deletion done successfully!!")
                        else:
                                print("Error: Either the key name is incorrect or key is already deleted")
                                del_key_pair()

                def create_security_group():
                        # Creating a Security Group
                        gname=input("Enter the security group name: ")
                        des=input("Enter the description for the security group: ")
                        status,output=sp.getstatusoutput("aws ec2 create-security-group  --group-name {}  --description '{}'".format(gname,des))
                        if status==0:
                                print("Security group creation done successfully!!")
                        else:
                                print("Error: The field name are provided empty. Please try again! ")
                                create_security_group()

                def del_security_group():
                        # Deleting Security Group
                        gname=input("Enter the group name to be deleted: ")
                        status,output=sp.getstatusoutput("aws ec2 delete-security-group --group-name {}".format(gname))
                        if status==0:
                                print("Security group deletion done successfully!!")
                        else:
                                print("Error: The field name is provided empty. Please try again! ")
                                del_security_group()

                def launch_ec2_instance():
                        # Launching an EC2 instance
                        print("""Enter your choice:
                        Press 1: For Amazon Linux AMI
                        Press 2: For Red Hat Linux AMI
                        Press 3: For Ubuntu Linux AMI""")
                        ch=int(input())
                        if ch==1:
                                ami="ami-0e306788ff2473ccb"
                        elif ch==2:
                                ami="ami-052c08d70def0ac62"
                        elif ch==3:
                                ami="ami-0cda377a1b884a1bc"

                        # Number of instances
                        count=int(input("Enter the number of instances you want to launch"))
                        print("""Press 1: To create a new key-pair
                        Press 2: Use the existing key-pair""")
                        ch=int(input())
                        if ch==1:
                                create_key_pair()
                                key=input("Enter the key name")
                        elif ch==2:
                                key=input("Enter the key name")
                                os.system("aws ec2 run-instances --image-id {} --instance-type t2.micro --count {} --key-name {}".format(ami,count,key))
                                print("Launched Instance successfully!!")

                print("Welcome to the Python Integration Program with AWS CLI")
                while True:
                        os.system('clear')
                        print("""
                        Press 0: For exit
                        Press 1: For downloading & installing AWS CLI V2
                        Press 2: For configuring AWS CLI V2
                        Press 3: For creating an AWS Key Pair
                        Press 4: For deleting an AWS Key Pair
                        Press 5: For creating a Security Group
                        Press 6: For deleting a Security Group
                        Press 7: Launch an EC2 instance""")
                        ch=int(input())

                        if ch==0:

                                        time.sleep(2)
                                        os.system("python3 automation.py")
                                        exit()
                        elif ch==1:
                                        install_aws_cli()
                        elif ch==2:
                                        configure_aws_cli()
                        elif ch==3:
                                        create_key_pair()
                        elif ch==4:
                                        del_key_pair()
                        elif ch==5:
                                        create_security_group()
                        elif ch==6:
                                        del_security_group()
                        elif ch==7:
                                        launch_ec2_instance()

                        input("Press Enter to continue")
                        #os.system("clear")

        elif int(ch) == 7:
                os.system('tput setaf 4')
                print('Create Physical Volume : ')
                hd1 = input('Enter hard disk 1 : ')
                os.system('tput setaf 7')
                os.system('pvcreate {}'.format(hd1))
                os.system('tput setaf 4')
                hd2 = input('Enter hard disk 2 : ')
                os.system('tput setaf 7')
                os.system('pvcreate {}'.format(hd2))
                os.system('tput setaf 4')
                print('Show the physical volume :')
                pv1 = input('Enter First Hard disk Name : ')
                os.system('tput setaf 7')
                os.system('pvdisplay {}'.format(pv1))
                os.system('tput setaf 4')
                pv2 = input('Enter Second Hard disk Name : ')
                os.system('tput setaf 7')
                os.system('pvdisplay {}'.format(pv2))
                os.system('tput setaf 4')
                print('Create Volume Group : ')
                vg_name = input('Enter Volume Group Name : ')
                os.system('tput setaf 7')
                os.system('vgcreate {} {} {}'.format(vg_name , pv1 , pv2))
                os.system('tput setaf 4')
                print('Show the Volume Group : ')
                os.system('tput setaf 7')
                os.system('vgdisplay {}'.format(vg_name))
                os.system('tput setaf 4')
                print('Create Logical Volume : ')
                lv1 = input('Enter Logical Volume Name : ')
                size = input('Enter size of the LV : ')
                size = int(size)
                os.system('tput setaf 7')
                os.system('lvcreate --size {}G --name {} {}'.format(size , lv1 , vg_name))
                os.system('tput setaf 4')
                print('Show the Logical Volume : ')
                os.system('tput setaf 7')
                os.system('lvdisplay {}/{}'.format(vg_name , lv1))
                os.system('tput setaf 4')
                print('Format the logical volume : ')
                os.system('tput setaf 7')
                os.system('mkfs.ext4 /dev/{}/{}'.format(vg_name , lv1))
                os.system('tput setaf 4')
                print('Mount LV to any folder : ')
                folder = input('Enter folder Name : ')
                os.system('tput setaf 7')
                os.system('mkdir /{}'.format(folder))
                os.system('mount /dev/{}/{} /{}'.format(vg_name , lv1 , folder))
                os.system('df -h')

        elif int(ch) == 8:
                resize = input('How many size You want to extend : ')
                resize = int(resize)
                vg_name = input('Enter volume group name which you want extend : ')
                lv1 = input('Enter logical volume name : ')
                os.system('lvextend --size +{}G /dev/{}/{}'.format(resize , vg_name , lv1))
                os.system('resize2fs /dev/{}/{}'.format(vg_name , lv1))
                os.system('df -h')
        elif int(ch) == 9:
                exit()
                os.system('tput setaf 4')
                os.system('tput setaf 7')

        else:
                os.system('tput setaf 4')
                print('Invalid Input.....!')
                os.system('tput setaf 7')
        input('Please Enter to Continued.......!')

