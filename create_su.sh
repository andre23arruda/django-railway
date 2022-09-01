#!/bin/bash
# run with `. create_su.sh`
PWD=`pwd`

create_su () {
        if [ "$(uname)" == "Darwin" ]; then
        . $PWD/venv/bin/activate
        elif [ "$(expr substr $(uname -s) 1 5)" == "Linux" ]; then
                . $PWD/venv/bin/activate
        elif [ "$(expr substr $(uname -s) 1 10)" == "MINGW32_NT" ]; then
                . $PWD/venv/Scripts/activate
        elif [ "$(expr substr $(uname -s) 1 10)" == "MINGW64_NT" ]; then
                . $PWD/venv/Scripts/activate
        fi

        printf "\n Virtual enviroment activated. \n\n Use 'deactivate' to close it. \n\n\n"

        echo "from users.models import User; User.objects.create_superuser('dev', 'teste@example.com', '123')" | python manage.py shell

        printf "\n User created successfully!! \n "

}

create_su
