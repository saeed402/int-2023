#! /bin/bash

name="saeed"

while getopts ":ain" opt; do
case $opt in 
  a) echo "lignum Tower DHA phase 2 Islamabad ";;
  i) echo "My name is Muhammad Saeed JavedI am student of Bachelors of computer science.";;
  n) echo "Muhammad Saeed javed S/O javed iqbal";;
  \?) echo "Invalid option :  -$OPTARG" ;;

  esac
done

echo "Name: $name"
   
