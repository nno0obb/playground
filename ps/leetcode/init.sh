#!/bin/bash


NO=$1

mkdir "${NO}"
DIR="./${NO}"

sed "s/NO/${NO}/g" "NO.py" > "${DIR}/${NO}.py"
sed "s/NO/${NO}/g" "NO_test.py" > "${DIR}/${NO}_test.py"
