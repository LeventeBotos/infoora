# # ahol találsz benne olyan karakter sorozatot hogy két '-' között egy szám van, akkor azt ne írd vissza pl. a '- 3 -' kihagyandó.
# # a sorvégi 'új sor' karaktereket ne írd vissza, kivéve, ha a rákövetkező sor üres. 
# # Ha sorvégi elválasztás van, akkor az elválasztó jelet is hagyd ki. 

   

def remove_dash_number_dash(line):
    new_line = ""
    i = 0
    while i < len(line):
        if line[i] == '-':
            
            j = i + 1
            while j < len(line) and line[j] != '-':
                j += 1
            
            if j < len(line):
                candidate = line[i+1:j].strip()
                if candidate.isdigit():
                   
                    i = j + 1
                    continue
        
        new_line += line[i]
        i += 1
    return new_line


with open('/Users/leventebotos/infoora/szovegjavito/hf11ab.txt', 'r') as f:
    lines = f.readlines()

result = []

for i, line in enumerate(lines):
   
    processed_line = remove_dash_number_dash(line.rstrip('\n'))
    
  
    if i < len(lines) - 1:
       
        if lines[i+1].strip() != "":
            result.append(processed_line)
        else:
          
            result.append(processed_line + "\n")
    else:
       
        result.append(processed_line)


output = ''.join(result)
print(output)
