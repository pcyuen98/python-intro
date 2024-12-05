import json

data = '''[
   {
      "py/object":"news.news_redis.News",
      "title":"Fri, 01 Nov 2024 00:01:11 GMT",
      "bible_ai":"Proverbs 14:15 - The naive believe everything, but the prudent give thought to their steps.",
      "bible_life":"The story of Solomon seeking wisdom from God in 1 Kings 3 demonstrates the importance of seeking counsel and thoughtful consideration before making important decisions, especially those affecting many.",
      "bible_life_cn":"\u6240\u7f57\u95e8\u738b\u5728\u5217\u738b\u8bb0\u4e0a\u7b2c\u4e09\u7ae0\u4e2d\u5411\u795e\u5bfb\u6c42\u667a\u6167\u7684\u6545\u4e8b\u8868\u660e\uff0c\u5728\u505a\u51fa\u91cd\u5927\u51b3\u5b9a\uff0c\u5c24\u5176\u662f\u5f71\u54cd\u8bb8\u591a\u4eba\u7684\u51b3\u5b9a\u4e4b\u524d\uff0c\u5bfb\u6c42\u5efa\u8bae\u548c\u6df1\u601d\u719f\u8651\u81f3\u5173\u91cd\u8981\u3002",
      "pinyin":"Su\u01d2lu\u00f3m\u00e9n w\u00e1ng z\u00e0i Li\u00e8w\u00e1ng j\u00ec sh\u00e0ng d\u00ec s\u0101n zh\u0101ng zh\u014dng xi\u00e0ng sh\u00e9n x\u00fanqi\u00fa zh\u00echu\u00ec de g\u00f9sh\u00ec bi\u01ceom\u00edng, z\u00e0i zu\u00f2 ch\u016b zh\u00f2ngd\u00e0 ju\u00e9d\u00ecng, y\u01d0sh\u00ec y\u01d0ngxi\u01ceng x\u01d4du\u014d r\u00e9n de ju\u00e9d\u00ecng zh\u012bqi\u00e1n, x\u00fanqi\u00fa ji\u00e0ny\u00ec h\u00e9 sh\u0113ns\u012b sh\u00fali\u00f9 zh\u00ec gu\u0101nj\u00ec zh\u00f2ngy\u00e0o.",
      "news_ai":"This situation highlights the importance of considering all sides of an issue before making a decision. Weighing the benefits and drawbacks, and listening to diverse opinions, can lead to a more informed and responsible outcome.",
      "isPositive": "true"
   },
   {
      "py/object":"news.news_redis.News",
      "title":"Tip of the Day: Practice Gratitude",
      "headline":"Tip of the Day: Practice Gratitude",
      "isPositive": "false",
      "pinyin":"H\u01ceo S\u0101m\u01cel\u00ecy\u00e0r\u00e9n de b\u01d0y\u00f9 (L\u00f9g\u0101 f\u00fay\u012bn 10:25-37) ji\u0101od\u01ceo w\u01d2men y\u00e0o t\u00f3ngq\u00edng h\u00e9 zh\u00e0og\u00f9 t\u0101r\u00e9n, c\u00f9j\u00ecn j\u012bj\u00ed de sh\u00e8ji\u0101o gu\u0101nx\u00ec, zh\u00e8 sh\u00ec ji\u00e0nk\u0101ng sh\u0113nghu\u00f3 f\u0101ngsh\u00ec de gu\u0101nji\u00e0n y\u00e0osu."
   }
]'''

data = json.loads(data)

filtered_data = list(filter(lambda x: x.get('isPositive') == "true", data))

for item in filtered_data:
    print(item)