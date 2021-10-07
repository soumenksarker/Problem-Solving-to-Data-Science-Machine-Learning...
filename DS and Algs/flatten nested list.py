def flatten(nestedList):
        def aux(listOrItem):
            if isinstance(listOrItem, list):
                for elem in listOrItem:
                    for item in aux(elem):
                        yield item
            else:
                yield listOrItem
        return list(aux(nestedList))
