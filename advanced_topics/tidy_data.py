import pandas as pd 
df = pd.read_csv("attendance.csv")
df = df.rename(columns=({"Unnamed: 0":"name"}))
df = df.melt(id_vars=['name'])
final = pd.DataFrame()
atten = []
for n in df.name.unique():
    atten.append(df[df.name == n].value.values)

for x,n in zip(atten, df.name.unique()):
    quant = []
    out = 0
    for item in x:
        if item == "P":
            quant.append(1)
        if item == "T":
            quant.append(.9)
        if item == "H":
            quant.append(.5)
        if item == "A":
            quant.append(0)
    for item in quant:
        out += item
    out = out/len(quant)
    fo = pd.DataFrame({"name":[n],"score":out})
    final = final.append(fo, ignore_index=True)


cf = pd.read_csv("coffee_levels.csv")
cf.pivot(index='hour', columns='coffee_carafe')

cr = pd.read_csv("cake_recipes.csv")
cr = cr.melt(id_vars=["recipe:position"])
brin = cr["recipe:position"].str.split(':', expand=True)
cr["recipe"] = brin[0]
cr["rack"] = brin[1]
cr.drop(columns="recipe:position", inplace=True)
cr.rename(columns=({"variable":"temp", "value":"time"}, inplace=True))
cr.pivot_table(index=["recipe","rack"], columns='temp', values='time')


