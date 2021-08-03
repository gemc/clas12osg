#!/bin/zsh

echo
echo 'Testing help:'
./client/Submit.py -h
echo

echo 'Type 1 Test1: mysql configuration, production database'
echo
./client/Submit.py test/t1test1.txt
echo
echo

echo 'Type 1 Test2: mysql configuration, devel database'
echo
./client/Submit.py test/t1test2.txt
echo
echo

echo 'Type 1 Test3: sqlite configuration, production database'
echo
./client/Submit.py test/t1test3.txt
echo
echo

echo 'Type 1 Test4: sqlite configuration, production database'
echo
./client/Submit.py test/t1test4.txt
echo
echo


