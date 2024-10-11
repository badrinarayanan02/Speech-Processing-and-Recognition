# Speech to Text Implementation

# Loading the libraries

import streamlit as st # For User Interface
import speech_recognition as sr # For Recognizing and Conversion

# This function is responsible to record the audio

def record_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("Speak Something")
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=10)
            return audio
        except sr.WaitTimeoutError:
            st.warning("No Speech Detected")
            return None
        
# This function is responsible to convert speech to text

def speech_to_text(audio):
    
    r = sr.Recognizer()
    try:
        st.info("Recognizing...")
        text = r.recognize_google(audio)
        st.success(f'Speech Recognized: "{text}"')
        return text
    except sr.UnknownValueError:
        st.warning("Could not understand audio. Please try speaking more clearly.")
        return None
    except sr.RequestError as e:
        st.error(f"Could not request results {e}")
        return None
    
# Main Functionality

def main():
    st.title("Voxscribe")
    st.write("Converts your speech to text in real time")
    
    if 'text_output' not in st.session_state:
        st.session_state.text_output = ""
        
    col1, col2 = st.columns(2)
        
    with col1:
        if st.button("Start Listening"):
            audio = record_audio()
            if audio:
                text = speech_to_text(audio)
                if text:
                    st.session_state.text_output += f"{text}\n"
                    st.success("Converted Successfully")
                else:
                    st.warning("Failed")
            else:
                st.warning("No audio Recorded")
                
    with col2:
        if st.button("Clear Text"):
            st.session_state.text_output = ""
    
    st.text_area('Converted Text: ', value = st.session_state.text_output, height=300)
    
    st.markdown("Instructions:")
    st.write("1. Click 'Start Listening' and speak clearly into your microphone.")
    st.write("2. Wait for the system to recognize and convert your speech.")
    st.write("3. The converted text will appear in the text area below.")
    st.write("4. If the speech is unclear, you'll be prompted to try again.")
    st.write("5. Use the 'Clear Text' button to reset the output.")

if __name__ == "__main__":
    main()    
    
# Conclusion

# Thus developed simple speech to text system. It takes the speech input from the user and it converts into text. Speech Recognition library is utilized for the whole process. Additionaly exceptional handling is performed for better efficiency.



