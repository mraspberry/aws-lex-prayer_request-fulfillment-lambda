import json
import os
import pprint
import requests

def send_request_to_slack(event, context):
    pprint.pprint(event)
    intent = event['currentIntent']
    name = intent['slots']['PrayerFor']
    request_body = intent['slots']['PrayerBody']
    followup = intent['slots']['FollowUp'].lower()
    slack = os.getenv('SLACK_WEBHOOK_URL')
    text = 'Prayer request for {n}:\n{b}\nFollow Up Requested:{f}'.format(
            n=name,
            b=request_body,
            f=followup,
            )
    data = {'text': text}
    header = {'ContentType': 'application/json'}
    print('Sending request to slack')
    result = requests.post(slack, json=data, headers=header)
    print('Slack result:', result.status_code)
    returndict = dict(dialogAction=dict())
    returndict['dialogAction']['type'] = 'Close'
    if result.status_code == requests.codes.ok:
        returndict['dialogAction']['fulfillmentState'] = 'Fulfilled'
        returndict['dialogAction']['message'] = dict(
                contentType='PlainText',
                content='Thank you for letting me know of your need. I have notified the prayer team.',
                )
    else:
        print("Failed with status_code", result.status_code, "text:", result.text)
        print(result.status_code, result.text)
        returndict['dialogAction']['fulfillmentState'] = 'Failed'
        returndict['dialogAction']['message'] = dict(
                contentType='PlainText',
                content='Sorry. Something went wrong. Contact Matt Raspberry (matt@skyline.church) for assistance',
                )
    return returndict
