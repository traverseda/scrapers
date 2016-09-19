import demiurge
from demiurge import AttributeValueField as AttrField

class RedditComments(demiurge.Item):
    text = demiurge.TextField(selector=" .usertext-body")
    author = demiurge.TextField(selector=".author")
    #score = demiurge.TextField(selector=".score .unvoted")
    date = AttrField(selector=".live-timestamp", attr="datetime")
    comments = demiurge.RelatedItem('self', selector='.child')
    def clean_score(self, value):
        if len(value.split(" ")) > 1:
            return int(value.split(" ")[0])
        return 0


    class Meta:
        selector = '.sitetable > .thing'
        headers = {'User-agent': 'traverse.da@gmail.com'}

class RedditPost(demiurge.Item):
    url = demiurge.AttributeValueField(
         attr='data-url')
    author = demiurge.TextField(selector=".author")
    date = AttrField(selector=".live-timestamp", attr="datetime")
    commentUrl = demiurge.AttributeValueField(selector=".comments", attr="href")
    commentCount = demiurge.TextField(selector=".comments")
    comments = demiurge.RelatedItem(
        RedditComments, selector='.comments', attr='href')
    score = demiurge.TextField(selector=".score .unvoted")
    name = demiurge.TextField(selector='a.title')

    def clean_commentCount(self, value):
        if len(value.split(" ")) > 1:
            return int(value.split(" ")[0])
        return 0

    class Meta:
        selector = '.thing'
        base_url = 'http://reddit.com'
        headers = {'User-agent': 'traverse.da@gmail.com'}

