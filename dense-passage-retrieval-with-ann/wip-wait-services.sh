#!/bin/sh

export VESPA_USER=$(id -un)
export VESPA_HOME=$HOME/vespa
export VESPA_CONFIGSERVERS=$(hostname)

waitapp()
{
    port=$1
    appup=false
    while test $appup = false
    do
	response="$(curl -s --head http://localhost:$port/ApplicationStatus)"
	echo resp="$response"
	case "$response" in
	    "HTTP/1.1 200 OK"*) appup=true;;
	    *) sleep 1;;
	esac
    done
}

# Wait for container
waitapp 8080
