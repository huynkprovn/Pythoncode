Man, I know nothing about python, but may i suggest something?
Instead of returning a txt file, i'd sugget an html with the pokemons listed in the pokemonsniper2 url format.
Looking at your code on github i saw it's not a very complex language, the line would be something like that
Code:
"pokesniper2://"+name+"/"+str(lat)+","+str(lng)
or
Code:
"pokesniper2://"+name+"/"+str(lat)+","+str(lng)+"\n"
and you could add it after the usual
[pokemonId] [latitude, longitude] [expire time]
So it would look like
HTML Code:
[Bulbasaur] [40.746662,-74.004351] [7 Minutes, 51 Seconds]
pokesniper2://Bulbasaur/40.746662,-74.004351
I don't know what's the incompatibility between your program and pokesniper2, but the way i suggested would greatly help a lot of people right now.

That said, I'm no programmer, just a wannabe, feel free to ignore me, it was just an idea xD
