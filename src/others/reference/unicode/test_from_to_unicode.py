
class CN:
    @staticmethod
    def toUnicode(word):
        if word is None:
            return None
        else:
            chinese_encode = word.encode('unicode-escape')
        #print("UTF-8 Encode String:", chinese_encode)

            chinese_unicode = chinese_encode.decode('utf-8')
            return chinese_unicode

    @staticmethod
    def fromUnicode(word):
        if word is None:
            return None
        #print("UTF-8 Encode String:", word)
        else:
            decoded_text = bytes(word, 'utf-8').decode('unicode-escape')
            return decoded_text

if __name__ == '__main__':
    unicode = CN.toUnicode('大卫和拔')
    print ('unicode-->' + unicode)
    chinese = CN.fromUnicode(unicode)
    print ('chinese-->' + chinese)