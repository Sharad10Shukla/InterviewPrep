# implement file system in Unix that supports search by name,extension
# How to implement file directory hierarchy
from abc import ABC, abstractmethod
from typing import List
from collections import deque
class File():
    def __init__(self,name,size):
        self.name = name
        self.size = size
        self.is_directory = False if "." in self.name else True
        self.children = []
        self.extension = self.name.split(".")[-1] if "." in self.name else ""



class Filter(ABC):
    def __init__(self,file: File):
        self.file = file
    @abstractmethod
    def apply(self):
        pass

class FilterbyName(Filter):
    def __init__(self,file: File):
        self.filter_file = file

    def apply(self,file):
        # print(self.filter_file,)
        return file.name == self.filter_file

class FilterbyExtension(Filter):
    def __init__(self,extension: str):
        self.extension = extension

    def apply(self,file):
        return file.name.split(".")[-1] == self.extension


class UnixFS():
    def __init__(self):
        self.filters: List[Filter] = []
    def add_filter(self, filter: Filter):
        self.filters.append(filter)

    def or_filter(self,root):
        found_files = []
        queue = deque()
        queue.append(root)
        while queue:
            curr_root = queue.popleft()
            if curr_root.is_directory:
                for child in curr_root.children:
                    queue.append(child)
            else:
                for filter in self.filters:
                    if filter.apply(curr_root):
                        found_files.append(curr_root)
        found_files = [f.name for f in found_files]
        return found_files

    def and_filter(self,root):
        found_files = []
        queue = deque()
        queue.append(root)
        while queue:
            curr_root = queue.popleft()
            if curr_root.is_directory:
                for child in curr_root.children:
                    queue.append(child)
            else:
                is_valid = True
                for filter in self.filters:
                    if not filter.apply(curr_root):
                        is_valid = False
                        break
                if is_valid:
                    found_files.append(curr_root)
        found_files = [f.name for f in found_files]
        return found_files

if __name__ == "__main__":
    f1 = File("root_300", 300)

    f2 = File("fiction_100", 100)
    f3 = File("action_100", 100)
    f4 = File("comedy_100", 100)
    f1.children = [f2, f3, f4]

    f5 = File("StarTrek_4.txt", 4)
    f6 = File("StarWars_10.xml", 10)
    f7 = File("JusticeLeague_15.txt", 15)
    f8 = File("Spock_1.jpg", 1)
    f2.children = [f5, f6, f7, f8]

    f9 = File("IronMan_9.txt", 9)
    f10 = File("MissionImpossible_10.rar", 10)
    f11 = File("TheLordOfRings_3.zip", 3)
    f3.children = [f9, f10, f11]

    f11 = File("BigBangTheory_4.txt", 4)
    f12 = File("AmericanPie_6.mp3", 6)
    f4.children = [f11, f12]

    bbt_filter = FilterbyName("StarWars_10.xml")
    txt_filter = FilterbyExtension("xml")

    my_linux_find = UnixFS()
    my_linux_find.add_filter(bbt_filter)
    my_linux_find.add_filter(txt_filter)

    # print(my_linux_find.or_filter(f1))
    # print(my_linux_find.or_filter(f2))
    print(my_linux_find.and_filter(f1))



