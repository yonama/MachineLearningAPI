import json
import sys
sys.path.append("./controllers/")
from controller import controller
sys.path.append("./models/")
from articles import articles

class automatic_tag(controller):
    def setup(self):
        self.POST = self.filter.befour_filter()(self.POST)
        self.articles = articles()

    def befour_action(self):
        print("hogehoge")

    def POST(self, article_json):
        #article_dic = json.loads(article_json)
        result = self.articles.find(1000)
        return json.dumps(result, ensure_ascii=False)

    def PUT(self, article_json):
        article_dic = json.loads(article_json)
        return json.dumps(article_dic, ensure_ascii=False)

    def DELETE(self, article_id):
        article_dic = json.loads(article_json)
        return json.dumps(article_dic, ensure_ascii=False)
