from WebPageIndex import WebPageIndex


class MaxHeap:
    def __init__(self):
        self.heap = []
        self.size = 0

    def left(self, index):
        return (2 * index) + 1

    def right(self, index):
        return (2 * index) + 2

    def parent(self, index):
        return (index - 1) / 2

    def heapify(self, i):
        right = self.right(i)
        left = self.left(i)
        max_i = i
        if left < self.size and self.heap[left][0] > self.heap[max_i][0]:
            max_i = left
        if right < self.size and self.heap[right][0] > self.heap[max_i][0]:
            max_i = right
        if max_i != i:
            temp = self.heap[i][0]
            self.heap[i][0] = self.heap[max_i][0]
            self.heap[max_i][0] = temp
            self.heapify(max_i)

    def insert(self, occurrences, index_obj):
        node = (occurrences, index_obj)
        i = self.size
        parent_node = self.parent(i)
        while i > 0 and self.heap[parent_node] < occurrences:
            self.heap[i] = self.heap[parent_node]
            i = parent_node
            parent_node = self.parent(i)
        self.heap.append(node)
        self.size += 1


# initialization function takes a query (string) and a set of WebpageIndex
# instances as input. Creates a max heap where each node  in  the
# max  heap  represents  a  WebpageIndex  instance
class WebpagePriorityQueue:
    def __init__(self, search_query, list_of_webpageindex):
        self.search_query = search_query
        self.list_of_webpageindex = list_of_webpageindex
        self.MaxHeap = MaxHeap()

        search = self.search_query.split()
        # computes occurrences of query of webpageindex instance
        # priority = sum of word counts of the page for all words in the query
        for webpage_index in list_of_webpageindex:
            occurrences = 0
            for i in range(len(search)):
                occurrences += webpage_index.getCount(search[i])
            self.MaxHeap.insert(occurrences, webpage_index)

    # returns highest priority webpageindex
    def peek(self):
        return self.MaxHeap.heap[0][1]

    # removes and returns highest priority webpageindex
    def pull(self):
        if self.MaxHeap.heap[0] is None:
            return ModuleNotFoundError
        result = self.MaxHeap.heap[0]
        self.MaxHeap.heap[0] = self.MaxHeap.heap[self.MaxHeap.size - 1]
        self.MaxHeap.heapify(0)
        self.MaxHeap.size -= 1
        return result[1]

    def reheap(self, search_query):
        WebpagePriorityQueue(search_query, self.list_of_webpageindex)


if __name__ == "__main__":
    doc1 = WebPageIndex("path" + "doc1.txt")
    doc2 = WebPageIndex("path" + "doc2-graph.txt")
    doc3 = WebPageIndex("path" + "doc3-binarysearchtree.txt")
    doc4 = WebPageIndex("path" + "doc4-stack.txt")
    doc5 = WebPageIndex("path" + "doc5-queue.txt")
    doc6 = WebPageIndex("path" + "doc6-AVLtree.txt")
    doc7 = WebPageIndex("path" + "doc7-redblacktree.txt")
    doc8 = WebPageIndex("path" + "doc8-heap.txt")
    doc9 = WebPageIndex("path" + "doc9-hashtable.txt")

    index_set = [doc1, doc2, doc3, doc4, doc5, doc6, doc7, doc8, doc9]
    x = WebpagePriorityQueue("the", index_set)
    print(x.peek())
