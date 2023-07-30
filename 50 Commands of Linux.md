# 50 Commands of Linux
**These comprehensive notes on 50 Commands of Linux offer numerous benefits that can significantly enhnace my Knowledge,Improved efficiency,Ehance productivity,Deeper system understanding**
***versatility,career,Career Advancement,Troubleshooting skills,Community Engagement***

**1. ls command**

 *It is **designed to list the names and features of files and directories**.*

 *It can be used for a single file or as many as all files and folders in a selected set of directories.*

````syntax
ls [options] [file… | directory …]
````

![touch ls -al command](https://github.com/saeed402/int-2023/assets/139351697/01d37f68-89b9-4cdd-ac65-86ab92e57b2e)


**2. pwd command**

*The pwd command is used to display the location of the current working directory.*

````syntax
pwd  

````

![Pwd command](https://github.com/saeed402/int-2023/assets/139351697/7717f4b0-8c13-4af8-bfda-a20fb9692de8)


**3. mkdir Command**

*The mkdir command is used to create a new directory under any directory.*

````syntax
mkdir <directory name> 
````

![mkdir command](https://github.com/saeed402/int-2023/assets/139351697/7a05e652-008a-4fd0-8098-e16d97d64f99)


**4. rmdir command**

*The rmdir command is used to delete a directory.*

````syntax
rmdir <directory name>
````

![rmdir 1](https://github.com/saeed402/int-2023/assets/139351697/fa37e968-74f7-4a1b-ad7c-0e2f939f9ec9)


*The rmdir command **removes the directory, specified by the Directory parameter, from the system**. The directory must be empty before you can remove it, and you must have write permission in its parent directory.*

![rmdir 2](https://github.com/saeed402/int-2023/assets/139351697/da1865fc-084e-41ea-9fe1-5a8447656e0b)


**5. cd command**

*The cd command is used to change the current directory. It is used **to move efficiently from the current working directory to different directories in our System**.*

````syntax
cd <directory name>  
````

![cd command](https://github.com/saeed402/int-2023/assets/139351697/10139686-b036-486f-a728-68a201d4412e)


**6. touch command**

*The touch command is used to create empty files. We can create multiple empty files by executing it once.  And modify the file timestamps (file access time, last date, or modification).*

````syntax
touch <file name>  
touch <file1>  <file2> ....  
````

![touch ls -al command](https://github.com/saeed402/int-2023/assets/139351697/28a5c8df-e9bc-4c60-acea-41c666ebc2b8)


**7. cat command**

*The cat command is a multi-purpose utility in the Linux system.*

*It can be used to create a file, display content of the file, copy the content of one file to another file, and more.*

````syntax
cat [OPTION]... [FILE]..

To create a file, execute it as follows:

cat > <file name>  
// Enter file content  
````
![cat command](https://github.com/saeed402/int-2023/assets/139351697/a2e70227-0f51-4fd8-9a8a-479115123b10)


**8. rm command**

*The rm command is used to remove a file.*

````syntax
rm <file name>
````

![rmdir 2](https://github.com/saeed402/int-2023/assets/139351697/b093973d-89b6-4fb5-bf32-e083e13a02ae)


**9. cp command**

*The cp command is used to copy a file or directory.*

````syntax
cp <existing file name> <new file name> 
````

![cp 1](https://github.com/saeed402/int-2023/assets/139351697/09975d90-fb2c-43ac-beeb-5dea02cdb363)
![cp 2](https://github.com/saeed402/int-2023/assets/139351697/93ce8503-435f-4e3a-957e-9b870d7e2acf)


**10. mv command**

*The mv command is used to move a file or a directory form one location to another location.*

````syntax
mv <file name> <directory path> 
````

![mv](https://github.com/saeed402/int-2023/assets/139351697/a8878f98-4a69-41f7-a70a-ef04cc21ba0f)


**11. head command**

*The head command is used to display the content of a file. It displays the first 10 lines of a file.*

````syntax
head <file name>  
````

![head command](https://github.com/saeed402/int-2023/assets/139351697/392c0ce4-df5a-4de1-8487-da9a36dae817)


**12. tail command**

*The tail command is similar to the head command.*

*The difference between both commands is that it displays the last ten lines of the file content.*

*It is useful for reading the error message.*

````syntax
tail <file name>  

````

![tail command](https://github.com/saeed402/int-2023/assets/139351697/07ed1f55-77cc-4ca5-91d4-f768414cccd8)


**13. tac command**

*The tac command is the reverse of cat command, as its name specified.*

*It displays the file content in reverse order (from the last line).*

````syntax
tac <file name>  
````

![tac command](https://github.com/saeed402/int-2023/assets/139351697/b3546bed-5c9c-41d6-9dce-5681223d01dd)


**13. su command**

*The su command provides administrative access to another user.*

*In other words, it allows access of the Linux shell to another user.*

````syntax
su <user name>  
````

![su 1](https://github.com/saeed402/int-2023/assets/139351697/d1f8b6f2-bc13-47ae-91de-beff0d937e39)


**14. cat command**

*The cat command is also used as a filter. To filter a file, it is used inside pipes.*

````syntax
cat <fileName> | cat or tac | cat or tac |. . . 
````

![cat filter](https://github.com/saeed402/int-2023/assets/139351697/3d247837-f3ff-4af6-9dd4-d44065a2f563)


**15. tr command**

*The tr command is used to translate the file content like from lower case to upper case.*

````syntax
command | tr <'old'> <'new'>  
````



**16. uniq command**

*The uniq command is used to form a sorted list in which every word will occur only once.*

````syntax
command <fileName> | uniq  
````

**17. wc command**

*The wc command is used to count the lines, words, and characters in a file.*

````syntax
wc <file name>  
````

**18. od command**

*The od command is used to display the content of a file in different s, such as hexadecimal, octal, and ASCII characters.*

````syntax
od -b <fileName>      // Octal format  
od -t x1 <fileName>   // Hexa decimal format  
od -c <fileName>     // ASCII character format  
````

**19. sort command**

*The sort command is used to sort files in alphabetical order.*

````syntax
sort <file name>  
````

**20. gzip command**

*The gzip command is used to truncate the file size.*

 *It is a compressing tool.*

*It replaces the original file by the compressed file having '.gz' extension.*

````syntax
gzip <file1> <file2> <file3>...  
````

**21. gunzip**

*The gunzip command is used to decompress a file.*

*It is a reverse operation of gzip command.*

````syntax
gunzip <file1> <file2> <file3>. .  
````

**22. find command**

*The find command is used to find a particular file within a directory.* 

*It also supports various options to find a file such as byname, by type, by date, and more.*

*The following symbols are used after the find command:*

(.) : For current directory name

(/) : For root

````syntax
find . -name "*.pdf"  
````
![find command](https://github.com/saeed402/int-2023/assets/139351697/27ad21a4-49a0-40c3-8915-32ac2567f1bd)


**23. locate command **

*The locate command is used to search a file by file name.* 

*It is quite similar to find command; the difference is that it is a background process.* 

*It searches the file in the database, whereas the find command searches in the file system.* 

*It is faster than the find command. To find the file with the locates command, keep your database updated.*

`````syntax
locate <file name>  
`````

![locate command](https://github.com/saeed402/int-2023/assets/139351697/b149bc12-1d5b-4fbf-ae59-596040ba9da2)


**24. date command**

*The date command is used to display date, time, time zone, and more.*

````syntax
date 
````

![Date command](https://github.com/saeed402/int-2023/assets/139351697/37f3ce1e-43d5-4aae-b1b1-d6ff807b3440)


**25. cal command**

*The cal command is used to display the current month's calendar with the current date highlighted.*

````syntax
cal<
````

![cal command](https://github.com/saeed402/int-2023/assets/139351697/c8cd6654-f58d-4308-9f03-aa6a9f265feb)


**26. sleep command**

*The sleep command is used to hold the terminal by the specified amount of time. By default, it takes time in seconds.*

````syntax
sleep <time>  
````

**27. zcat command**

*The zcat command is used to display the compressed files.*

````syntax
zcat <file name>  
````

**28. df command**

*The df command is used to display the disk space used in the file system.* 

*It displays the output as in the number of used blocks, available blocks, and the mounted directory.*

````syntax
df
````
![df command](https://github.com/saeed402/int-2023/assets/139351697/600e2159-a784-4ebd-8db8-f3fe0c43afe5)


**29. mount command**

*The mount command is used to connect an external device file system to the system's file system.*

````syntax
mount -t type <device> <directory>  
````

**30. exit command**

*Linux  exit command is used to exit from the current shell.* 

*It takes a parameter as a number and exits the shell with a return of status number.*

````syntax
exit 
````

**31. clear**

*Linux **clear** command is used to clear the terminal screen.*

````syntax 
clear 
````

![clear command](https://github.com/saeed402/int-2023/assets/139351697/3651ac66-229f-4a2c-b428-9b226899527c)


**32. ip command**

*Linux ip command is an updated version of the ipconfig command.*

*It is used to assign an IP address, initialize an interface, disable an interface.*

````syntax
ip a or ip addr  
````

![ip command](https://github.com/saeed402/int-2023/assets/139351697/b54ef421-a1bc-4fa1-b6a4-b057c612983e)


**33. mail commmand **

*The mail command is used to send emails from the command line.*

````syntax
mail -s "Subject" <recipient address>  
````

**34. ping command**

*The ping command is used to check the connectivity between two nodes, that is whether the server is connected.* 

*It is a short form of "Packet Internet Groper".*

````syntax
ping <destination>  
````

![ping command](https://github.com/saeed402/int-2023/assets/139351697/c80c6d5a-fbd0-4772-8e28-93bf4d31914e)


**35. host command**

*The host command is used to display the IP address for a given domain name and vice versa.*

*It performs the DNS lookups for the DNS Query.*

````syntax
host <domain name> or <ip address>  
````

**36. sed command**

*The sed command is also known as **stream editor**.*

*It is used to edit files using a regular expression.*

*It does not permanently edit files; instead, the edited content remains only on display. It does not affect the actual file.*

````syntax
command | sed 's/<oldWord>/<newWord>/'  
````

**37. uname and whoami**

*uname and whoami commands allow you to know basic information which comes really handy when you work on multiple systems.*

````syntax
 uname -a
````

![uname and whoami command](https://github.com/saeed402/int-2023/assets/139351697/0f26d911-d94a-4e1a-b81b-f53cee3f5c31)


**38. ssh command**

*The ssh command allows us to connect to an external machine on the network with the use of the ssh protocol.*

````syntax
ssh username@hostname
````

**39. service command**

*The service command in Linux is used for starting and stopping different services within the operating system.*

````syntax
 -->> service ssh status
 -->> service ssh stop
 -->> service ssh start 
````

**40. ps command**

*To find the running processes, we can simply type **ps** in the terminal prompt and get the list of running processes.*

````syntax
-->> ps 
````

**41. kill command and killall command**

 *To kill a process with the **kill** command, you can type **kill** followed b the PID of the process.*

*if you do not know the process ID and just want to kill the process with the name, you can make use of the **killall** command.*

````syntax
-->> kill <process ID>
-->> killall <process name>
````

**42. ifconfig and traceroutes commands**

*The ifconfig command will give you the list of all the network interfaces.*

*Along with the IP addresses, MAC addresses and other information about the interface.*

````syntax
-->> ifconfig
````

**43. passwd command**

 *The **passwd** command lets you set the password for your own account.*

*If you have the permissions, set the password for other accounts.*

````syntax
:~# passwd
New password: 
````

**44. In command**

*To create a link to another file, we use the ln command.*

*This is one of the important Linux commands that you should know if you’re planning to work as a Linux administrator.*

````syntax
 ln -s <source path> <link name>
````

**45. grep command **

*If you wish to search for a specific string within an output, the grep command comes into the picture.*

*We can pipe (**|**) the output to the grep command and extract the required string.*

````syntax
 <Any command with output> | grep "<string to find>"
````

**46. export command**

*The export command is specially used when exporting environment variables in runtime.* 

*For example, if I wanted to update the bash prompt, I’ll update the PS1 environment variable.* 

*The bash prompt will be updated with immediate effect*

````syntax
 export <variable name>=<value>
````

**47. chmod and chown commands**

*The chmod and chown commands give us the functionality to change the file permissions.*

*File ownership are the most important Linux commands you should know.*

````syntax
 -->> chmod +x loop.sh
 -->> chmod root:root loop.sh
````

![chmod command](https://github.com/saeed402/int-2023/assets/139351697/d60ed4af-c9f5-410c-8988-562bb6f0437b)


**48. wget command**

*If you want to download a file from within the terminal, the wget command is one of the handiest command-line utilities.*

````syntax
 wget <link to file>
OR
wget -c <link to file>
````

**49. ufw and iptables commands**

*UFW and IPTables are firewall interfaces for the Linux Kernel’s netfilter firewall.* 

*IPTables directly passes firewall rules to netfilter.*

*UFW configures the rules in IPTables which then sends those rules to netfilter.*

````syntax
 iptables -A INPUT -p tcp -m tcp --dport 80 -j ACCEPT
 ufw allow 80
````

**50. dd command**

*This command was created to convert and copy files from multiple file system formats.*

*The command is used to create bootable USB for Linux but there still are some things important you can do with the command.*

*For example, if I wanted to back up the entire hard drive as is to another drive, I’ll make use of the dd command.*

````syntax
dd if = /dev/sdb of = /dev/sda
````

