highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"

print(highlighted_poems + '\n')

highlighted_poems_list = highlighted_poems.split(',')
print(highlighted_poems_list)
print('\n')

highlighted_poems_stripped = []
k=0
for statements in highlighted_poems_list:
  highlighted_poems_stripped.append(highlighted_poems_list[k].strip())
  k+=1
  
print(highlighted_poems_stripped)
print('\n')
i = 0
highlighted_poems_details = []
for items in highlighted_poems_stripped:
  highlighted_poems_details.append(highlighted_poems_stripped[i].split(':'))
  i+=1
  
print(highlighted_poems_details)

titles = []
poets = []
dates = []

for item in highlighted_poems_details:
  j = 0
  titles.append(item[j])
  j+=1
  poets.append(item[j])
  j+=1
  dates.append(item[j])

print('\n')
print(titles)
print(poets)
print(dates)

i=0
for items in titles:
  print("The poem {} was published by {} in {}".format(titles[i],poets[i],dates[i]))
  i+=1

