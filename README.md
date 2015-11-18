# MachineLearningAPI

##note
this project is powerd by python3.
not working python2.x versions.

##install
$pip3 install cherrypy
$clone https://github.com/hobbee/MachineLearningAPI.git

##run
$python3 index.py

##use
post to http://<domain>/api/auto_tag with article data.
you will get tags list cleated automatic soon.
###article data format example
var settings = {
  "async": true,
  "crossDomain": true,
  "url": "http://127.0.0.1:8080/api/auto_tag",
  "method": "POST",
  "headers": {
    "cache-control": "no-cache",
    "postman-token": "e230815c-fbc2-5cf2-613f-1ca44139a45f",
    "content-type": "application/x-www-form-urlencoded"
  },
  "data": {
    "article_json": "{\"contents\":[{\"type\":\"Head\",\"content\":[\"登山にカメラとは？\"]},{\"type\":\"Body\",\"content\":[\"自然っていいですよね？その中でも山に登って癒されたいと思われる方は多いのではないでしょうか？自分の思い出として自然、一緒に行った仲間達と写真を撮る事で何時でも思い出を写真で見れます。\"]},{\"type\":\"Head\",\"content\":[\"カメラザック\"]},{\"type\":\"Body\",\"content\":[\"登山にカメラを持って行く場合一番気にする事は登山の際カメラをどの様に収納するかです。自分に合ったカメラザックを選びカメラ収納が出来るカメラザックを使う事で他カメラ用品の収納の出来て、便利にカメラ用品が持ち運び出来ます。\\nサイズ、デザイン、収納力でも豊富な商品が多く有るのでいろいろと試してみてください。\"]},{\"type\":\"Head\",\"content\":[\"登山用カメラストラップ\"]},{\"type\":\"Body\",\"content\":[\"登山の時、シャッターチャンスを逃したくない！でもカメラを持って登山するのはカメラが邪魔という方におすすめなのは、多様に使用出来るストラップショットでカメラザックのベルトにもつけれて登山用カメラアイテムとして多くが販売されています。\"]},{\"type\":\"Head\",\"content\":[\"コンパクト三脚\"]},{\"type\":\"Body\",\"content\":[\"せっかく登山に来たんだから、ブレの無いきれいな写真を撮りたいですよね。\\nそんな時持っていって間違い無いのはコンパクト三脚です。収納時は短くがざばらない三脚は多くあります。重さも軽い物が選べます。カメラザックに収納する事で邪魔にならない三脚を選ぶのがオススメです。\"]},{\"type\":\"Head\",\"content\":[\"一脚\"]},{\"type\":\"Body\",\"content\":[\"いくら軽くてもコンパクトでも登山に持って行くのに三脚はかさばって嫌だ、と言う方におすすめするのが一脚です。\\n工夫次第では登山で疲れ防止に役立つストックにもなってしまう。いざ撮影時にはカメラを取り付けブレの無い撮影や山の風景をバックに自撮りまで出来てしまいます。欲張りなアイテムです。\"]},{\"type\":\"Head\",\"content\":[\"カメラ用レインカバー\"]},{\"type\":\"Body\",\"content\":[\"山の天気は変わりやすいです。突然の雨、、、でも不思議な事に雨の中の撮影は雨の滴が綺麗でいいシャッターチャンスが突然訪れる事もあります。そんな時、カメラを雨から保護するのがレインカバーです。登山の時レインウェアを常備する事は大切な事の１つです。人と同じくカメラにも雨具を用意する事でより万全な準備ではないでしょうか？\"]},{\"type\":\"Head\",\"content\":[\"終わりに\"]},{\"type\":\"Body\",\"content\":[\"今回はあくまでもカメラを登山に持って行く時に一緒に用意すれば、よりカメラ撮影が楽になる物を紹介しました。\\nぜひ自然の素晴らしい写真を撮る為に、この用品が役にたつ事が出来れば嬉しいです。\"]}],\"title\":\"登山でもきれいな写真を！登山用カメラのおすすめ用品５選\",\"description\":\"登山に行くならカメラを持って、ダイナミックな自然を撮りたいですよね？\\nそんな時一緒に持っていったら便利なカメラ用品５個を紹介します。ぜひこれらを活用して素敵な写真を撮ってみてください。\",\"category\":\"outdoor\",\"author_comment\":\"車やバイクで風景撮りが好きでよく出かけています。甘党ですが最近お酒もおぼえました。\\r\\n\"}"
  }
}

$.ajax(settings).done(function (response) {
  console.log(response);
});

