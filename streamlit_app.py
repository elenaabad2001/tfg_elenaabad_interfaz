#LIBRERÍAS
import streamlit as st 
import langchain 
import chromadb 
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())
import os 
from langchain.llms import OpenAI


class StreamlitApp:
    def __init__(self):
        st.title('Interfaz TFG Elena Abad.')
        # Ruta al directorio de documentos.
        self.docs_dir = "/Users/UniversidadElenaAbad/Desktop/TFG1/PROGRAMACION2/docs"
        self.openai_api_key = st.sidebar.text_input('OpenAI API Key', type='password')
        #Asegurar que la ruta sea absoluta.
        self.docs_dir = os.path.abspath(self.docs_dir)

    def generate_response(self, input_text):
        llm = OpenAI(temperature=0.7, openai_api_key=self.openai_api_key)
        response = llm(input_text)
        return response

    def run(self):
        with st.form('my_form'):
            text = st.text_area('Introduzca una instrucción', 'Una persona tiene un salario neto de 2000 euros al mes. Solicita una hipoteca por importe de 400000 euros. La tasa de riesgo hipotecario que prescriben entidades como el Banco de España es de un 30 por ciento del salario mensual.¿Cuánto tiene que pagar al mes?')
            submitted = st.form_submit_button('Enviar')
            
            if not self.openai_api_key.startswith('sk-'):
                st.warning('Por favor, introduzca su clave de OpenAI (OpenAI API Key).', icon='⚠')

            if submitted and self.openai_api_key.startswith('sk-'):
                response = self.generate_response(text)
                st.info(response)

if __name__ == "__main__":
    app = StreamlitApp()
    app.run()