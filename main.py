from pyscript import display

a = {"Ricky, Mia, Zoe, Adam"} #art
m = {"Zoe, Adam, Mina, Emma"} #math

display(a - m, target='output')  #students who take art but not math
display(a.union(m), target='output')  #all students
display(a & m, target='output')  #students who take both art and math
display(a | m, target='output')  #students who take either art or math

display("Art Club", target="output")
display(a, target='output')

display("Math Club", target="output")
display(m, target='output')
