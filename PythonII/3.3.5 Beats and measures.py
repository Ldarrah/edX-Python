beats_per_measure = 4
measures = 5

for i in range(measures):
    n=1
    for beat in range(n,beats_per_measure+1):
         if beat <= beats_per_measure:
             print(beat)
    i += 1