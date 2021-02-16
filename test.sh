#!/bin/bash
func()
{
 cd src
 for i in ls ../lib/*.jar
    do
    THE_CLASSPATH=${THE_CLASSPATH}:${i}
    done

 java -cp ".:${THE_CLASSPATH}" "TestRunner"
}
func
exit $?
