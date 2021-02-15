#!/bin/bash
func()
{
 local ex=$(javac src/*.java)
}
func
exit $ex 
