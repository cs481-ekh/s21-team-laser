#!/bin/bash
func()
{
 javac -cp ".:./lib/junit.jar" src/*.java
}
func
exit $?