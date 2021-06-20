class Classroom:
  
  classlist = {}
  
  def _init_(self, room_number, teacher, students = None):
    self.room_number = room_number
    self.teacher = teacher
    self.students = students if students else []
    
  
  def add_student(self, classlist):
    for i in classlist:
      return classlist[i].append(self.student)
    
  def remove_student(self,name):
    if name in self.students:
     self.students.remove(name)
      
    else:
      print ("That name does not exist")      
   
    
  def matches_age(self):
    new_age = input("Enter age as a number: ")
    if new_age == self.students.age:
      self.students.append(new_age)
  
       
  
  def get_classlist(self, classlist):
    for i in classlist:
      print(i, ":", classlist[i])
