class FilerClass(object):
    """Filer"""

    def FileCreate(self, fileName, filePath, fileType):
        fileObject = open(filePath + fileName + fileType, 'w', encoding='utf-8')
        fileObject.write("File was created!")
        print("FilerClass.FileCreate: " + fileObject.name)
        fileObject.close()

    def FileWrtie(self, filePath, fileContent):
        fileObject = open(filePath, "a", encoding='utf-8')
        fileObject.write(fileContent)
        fileObject.close()


if __name__ == "__main__":
    print("File was created with name ->CreatedFile")
    f = FilerClass()
    f.FileCreate("","CreatedFile", ".txt")
    f.FileWrtie("CreatedFile.txt", "NEW")