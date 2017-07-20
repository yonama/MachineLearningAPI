# MachineLearningAPI

## note
this project is powerd by python3.
not working python2.x versions.

## install
$pip3 install cherrypy  
$clone https://github.com/hobbee/MachineLearningAPI.git

## run
$python3 index.py

## use
### find keyword
post to `http://<domain>:8080/api/auto_tag` with __article data__.  
you will get tags list cleated automatic soon.
#### send data format example
```
var settings = {  
  "async": true,
  "crossDomain": true,
  "url": "http://<domain>:8080/api/auto_tag",
  "method": "POST",
  "headers": {
    "cache-control": "no-cache",
    "content-type": "application/x-www-form-urlencoded"
  },
  "data": {
    "article_json": "{\"contents\":[{\"type\":\"Head\",\"content\":[\"キュー（CUE）\"]},{\"type\":\"Head3\",\"content\":[\"タップ\"]},{\"type\":\"Body\",\"content\":[\"球が触れる重要な部品で、多くのプレーヤーがもっとも気を使う部分です。\\n主な材質は皮でチョークを塗って使います。大切なのが丸み。\\n一般的に１０円玉の丸みに整えますがそれぞれの好みですのであくまで目安と思ってください。ハウスキューを選ぶときにはこの”丸み”に気をつけて選んでみてください。\"]},{\"type\":\"Head3\",\"content\":[\"先角\"]},{\"type\":\"Body\",\"content\":[\"白い部分です。\\n主に樹脂ですが高級な物になると象牙が使われます。\"]},{\"type\":\"Head3\",\"content\":[\"シャフト\"]},{\"type\":\"Body\",\"content\":[\"キューの性能のほとんどがこの部品で決まります。\\n昔は１本の角材から削り出していました。そのため非常に性能にばらつきがあったのですが最近では木材を貼り合わせて性能のばらつきを少なくする”ハイテク・シャフト”が主流になりつつあります。\"]},{\"type\":\"Head3\",\"content\":[\"ジョイント\"]},{\"type\":\"Body\",\"content\":[\"シャフトとバットをつなぐ重要な部分でネジでシャフトとつなぎます。\\nいろいろな種類のネジ山や形がありそれぞれ打感が違いキューメーカーのこだわりが出る部分でもあります。\"]},{\"type\":\"Head3\",\"content\":[\"バット\"]},{\"type\":\"Body\",\"content\":[\"グリップとフォアアームから成る”本体”に当たる部分です。\\n様々な木材(銘木）、樹脂、貴金属、宝石などが使われ意匠を凝らしたものがあります。\\nデザインの美しさからコレクションとして所有する人も多く海外では投資の対象としても扱われています。\\nグリップも糸巻き、革巻き等がありプレーヤーの好みで様々です。\"]},{\"type\":\"Head\",\"content\":[\"テーブル\"]},{\"type\":\"Head3\",\"content\":[\"ポケット\"]},{\"type\":\"Body\",\"content\":[\"ボールを落とす穴の事です。\\nコーナーポケット４つ、サイドポケット２つの計６つの穴が開いています。\\nお店により穴の大きさに違いがありボール２個が並んで入る所もあれば１.６個分の大きさのところがあります。\\n店内で一番目立つ所に設置されている台を華台（はなだい）といい穴を狭く設定してある事が一般的です。\"]},{\"type\":\"Head3\",\"content\":[\"レール\"]},{\"type\":\"Body\",\"content\":[\"台を囲う枠の部分です。\\n落ちたボールが集まる側がフットレール、ブレイクをする側をヘッドレール、両脇がサイドレールと呼びレールに刻まれている点をポイントと呼びます。\\nこのポイントですがただの飾りではなくバンクショット（クッションに反射させてポケットするテクニック）の角度を計算するのに使ったりします。\"]},{\"type\":\"Head3\",\"content\":[\"クッション\"]},{\"type\":\"Body\",\"content\":[\"レールに取り付けてあるゴム製の部品。\\nボールが正確に跳ねるようにメンテナンスされている物が好ましいです。\\n図の様なショットをバンクショットと言いますがクッションがへたっているとこのようなショットの成功率に大きく影響してしまいます。\"]},{\"type\":\"Head3\",\"content\":[\"ラシャ\"]},{\"type\":\"Body\",\"content\":[\"テーブルに皺なく張り付けてある布。\\nざまざまな色がありますが性能は関係ありません（見やすい見にくいはありますが。）\\n一枚布ですので咥え煙草で灰を落として穴をあけてしまうと全部張り替えになってしまいます。\\nくれぐれも穴を開けないように気をつけましょう。\"]},{\"type\":\"Head\",\"content\":[\"チョーク\"]},{\"type\":\"Body\",\"content\":[\"大体どこのお店にもテーブル１台につき２個のチョークが置いてありますね。タップに塗る事によってボールを撞いた時に滑らず撞けるようにする為です。この事によりボールに回転を掛けられ様々なアクションを与える事が出来ます。１ショット撞くたびに塗るようにしましょう！\"]},{\"type\":\"Head\",\"content\":[\"メカニカルブリッジ\"]},{\"type\":\"Body\",\"content\":[\"手玉の位置が遠く届かない時に使います。\\n初心者が使う道具だと勘違いされてる方がおられますがそんな事はありません。\\nむしろメカニカルブリッジを使って押し玉、引き玉、ストップ、ひねりが使えるくらいになるまで練習しましょう。\"]},{\"type\":\"Head\",\"content\":[\"グローブ\"]},{\"type\":\"Body\",\"content\":[\"キューが滑りにくくイライラする。\\nそんな経験ありませんか？\\n特にハウスキューはシャフトのニスを落としていないので滑りにくいのです。\\nそんな時に使うのがこの道具。\\nお店では貸出していない事が多いので１つ持っておくと便利です。\"]},{\"type\":\"Head\",\"content\":[\"まとめ\"]},{\"type\":\"Body\",\"content\":[\"いかがでしたでしょうか？\\nビリヤードは道具を使いこなすスポーツでもあります。\\nそのためにも道具の各名前を知っておくことは大事だと思います。同じバランスのキューで練習する事によって、同じようにストローク出来る事からもマイキューを持つ事は非常に有益な事です。これを機に道具にも目を向けてみてください。\"]}],\"title\":\"初心者もこれだけ知っておけば大丈夫！ビリヤードの基本用語\",\"description\":\"普段何気に使っているキュー。各部分にも名前があるのを知っていますか？他にもテーブルの真ん中に付いている点や脇に備え付けられている「熊手」みたいな棒。そんな用具の名前や役割を便利グッズなども交えてご紹介します。これらを使いこなしてもっとビリヤードを楽しみましょう。\",\"category\":\"sport\",\"author_comment\":\"インドアはビリヤード・プラモ・料理・お酒。\\r\\nアウトドアは車・バイク・キャンプ・スキー・スノーボード・旅行などなど。\\r\\nとにかく多趣味でいろんな事に手を出しております。\"}"
  }
}

$.ajax(settings).done(function (response) {  
  console.log(response);  
});  
```

#### receive data format example
```
["クッション", "ショット", "タップ", "テーブル", "ブリッジ", "ボール", "ポケット", "丸み", "木材", "樹脂", "玉", "穴", "道具"]
```

### find asosiation rule
post to `http://<domain>:8080/api/asosiation` with __trans_list__.  
you will get asosiation rule list.

#### send data format example
```
var settings = {
  "async": true,
  "crossDomain": true,
  "url": "http://<domain>:8080/api/association?trans_json=%5B1%5D",
  "method": "GET",
  "headers": {
    "content-type": "application/json",
    "cache-control": "no-cache",
    "postman-token": "0fd0c14a-4e25-e713-91a9-0c3084b3fa44"
  }
}
```

#### receive data format example
```
[
  [
    2,
    1.28
  ],
  [
    3,
    1.0666666666666667
  ],
  [
    4,
    1.2
  ],
  [
    5,
    1.0666666666666667
  ]
]
```

### send transaction list
post to `http://<domain>:8080/api/association` with __trans_list__ and __user_id__.

#### send data format example
```
var settings = {
  "async": true,
  "crossDomain": true,
  "url": "http://<domain>:8080/api/association",
  "method": "POST",
  "headers": {
    "content-type": "application/json",
    "cache-control": "no-cache",
    "postman-token": "81169823-148d-8c71-4435-f3695fe1fba5"
  },
  "processData": false,
  "data": "{\n    \"list\" : [4],\n    \"user_id\" : 111\n}"
}

$.ajax(settings).done(function (response) {
  console.log(response);
});
```
