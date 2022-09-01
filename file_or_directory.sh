#!usr/bin/bash

touch file1 file 3
mkdir file2

function dir_or_file (){
    for file in $(cat file1 file2 file3)
    do
        if [ -d $file ]
        then
            echo "Directory: $file"
        fi  
        break
    done
}

dir_or_file
