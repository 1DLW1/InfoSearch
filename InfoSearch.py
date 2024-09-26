#!/usr/bin/env python3
import subprocess, os, platform, time, requests, socket

#internetconection
def internetconection():
    try:
        subprocess.check_output(["ping","-c","1","1.1.1.1"], stderr=subprocess.STDOUT, universal_newlines=True)
        return True
    except subprocess.CalledProcessError:
        return False

#install modules
if internetconection():
    lista = ('ping3', 'keyboard', 'pyautogui', 'colorama')
    for i in lista:
        os.system('pip install ' + i)
    #upgrade modules
    listaupgrade = ('subprocess.run', 'os-sys', 'requests', 'sockets', 'ping3', 'keyboard', 'pyautogui', 'colorama')
    modulesupdate=input('\n\n[+] Do you want to upgrade the python modules? [y/n] > ')
    if modulesupdate == 'yes' or modulesupdate == 'y' or modulesupdate == '':
        for i in listaupgrade:
            os.system('pip install --upgrade pip')
            os.system('pip install --upgrade ' + i)
            print()
    elif modulesupdate == 'no' or modulesupdate == 'n':
        print()
    else:
        print()
else:
    print("X NO INTERNET CONECTION X")
    time.sleep(2)
try:
    import ping3, keyboard, pyautogui, colorama
    from ping3 import ping
except:
    print('TRY TO RESTART THE SCRIPT OR INSTALL MISSING MODULES BY YOURSELF > subprocess, os, platform, time, ping3, keyboard, pyautogui, colorama')
    time.sleep(4)

#Colours
from colorama import Fore
red=Fore.LIGHTRED_EX
green=Fore.LIGHTGREEN_EX
blue=Fore.LIGHTBLUE_EX
Purple=Fore.LIGHTMAGENTA_EX
white=Fore.LIGHTWHITE_EX

#Clean screen
def clean():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')
clean()

#directoryfind
def search_directory(directory_name, start_path='/'):
    found_paths = []  # Initialize a list to hold found paths
    for current_path, directories, files in os.walk(start_path):
        if directory_name in directories:
            # If found, add the full path to the list
            found_paths.append(os.path.join(current_path, directory_name))
            # Optionally, remove the found directory from the directories list
            # to prevent re-visiting it in the same `os.walk()` call
            directories.remove(directory_name)
    return found_paths  # Return the list of found paths

print(blue + '~' + '\033[4m' + Purple + 'INFOSEARCH' +  '\033[0m' + blue + '~\n\n')
time.sleep(3)
clean()

try:
    while True:

        #directory route
        if platform.system() == 'Windows':
            pwd1 = subprocess.Popen('cd', stdout=subprocess.PIPE, shell=True)
            (out, err) = pwd1.communicate()
            out1 = str(out[3:-2]).replace("'",'')
            out2 = str(out1[1:]).replace('\\', "/")
            out3 = str(out2).replace('//', '/')
            out3 = str(out3)
            pathD = out3
        else:
            pwd1 = subprocess.Popen('cd', stdout=subprocess.PIPE, shell=True)
            (out, err) = pwd1.communicate()
            out1 = str(out[3:-2]).replace("'",'')
            out2 = str(out1[1:]).replace('\\', "/")
            out3 = str(out2).replace('//', '/')
            pathC = subprocess.Popen("pwd", stdout=subprocess.PIPE, shell=True)
            (out, err) = pathC.communicate()
            pathCout = str(out).replace("b'", '')
            pathCout1 = str(pathCout).replace("n'", '')
            pathCout2 = str(pathCout1[:-1])
            pathD = pathCout2

        #input
        print(blue + '~' + '\033[4m' + Purple + 'INFOSEARCH' + '\033[0m' + blue + '~')
        ask=input(Purple + '$' + blue + pathD + red + '\n>' + green)
        if ask == '':
            print('')
            continue

        #clean
        if ask == 'clean' or ask == 'cls' or ask == 'clear':
            clean()
            
        #Help
        help_dict = {
            'clean':    'Clean the screen.',
            'shell':    'Invoke a shell console.(Also you can add "shell" at the beginning for use a command console)',
            'ping':     'Ping a target for check if is up.\n' + red +  ' '*18 + 'USAGE>' +  blue + ' ping -target-',
            'whois':    'Search information about an address with whois tools.\n'  + red + ' '*18 + 'USAGE>' +  blue + ' whois -target-',
            'webscan':  'Scan for web services, existing directories, subdomains and more.\n' + red + ' '*18 +  'USAGE>' +  blue + ' webscan -target-',
            'nmap':     'Scan for active services in open ports and get information of the target.\n'  + red + ' '*18 + 'USAGE>' +  blue + ' nmap ' + green + '-target-' + white + ' <option>' + green + ' |udp|tcp|fullscan|' + white + ' <velocity> ' + green + '|fast|normal|slow|',

                        }
        
        help_message = ""
        for command, description in help_dict.items():
            command_string = f"{red}\n-{green}{command.ljust(15, ' ')} {red}-{green}{description}\n"
            help_message += command_string
                        
        help_call = {'help', '-help', '--help', '-h', 'ayuda'}
        for i in help_call:
            helpcommand = i
            if ask == helpcommand:
                print('\n' + Purple + '\033[4m' + blue + 'Commands' + Purple + '\033[0m' + '\n' + help_message)
        
        #ping for check if devices are up
        def check_host(host):
            try:
                response = ping(host)
                if response:
                    print(blue + '\n[' + red + '+' + blue + '] ' + green + str(host) + red + ' UP')
                else:
                    print(blue + '\n[' + red + '-' + blue + '] ' + green + str(host) + red + ' DOWN')
            except:
                pass
        if 'ping' in ask[0:4]:
            ip=str(ask[5:])
            check_host(ip)
        
        #whois
        if 'whois' in ask:
            print(Purple + '\n-' + red + 'WHOIS\n')
            targetwhois= ask[6:]
            subprocess.run('whois ' + str(targetwhois), shell=True)


        #nmap for service detection
        if 'nmap' in ask:
            print(Purple + '\n-' + red + 'NMAP\n' + green)
            targetnmap= ask[5:]

            #tcp
            if 'fast' in ask and 'tcp' in ask:
                targetnmap=targetnmap.replace('fast', '').replace('tcp', '')
                subprocess.run('nmap -sSCV -n -Pn --open -p- -v ' + str(targetnmap) + ' -oN nmap-scan -T5', shell=True)
            elif 'slow' in ask and 'tcp' in ask:
                targetnmap=targetnmap.replace('slow', '').replace('tcp', '')
                subprocess.run('nmap -sSCV -n -Pn --open -p- -v ' + str(targetnmap) + ' -oN nmap-scan -T2', shell=True)
            elif 'normal' in ask and 'tcp' in ask:
                targetnmap=targetnmap.replace('normal', '').replace('tcp', '')
                subprocess.run('nmap -sSCV -n -Pn --open -p- -v ' + str(targetnmap) + ' -oN nmap-scan', shell=True)
            #udp
            elif 'fast' in ask and 'udp' in ask:
                targetnmap=targetnmap.replace('fast', '').replace('udp', '')
                subprocess.run('nmap -sUCV -n -Pn --open -p- -v ' + str(targetnmap) + ' -oN nmap-scan -T5', shell=True)
            elif 'slow' in ask and 'udp' in ask:
                targetnmap=targetnmap.replace('slow', '').replace('udp', '')
                subprocess.run('nmap -sUCV -n -Pn --open -p- -v ' + str(targetnmap) + ' -oN nmap-scan -T2', shell=True)
            elif 'normal' in ask and 'udp' in ask:
                targetnmap=targetnmap.replace('normal', '').replace('udp', '')
                subprocess.run('nmap -sUCV -n -Pn --open -p- -v ' + str(targetnmap) + ' -oN nmap-scan', shell=True)
            #full
            elif 'fast' in ask and 'fullscan' in ask:
                targetnmap=targetnmap.replace('fast', '').replace('fullscan', '')
                subprocess.run('nmap -sSCV -sU -n -Pn --open -p- -v ' + str(targetnmap) + ' -oN nmap-scan -T5', shell=True)
            elif 'slow' in ask and 'fullscan' in ask:
                targetnmap=targetnmap.replace('slow', '').replace('fullscan', '')
                subprocess.run('nmap -sUCV -n -Pn --open -p- -v ' + str(targetnmap) + ' -oN nmap-scan -T2', shell=True)
            elif 'normal' in ask and 'fullscan' in ask:
                targetnmap=targetnmap.replace('normal', '').replace('fullscan', '')
                subprocess.run('nmap -sUCV -n -Pn --open -p- -v ' + str(targetnmap) + ' -oN nmap-scan', shell=True)
            else:
                print('USAGE>' +  blue + ' nmap ' + green + '-target-' + white + ' <option>' + green + ' |udp|tcp|fullscan|' + white + ' <velocity> ' + green + '|fast|normal|slow|')

        #webScan
        if 'webscan' in ask and len(ask) == 7:
            print(red + 'Add a target for scan: ' + green + 'USAGE>' +  blue + ' webscan ' + red + '-target-')
        
        elif 'webscan' in ask and len(ask) > 8:
            try:

                targetweb = ask[8:]

                if 'http' in ask or 'https' in ask:

                    if targetweb != '':
                        print(targetweb)
            
                    #hostname add
                    hostname=input(Purple + '\n-' + blue + 'Does the target has any host name? ' + green + '[y/n] ' + red + '(if you already introduced after the webscan command press no.)\n' + Purple + '>')
                    if hostname == 'y' or hostname == 'Yes' or hostname == '' or hostname == 'yes':
                        providehost=input(blue + '\nProvide it' + Purple + '>')
                    else:
                        providehost = ''

                    #whatweb for web services and plugins
                    print(Purple + '\n-' + red + 'WHATWEB\n')
                    subprocess.run('whatweb ' + str(targetweb),shell=True)
                    time.sleep(1)

                    #SecLists dictionary (must be installed)
                    name_to_search = 'SecLists'  # Change this to the name of the directory you want to search for
                    found_paths = search_directory(name_to_search)
                    if found_paths:
                        for path in found_paths:
                            path = path
                    else:
                        print(red + 'Download Seclists list from https://github.com/danielmiessler/SecLists')
                        downloadList = input(Purple + '\n- ' + blue + 'Do you want to download now? [y/n]\n' + Purple + '>')
                        if downloadList == 'y' or downloadList == 'Yes' or downloadList == '' or downloadList == 'yes':
                            try:
                                subprocess.run('git clone https://github.com/danielmiessler/SecLists',shell=True)
                                found_paths = search_directory(name_to_search)
                                if found_paths:
                                    for path in found_paths:
                                       path = path
                            except:
                                print(red + 'Download Seclists list from https://github.com/danielmiessler/SecLists and rerun.')

                    print(green + '\nSecLists directory in ' + Purple + '> ' + blue + str(path))

                    #feroxbuster for directory listing
                    print(Purple + '\n-' + red + 'FEROXBUSTER\n')
                    webdirectories=input(Purple + '-' + blue + 'Do you want to search web directories? '  + green + '[y/n]\n' + Purple + '>')
                    if webdirectories == 'y' or webdirectories == 'Yes' or webdirectories == '' or webdirectories == 'yes':
                        if providehost != '':
                            if 'http' in providehost:
                                addhttp=providehost
                            elif 'https' in providehost:
                                addhttp=providehost
                            else:
                                addhttp=input(Purple + '-' + green + 'Add ' + red + 'http://' + blue + ' or' + red + ' https://' + blue + ' to the web target.' + green + 'Example> http://hostname.com' + Purple + '\n>')
                            subprocess.run('feroxbuster -u ' + addhttp + ' -w ' + path + '/Discovery/Web-Content/raft-medium-directories-lowercase.txt',shell=True)
                            time.sleep(1)
                                               
                        elif providehost == '':
                            subprocess.run('feroxbuster -u ' + targetweb + ' -w ' + path + '/Discovery/Web-Content/raft-medium-directories-lowercase.txt',shell=True)
                            time.sleep(1)

                    #ffuf for subdomain
                    print()
                    print(Purple + '\n-' + red + 'FFUF\n')
                    subdomainask=input(Purple + '-' + blue + 'Do you want to search for subdomains? ' + green + '[y/n]\n' + Purple + '>')
                    if subdomainask == 'y' or subdomainask == 'Yes' or subdomainask == '' or subdomainask == 'yes':
                        
                        if providehost != '':
                            if 'http' in providehost:
                                providehost=providehost.replace('http://','')
                            elif 'https' in providehost:
                                providehost=providehost.replace('https://','')
                            subprocess.run('ffuf -u ' + targetweb + ' -H "Host: FUZZ.' + providehost + '" -w ' + path + '/Discovery/DNS/subdomains-top1million-20000.txt  -H "Content-Type: application/x-www-form-urlencoded" -c -mc 200',shell=True)
                            time.sleep(1)

                        elif providehost == '':
                            print()
                            askffuf=input(Purple + '-' + blue + 'For a better results try to provide the ip addres of the target and the host name of the web.\n' +  Purple + '-' + blue + 'Do you want to provide the ip and the host name? ' + green + ' press > [y/yes]' + blue + ' or continue with the target already provided ' + green + 'press > [continue]\n' + green + '>')
                            if 'yes' in askffuf or 'y' in askffuf or '' in askffuf:
                                print(Purple + '\nRemember to add ' + red + 'http:// ' + Purple + 'or' + red + ' https://' + Purple + ' in the ip address.' + blue + ' Example> http://192.168.1.1')
                                ipaddressffuf=input(Purple + '-' + blue + 'Introduce the ip address> ' + green)
                                hostnameffuf=input(Purple + '-' + blue + 'Introduce the hostname> ' + green)
                                if 'http' in hostnameffuf:
                                    hostnameffuf=hostnameffuf.replace('http://','')
                                elif 'https' in providehost:
                                    hostnameffuf=hostnameffuf.replace('https://','')
                                print()
                                if 'http' in ipaddressffuf or 'https' in ipaddressffuf:
                                    subprocess.run('ffuf -u ' + ipaddressffuf + ' -H "Host: FUZZ.' + hostnameffuf + '" -w ' + path + '/Discovery/DNS/subdomains-top1million-20000.txt  -H "Content-Type: application/x-www-form-urlencoded" -c -mc 200',shell=True)
                                    time.sleep(1)
                                else:
                                    print(blue + 'Add ' + red + 'http://' + blue + ' or' + red + ' https://' + blue + ' to the ip address.')

                            else:
                                subprocess.run('ffuf -u FUZZ.' + targetweb + ' -w ' + path + '/Discovery/DNS/subdomains-top1million-20000.txt  -H "Content-Type: application/x-www-form-urlencoded" -c -mc 200',shell=True)
                                time.sleep(1)
                else:
                    print(blue + 'Add ' + red + 'http://' + blue + ' or' + red + ' https://' + blue + ' to the web target.')
   
            except Exception as error:
                print(error)
        
        #command console usage
        commandshell = 'shell' + ' '
        if ask[0:6] == commandshell:
            try:
                subprocess.run(ask[6:])
            except:
                pass
        else:
            pass

        
        #full console control
        if ask=='shell':
            print('\n' + red + '-'*50 + red + "\n- " + blue + 'Mode console ' + green + 'ON' + red + ' '*32 + '-' + red + "\n- " + blue + "Command" + green + ' off ' + blue + 'for return to InfoSearch.' + red  + ' '*10 + '-' + '\n' + '-'*50 + '\n')
            
            while True:
                #directory route
                if platform.system() == 'Windows':
                    pwd1 = subprocess.Popen('cd', stdout=subprocess.PIPE, shell=True)
                    (out, err) = pwd1.communicate()
                    out1 = str(out[3:-2]).replace("'",'')
                    out2 = str(out1[1:]).replace('\\', "/")
                    out3 = str(out2).replace('//', '/')
                    out3 = str(out3)
                    pathD = out3
                elif platform.system() == 'Linux':
                    pwd1 = subprocess.Popen('cd', stdout=subprocess.PIPE, shell=True)
                    (out, err) = pwd1.communicate()
                    out1 = str(out[3:-2]).replace("'",'')
                    out2 = str(out1[1:]).replace('\\', "/")
                    out3 = str(out2).replace('//', '/')
                    pathC = subprocess.Popen("pwd", stdout=subprocess.PIPE, shell=True)
                    (out, err) = pathC.communicate()
                    pathCout = str(out).replace("b'", '')
                    pathCout1 = str(pathCout).replace("n'", '')
                    pathCout2 = str(pathCout1[:-1])
                    pathD = pathCout2

                #console set
                print(blue + '~' + '\033[4m' + Purple + 'CONSOLE MODE' + '\033[0m' + blue + '~')
                command=input(Purple + '$' + blue + pathD + red + '\n>' + green)
                if command == 'off':
                    print(Fore.LIGHTBLUE_EX + '\nMode console ' + Fore.LIGHTRED_EX + 'OFF')
                    break
                elif command == '':
                    print('')
                    continue

                #cd
                elif 'cd ' in command:
                    try:
                        os.chdir(command[3:])
                    except OSError:
                        continue
                else:
                    if platform.system() == 'Windows':
                        subprocess.run('powershell.exe ' + str(command), shell=True)
                        continue
                    elif platform.system() == 'Linux':
                        subprocess.run(str(command), shell=True)
                        continue
        else:
            print('')
        
except Exception as error:
    print(error)
