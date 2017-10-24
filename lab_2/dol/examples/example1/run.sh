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
example_dir=../../examples

CLASSPATH_DELIMITER="@classpath_delimiter@"

if [[ "${CLASSPATH_DELIMITER}" != ":" &&  "${CLASSPATH_DELIMITER}" != ";" ]]
then
  CLASSPATH_DELIMITER=":"
fi

JARS="../../jars/xercesImpl.jar${CLASSPATH_DELIMITER}../../jars/jdom.jar"


HEADER="[RUNEXAMPLE] "

echo
echo ${HEADER} Create flattened XML "example${example}_flattened.xml".
echo
java -classpath "${JARS}${CLASSPATH_DELIMITER}./../../build/bin/main" dol.helper.flattener.XMLFlattener ${example_dir}/example${example}/example${example}.xml Example${example}Generator
javac Example${example}Generator.java
java Example${example}Generator > example${example}_flattened.xml


echo
echo ${HEADER} Run dol.
echo
java -classpath "${JARS}${CLASSPATH_DELIMITER}./../../build/bin/main" dol.main.Main -P example${example}_flattened.xml -D example${example}.dot -C systemc -c

echo
echo ${HEADER} Make SystemC application.
echo
cd systemc/src
make
cp sc_application ./../..
cd ./../..


java -classpath "${JARS}${CLASSPATH_DELIMITER}./../../build/bin/main" dol.main.Main  -P example${example}_flattened.xml -H hds
