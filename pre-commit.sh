#!/bin/sh

# https://gist.github.com/milancermak/3849310
# make sure requirements.txt is up to date with every commit
# by comparing the output of pip freeze
pip freeze | diff requirements.txt - > /dev/null
if [ $? != 0 ]
then
    echo "Missing python module dependencies in requirements.txt. Run 'pip freeze > requirements.txt' to update."
    exit 1
fi

# Check pyflakes
echo '
Checking Pyflakes'
flakes=$(pyflakes rhiz)
if [ $? == 0 ]; then
    echo "Pyflakes passed :)"
else
    echo "$flakes"
    echo "Pyflakes failed, can't commit. :("
    exit 1
fi
