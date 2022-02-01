from AVLTreeMap import AVL


# WebPageIndex inherits AVL
class WebPageIndex(AVL):
    def __init__(self, file):
        AVL.__init__(self)
        self.path = file

    def getCount(self, key):
        return len(self.get(key))

    def main(self):
        # tokenize text file into word list
        textFile = open(self.path, 'r')
        text = textFile.read()
        text = text.lower()
        words = text.split()
        words = [word.strip('.,!;:?()[] - ') for word in words]
        words = [word.replace("'s", '') for word in words]
        # deals with annoying forward slash
        for i in range(len(words)):
            if "/" in words[i]:
                splitWord = words[i].split("/", 1)
                words.remove(words[i])
                words.insert(i, splitWord[0])
                words.insert(i + 1, splitWord[1])
        # maps words to a list of the index's at each occurrence
        wordDict = {}
        for i in range(len(words)):
            if words[i] not in wordDict.keys():
                wordDict[words[i]] = [i]
            else:
                wordDict[words[i]].append(i)
        # calls AVL function (insert) to build tree
        for key in wordDict:
            x.insert(key, wordDict.get(key))


if __name__ == "__main__":
    filePath = "put path here" + "doc1.txt"
    x = WebPageIndex(filePath)  # initialize instance of WebPageIndex

    x.main()
    x.printer()
    print(x.getCount("dic"))
