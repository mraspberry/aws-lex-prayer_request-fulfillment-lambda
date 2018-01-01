#!/usr/bin/env bash

## REQUIRES YOU CREATE SLACKURL AND IAMROLE FILES
LAMBDA_ENV_VARS="Variables={SLACK_WEBHOOK_URL=$(cat slackurl)}"
LAMBDA_IAM_ROLE="$(cat iamrole)"

ZIPFILE=$(./create_zip.sh)

aws lambda create-function \
    --function-name=PrayerReqFulfillment\
    --runtime=python3.6\
    --role=$LAMBDA_IAM_ROLE\
    --handler=slack_notify.send_request_to_slack\
    --environment=$LAMBDA_ENV_VARS\
    --zip-file=fileb://$ZIPFILE
