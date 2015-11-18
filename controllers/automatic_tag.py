import json
import sys
sys.path.append("./controllers/")
from controller import controller
sys.path.append("./models/")
from articles import articles
sys.path.append("./components/")
from autotagcompo import autotagcompo
from nominalization import nominalization

class automatic_tag(controller):
    def setup(self):
        self.POST = self.filter.befour_filter()(self.POST)
        self.articles = articles()
        self.tag_compo = autotagcompo()
        self.noun_compo = nominalization()

    def befour_action(self):
        print("hogehoge")

    def POST(self, article_json):
        article_noun = self.noun_compo.nominalization(article_json)
        result = self.tag_compo.make_tags_with_new_text(article_noun)
        return json.dumps(result, ensure_ascii=False)

    def PUT(self, article_json):
        article_dic = json.loads(article_json)
        return json.dumps(article_dic, ensure_ascii=False)

    def DELETE(self, article_id):
        article_dic = json.loads(article_json)
        return json.dumps(article_dic, ensure_ascii=False)
