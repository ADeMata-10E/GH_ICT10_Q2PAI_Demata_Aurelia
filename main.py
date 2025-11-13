from pyscript import display

a = {"Ricky, Mia, Zoe, Adam"} #art
m = {"Zoe, Adam, Mina, Emma"} #math

display(a - m, target='output')  #students who take art but not math
display(m - a, target='output')  #students who take math but not art
display(a & m, target='output')  #students who take both art and math
display(a | m, target='output')  #students who take either art or math