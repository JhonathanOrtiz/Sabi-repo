def categories():
    categories = sorted(["Frutas y Verduras", 
                "Golosinas y Snacks",
                "Viveres",
                "Bebidas",
                "Condimentos y Especias",
                "Enlatados",
                "Granos y Cereales",
                "Carniceria",
                "Embutidos y Lacteos",
                "Aseo Personal y Cosmeticos",
                "Hogar",
                "Maternidad",
                "Farmacia",
                "Mascotas",
                "Miscelaneos",
                "Panaderia y Pasteleria",
                "Untables",
                "Comida preparada",
                "Fitness",
                "Kosher",
                "Vehiculos",
                "Vegano",
                "Papeleria"])
    return categories

def sub_categories():
    sub_categories = {"Frutas y Verduras": sorted(["Frutas naturales", "Frutas empacadas", "Veduras naturales", "Frutas empacadas", "Frutos secos"]), 
                "Golosinas y Snacks": sorted(["Dulces", "Salados", "Helados", "Chocolates", "Galletas"]),
                "Viveres": sorted(["Harinas", "Salsas", "Pastas", "Huevos", "Vinagres", "Aderezos", "Aceites", "Café", "Azucar y Endulzantes", "Harinas", "Sopas"]),
                "Bebidas": sorted(["Gaseosas", "Licores", "Jugos", "Vinos y Espumates", "Te"]),
                "Condimentos y Especias":sorted(["Sal", "Cubitos", "Especias", "Condimentos"]),
                "Enlatados": sorted(["Atun", "Sadinas", "Almibar", "Encurtidos"]),
                "Granos y Cereales": sorted(["Arroces", "Avena", "Frijoles", "Lentejas", "Linaza", "Maiz", "Cereales"]),
                "Carniceria": sorted(["Cane de res", "Pollos", "Pescados", "Mariscos y Calamares", "Cerdo", "Cordero", "Ovejo"]),
                "Embutidos y Lacteos": sorted(["Leches", "Quesos", "Jamon", "Mantequillas y Marganrinas", "Chorizos, Salchichas y Salchichones", "Yogurts"]),
                "Aseo Personal y Cosmeticos": (["Maquillaje", "Cuidado del cabello", "Cuidado corporal", "Perfumes y Desodorantes", "Depilacion", "Preservativos y Anticonceptivos"]),
                "Hogar": sorted(["Bolsas", "otros", "Detergentes", "Vajilla", "Cocina", "Insectisida", "Patio y Jardín", "Decoración", "Cuartos", "Aromatizantes y Sprays", "Papel y plástico"]),
                "Maternidad": ["Biberones", "Pañales", "Utensilios para comdia", "Jugues", "Cuidado y Aseo"],
                "Mascotas": sorted(["Comida", "Aseo", "Utensilios"]),
                "Miscelaneos": sorted(["Pilas", "Telefonía"]),
                "Panaderia y Pasteleria": sorted(["Pan", "Tortas"]),
                "Farmacia": sorted(["Medicamentos con Prescripcion", "Medicamentos sin Prescripción", "Primeros Auxilios"]),
                "Untables": sorted(["Mermeladas", "Cremas", "Siropes", "Mantequillas saborizadas", "Otros"]),
                "Comida preparada": sorted(["Desayunos y meriendas", "Empanadas", "Pasapalos", "Alumerzos", "Otros"]),
                "Fitness": sorted(["Ropa", "Calzado", "Equipamento", "Sulplementos", "Dulces Fitness", "Gluten Free"]),
                "Kosher": sorted(["Granos y Cereales", "Carnes", "Viveres", "Bebidas", "Golosinas y Snacks", "Nutricion"]),
                "Vehiculos": sorted(["Fluidos", "Accesorios", "Repuestos", "Herramientas", "Baterias"]),
                "Vegano": sorted(["Carne de soya", "Leche vegetal"]),
                "Papeleria": sorted(["Utiles Escolares", "Paperleria en General"])}
    return sub_categories

def credentials():
    users = ["all-backend-gerson", "all-backend-sandra", "all-backend-juan", "all-backend-jhon", "all-admin"]
    passwords ={"all-backend-gerson":["gerson"], 
                "all-backend-sandra":["sandra"], 
                "all-backend-juan":["juan"], 
                "all-backend-jhon": ["jhonathan"],
                "all-admin":["admin"]}

    return users, passwords

def auth(user, password):

    users , passwords = credentials()
    
    if user in users and password in passwords[user]:
        return True
    else:
        return False
        
