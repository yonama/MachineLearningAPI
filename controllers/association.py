import cherrypy
import simplejson
import datetime
import sys
sys.path.append("./controllers/")
from controller import controller
sys.path.append("./models/")
import model as Model
from model import model
from visit_history import visit_history
from transaction import transaction
sys.path.append("./components/")
from aprioricompo import aprioricompo

'''
items=['beer','nuts','cheese','jam','butter']

testdata=[      ['beer','nuts','cheese'], #1,2,3
                ['beer','nuts','jam'], #1,2,4
                ['beer','butter'], #1,5
                ['nuts','cheese'], #2,3
                ['beer','nuts','cheese','jam'], #1,2,3,4
                ['butter'], #5
                ['beer','nuts','jam','butter'], #1,2,4,5
                ['jam'] ] #4
'''

class association(controller):
    def setup(self):
        self.POST = self.filter.befour_filter()(self.POST)
        self.apriori_compo = aprioricompo()

    def befour_action(self):
        print("hogehoge")

    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def GET(self, trans_json):
        trans_list = simplejson.loads(trans_json)
        n = len(trans_list) + 1
        trans_all_data = [[j.article_id for j in i.visit_histories] for i in model.session.query(transaction).all()]
        items = [1,2,3,4,5]
        sol=self.apriori_compo.apriori(trans_all_data, items, n)
        for s in sol:
            print(s[0])
        #n個の支持度リスト
        XY = [i for i in [l for l in sol if len(l[0])==n]]
        #n-1個の支持度dict
        X = {tuple(i[0]):[i[1], i[2]] for i in [l for l in sol if len(l[0])==n-1] if i[0] == trans_list}
        print(X)
        #1個の支持度リスト
        Y = [i for i in [l for l in sol if len(l[0])==1]]
        result = []
        for xy in XY:
            for y in Y:
                if y[0][0] in xy[0]:
                    xtuple = tuple([x for x in xy[0] if x!=y[0][0]])
                    sup = y[1]
                    if xtuple in X:
                        if X[xtuple][1][0]==0:
                            rel = 0
                        else:
                            rel = xy[2][0] / X[xtuple][1][0]
                        if sup==0:
                            lif = 0
                        else:
                            lif = rel/sup
                        result.append([y[0][0], lif])
        return result

    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def POST(self):
        trans_data = cherrypy.request.json
        trans_list = trans_data['list']
        user_id = trans_data['user_id']
        from sqlalchemy import and_
        ipaddress = cherrypy.request.remote.ip
        mytransaction = model.session.query(transaction).filter(
                and_(
                    transaction.created >= datetime.date.today(),
                    transaction.created < datetime.date.today() + datetime.timedelta(days=1),
                    transaction.ipadress == ipaddress,
                    transaction.user_id == user_id
                )
            ).one_or_none()
        if mytransaction is None:
            mytransaction = transaction(user_id, ipaddress)
            mytransaction.save()
        for vh in trans_list:
            myvisit_history = visit_history(vh, mytransaction.id)
            myvisit_history.save()

        return []
