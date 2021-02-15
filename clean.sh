#!/bin/bash
func()
{
 local ex=$(rm src/*.class)
}
func
exit $ex
