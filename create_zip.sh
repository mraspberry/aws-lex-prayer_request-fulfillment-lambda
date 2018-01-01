#!/usr/bin/env bash

ZIPNAME=lambda_deploy.zip

rm -f $ZIPNAME
# we don't want to see STDOUT of the below commands
# because this echos out the zip name it creates for the caller
pip3.6 install --upgrade -t . requests >/dev/null
find . -type d -name __pycache__ | xargs rm -rf
zip -9 -r $ZIPNAME chardet idna requests certifi urllib3 slack_notify.py >/dev/null

# echo the zipname so callers don't have to hardcode
echo $ZIPNAME
