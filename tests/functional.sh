#!/bin/bash
export DATABASE_URL="sqlite:///test-sqlite"
export STORAGE="dbbackup.storage.filesystem_storage"
export STORAGE_OPTIONS="location=/tmp/"


python tests/runtests.py migrate

echo 'import testapp; testapp.models.CharModel.objects.all().delete(); testapp.models.CharModel.objects.create(field="a")' | python tests/runtests.py shell

python tests/runtests.py dbbackup
echo 'import testapp; testapp.models.CharModel.objects.all().delete()' | python tests/runtests.py shell

python tests/runtests.py dbrestore --noinput

response=$(echo 'import testapp; assert 1 == testapp.models.CharModel.objects.count()' | python tests/runtests.py shell &> /dev/stdout)
[[ ! "$response" == *"AssertionError"* ]]

exit $?
