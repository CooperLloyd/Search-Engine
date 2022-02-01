from WebPageIndex import WebPageIndex
from WebpagePriorityQueue import WebpagePriorityQueue


def readFiles(path):
    doc1 = WebPageIndex(path + "doc1.txt")
    doc2 = WebPageIndex(path + "doc2-graph.txt")
    doc3 = WebPageIndex(path + "doc3-binarysearchtree.txt")
    doc4 = WebPageIndex(path + "doc4-stack.txt")
    doc5 = WebPageIndex(path + "doc5-queue.txt")
    doc6 = WebPageIndex(path + "doc6-AVLtree.txt")
    doc7 = WebPageIndex(path + "doc7-redblacktree.txt")
    doc8 = WebPageIndex(path + "doc8-heap.txt")
    doc9 = WebPageIndex(path + "doc9-hashtable.txt")

    index_set = [doc1, doc2, doc3, doc4, doc5, doc6, doc7, doc8, doc9]
    return index_set


if __name__ == "__main__":
    folder_path = "put path here"
    files = readFiles(folder_path)

    with open("queries-1.txt", "r") as queries:
        query_list = queries.readlines()
    for q in query_list:
        search_instance = WebpagePriorityQueue(q, files)
        while True:
            try:
                print(search_instance.pull())
                break
            except IOError or ValueError:
                print("error: made this at 4am")
            try:
                print(search_instance.pull())
                break
            except IOError or ValueError:
                print("error: made this at 4am")
            try:
                print(search_instance.pull())
                break
            except IOError or ValueError:
                print("error: made this at 4am")


