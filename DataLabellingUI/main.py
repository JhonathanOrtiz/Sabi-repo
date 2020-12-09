from streamlit import caching
from streamlit.script_runner import RerunException
import streamlit as st
import pandas as pd
from app.utils import categories, sub_categories, auth
from PIL import Image
from app.db_controller.orm import get_most_recent_default_product, pass_product_transformation, full_product_transformation, get_full_described_product_dict




PAGE_CONFIG = {'page_title': "Sabiapp", "page_icon": "smiley", "layout":"centered"}
st.beta_set_page_config(**PAGE_CONFIG)
image = Image.open("sabi.png")

def main():
  

  ## Sidebar
  user = st.sidebar.text_input("USUARIO")
  password = st.sidebar.text_input("CLAVE", value="", type="password")
  login = st.sidebar.checkbox("Login")
  categorie = categories()
  sub_categorie = sub_categories()
  current_default_product = get_most_recent_default_product()

  st.sidebar.markdown(" # Instrucciones")
  st.sidebar.markdown("Be careful")
  st.sidebar.markdown(" * La base de datos de dará un producto y un bodegón")
  st.sidebar.markdown(" * Completa los campos con la informacion requerida")
  st.sidebar.markdown(" * Si no puedes completar la información presiona SALTAR")
  st.sidebar.markdown(" * Presiona enviar y verifica la información")
  st.sidebar.markdown(" * Si la información es correcta presiona CONFIRMAR")

  st.image(image)
  st.title("Bienvenido/a a interfaz de etiquetado de datos de Sabi")
  st.subheader("Por favor lee las instrucciones")
 
  if login:
    
    if auth(user, password):
      st.markdown(" ### El producto a etiquetar es")
      st.write(get_most_recent_default_product()["product"])
      
      skip = st.button("Saltar Producto")
      if skip:
          pass_product_transformation(get_most_recent_default_product())
          st.text_input("Ingresa tu nombre para confirmar la operacion")

      st.markdown("### Título del producto")
      product = st.text_input("Ingresa el título del producto")

      st.markdown(" ### Marca")
      marca = st.text_input("Ingresa marca del producto")
    
      st.markdown(" ### Categoría")
      cat = st.selectbox("Selecciona una opción", categorie)

      st.markdown(" ### Sub categoría")
      sub_cat = st.selectbox("Selecciona una sub categoría", sub_categorie[cat])

      st.markdown(" ### Sinónimos y coloquios")
      st.write("Imagina como maneras en las que un usuario puede buscar el producto")
      sinon = st.text_input("Cada item debe ir separado por coma")
      
      st.markdown(" ### Descripción del producto")
      description = st.text_input("Decribe brevemente el producto")
      
      described_product = get_full_described_product_dict(product, cat, marca, sub_cat, sinon, current_default_product["owner"], description) 

      send = st.button("Revisar")
      confirm = st.button("Enviar")
         

      if send:
        if not marca or not sinon:
            st.error("Ingresa llena todos los campos por favor")
        st.warning("### Revisar la información enviada")
        st.markdown(" ")
        df = pd.DataFrame({"Producto": [product],
                          "Bodegón": [current_default_product["owner"]],
                          "Marca": [marca],
                          "Categoria": [cat],
                          "Sub Categoria": [sub_cat],
                          "Sinonimos y coloquios": [sinon],
                          "Descripción": [description]})
                          
        st.table(df)
    
    
      if confirm:
         full_product_transformation(current_default_product, described_product) 
         st.success("Informacion enviada correctamente")
         st.balloons()
    
    else:
       st.error("Clave o Usuario errado")
    

if __name__ == "__main__":
    main()
