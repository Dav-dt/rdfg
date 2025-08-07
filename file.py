from guiUtils import *

class FileHandler:
    """
    File Handler class
    """
    def __init__(self, nbOfFiles: int, sizeOfEachFile: int, category: str, pathGiven: str):
        assert category in GuiUtils.fileSize
        assert nbOfFiles and sizeOfEachFile

        self.nbOfFiles = nbOfFiles
        self.sizeOfEachFile = sizeOfEachFile
        self.category = category
        self.pathGiven = pathGiven


    def generateFile(self, index: int) -> None:
        """
        Function to generate one file
        file is in .bin
        """
        size = 0
        match self.category:
            case "Bytes":
                size = self.sizeOfEachFile
            case "KB" :
                size = self.sizeOfEachFile*10**3
            case "MB" :
                size = self.sizeOfEachFile*10**6
            case "GB" :
                size = self.sizeOfEachFile*10**9

        with open(self.pathGiven+"/RDFG"+str(index), "wb") as file:
            file.write(bytearray(size))

        return None


    def generateAllFiles(self) -> None:
        """
        Function to generate all files
        """
        for i in range(self.nbOfFiles):
            self.generateFile(i)

        return None