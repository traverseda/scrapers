import utils
from scrapers import reddit

s = reddit.RedditPost.one('/r/programming')

comments = [comment for comment in utils.consolodateComments(s.comments)]

from yaml import load, dump
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper
import yaml


print(yaml.dump(comments, default_flow_style=False, allow_unicode=True))
