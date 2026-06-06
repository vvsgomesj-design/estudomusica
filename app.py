import streamlit as st
from music21 import stream, note, meter, metadata, midi
import io

# --- 1. NÚCLEO DE TRANSFORMAÇÃO ---
def materializar_terapia_r3(texto_clinico, oitava_base=4):
    sc = stream.Score()
    sc.insert(0, metadata.Metadata())
    sc.metadata.title = 'Equação Diferencial R3 - Terapia'
    
    part = stream.Part()
    part.append(meter.TimeSignature('4/4'))
    
    escala = [f'C{oitava_base}', f'D{oitava_base}', f'E{oitava_base}', f'F{oitava_base}', 
              f'G{oitava_base}', f'A{oitava_base}', f'B{oitava_base}', f'C{oitava_base+1}']

    for char in texto_clinico.upper():
        if char.isalpha():
            idx = (ord(char) - ord('A')) % len(escala)
            if char in "AEIOU":
                part.append(note.Rest(quarterLength=0.125))
            else:
                n = note.Note(escala[idx])
                n.quarterLength = 2.0 
                if ord(char) % 2 == 0:
                    n.pitch.accidental = 'sharp'
                part.append(n)
        elif char == " ":
            part.append(note.Rest(quarterLength=1.0))
    sc.append(part)
    return sc

# --- 2. INTERFACE ---
st.set_page_config(page_title="Sistema Audível R3", layout="wide")
st.title("Aplicativo de Música Personalizada")

# Aqui usamos "Natureza" para a interface, que define a "Oitava" na lógica
elemento_natureza = st.sidebar.selectbox("Natureza da Terapia", ["Grave", "Média", "Aguda"])

relato = st.text_area("Relato do Paciente", height=150)
intervencao = st.text_area("Intervenção do Especialista", height=150)

# --- 3. PROCESSAMENTO ÚNICO ---
if st.button("Materializar Terapia Musical"):
    texto_total = f"{relato} {intervencao}".strip()
    
    if texto_total:
        try:
            # Lógica clara de Natureza -> Oitava
            oitava = 4 # Padrão
            if "Grave" in elemento_natureza:
                oitava = 2
            elif "Aguda" in elemento_natureza:
                oitava = 6

            musica = materializar_terapia_r3(texto_total, oitava)
            
            midi_buffer = io.BytesIO()
            musica.write('midi', fp=midi_buffer)
            midi_buffer.seek(0)
            
            st.download_button(
                label="Baixar Áudio-Terapia (MIDI)",
                data=midi_buffer,
                file_name="terapia_r3.mid",
                mime="audio/midi"
            )
            st.success("Terapia pronta para download!")
        except Exception as e:
            st.error(f"Erro ao processar música: {e}")
    else:
        st.warning("Por favor, preencha os campos de texto.")
