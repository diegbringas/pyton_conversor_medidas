import pandas as pd 

#dataframe

data = {
    "Piezas": ["Pata", "Tablero", "Puerta", "Estante", "Panel Lateral"],
    "Centimetros": [40, 120, 60, 30, 180]
}

df = pd.DataFrame(data)

# Guardar el df en un archivo local

df.to_excel("muebles_medidas.xlsx", index=False)
