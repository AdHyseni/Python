"""
Dictionary ose fjalori eshte nje data type jo primitiv.
Ashtu si listat dhe touples eshte nje grumbullim te dhenash 
Ndryshe nga to dictionary eshte i ndertuar me key/value
Ku celsat jane te renditur dhe ku cdo celes i referohet nje vlere
Celsat jane unik 

"""

#Sintaksa
numrat = {1:'nje',2:'dy',3:'tre'}
print('Numrat',numrat)
#celsat jane 1,2,3
#vlerat per cdo celes jane: nje, dy, tre

#Vendosim nje vlere ne dictionary
numrat[4] = 'kater'
print('Numrat me vleren e shtuar',numrat)
 


#Printojm nje vlere ne baze te celsit perkates
print('Vlera qe i perket celsit 4 eshte ',numrat[4])

#Fshijme nje element
del numrat[4]
print('Fjalori mbas fshirjes', numrat)

#Merr te gjith celsat e fjalorit
celsat = numrat.keys()
print('Celsat/key jane: ',celsat)

vlerat = numrat.values()
print('Vlerat/values jane: ',vlerat)






