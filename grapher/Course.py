class Course:
    def __init__(self, code, title, semester, type, category, hcid, insertion_time):
        self.code = code
        self.title = title
        self.semester = semester
        self.type = type
        self.category = category
        self.hcid = hcid
        self.insertion_time=insertion_time





    def display(self):
        print("Code=>",'{:9s}'.format(self.code[0:9])," //Title:",'{:30s}'.format(self.title[0:30])," //Semester:",self.semester," //Type:",'{:20s}'.format(self.type[0:20])," //Category:",'{:15s}'.format(self.category[0:15])," //InsertionTime:",self.insertion_time)

    def __str__(self) -> str:
        return "Course code: " + str(self.code) + " Title: " + str(self.title) + " Semester: " + str(self.semester) + " Type: " + str(self.type) + " Category: " + str(self.category) + "Insertion Time: " + str(self.insertion_time)

    def __eq__(self, o) -> bool:
        return self.code == o.code and \
               self.semester == o.semester and \
               self.insertion_time == o.insertion_time and \
               self.category == o.category and \
               self.hcid == o.hcid

    def __hash__(self) -> int:
        # return super().__hash__()
        return hash((self.code, self.semester, str(self.hcid), self.insertion_time))

    def __lt__(self, other):
        return hash(self.code)<hash(other.code)
