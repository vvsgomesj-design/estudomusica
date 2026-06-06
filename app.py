import streamlit as st
from music21 import stream, note, meter, metadata, midi
import io

# 1. Função de processamento musical (sempre no topo)
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

# 2. Interface (sem duplicações)
st.set_page_config(page_title="Sistema Audível R3", layout="wide")
st.title("Sistema Audível R3 - Terapia Musical")

elemento_natureza = st.sidebar.selectbox("Natureza da Terapia", ["Grave", "Média", "Aguda"], key="natureza_terapia_sidebar")
col1, col2 = st.columns(2)
with col1:
    nome_paciente = st.text_input("Nome do Paciente")
with col2:
    idade_paciente = st.number_input("Idade do Paciente", min_value=0, max_value=120, value=30)

relato = st.text_area("Relato do Paciente", height=150)
intervencao = st.text_area("Intervenção do Especialista", height=150)

# 3. Processamento ÚNICO
if st.button("Materializar Terapia Musical"):
    texto_total = f"Paciente: {nome_paciente}. Idade: {idade_paciente}. Relato: {relato}. Intervenção: {intervencao}".strip()
    
    if nome_paciente and (relato or intervencao):
        try:
            oitava = 4
            if "Grave" in elemento_natureza: oitava = 2
            elif "Aguda" in elemento_natureza: oitava = 6

            musica = materializar_terapia_r3(texto_total, oitava)
            mf = midi.translate.streamToMidiFile(musica)
            midi_bytes = mf.writestr()
            midi_buffer = io.BytesIO(midi_bytes)
            
            st.download_button(
                label="Baixar Áudio-Terapia (MIDI)",
                data=midi_buffer,
                file_name=f"terapia_{nome_paciente.replace(' ', '_')}.mid",
                mime="audio/midi"
            )
            st.success("Terapia musical gerada com sucesso!")
        except Exception as e:
            st.error(f"Erro ao gerar: {e}")
    else:
        st.warning("Por favor, preencha os campos obrigatórios.")

import streamlit as st
from music21 import stream, note, meter, metadata, midi
import io

# 1. Função de processamento musical (sempre no topo)
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

# 2. Interface (sem duplicações)
st.set_page_config(page_title="Sistema Audível R3", layout="wide")
st.title("Sistema Audível R3 - Terapia Musical")

elemento_natureza = st.sidebar.selectbox("Natureza da Terapia", ["Grave", "Média", "Aguda"])
col1, col2 = st.columns(2)
with col1:
    nome_paciente = st.text_input("Nome do Paciente")
with col2:
    idade_paciente = st.number_input("Idade do Paciente", min_value=0, max_value=120, value=30)

relato = st.text_area("Relato do Paciente", height=150)
intervencao = st.text_area("Intervenção do Especialista", height=150)

# 3. Processamento ÚNICO
if st.button("Materializar Terapia Musical"):
    texto_total = f"Paciente: {nome_paciente}. Idade: {idade_paciente}. Relato: {relato}. Intervenção: {intervencao}".strip()
    
    if nome_paciente and (relato or intervencao):
        try:
            oitava = 4
            if "Grave" in elemento_natureza: oitava = 2
            elif "Aguda" in elemento_natureza: oitava = 6

            musica = materializar_terapia_r3(texto_total, oitava)
            mf = midi.translate.streamToMidiFile(musica)
            midi_bytes = mf.writestr()
            midi_buffer = io.BytesIO(midi_bytes)
            
            st.download_button(
                label="Baixar Áudio-Terapia (MIDI)",
                data=midi_buffer,
                file_name=f"terapia_{nome_paciente.replace(' ', '_')}.mid",
                mime="audio/midi"
            )
            st.success("Terapia musical gerada com sucesso!")
        except Exception as e:
            st.error(f"Erro ao gerar: {e}")
    else:
        st.warning("Por favor, preencha os campos obrigatórios.")
