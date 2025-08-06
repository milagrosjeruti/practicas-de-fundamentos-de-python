print("¿¿¿¿CUANTO HAS  VIVIDO???")

from datetime import datetime

naciste = input("¿cuando naciste?" 
"(YYYY-MM-DD) > ")
fecha = datetime.strptime(naciste,
                          "%Y-%m-%d")
hoy = datetime.now()
dias = (hoy - fecha).days
print(f"Has vivido {dias} dias")
