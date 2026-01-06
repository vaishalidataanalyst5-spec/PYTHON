
# Assignment on class, object,variable type and functon Type


passing_marks = 35  # Global variable
class Student:
    instituteName = "AadiandPython" # staic/class variable
    totalSubMarks = 500             # staic/class variable
    
    def getStudentData(self,id,name,marks,course="IT"): # instace method and local variable id name marks and course is local and has default value 
        self.id = id #self used variable are instance variable
        self.name = name
        self.marks = marks
        self.course = course
    
    def calculatePercentage(self):   # instace method
        self.percentage = (self.marks/Student.totalSubMarks)*100
        return self.percentage
        
    def showGrade(self): # instace method
        if self.percentage >= passing_marks:
            if self.percentage >=90:
                return "Grade A"
            elif self.percentage >=75:
                return "Grade B"
            elif self.percentage >=60:
                return "Grade C"
            else:
                return "Grade Pass"
        else:
            return "You are Fail"
    
    @classmethod
    def rename(cls):
      cls.instituteName = "AadiandPythonWithSQL"  
      print("Institute Name is :",cls.instituteName)

    @staticmethod
    def courseDetails():
        print("This is IT course")
        print("each subject has 100 marks")
        print("subject 1 ---Data Structure")
        print("Sunject 2 ---C ")
        print("subject 3 --- MYSQL")
        print("Subject 4 --- CPP")
        print("Subject 5 --- Python")

    def showStudentDetails(self):   # instace method
        print("==================================================")
        Student.rename() #calling of classmethod using class name
        Student.courseDetails() #calling of static method using class name
        print("-------------------------------")
        print("Student id -",self.id)
        print("Student Name -",self.name)
        print("Student Marks -",self.marks)
        print("Student Course -",self.course)
        print("Student percentage -",self.calculatePercentage())
        print("Student Grade -",self.showGrade())


    
    
s1 =Student ()  #object
s1.getStudentData(1,"ram",350,"IT") #calling instance method using object
#s1.calculatePercentage()
s1.showStudentDetails()  #calling instance method using object
#s1.showGrade()

s2 = Student()  #object
s2.getStudentData(2,"shyam",80)
s2.showStudentDetails()

s3 = Student()  #object
s3.getStudentData(3,"Geeta",490)
s3.showStudentDetails()

s4 = Student()  #object
s4.getStudentData(4,"Seeta",230)
s4.showStudentDetails()

