# 50 Commands of Linux
**These comprehensive notes on 50 Commands of Linux offer numerous benefits that can significantly enhnace my Knowledge,Improved efficiency,Ehance productivity,Deeper system understanding**
***versatility,career,Career Advancement,Troubleshooting skills,Community Engagement***

**1. ls command**

 *It is **designed to list the names and features of files and directories**.*

 *It can be used for a single file or as many as all files and folders in a selected set of directories.*
 Following are the flags used with ls command:

    - ls -a	list all files including hidden file starting with '.'.
    -ls -d	*list directories - with ' /'.
    -ls -l	list with long format - show permissions.
    -ls -F	*Append indicator (one of /=>@|) to entries.
    -ls -lh	This command will show you the file sizes in human readable format.
    -ls -r	list in reverse order.
    -ls -i	list file's inode(index) number.
    -ls -ltr	View Reverse Output Order by Date.
    -ls -t	sort by time & date.
    -ls -n	It is used to print group ID and owner ID instead of their names.
    -ls -m	A list of entries separated by commas should fill the width.
    -ls -g	This allows you to exclude the owner and group information columns.
    -ls -q	Force printing of non-graphic characters in file names as the character `?';.
    -ls -Q	Place double quotations around the entry names.


````syntax
ls [options] [file… | directory …]
````

![touch ls -al command](https://github.com/saeed402/int-2023/assets/139351697/01d37f68-89b9-4cdd-ac65-86ab92e57b2e)


**2. pwd command**

*The pwd command is used to display the location of the current working directory.*
*Following are the options we can use with pwd command:*

    -L (logical) : Use PWD from environment, even if it contains symbolic links
    -P (physical) : Avoid all symbolic links
    –help : this help and exit
    –version : Output version information and exit


````syntax
pwd  

````

![Pwd command](https://github.com/saeed402/int-2023/assets/139351697/7717f4b0-8c13-4af8-bfda-a20fb9692de8)


**3. mkdir Command**

*The mkdir command is used to create a new directory under any directory.*

*Following are the options used with touch command:*

    -a, change the access time only
    -c, if the file does not exist, do not create it
    -d, update the access and modification times
    -m, change the modification time only
    -r, use the access and modification times of the file
    -t, creates a file using a specified time


````syntax
mkdir <directory name> 
````

![mkdir command](https://github.com/saeed402/int-2023/assets/139351697/7a05e652-008a-4fd0-8098-e16d97d64f99)


**4. rmdir command**

*The rmdir command is used to delete a directory.*

*Following are the options ised with rmdir command:*

    -p: This option removes the DIRECTORY and any empty parent directories.
    -v: This option displays a message for each removed directory.
    --ignore-fail-on-non-empty: This option suppresses error messages if a directory is not empty.
    --help: This option displays the help message for the rmdir command.


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

*The cp command is used to copy a file or directory.Copies a file. Use the cp command to create a copy of the contents of the file or directory specified by the SourceFile or SourceDirectory parameters into the file or directory specified by the TargetFile or TargetDirectory parameters.*

*Following are the options used with cp command:*

    cp -a: This option is used to archive the existing files in the directory for retention purpose.
    cp -f: This option forcefully copy the files even it may remove the target file if needed. It is applicable if the file is already in use.
    cp -i: This option stands for interactive mode, which means that it will ask the user to overwrite the file by prompt.
    cp -l: This option is used to link a file with another existing one instead of copying it.
    cp -L: It is will create a symbolic link for the file.
    cp -n: This option is used not to overwrite any existing file.
    cp -R: This option means recursive copy means that it will copy all files with a cascading directory, including hidden file.
    cp -u: This means update, copy when the source file is new than the destination file.
    cp -v: This option stands for verbose which means that will it print all the process which happens on a file while copying.


````syntax
cp <existing file name> <new file name> 
````

![cp 1](https://github.com/saeed402/int-2023/assets/139351697/09975d90-fb2c-43ac-beeb-5dea02cdb363)
![cp 2](https://github.com/saeed402/int-2023/assets/139351697/93ce8503-435f-4e3a-957e-9b870d7e2acf)


**10. mv command**

*The mv command is used to move a file or a directory form one location to another location.Renames a file. We can use the mv command to move files and directories from one directory to another or to rename a file or directory. If you move a file or directory to a new directory without specifying a new name, it retains its original name.*

*Following are the options used with mv command:*

    -i Interactive mode. Ask before overwriting destination files.
    -f Force the move. If a destination file exists, overwrite it unconditionally

````syntax
mv <file name> <directory path> 
````

![mv](https://github.com/saeed402/int-2023/assets/139351697/a8878f98-4a69-41f7-a70a-ef04cc21ba0f)


**11. head command**

*The head command is used to display the content of a file. It displays the first 10 lines of a file.*

*Following are the options used with head command:*

    -n --lines : show the specified number of lines
    -c --bytes : show the specified number of bytes
    -v --verbose : show the file name tag
    -q --quiet : don't separate the content of multiple files with a file name tag

head picture

````syntax
head <file name>  
````

![head command](https://github.com/saeed402/int-2023/assets/139351697/392c0ce4-df5a-4de1-8487-da9a36dae817)


**12. tail command**

*The tail command is similar to the head command.*

*The difference between both commands is that it displays the last ten lines of the file content.*

*It is useful for reading the error message.*

*Following are the options used with tail command:*

    -n / --lines : Limit output to the last n lines/limit output to the lines following from line n
    -c / --bytes : Limit output to the last n bytes/limit output to the bytes following from byte n
    -q / --quiet, --silent : When using multiple files, suppress the output of the file names
    -v / --verbose : Force output of file names when used with multiple files
    --help : View Help section for command
    --version : View version information of command


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

*Following are the options used with cat command:*

    --show-all, -A: It is the same as -vET.
    --number-nonblank, -b: It shows the total non-empty output lines. Also, it overrides -n.
    -e: It is the same as -vE.
    --show-ends, -E: It shows the $ symbol at the completion of all lines.
    --number, -n: It gives the total of every output line.
    --squeeze-blank, -s: It suppresses redundant empty output lines.
    -t: It is the same as -vT.
    --show-tabs, -T: It shows TAB characters as ^|.
    -u: ignored.
    --show-nonprinting, -v: It uses M- and ^ notation, except TAB and LFD.
    --version: It displays the information of the output version and exit.
    --help: It shows the help menu and exit.


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
Example:

Apples

Bananas

*For finding non-duplicates only, with uniq use -u*

	`sort filename.txt | uniq -u`

Example:

Pear

*For finding count, with uniq use -c*

	`sort filename.txt | uniq -c`

Example:

4 Apples

6 Bananas

1 Pear

*For finding count in asc order, with uniq use -c*

	`sort filename.txt | uniq -c | sort -n`

Example:

1 Pear

4 Apples

6 Bananas

````syntax
command <fileName> | uniq  
````

**17. wc command**

*The wc command is used to count the lines, words, and characters in a file.The Linux wc command calculates a file's word, line, character, or byte count. Far from just being a utility for word processing, wc is a useful tool for a variety of system tasks.*

*Some useful command line options supported by the wc command are as following:*

    -c, --bytes : It is used to print the byte counts.

    -m, --chars : It is used to print the character counts.

    -l, --lines : It is used to print the newline counts.

    --files0-from=F : It is used to read input from specified files.

    -L, --max-line-length : It is used to print the maximum display width.

    -w, --words : It is used to print the word counts.

    --help : It is used to display the help manual.

    --version : It is used to display the version information.

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

*The sort command is used to sort files in alphabetical order.It prints the sorted information on the screen, doesn't change the file. This command processes on your data (the content of the file or output of any command) and reorders it in the specified way, which helps us to read the data efficiently.*

Following are the flags used with sort:

    -b --ignore-leading-blanks Causes sort to ignore leading blanks.

    -d --dictionary-order Causes sort to consider only blanks and alphanumeric characters.

    -f --ignore-case Ignores the default case, changes all lowercase letters to uppercase before comparison.

    -M --month-sort Sorts lines according to months (Jan-Dec).

    -h --human-numeric-sort Compares human-readable numbers (e.g., 2K 1G).

    -n --numeric-sort Compares data according to string numerical values.

    -R --random-sort Sorts data by a random hash of keys but groups identical keys together.

    / --random-source=FILE Gets random bytes from the specified FILE.

    -r --reverse Reverses the comparison results.

    -c --check, --check=diagnose-first Checks if the input is already sorted but doesn't sort it.

    / --debug Annotates the part of the line used for sorting.

    -k --key=KEYDEF Sort data using the specified KEYDEF, which gives the key location and type.

    -m --merge Causes sort to merge already sorted files.

    -o --output=FILE Redirects the output to FILE instead of printing it in standard output.

    -t --field-separator=SEP Uses the specified SEP separator instead of non-blank to blank transition.

    -z --zero-terminated Causes sort to use NUL as the line delimiter instead of the newline character.

    / --help Displays the help file with full options list and exits.

    / --version Outputs the program version and exits.

````syntax
sort <file name>  
````

**20. gzip command**

*The gzip command is used to truncate the file size.*

 *It is a compressing tool.*

*It replaces the original file by the compressed file having '.gz' extension.*

`gzip filename` 	: Compress the file and replaces the old file with compressed one
	
	`gzip -k filename` 	: Makes a new compressed file with the gz extension
	
	`gzip -d filename.gz`	: Decompresses a file


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

*Find files and folders with different criteria ( name, size, type etc ).*

	`find .` : Finds every single nested file inside the current directory	
	
	`find . -name '*.py'` : Finds every single nested file ending with .py inside the current directory
​	
	`find folderName -name '*.txt'` : Finds every single  file inside the folder ending with .txt

	`find . -type d` : Finds every single directory inside the current directory
​	
	`find . -type f` : Finds every single file inside the current directory
​	
	`find . -type d -name '*E*'` : Finds every single directory inside the current directory with E in its name


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

*These are the most common formatting characters for the date command:*

    %D – Display date as mm/dd/yy
    %Y – Year (e.g., 2020)
    %m – Month (01-12)
    %B – Long month name (e.g., November)
    %b – Short month name (e.g., Nov)
    %d – Day of month (e.g., 01)
    %j – Day of year (001-366)
    %u – Day of week (1-7)
    %A – Full weekday name (e.g., Friday)
    %a – Short weekday name (e.g., Fri)
    %H – Hour (00-23)
    %I – Hour (01-12)
    %M – Minute (00-59)
    %S – Second (00-60)

Following are some of the options used with date command:

    -d, --date=STRING : display time described by STRING, not 'now'
    -f, --file=DATEFILE : like --date; once for each line of DATEFILE
    -r, --reference=FILE : display the last modification time of FILE
    -s, --set=STRING : set time described by STRING
    -u, --utc, --universal : print or set Coordinated Universal Time (UTC)
    -V, --version : Print the version number of accton to standard output and quit.
    -h, --help : Prints the usage information to standard output and quit.


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

*Following are the flags available for df command.*

    ‘-a’ or ‘–all’ : Includes pseudo, duplicate, and inaccessible file systems in the output.

    ‘-B ’ or ‘–block-size=’ : Scales sizes by SIZE before printing them.

    ‘-h’ or ‘–human-readable’ : Prints sizes in a human-readable format using power of 1024.

    ‘-H’ or ‘–si’ : Prints sizes in a human-readable format using power of 1000.

    ‘-i’ or ‘–inodes’ : Lists inode information instead of block usage.

    ‘-l’ or ‘–local’ : Limits listing to local file systems.

    ‘-P’ or ‘–portability’ : Uses POSIX output format for better portability.

    ‘–sync’ : Invokes sync before getting usage info.

    ‘–total’ : Elides all entries insignificant to available space and produces a grand total.

    ‘-t ’ or ‘–type=’ : Limits listing to file systems of type TYPE.

    ‘-T’ or ‘–print-type’ : Prints file system ty

pe

  `df -h` : Shows the size, space etc in human readable size


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

*Some common signals in kill command are:*

    SIGHUP 1 It hangup detected on controlling terminals or death of controlling process.
    SIGINT 2 It interrupts from keyboard.
    SIGKILL 9 It kills signal.
    SIGTERM 15 It terminates signal.
    


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

*Following are the options used with passwd command:*

    -a, --all : This option can be used only with -S and causes show status for all users.
    -d, –delete: This option deletes the user password and makes the account password-less.
    -e, –expire: This option immediately expires the account password and forces the user to change password on their next login.
    -h, –help: Display help related to the passwd command.
    -i, –inactive INACTIVE_DAYS: This option is followed by an integer, INACTIVE_DAYS, which is the number of days after the password expires that the account will be deactivated.
    -k, –keep-tokens: This option is used when you only want to change the password if it is expired. It keeps the authentication tokens for the authentication if the password is not yet expired, even if you requested to change it. Note that if the expiry period for a user is set to 99999, then this option will not keep tokens and the password will be changed.
    -l, –lock: Lock the password of user. This appends the encrypted password of the user with a character ‘!’, and thus making it unable to match with any of input password combinations. This does not disable the account but prevents the user from logging in using a password. Though other authentication methods like ssh keys can be used to login to the account.
    -n, –mindays MIN_DAYS: Change the minimum number of days between password changes to MIN_DAYS so that the user can’t change the password for MIN_DAYS.
    -q, –quiet: This option is used for quiet mode. While using this option to change a password, the message “Changing password for $user.”, which usually gets printed before changing a password, does not get echoed.
    -r, –repository REPO: This option is used to change password for repository named “REPO”.
    -R, –root CHROOT_DIR: Apply changes in the CHROOT_DIR directory and use the configuration files from the CHROOT_DIR directory. This basically changes the root directory for the passwd process for once, and since CHROOT_DIR is a sub-directory of the root, it can not access the configuration files outside the CHROOT_DIR.
    -S, –status: Shows the password status (7 fields) of user
    -S [, –status] -a [, –all]: This combination of options shows password status for all users. Note that -a or –all cannot be used without -S option.
    -u, –unlock: Unlock the password of an account.
    -w, –warndays WARN_DAYS: This option is used to change the number of days before the password is to expire, to display the warning for expiring password.
    -x, –maxdays MAX_DAYS Set the maximum number of days for which the password remains valid. After MAX_DAYS, the password will expire and the user will be forced to change password.


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

*We need to tell:*

    Who are we changing permissions for
        (u - user/owner of file)
        (g - group/member of the group)
        (o - others)
        (a - all of the above)

    What changes are we making
        ( - (minus sign) removes permission)
        ( + (plus sign) grants permission)
        ( = (equals sign) set a permission and remove others)

    Which permissions are we setting.
        (r - read permission)
        (w - write permission)
        (x - execute permission)

Example:

	`chmod mode <file>` 
	
	`chmod u+x <file>`  : Grants permission to the user of the file to execute .
	
	`chmod a-x <file>`  : Removes permission from all (user, group, others) to execute.
	
	`chmod a+w <file>`  : Grants permission of write to all (user, group, others).


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
**scp Command**

*The scp (Secure Copy) command is a Linux utility used to securely transfer files and directories between hosts. It operates over SSH, providing encryption and authentication for secure file transfers. Below are the details of how the scp command works, along with some key options:*

Basic Syntax
bash
Copy code
scp [options] source destination
source: The source file or directory you want to copy.
destination: The target location where you want to copy the source. This can be a local path or in the format user@host:path for remote copying.
Options
-r or --recursive: Enables recursive copying for directories and their contents.
-P <port>: Specifies the SSH port to use on the remote host (default is 22).
-i <identity_file>: Specifies the private key file for authentication.
-v: Enables verbose mode, providing more detailed output during the transfer.
-p: Preserves the modification times, access times, and modes from the original file.
-q: Suppresses non-error messages.
-C: Enables compression during the transfer to reduce bandwidth usage.
Examples
Copy a local file to a remote server:

bash
Copy code
scp localfile.txt user@remotehost:/path/on/remote/server/
Copy a remote file to the local machine:

bash
Copy code
scp user@remotehost:/path/on/remote/server/remotefile.txt /local/path/
Copy a directory and its contents from a remote server to the local machine:

bash
Copy code
scp -r user@remotehost:/path/on/remote/server/directory /local/path/
Copy a local file to a remote server using a specific SSH key:

bash
Copy code
scp -i /path/to/private_key localfile.txt user@remotehost:/path/on/remote/server/
Copy a remote file to the local machine using a specific SSH port:

bash
Copy code
scp -P 2222 user@remotehost:/path/on/remote/server/remotefile.txt /local/path/
scp provides a secure and efficient way to transfer files between hosts while maintaining encryption and security. For large-scale data transfers, other tools like rsync might be more suitable.

