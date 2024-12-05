from news.news_redis import News

newsObject = News()
newsObject.isPositive = "false"
newsObject.isPositive = newsObject.isPositive.lower()
if newsObject.isPositive == "true" or newsObject.isPositive == "mixed" or newsObject.isPositive == "neutral" or newsObject.isPositive is None:
    newsObject.isPositive = "true"
else:
    newsObject.isPositive = "false"
    
print (newsObject.isPositive)