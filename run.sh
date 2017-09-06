#!/bin/bash
if [ -e login.pid ]; then
        PID=$(cat "login.pid")
else
        PID=-1
fi

start(){
        echo "Starting gunicorn server"
        PROD=1 gunicorn --pid login.pid --daemon --bind 0.0.0.0:8001 login.wsgi:application
}

stop(){
        if [ $PID -eq -1 ]; then
                echo "Is the server running?"
                exit 0
        fi
        echo "Stopping server"
        kill $PID
}

restart(){
        stop
        start
}

case $1 in
        start|stop|restart) "$1"
        ;;
esac

exit 0
