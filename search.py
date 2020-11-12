import pickle as pu
import time

from models import InvertedIndexDict, InvertedIndexTfIdf, VectorSpaceModel

if __name__ == "__main__":
    # idxObj = InvertedIndexDict(r"./archive/TelevisionNews")
    idxObj = VectorSpaceModel(r"./archive/TelevisionNews")

    query = input("Enter search query: ")
    startTime = time.time()
    res = idxObj.search(query)
    endTime = time.time()

    searchTime = round(endTime - startTime, 3)
    # print(
    #     "Searched across "
    #     + str(len(idxObj.documentIndex))
    #     + " documents in "
    #     + str(searchTime)
    #     + " seconds."
    # )
    with open("./obj/docIdx.pk", "rb") as f:
        documentIndex = pu.load(f)
    for docId in res:
        print("DocID", docId)
        print(documentIndex[docId])
        print("----------------------")
