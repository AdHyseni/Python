# sintaksa e string
a = 'text' # pra cdo tekst i vendosur ne thonjza do te interpretohet ne string

# string do te quajm cdo sekuenc karakteresh

#Ashtu si listat ne mund
#Te gjejm gjatsine e string
len(a)
#printojme nje nder karakteret
print(a[2])
#te ndajme string duke perdorur slice
b = a[0:1]

#ndryshe nga listat string nuk mund te ndryshohet 
# b[0] = 'i' ky operim eshte i pa mundur ne string


# mund te kontrollojm nese nje vlere gjendet ne string 
fjala = 'pershendetje'
'p' in fjala

#Metodat
print(f'Capitalize {fjala.capitalize()} ')
print(f'Upper {fjala.upper()}')
print(f'Lower {fjala.lower()}')
index =fjala.find('r') #gjen ne cilin index ndodhet shkronja e kerkuar 
print(f'find {index}')
fjala = ' pershendetje '
#Strip fshin te gjithe hapsirat boshe
print(f'strip{fjala.strip()}')
#kontrollon nese fjali fillon me nje parameter apo jo 
print(fjala.startswith(' '))

