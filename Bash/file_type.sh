#! usr/bin/bash

mkdir my_folder
touch my_file
touch my_executable_file 
chmod +x my_executable_file
ln -s my_file my_link_file

if [ -d my_folder ]
then
    echo "Directory: my_folder"
fi

if [ -f my_file ]
then
    echo "File: my-file"
fi

if [ -x my_executable_file ]
then
    echo "Executable_file: my_executable_file"
fi

if [ -h my_link_file ]
then
    echo "Soft_link_file: my_link_file"
fi
