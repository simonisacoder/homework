#!/bin/bash

##########################################################################
# Run script for examples.                                               #
##########################################################################

if [ -n "$2" ]; then
  echo "Usage: ./runexample number_of_example"
  exit
fi

if [ -z "$1" ]; then
  echo "Usage: ./runexample number_of_example"
  exit
fi

example=$1
example_dir=../../../../examples

CLASSPATH_DELIMITER=":"

if [[ "${CLASSPATH_DELIMITER}" != ":" &&  "${CLASSPATH_DELIMITER}" != ";" ]]
then
  CLASSPATH_DELIMITER=":"
fi

JARS="./../../../../bin/dol.jar${CLASSPATH_DELIMITER}./../../../../bin/xercesImpl.jar${CLASSPATH_DELIMITER}./../../../../bin/jdom.jar"

HEADER="[RUNEXAMPLE] "

echo 
echo ${HEADER} Create directory "example${example}".
echo 
rm -rf example${example}
mkdir example${example}
cd example${example}


echo
echo ${HEADER} check compliance for "example${example}_flattened.xml".
echo
java -classpath "${JARS}${CLASSPATH_DELIMITER}./.." dol.helper.validator.XMLValidator ${example_dir}/example${example}/example${example}.xml 

if [ "$?" != "0" ]; then 
  exit
fi

echo
echo ${HEADER} Create flattened XML "example${example}_flattened.xml".
echo
java -classpath "${JARS}${CLASSPATH_DELIMITER}./.." dol.helper.flattener.XMLFlattener ${example_dir}/example${example}/example${example}.xml Example${example}Generator
javac Example${example}Generator.java
java Example${example}Generator > example${example}_flattened.xml


echo
echo ${HEADER} Copy C source files.
echo
rm -rf src
mkdir src
cp -r ${example_dir}/example${example}/src/*.h ./src
cp -r ${example_dir}/example${example}/src/*.c ./src

echo
echo ${HEADER} Run dol.
echo
java -classpath "${JARS}${CLASSPATH_DELIMITER}./.." dol.main.Main -P example${example}_flattened.xml -D example${example}.dot -H systemc 


echo
echo ${HEADER} Make SystemC application.
echo
cd systemc/src
make
cp sc_application ./../..
cd ./../..

echo
echo ${HEADER} Run SystemC application.
echo
./sc_application

echo
echo ${HEADER} Exited normally.

