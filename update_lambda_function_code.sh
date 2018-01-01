#!/usr/bin/env bash

## updates the code of the lambda function

zipfile=$(./create_zip.sh)

aws lambda update-function-code\
    --function-name PrayerReqFulfillment\
    --zip-file fileb://$zipfile
