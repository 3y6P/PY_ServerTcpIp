import re

class RegexClass(object):

    tagsArray = "DF20023030DF210130DF2206303844374234DF230154DF24034B4C4BDF260130DF270130"

    def StrokingCut(self, array, min , max):
        strokeResult = ""
        for i in range(len(array)):
            if(i >= min and i < max):
                strokeResult = strokeResult + array[i]
        return strokeResult

    def StrokeMagic(self, tags):
        stringTag = "DF"

        DFpositions = []
        Substrings = []
        TagsArr = []
        # DFpositions
        for i in range(len(tags)):
            if tags[i] == stringTag[0] and tags[i + 1] == stringTag[0 + 1]:
                DFpositions.append(i)

        # substrings
        for i in range(len(DFpositions)):
            if (i == 0):
                Substrings.append(self.StrokingCut(tags, 0, DFpositions[1]))
            else:
                try:
                    Substrings.append(self.StrokingCut(tags, DFpositions[i], DFpositions[i + 1]))
                except:
                    Substrings.append(self.StrokingCut(tags, DFpositions[i], len(tags)))

        for i in range(len(Substrings)):
            stroke = Substrings[i]
            tagName = str(re.findall(r'([a-zA-Z]{2}[0-9]{2,2})', stroke)).replace("['", "").replace("']", "")
            valueCount = stroke.replace(tagName, "")
            resultStroke = "TAG " + tagName + ": value=" + valueCount
            TagsArr.append(resultStroke)

        return TagsArr

if __name__ == "__main__":
    f = RegexClass()
    print(f.StrokeMagic(f.tagsArray))
#print(StrokeMagic(tagsArray))