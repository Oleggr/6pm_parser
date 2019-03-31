import config
import os

TOKEN = config.token
MONITORING_TOKEN = config.monitoring_bot_token
MY_ID = config.oleggr_id


command = 'curl -s -X POST ' \
        + 'https://api.telegram.org/bot' \
        + MONITORING_TOKEN \
        + '/sendMessage -d chat_id=' \
        + MY_ID \
        + ' -d text=\"Привет парень\"'

print(command)
print()
os.system(command)
print()
