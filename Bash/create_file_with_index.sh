#!usr/bin/bash

for i in {1..10}
do
    touch file_${i}.txt
    echo $i >> file_${i}.txt
done
