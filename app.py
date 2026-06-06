import streamlit as st
from music21 import stream, note, meter, metadata, midi
import tempfile
import os

# --- 1. NÚCLEO DE TRANSFORMAÇÃO MATEMÁTICA R3 ---
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

# --- 2. Interface ---
st.set_page_config(page_title="Sistema Audível R3", layout="wide")
st.title("Aplicativo de Música Personalizada")

# [Sidebar mantida igual]
# ... (seu código de sidebar aqui) ...

relato = st.text_area("Relato do Paciente", height=150)
intervencao = st.text_area("Intervenção do Especialista", height=150)

# --- 3. PROCESSAMENTO ---
if st.button("Materializar Terapia Musical"):
    texto_total = f"{relato} {intervencao}".strip()
    
    if texto_total:
        # Lógica de oitava
        oitava = 2 if "Grave" in "Mar" else (4 if "Média" in "Chuva" else 6)

        musica = materializar_terapia_r3(texto_total, oitava)
        
        # CORREÇÃO: Usar diretório temporário para evitar erro de permissão
        tmp_dir = tempfile.gettempdir()
       # Em vez de tempfile, vamos usar o diretório local onde o script corre
        fp = "terapia_r3.mid"
        
        # Gerar e salvar
        mf = midi.translate.streamToMidiFile(musica)
        mf.open(fp, 'wb')
        mf.write()
        mf.close()

        # Leitura binária
        with open(fp, "rb") as f:
            st.download_button(
                label="Baixar Áudio-Terapia (MIDI)",
                data=f,
                file_name="terapia_r3.mid",
                mime="audio/midi"
            )
        st.success("Equação musical gerada com sucesso!")

    else:
        st.warning("Preencha os campos.")