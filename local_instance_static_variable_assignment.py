class Student:
    totalStudent =0
    totalFees = 10000

    def set_data(self,name,course,feesPaid):
        self.name = name
        self.course= course
        self.feesPaid = feesPaid
        Student.totalStudent+=1


    def remainingFees(self):
        return Student.totalFees-self.feesPaid
    
    def display(self):
        print("Name      :",self.name)
        print("Course    :",self.course)
        print("FeesPaid  :",self.feesPaid)
        print("Remaining fees :",self.remainingFees())
        print("------------------------------------------")

    def totalStudentAdmitted():
        print("Total Student   :",Student.totalStudent)


s1 =Student()
s1.set_data("Akash","python",5000)


s2 = Student()
s2.set_data("Ravi","java",7000)

s3 = Student()
s3.set_data("Suresh","C",9000)

s4 = Student()
s4.set_data("Ramesh","C++",1000)

s5 = Student()
s5.set_data("Raj","C#",2000)

s1.display()
s2.display()
s3.display()
s4.display()
s5.display()


Student.totalStudentAdmitted()



############ 22222222222222222222


class CollegeAdmission:
    totalAdmission =0
    cutoff_percentage =60

    def apply(self,name,percentage,course):
        self.name = name
        self.percentage = percentage
        self.course = course

        if self.percentage >= CollegeAdmission.cutoff_percentage:
            CollegeAdmission.totalAdmission+=1
            self.status = "Admitted"
        else:
            self.status = "Rejected"

    def display(self):
        print("name :",self.name)
        print("percentage :",self.percentage)
        print("course :",self.course)
        print("Status :",self.status)

    def totalAdmissions(self):
        print("total admissions :",CollegeAdmission.totalAdmission)

s1 = CollegeAdmission()
s1.apply("Akash",75,"CSE")
s1.display()
s1.totalAdmissions()

print("-------------------------")

s2 = CollegeAdmission()
s2.apply("Ravi",55,"ECE")
s2.display()
s2.totalAdmissions()


print("-------------------------")

s3 = CollegeAdmission()
s3.apply("Suresh",65,"MECH")
s3.display()
s3.totalAdmissions()