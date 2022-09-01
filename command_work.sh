#! usr/bin/bash

read -p "Write command: " command

if [ $command = "ls" ]
then
    ls  
elif [ $command = "date" ]
then
    date
elif [ $command = "pwd" ]
then
    pwd 
elif [ $command = "ps -aux" ]
then
    ps -aux 
elif [ $command = "whoami" ]
then
    whoami
else
    echo "ENTER ls, date, pwd, ps -aux, whoami COMMANDS"
fi
