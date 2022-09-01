#! usr/bin/bash

if [ -f A/B/C ]
then
    echo A/B/C folders exist!
else
    mkdir -p A/B/C
    cd A/B/C
fi
