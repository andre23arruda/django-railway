#!/bin/bash
# run with `. run.sh`
PWD=`pwd`

run () {
	if [ "$(uname)" == "Darwin" ]; then
        . $PWD/venv/bin/activate
	elif [ "$(expr substr $(uname -s) 1 5)" == "Linux" ]; then
			. $PWD/venv/bin/activate
	elif [ "$(expr substr $(uname -s) 1 10)" == "MINGW32_NT" ]; then
			. $PWD/venv/Scripts/activate
	elif [ "$(expr substr $(uname -s) 1 10)" == "MINGW64_NT" ]; then
			. $PWD/venv/Scripts/activate
	fi

    printf "\n Virtual enviroment activated. \n\n Use 'deactivate' to close it. \n\n"

    python manage.py runserver
}

run
