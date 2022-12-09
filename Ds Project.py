# In The Name Of God
import re


class Node:
    def __init__(self, data):
        self.next = None
        self.prev = None
        self.data = data


class line_linked_list:
    def __init__(self):
        self.head = 0  # head data to save useful data
        self.first = Node(None)

        self.pointer = Node(None)

    def list_to_linked(self, a: list):
        self.chlist = a
        self.head = len(a)
        self.first.data = a[0]
        self.pointer = self.first
        for i in a[1:]:
            b = Node(i)
            self.pointer.next = b
            b = self.pointer
            self.pointer = self.pointer.next
            self.pointer.prev = b

    @staticmethod
    def merge_two_linear_linked_list(a: __init__, b: __init__):  # concat two list
        b.first.prev = a.pointer.prev
        # a.pointer=a.pointer.prev
        a.pointer.next = b.first
        a.head += b.head
        a.chlist.extend(b.chlist)
        return a

    @staticmethod
    def insert_node(a: Node, b: int, c: __init__):  # a is node b is possition
        # c is linked list of text
        # inplace insert
        i = 0
        k = c.first
        while (k != None):
            i += 1
            if (i == b):
                k.prev.next = a
                a.next = k
                a.prev = k.prev
                k.prev = a
                c.head += 1
                c.chlist.insert(b - 1, a.data)
                break
            else:
                k = k.next
        else:
            print("Not found that index! #error1058")

    @staticmethod
    def remove_node(b: int, c: __init__):
        i = 0
        k = c.first
        while (k != None):
            i += 1
            if (i == b):
                k.prev.next = k.next
                k.next.prev = k.prev
                c.head -= 1
                c.chlist.pop(b - 1)
                break
            else:
                k = k.next
        else:
            print("Not found that line! #error1076")

    @staticmethod
    def replace_node(a: str, b: int, c: __init__):
        # a is string data
        # b is position
        # c is linked list
        # inplace replace
        i = 0
        k = c.first
        while (k != None):
            i += 1
            if (i == b):
                k.data = a
                c.chlist[b - 1] = a
                break
            else:
                k = k.next
        else:
            print("Not found that line! #error1095")

    @staticmethod
    def swap_node(a: int, b: int, c: __init__):
        # a is int
        # b is second one
        # c is linked list
        # inplace replace
        a,b=min(a,b),max(a,b)
        an=None
        bn=None
        i = 0
        k = c.first
        while (k != None):
            i += 1
            if (i == b):
                bn=k
                an.data,bn.data=bn.data,an.data
                c.chlist[a-1],c.chlist[b-1]=c.chlist[b-1],c.chlist[a-1]
                break
            elif(i==a):
                an=k
                k=k.next
            else:
                k = k.next
        else:
            print("Not found that line! #error1095")


class Page:
    sep = "\$"

    def __init__(self, text):
        self.text = text
        self.prev_page = None
        self.next_page = None
        self.total_lines = self.count_lines()
        self.linear_list = self.line_list()[:-1]
        self.linked_list_of_lines = line_linked_list()
        self.linked_list_of_lines.list_to_linked(self.linear_list)

    def count_lines(self):
        r = str(self.text).count("\n")
        r = int(r)
        return r

    def parse_page(self):
        return self.text

    def line_list(self):
        pa="\n"
        b = re.split(pa,self.text)
        return b
    def find_in_page(self,s:str):
        i=0
        fin=[]
        k=self.linked_list_of_lines.first
        while(k!= None):
            if(s in k.data):
                fin.append((i,k.data))
            i+=1
            k=k.next
        return fin
    @staticmethod
    def make_it_new_page(text=None):
        temp = Page()
        temp.text = str(text) + Page.sep
        return temp

    def __str__(self):
        return self.text


def read_text_from_terminal():
    b = line_linked_list()
    a = []
    while ((s := input()) != "$finishtyping"):
        a.append(s)
    b.list_to_linked(a)
    return b
    # return first Node


class whole_file:
    # first page could handle all the file wihtout problem
    def __init__(self, path=None):  # contains parse method
        r = self.file_input_get(path)
        self.first_page = Page(r[0])
        self.current_page = self.first_page
        self.file_pointer = self.first_page
        self.total_page = len(r)
        self.page_number = 1
        r = r[1:]
        for i in r:
            self.file_pointer.next_page = Page(i)
            self.file_pointer.next_page.prev_page=self.file_pointer
            self.file_pointer = self.file_pointer.next_page
        # TODO:    save method

        self.now_we_run_the_program()

    def now_we_run_the_program(self):
        s = ""

        while (s != "$exit"):
            print("page number: {}".format(self.page_number))
            self.current_page.total_lines = self.current_page.linked_list_of_lines.head

            s = input()
            if (s.startswith("$")):  # it is a command
                if ("nextpage" in s):
                    self.page_number += 1
                    if (self.page_number <= self.total_page):
                        self.current_page = self.current_page.next_page
                    else:
                        print("No more page!")
                        self.page_number -= 1
                if ("previouspage" in s):
                    self.page_number -= 1
                    if (self.page_number > 0):
                        self.current_page = self.current_page.prev_page
                    else:
                        self.page_number += 1
                        print("No more page is available")
                if ("where" in s):
                    print("We are at page number {}".format(self.page_number))
                if ("lines" in s):
                    print(self.current_page.total_lines)
                if ("show" in s):
                    nes = s.strip()
                    patt = "(\d+)"
                    n = re.search(patt, nes).group()
                    n = int(n)
                    the_lines = self.current_page.linked_list_of_lines.chlist
                    print(the_lines[n])
                if ("append" in s):
                    p = read_text_from_terminal()
                    # self.current_page.linear_list.extend(p.chlist)
                    self.current_page.linked_list_of_lines = line_linked_list.merge_two_linear_linked_list(
                        self.current_page.linked_list_of_lines, p)

                if ("insert" in s):  # insert one line
                    nes = s.strip()
                    patt = "insert\((.+),(\d+)\)"
                    a = re.search(patt, s).groups()
                    n = int(a[1])
                    text = (a[0])
                    a = Node(text)
                    line_linked_list.insert_node(a, n, self.current_page.linked_list_of_lines)

                if ("remove" in s):
                    nes = s.strip()
                    patt = "(\d+)"
                    a = re.search(patt, s).group()
                    a = int(a)
                    line_linked_list.remove_node(a, self.current_page.linked_list_of_lines)
                if ("replace" in s):  # String and line number
                    nes = s.strip()
                    patt = "replace\((.+),(\d+)\)"
                    a = re.search(patt, s).groups()
                    n = int(a[1])
                    text = (a[0])
                    line_linked_list.replace_node(text,n,self.current_page.linked_list_of_lines)
                if ("swap" in s):
                    nes = s.strip()
                    patt = "swap\((\d+),(\d+)\)"
                    a = re.search(patt, s).groups()
                    b=int(a[0])
                    c=int(a[1])
                    line_linked_list.swap_node(b,c,self.current_page.linked_list_of_lines)
                if("find" in s):
                    op=self.first_page
                    nes = s.strip()
                    i=0
                    patt = "find\((.+)\)"
                    a = re.search(patt, s).groups()
                    finder=[]
                    while(op !=None):
                        i+=1
                        r=Page.find_in_page(op,a[0])
                        finder.extend([i,r])
                        op=op.next_page
                    if(len(finder)<=0):
                        print("Not found! #error276")
                    else:
                        print(finder,sep="\n")

                if()

            else:
                print("Not a command!")

        else:
            return 0

    def create_linked_mode(self, text=None):  # seperate all those pages
        rege = "\$"
        flist = re.split(rege, text)
        return flist[:-1]

    def file_input_get(self, file_path):
        self.file = open(file_path, 'r+')
        text = self.file.read()
        r = self.create_linked_mode(text)
        return r


path = "./problem/w.txt"
# file_input_get(path)

# i = open(path, 'r')
# a=str(i.read().)
# print(a)
# a = "!@#sep#@".strip()

# s = i.read()[:-10]
# c = re.split(a, s)
# s="show(5)"
# patt="(\d+)"
# a=re.search(patt,s).group()
# print(a)
# i = 0
# a = ""
# while (i < 5):
#     s = input()
#     a += "\n" + s
#     i += 1

whole_file(path)

# patt="insert\((.+),(\d+)\)"
# s="insert(sadsa,5)"
# a=re.search(patt,s).groups()
# print(a)