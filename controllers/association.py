import cherrypy
import simplejson
import sys
sys.path.append("./controllers/")
from controller import controller
sys.path.append("./models/")
from articles import articles
sys.path.append("./components/")
from aprioricompo import aprioricompo

items=['beer','nuts','cheese','jam','butter']

testdata=[      ['beer','nuts','cheese'],
                ['beer','nuts','jam'],
                ['beer','butter'],
                ['nuts','cheese'],
                ['beer','nuts','cheese','jam'],
                ['butter'],
                ['beer','nuts','jam','butter'],
                ['jam'] ]

class association(controller):
    def setup(self):
        self.POST = self.filter.befour_filter()(self.POST)
        self.apriori_compo = aprioricompo()

    def befour_action(self):
        print("hogehoge")

    def GET(self):
        n = 3
        sol=self.apriori_compo.apriori(testdata, items, n)
        #n個の支持度リスト
        XY = [i for i in [l for l in sol if len(l[0])==n]]
        #n-1個の支持度dict
        X = {tuple(i[0]):[i[1], i[2]] for i in [l for l in sol if len(l[0])==n-1]}
        #1個の支持度リスト
        Y = [i for i in [l for l in sol if len(l[0])==1]]
        result = []
        for xy in XY:
            for y in Y:
                if y[0][0] in xy[0]:
                    xtuple = tuple([x for x in xy[0] if x!=y[0][0]])
                    sup = y[1]
                    if X[xtuple][1][0]==0:
                        rel = 0
                    else:
                        rel = xy[2][0] / X[xtuple][1][0]
                    if sup==0:
                        lif = 0
                    else:
                        lif = rel/sup
                    result.append([xtuple, y[0][0], lif])
        return json.dumps(result, ensure_ascii=False)

    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def POST(self):
        trans_list = cherrypy.request.json
        n = len(trans_list) + 1
        sol=self.apriori_compo.apriori(testdata, items, n)
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
