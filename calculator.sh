#! usr/bin/bash

echo "ENTER NUMBER: "
read a
echo "ENTER NUMBER: "
read b

echo "ENTER ACTION NUMBER: "
echo "1. ADDITION"
echo "2. SUBTRACTION"
echo "3. MULTIPLICATION"
echo "4. DIVISION"
read ACTION

if [ $ACTION = "1" ]
then
    echo THE RESULT OF THE ACTION: $((a+b))
elif [ $ACTION = "2" ]
then
    echo THE RESULT OF THE ACTION: $((a-b))
elif [ $ACTION = "3" ]
then
    echo THE RESULT OF THE ACTION: $((a*b))
elif [ $ACTION = "4" ]
then
    echo THE RESULT OF THE ACTION: $((a/b))
fi
