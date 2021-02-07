import datetime
import os
import re

_PATH_SETUP = os.path.join(os.getcwd(), 'setup.py')

# get today date
now = datetime.datetime.now()
now_date = now.strftime("%Y%m%d")

print(f"Update setup - replace version by {now_date} and update to fakeproj-nightly")
with open(_PATH_SETUP, 'r') as fp:
    setup = fp.read()
setup = re.sub(r'version=[\d\.\w\'"]+', f'version="dev-{now_date}"', setup)
setup = re.sub(r'name="fakeproj"', f'name="fakeproj-nightly"', setup)
with open(_PATH_SETUP, 'w') as fp:
    fp.write(setup)