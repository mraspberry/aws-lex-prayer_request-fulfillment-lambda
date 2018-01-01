# Prayer Request Fulfillment Lambda function

This repository contains an AWS lambda function and deployment scripts for it. The function takes an event from Amazon Lex that is a prayer request and posts a message with the request information to a slack webhook URL. Here are the steps to get up and running using this. The deployment scripts have been tested on macOS High Sierra but they should work on Linux and the Windows WSL as well. If they don't create an issue and I'll fix it.

## Step 0
Create or login to your AWS account create an [Amazon Lex](https://docs.aws.amazon.com/lex/latest/dg/what-is.html) bot with the following intent and slots:
  1. MakePrayerRequest <-- This is the intent
      * PrayerFor <-- First slot, who is the prayer for?
      * PrayerBody <-- Second slot, what is the request?
      * FollowUp <-- Third slot, should someone follow up?

## Step 1
Install and configure the [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html), ensure the IAM account you use can create lambda functions, update their code, and create IAM roles. For more on IAM accounts see https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html

## Step 2
Create IAM role for the lambda function.
  1. Go to [AWS IAM](https://console.aws.amazon.com/iam/home?region=us-east-1#/home), click on Roles, and click Create Role.
  2. For type of Trusted Entity, select Lambda and click Next
  3. Search for AWSLambdaEdgeExecutionRole and select the returned value. Click Next
  4. Type something descriptive into the Role Name and Role description fields then click "Create Role"
  5. Go back to the dashboard and click "Roles", then click the role you just created and note the "Role ARN". You'll need it later

## Step 3
Create the lambda function
  1. `git clone https://github.com/nixalot/aws-lex-prayer_request-fulfillment-lambda.git`
  2. `cd aws-lex-prayer_request-fulfillment-lambda`
  3. `vi iamrole`
      * put the role ARN of the IAM role you created in this file
  4. Create a [Slack Webhook](https://api.slack.com/incoming-webhooks). Note the URL because you'll need it in the next step
  5. `vi slackurl`
      * put the URL for the slack webhook you created in this file
  6. `./add_to_lambda.sh`
  7. If all goes well the AWS CLI will return the JSON of the created lambda function

## Step 4
Add the created lambda function to Amazon Lex
  1. Go to the created Amazon Lex bot in the Lex management console
  2. Under "Fulfillment", select "AWS Lambda Function" and select PrayerReqFulfillment from the dropdown.
  3. Build and test the bot, if all goes well publish it!

I currently use Twilio to interact with the Amazon Lex bot but you can use many different messaging platforms for your congregation to interact with it. Use what works best for you, or expose the bot via multiple channels. Enjoy, and let me know if you run into any problems. I'm happy to help however I can.
