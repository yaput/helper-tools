from os.path import expanduser
import os
import re
home = expanduser("~")

with open(home+"/.aws/config", "r") as config:
    profile_pattern = re.compile("\[profile.*?\]")
    profile_group = profile_pattern.findall(config.read())
    for profile in profile_group:
        print("-" + profile.replace("[profile", "").replace("]", ""))
