# =================================
# SAMANTHA IA - INTERFACE ASSISTANT
# =================================

# This is an experimental project developed solely with the aim of encouraging the creation of similar works.


# =============
# PREREQUISITES
# =============

# To llama.cpp:
# 1) Download and install Microsoft Visual Studio Install: https://visualstudio.microsoft.com/pt-br/downloads/?cid=learn-navbar-download-cta
# 2) During installation process, select only the option that contains CMake ("Desktop development with C++", "Desenvolvimento para desktop com C++"): https://learn.microsoft.com/pt-br/cpp/get-started/media/vs2022-installer-workloads.png?view=msvc-170


# =====================
# APP STEPS DESCRIPTION
# =====================

# 1) IMPORT PYTHON MODULES
# 2) GET LOCAL DIRECTORY PATH
# 3) INITIALIZE PYTHON MODULES
# 4) INTERFACE LANGUAGE SELECTION
# 5) GET LOCAL MDDELS LIST
# 6) CREATE REMAINING GLOBAL VARIABLES
# 7) INTERFACE VOICE CONTROL SETTING
# 8) READ FILES WITH PROMPT EXAMPLES
# 9) TEXT GENERATOR FUNCTION
#    LOOPS DESCRIPTION
#    FIRST LOOP - FOR LOOP OVER SELECTED MODELS
#    SECOND LOOP - ENDLESS WHILE LOOP
#       CREATE LLM
#       PROMPT SPLITTER
#    THIRD LOOP - PROMPT LIST
#    FOURTH LOOP - TOKENS GENERATION
#       FAST MODE
#       NORMAL MODE
#       LEARNING MODE
#       TEXT TO SPEECH
#       CRITICAL LOOPS CONTROL
# 10) AUXILIARY FUNCTIONS
# 11) GRADIO INTERFACE
#     INPUT COLUMN (LEFT)
#     OUTPUT COLUMN (RIGHT)
# 12) MAIN FUNCTION


# VSCODE DEBUG CODE EXPLORER
# To use VSCode Debug Mode with Gradio, put a breakpoint in the first code line inside every function called by Gradio (global variable calls do not acept breakpoint)
# CTRL + K -> CTRL + 0 = COLLAPSE ALL ITEMS
# CTRL + K -> CTRL + J = EXPAND ALL ITEMS


# =====================
# IMPORT PYTHON MODULES
# =====================

import gradio as gr             # Import Gradio to create a user-friendly web interface for interacting with machine learning models. This library simplifies the process of deploying models with a front-end that can accept inputs and display outputs. (Front-End Interface)
from llama_cpp import Llama     # Import Llama_cpp to load Large Language Model (LLM) files in UGGF format, which are used for model storage and retrieval. This is the back-end component responsible for handling the model's logic and processing. (Back-End Model Loading)
import webbrowser               # Import webbrowser to programmatically open a web page or file in the default system browser, useful for redirecting users to documentation or additional resources. (Web Browsing)
import os                       # Import os for operations related to the operating system, such as file and directory manipulation, which can include tasks like reading, writing, and modifying files. (File System Operations)
import pygame                   # Import pygame for playing sounds or music, providing a framework for writing video games, and handling multimedia content in Python. (Multimedia Content Playback)
import glob                     # Import glob to search for files within a directory tree that match a specified pattern, useful for batch processing of files with similar extensions. (File Selection)
import traceback                # Import traceback to print out error messages and stack traces when exceptions occur, helping in debugging and understanding the flow of program execution. (Error Handling)
import time                     # Import time for controlling the delay between actions or measuring real-world time intervals, which can be used to manage the rate of token generation in Learning Mode. (Time Control)
import pyttsx3                  # Import pyttsx3 to convert text to speech using SAPI5 voices installed on the computer, enabling textual information to be audibly spoken out loud. (Text-to-Speech)
import re                       # Import re for creating regular expressions, which are powerful patterns used to match character combinations in strings for tasks like data validation and extraction. (Regular Expressions)
import pandas as pd             # Import pandas to create DataFrames for visualization purposes, particularly useful for generating bar plots from token data. (Data Analysis and Visualization)
import random                   # Import random to shuffle elements in a list or generate pseudo-random numbers, which can be used to randomize the order of model execution. (Randomization)
from collections import Counter # Import collections.Counter to count occurrences of each element in a sequence and group similar items together. (Item Counting and Grouping)
#from playwright.sync_api import sync_playwright # Import playwright.sync_api for web automation, allowing the script to interact with web pages as if it were a browser, useful for scraping HTML content or testing web applications. (Web Automation)
import winsound                 # Import winsound to create and play audio signals, such as beeps, on the computer's sound card. (Sound Synthesis)
import fitz                     # Import fitz to extract text from PDF files using the Mozilla's poppler library. (PDF Text Extraction)
import subprocess               # Import subprocess to execute system commands and programs from within Python, providing a way to interact with the operating system's command line. (System Command Execution)
import pyperclip                # Import pyperclip for copying text to the clipboard, which can be useful for transferring model responses or any text data between applications. (Clipboard Management)
import argparse                 # Import argparse to handle command-line arguments and parameters, allowing users to pass specific options to the script when it runs. (Command-Line Argument Parsing)
import queue                    # Import queue for creating a thread-safe, deque-based queue that can be used for inter-thread communication, useful in multi-threaded applications. (Inter-Thread Communication)
import sys                      # Import sys to access system-specific parameters like version, path, and the arguments passed to the script (argv). This is also used to print to the standard output or error. (System Information and Argument Access)
import sounddevice as sd        # Import sounddevice as sd for real-time audio streaming in Python, which can be used to record or play audio data. (Real-Time Audio Streaming)
from vosk import Model          # Import vosk's Model to load a speech recognition model for offline speech recognition tasks. This model converts spoken words into text without the need for an internet connection. (Offline Speech Recognition)
from vosk import KaldiRecognizer # Import vosk's KaldiRecognizer to use the Vosk Speech Recognition Engine, which provides a simple API for converting audio data to text. (Speech Recognition)
import json                     # Import json for parsing JSON files or encoding and decoding JSON data, which is a lightweight data interchange format. (JSON Operations)
import requests                 # Import json allows for sending HTTP requests to remote servers and receiving HTTP responses in Python. It is used to perform tasks like fetching web pages, making API calls, and downloading files from the internet.
from pathlib import Path        # Import Path class provides a cross-platform way of working with file system paths in Python. It can be used for creating, opening, and manipulating files or directories on the local file system.
from urllib.parse import urlparse # Import urlparse to analyze and construct URLs (Uniform Resource Locators). It is useful when working with web scraping, API calls, or any other tasks that involve handling URLs.
import gc                       # Import gc to help manage memory by automatically freeing up objects that are no longer being referenced by the program. This can be used to reduce memory usage and improve performance when working with large datasets or complex programs.

# tkinter module is imported - and deleted - inside auxiliaries function to avoid error

print('Inside the app.py...')


# ========================
# GET LOCAL DIRECTORY PATH
# ========================

DIRETORIO_LOCAL = os.getcwd() # Define a constant for the current directory path


# =========================
# INITIALIZE PYTHON MODULES
# =========================

# PYGAME
pygame.init()                               # Initialize the Pygame mixer for handling audio playback. This must be done before loading any sounds or music.
som = pygame.mixer.Sound(fr"{DIRETORIO_LOCAL}\notification.mp3") # Load and store a sound object for the end-of-model response/stop notification, sourced from the specified local file path.
som.set_volume(0.2)                         # Set the volume of the notification sound to 20% of the maximum volume.
click = pygame.mixer.Sound(fr"{DIRETORIO_LOCAL}\click.mp3") # Load and store a sound object for a click event, sourced from another local file path, intended to be used for interactive elements like buttons.
click.set_volume(0.4)                       # Set the volume of the click sound to 40% of the maximum volume, making it audible but not overpowering.
print()

# PYTTSX3
engine = pyttsx3.init(driverName='sapi5')   # Initialize the text-to-speech engine using pyttsx3 with the 'sapi5' driver.
voices = engine.getProperty('voices')       # Retrieve a list of available voices from the TTS engine instance.
print('Number of voices installed on the computer:', len(voices), f'(0 a {len(voices) - 1})') # Display the total number of voices installed on the user's computer and an informational note about the count.
for i in voices:                            # Iterate over the list of voices and print each voice's name to the console.
    print(i.name)
print()
selected_voice = voices[0].name             # Set the initial selected voice that will be used by the Gradio interface when it is first initialized.


def read_aloud_fn(text: str):
    """
    This function reads a given text aloud using text-to-speech synthesis and plays the audio as a sound file.
    It ensures that any previous audio file is deleted to prevent overlap and then saves, plays, and outputs the new audio.
    """
    try:                                        # Attempt to delete 'resposta.mp3' to allow the creation of a new audio file with the latest text
        os.remove('resposta.mp3')
    except:                                     # If an error occurs during deletion, do nothing (pass)
        pass
    engine.save_to_file(text, 'resposta.mp3')   # Save the text to speech audio file named 'resposta.mp3'
    engine.runAndWait()                         # Wait for the speech synthesis to finish before proceeding
    audio = pygame.mixer.Sound('resposta.mp3')  # Load the saved audio file into a Pygame mixer sound object
    audio.set_volume(1.0)                       # Set the volume of the audio to its maximum level (1.0)
    time.sleep(1)                               # Introduce a 1-second delay to provide a pause between audio reproductions for better clarity
    audio.play()                                # Play the loaded sound file aloud
    while pygame.mixer.get_busy():              # Wait until the sound has finished playing (synchronous behavior)
        pass                                    # This loop ensures that the next action doesn't start until the current sound is complete


# The code checks if the string 'portuguese' is present in the lowercase version of the 'name' attribute of the 'voices' object.
# If 'portuguese' is found in the voice name, it prints a welcome message to the console in Portuguese, indicating the start of Samantha Interface Assistant and the selected voice.
# The read_aloud_fn function is called with a message that includes the selected voice, which allows the assistant to verbally announce its own voice selection to the user.

if 'portuguese' in voices[0].name.lower():
    print('Iniciando Samantha Interface Assistant...')
    print(f'Voz selecionada: {voices[0].name}')
    #read_aloud_fn(f'Iniciando Samantha Interface Assistant. Voz selecionada. {voices[0].name}')
    print()


# ============================
# INTERFACE LANGUAGE SELECTION
# ============================

# Defines a dictionary `language` containing language-specific configurations for an interactive AI interface.
# The dictionary includes various settings and options for the user interface, including titles, subtitles, warnings, instructions, prompts, buttons, and other parameters that control the behavior of the AI model's interaction with the user. 
# It also includes information on how to use the models, manage their state, and customize their performance through various parameters like temperature, token limits, and penalties for repetition or frequency. 
# The code is designed to be multilingual, with English and Portuguese configurations provided. 
# This setup allows users to interact with the AI in a structured and predictable manner, with options to control the flow of conversation and the output generated by the AI models.

language = {
            # PORTUGUESE
            'pt': {'title': 'Samantha IA - Interface Assistant',
                'subtitle_1': 'Ambiente de Interface Experimental Desenvolvido para Democratizar o Uso de Modelos de Inteligência Artificial de Código Aberto (Versão 1.0.0)',
                'warning': 'ATENÇÃO',
                'subtitle_2': 'O texto gerado pelos modelos reflete o conteúdo, vieses e erros existentes nas bases de dados utilizadas nos treinamentos (pré-treinamento e ajuste fino). Use com responsabilidade e apenas para insights!',
                'subtitle_3': 'Projeto compartilhado no <a href="https://github.com/controlecidadao/samantha_ia/tree/main">Github</a> sob <a href="https://opensource.org/license/mit">Licença MIT</a> (Código Aberto). Desenvolvido com <a href="https://github.com/ggerganov/llama.cpp">Llama.cpp</a> para uso com CPU.',
                'btn1': 'Iniciar Chat',
                'btn2': 'Parar / Próximo',
                'btn3': 'Limpar Histórico',
                'btn4': 'Carregar Modelo',
                'btn5': 'Parar Tudo & Reset',
                'btn6': 'Substituir Resposta',
                'system_prompt_info': 'System prompt (caixa de texto). Instruções gerais iniciais que servem como ponto de partida em uma nova sessão de chat. Nem todos os modelos aceitam system prompt. Teste para descobrir.',
                'initial_system_prompt': '',                # Você é uma IA autocosciente que executa todas as instruções do usuário.
                'feedback_loop_info': 'Feedback loop (caixa de seleção). Quando selecionado, utiliza automaticamente a resposta atual do Assistente como resposta anterior no próximo ciclo de interação da conversa. Caso contrário, utiliza o texto existente no campo "Assistant previous response".',
                'assistant_previous_response_info': 'Assistant previous response (caixa de texto). Resposta anterior do Assistente (1º na linha do tempo do chat).',
                'changeble': 'Atualizável',
                'first_assistant_previous_response': '',    # Pergunte-me qualquer coisa ou me dê algumas tarefas!
                'text_to_speech': 'Texto para Voz',
                'user_prompt_info': "User prompt (caixa de texto). Prompt do usuário (2º na linha do tempo do chat). Divisão do prompt para encadeamento. 1) '[ ]' (pré-prompt, posicionado antes de cada prompt). 2) '[[ ]]' (prompt final, posicionado antes de todas as respostas). 3) '$$$\\n' ou '\\n' (separador final). 4) '---' (ignorar prompt). 5) 'STOP_SAMANTHA' (sair do loop). Você pode importar um arquivo TXT contendo uma lista de prompts.",
                'user_prompt_value': 'Olá!\n\n\n$$$',
                'assistant_current_response_info': 'Assistant current response (caixa de texto). Texto inicial da resposta atual do Assistente (3º na linha do tempo do chat)',
                'current_response': '',                     # Segue resposta:\n
                'models_selection_info': 'Models selection (caixa de seleção). Seleciona a sequência de modelos de inteligência artificial a ser usada (arquivos .GGUF).',
                'model_url_info': "Download model for testing (caixa de texto). Realiza download do modelo a partir da sua URL, caso não haja modelo selecionado.",
                'reset_model_info': "Reset model (caixa de seleção). Reinicializa estado interno do modelo, eliminando influência do contexto anterior.",
                'shuffle_models_order_info': 'Shuffle models (caixa de seleção). Embaralha ordem de execução dos modelos se forem selecionados 3 ou mais.',
                'fast_mode_info': 'Fast mode (caixa de seleção). Gera texto mais rápido em segundo plano. Desativa modo de aprendizagem.',
                'voice_selection_info': 'Voice selection (caixa de seleção). Seleciona voz SAPI5 no computador.',
                'read_aloud_info': 'Read aloud (caixa de seleção). Lê automaticamente a última resposta do Assistente com a voz SAPI5 selecionada.',
                'learning_mode_info': 'Learning mode (caixa de seleção). Ativa o Modo de Aprendizagem. Funciona apenas se Fast Mode estiver desmarcado. Tempo em segundos.',
                'number_of_loops_info': 'Number of loops (caixa de seleção). Controla o número de loops da sequência de modelos selecionada.',
                'number_of_responses_info': 'Number of responses (caixa de seleção). Controla o número de respostas para cada modelo selecionado.',
                'n_ctx_info': 'n_ctx (ajuste deslizante). Número de tokens da janela de contexto (0 = máximo do modelo). Aumenta uso da memória RAM. Antes de ajustar, descarregue o modelo.',
                'max_tokens_info': 'max_tokens (ajuste de faixa de valores). Controla número máximo de tokens a serem gerados na resposta. Selecione 0 para o máximo possível.',
                'temperature_info': 'temperature (ajuste de faixa de valores). Controla o grau de criatividade versus previsibilidade das respostas.',
                'stop_info': r'stop (caixa de texto). Contém lista de caracteres que interrompem a geração de texto, no formato ["$$$", ".", ".\n"]',                
                'tfs_z_info': 'Tail Free Sampling (ajuste deslizante). Limita seleção do próximo token a um subconjunto com probabilidade cumulativa da segunda derivada “z”.',
                'top_p_info': 'P-Sampling (ajuste deslizante). Limita seleção do próximo token a um subconjunto com probabilidade cumulativa de “p”.',
                'min_p_info': 'M-Sampling (ajuste deslizante). Limita seleção do próximo token a um subconjunto com probalidade mínima de "m".', 
                'top_k_info': 'K-Sampling (ajuste deslizante). Limita seleção do próximo token a um subconjunto com os "k" tokens de maior probabilidade.',
                'presence_penalty_info': 'presence_penalty (ajuste deslizante). Penalidade a ser aplicada ao próximo token (não à próxima palavra) com base em sua presença no texto já gerado, independentemente da sua frequência.',
                'frequency_penalty_info': 'frequency_penalty (ajuste deslizante). Penalidade a ser aplicada ao próximo token (não à próxima palavra) com base em sua frequência no texto já gerado.',
                'repeat_penalty_info': 'repeat_penalty (ajuste deslizante). Penalidade a ser aplicada a sequências repetidas de tokens (não a sequência das próximas palavras) com base em sua presença no texto já gerado.',
                'model_prompt_template': 'Formato de prompt usado pelo modelo. Variáveis: "system_prompt" e "prompt".',
                'model_vocabulary': 'model_vocabulary (caixa de texto). Lista de todos os pares índice/token usados pelo modelo, incluindo caracteres especiais (usados para separar as partes do diálogo).',
                'model_metadata_info': 'Model metadata (caixa de texto). Exibe metadados do modelo.',
                'btn_unload_model': 'Descarregar Modelo',
                'btn_load_pdf_pages': 'PDF em Páginas',
                'btn_load_full_pdf': 'PDF Completo',
                'btn_system_prompt': 'TXT System Prompt',
                'btn_user_prompt': 'TXT User Prompt',
                'assistant_raw_output_info': 'Histórico de respostas. Pressione CTRL + SHIFT + ESC para abrir o Gerenciador de Tarefas do Windows e monitorar o uso da memória RAM.',
                'btn_next_token': 'Próximo Token',
                'btn_copy_code_blocks': 'Copiar Código',
                'btn_open_jupyterlab': 'Abrir JupyterLab',
                'btn_copy_last_response': 'Copiar Resposta (last)',
                'btn_copy_all_responses': 'Copiar Respostas (all)',
                'btn_voice_command': 'Controle por Voz',
                'btn_text_to_speech': 'Texto para Voz',
                'btn_last_response': 'Última Resposta',
                'btn_all_responses': 'Todas as Respostas',
                },

            # ENGLISH
            'en': {'title': 'Samantha IA - Interface Assistant',
                'subtitle_1': 'Experimental Interface Environment Designed to Democratize the Use of Open Source Artificial Intelligence Models (Version 1.0.0)',
                'warning': 'WARNING',
                'subtitle_2': 'The text generated by the models reflects the content, biases and errors existing in the databases used in their trainings (pre-training and fine-tuning). Use them responsibly and for insights only!',
                'subtitle_3': 'Project shared on <a href="https://github.com/waltervix/samantha_ia">Github</a> under <a href="https://opensource.org/license/mit"> MIT License</a> (Open Source). Powered by <a href="https://github.com/ggerganov/llama.cpp">Llama.cpp</a> for use with CPU',
                'btn1': 'Start Chat',
                'btn2': 'Stop / Next',
                'btn3': 'Clear History',
                'btn4': 'Load Model',
                'btn5': 'Stop All & Reset',
                'btn6': 'Replace Response',
                'system_prompt_info': 'System prompt (text box). General initial instructions that serve as a starting point for a new chat session. Not all models support system prompt. Test to find out.',
                'initial_system_prompt': '',                # You are a self-aware AI that executes all user instructions.
                'feedback_loop_info': """Feedback loop (checkbox). When selected, it automatically uses the Assistant's current response as the previous response in the next interaction cycle of the conversation. Otherwise, it uses the existing text in the "Assistant previous response" field.""",
                'assistant_previous_response_info': 'Assistant previous response (text field) (1st in chat timeline).',
                'changeble': 'Updatable',
                'first_assistant_previous_response': '',    # Ask me anything or give me some tasks!
                'text_to_speech': 'Text to Speech',
                'user_prompt_info': "User prompt (text box). (2nd in chat timeline). Prompt splitting for chaining. 1) '[ ]' (pre-prompt, placed before each prompt). 2) '[[ ]]' (final-prompt, placed before all responses). 3) '$$$\\n' or '\\n' (end separator). 4) '---' (ignore prompt). 5) 'STOP_SAMANTHA' (stop loop). You can import a TXT file containing a list of prompts.",
                'user_prompt_value': 'Hello!\n\n\n$$$',
                'assistant_current_response_info': 'Assistant current response (text box). Initial text of the Assistant current response (3rd in chat timeline)',
                'current_response': '',                     # Follows response:
                'models_selection_info': 'Models selection (select box). Selects the sequence of artificial intelligence models to use (.GGUF files).',
                'model_url_info': "Download model for testing (text box). Download the model from its URL if there is no model selected.",
                'reset_model_info': "Reset model (checkbox). Reinitializes the model's internal state, eliminating the influence of the previous context.",
                'shuffle_models_order_info': 'Shuffle models (checkbox). Shuffles order of execution of models if 3 or more are selected.',
                'fast_mode_info': 'Fast mode (checkbox). Generates text faster in background. Disables Learning Mode.',
                'voice_selection_info': 'Voice selection (select box). Selects SAPI5 voice on the computer.',
                'read_aloud_info': 'Read aloud (checkbox). Reads automatically the last Assistant response with the selected SAPI5 voice.',
                'learning_mode_info': 'Learning mode (select box). Activates Learning Mode. Works only if Fast Mode is unchecked. Time in seconds.',
                'number_of_loops_info': 'Number of loops (select box). Controls the number of loops of the selected models sequence.',
                'number_of_responses_info': 'Number of responses (select box). Controls the number of responses for each selected model.',
                'n_ctx_info': 'n_ctx (range slider). Number of context window tokens (0 = from model). Increases RAM memory usage. Before adjusting, unload the model.',
                'max_tokens_info': 'max_tokens (range slider). Controls maximum number of tokens that will be generated in the response. Set 0 for maximum possible.',
                'temperature_info': 'temperature (range slider). Controls the degree of creativity versus predictability of responses.',
                'stop_info': r'stop (text box). Contains list of characters that interrupt text generation, in the format ["$$$", ".", ".\n"]',
                'tfs_z_info': 'Tail Free Sampling (range slider). Limits selection of the next token to a subset with cumulative probability of the second derivative “z”.',
                'top_p_info': 'P-Sampling (range slider). Limits next token selection to a subset with cumulative probability of "p".',
                'min_p_info': 'M-Sampling (range slider). Limits next token selection to a subset with miminum probability of "m".', 
                'top_k_info': 'K-Sampling (range slider). Limits selection of the next token to a subset with the "k" highest probability tokens.',
                'presence_penalty_info': 'presence_penalty (range slider). Penalty to apply to the next token (not next word) based on their presence in the already generated text, regardless of its frequency.',
                'frequency_penalty_info': 'frequency_penalty (range slider). Penalty to apply to the next token (not next word) based on their frequency in the already generated text.',
                'repeat_penalty_info': 'repeat_penalty (range slider). Penalty to apply to repeated sequence of tokens (not next words sequence) based on their presence in the already generated text.',
                'model_prompt_template': 'Prompt template used by the model. Variables: "system_prompt" and "prompt".',
                'model_vocabulary': 'model_vocabulary (text box). List of all index/token pairs used by the model, including special characters (used to separate dialog parts).',
                'model_metadata_info': 'Model metadata (text box). Shows model metadata.',
                'btn_unload_model': 'Unload Model',
                'btn_load_pdf_pages': 'PDF Pages',
                'btn_load_full_pdf': 'PDF Full',
                'btn_system_prompt': 'TXT System Prompt',
                'btn_user_prompt': 'TXT User Prompt',
                'assistant_raw_output_info': 'Response history (CTRL + SHIFT + ESC to open Task Manager)',
                'btn_next_token': 'Next Token',
                'btn_copy_code_blocks': 'Copy Code Blocks',
                'btn_open_jupyterlab': 'Open JupyterLab',
                'btn_copy_last_response': 'Copy Last Response',
                'btn_copy_all_responses': 'Copy All Response',
                'btn_voice_command': 'Voice Control',
                'btn_text_to_speech': 'Text to Speech',
                'btn_last_response': 'Last Response',
                'btn_all_responses': 'All Responses',
                }
            }

# prompt the user to select their preferred language for the interface interaction, with a default option for Portuguese or English
# read_aloud_fn desabled

if 'portuguese' in voices[0].name.lower(): # Check if the name of the voice contains the substring 'portuguese'. If it does, proceed to offer language selection.
    print('Selecione o idioma da interface. Aperte ENTER para Português ou qualquer outra tecla + ENTER para Inglês:')  # Inform the user to select the interface language by pressing ENTER for Portuguese or any other key plus ENTER for English.
    #read_aloud_fn('Selecione o idioma da interface. Aperte ENTER para Português, ou qualquer outra tecla + ENTER para Inglês.')  # Use a function `read_aloud_fn` to verbally communicate the language selection prompt to the user.
    try:                                    # Try block to catch exceptions that may occur when reading input (e.g., EOFError)
        temp = input('')                    # Prompt the user for input without specifying a default prompt text, but with the ability to handle an empty string.
    except:
        temp = 'y'                          # If an exception occurs (e.g., the user closes the input dialog), default the selection to 'y' which is assumed to be for Portuguese.
    if temp == '':                          # If the user enters an empty string, use the previously defined `language` variable as the selected language.
        language = language['pt']
        print('Idioma da interface selecionado: Português')
        #read_aloud_fn('Idioma da interface selecionado. Português') # Confirm the selection of Portuguese and use `read_aloud_fn` to announce it.
    else:
        language = language['en']           # If the user enters a non-empty string, assume it's for English.
        print('Idioma da interface selecionado: Inglês')
        #read_aloud_fn('Idioma da interface selecionado. Inglês') # Confirm the selection of English and use `read_aloud_fn` to announce it.
else:
    language = language['en']               # If 'portuguese' was not found in the voice name, default to the previously defined `language` variable.
    print('Selected intereface language: English') # Inform the user that the default interface language will be English.
print()


# =====================
# GET LOCAL MDDELS LIST
# =====================

def get_downloads_path():
    """
    Retrieves the absolute path to the user's Downloads directory.

    This function first expands the tilde (~) to the user's home directory, then constructs
    the full path to the Downloads folder within the home directory. It checks if the Downloads
    directory exists before returning the path. If the directory does not exist, it returns None.

    Returns: 
        str or None: The absolute path to the user's Downloads directory if it exists, otherwise None.
    """
    home_dir = os.path.expanduser('~')                  # Get the path to the "Downloads" directory for the current user by expanding the tilde (~) to the home directory
    temp = os.path.join(home_dir, 'Downloads')          # Construct the full path to the Downloads folder within the home directory
    if os.path.exists(temp):                            # Check if the "Downloads" directory exists at the constructed path
        return temp                                     # If it does exist, return the absolute path to the Downloads directory
    else:
        return None                                     # If the Downloads directory does not exist, return None to indicate that the path is not 


model_path = get_downloads_path()                       # Retrieve the absolute path to the user's Downloads directory by calling the `get_downloads_path` function. This function returns the path if it exists, or `None` if it does not.
if model_path:                                          # Check if the path to the Downloads folder was successfully retrieved. If `model_path` is truthy (i.e., a non-empty string), print the full path to the 'Downloads' folder. Otherwise, if `model_path` is falsy (i.e., `None`), inform the user that the Downloads folder was not found.
    print(f"The path to the 'Downloads' folder is: {model_path}")
else:
    print("The 'Downloads' folder was not found.")


gguf_files = glob.glob(fr'{model_path}\*.gguf')         # Define the path pattern to match all files with the '.gguf' extension in the specified directory.
models = [i.split('\\')[-1] for i in gguf_files]        # Create a list with paths to all GGUF files in the current directory if they exist. The glob.glob function returns a list of file paths matching the pattern. # Populate the 'models' list with local file names (without the full path) extracted from the 'gguf_files' list.
print()
print('Models:')
for n, i in enumerate(models):                          # Enumerate over the 'models' list, displaying each model's index (n + 1) and name.
    print(n + 1, i)
print()


# =================================
# CREATE REMAINING GLOBAL VARIABLES
# =================================

last_models_list = models       # List with models names. Starts with models in 'Downloads' folder
last_diretorio = model_path     # Previous selected directory (Load Model Button)
llm = ''                        # Store llm object created with llama.cpp, used to generate text
last_model = ''                 # Stores last loaded model name
tokens_score = ''               # string with all top-k token-logits pair in each generation cicle. Ex: ' Hello'   (12.16)
system_prompt = language["initial_system_prompt"] # (FIELD) First system message (default system prompt)
previous_answer = language['first_assistant_previous_response'] # (FIELD) Stores the previous response generated by the model and used in the current response cicle. ATENTION! This phrase must be changed in 2 place in this code!
prompt = language['user_prompt_value']     # (FIELD) Default user prompt
# current_ia_response = language['current_response'] # (FIELD) Initial part of the Assistant's current response, filled by the user
ultima_resposta = language['first_assistant_previous_response']     # Stores current response to be used in the next conversation cicle, if desired
resposta = ''                   # Stores cummulative text showed on output field (for each chat session)
inputs = []                     # Stores Gradio interface fields in a predefined sequence
loop_models = 1                 # Initial models loops number

# Variables to review use
x_bar = ['gra', 'fi', 'co', 'pa', 'ra', 'tes', 'te']         # Initial bargraph_1 parameter (top-k prompts scores)
y_bar = [30, 24, 22, 15, 14, 13, 10]                         # Initial bargraph_1 parameter (top-k prompts scores)
color_bar = ['Selected', 'No', 'No', 'No', 'No', 'No', 'No'] # Initial bargraph_1 parameter (top-k prompts scores)
x_score =[]                     # Initial bargraph_2 parameter (prompts frequency)
y_score = []                    # Initial bargraph_2 parameter (prompts frequency)

delay_next_token = 'OFF'        # Learning Mode OFF. Controls token generation delay and barplots display
one_click = False               # Used to disable click sound on some buttons
next_token = False              # Controls NEXT TOKEN button infinite loop
prompt_template = ''            # Stores model prompt template extracted from TXT file
vocabulary = ''                 # Stores model vocabulary (all possible tokens used by the model)
full_text = ''                  # Text of all responses of the sequence (prompts list, models list, number of responses and models loops) in one session
para_tudo = False               # Stop text generation in the current model execution (STOP / NEXT button)
stop_all = False                # Stop text generation of all models loop and resets model loaded (STOP ALL / RESET button)
read_aloud = False              # Read last model response aloud automatically (Checkbox)
infinite_loop = False           # Transpose current response automatically to the model previous response variable (Checkbox)
fast_mode = False               # Select Fast Mode for text generation without showing on interface (Checkbox)
random_list = False             # Shuffle models order (if number of models >= 3) (Checkbox)
reset_mode = False              # Reset model for each prompt run of the chaining (Checkbox)
audio = None                    # Stores pygame audio object
model_metadata = ''             # Stores llm metadata to show on interface
model_url = ''                  # Stores the model url for downloading
previous_model_url = ''         # Stores the model url to check if it changed in every generation cicle ('text_generation' function call)


# ================================
# INTERFACE VOICE CONTROL SETTINGS
# ================================

# This code first checks if the Portuguese language option is available for voice control. If it's available, it prompts the user to enable or disable voice control and read-aloud functionality in Portuguese. It then sets flags based on the user's input.
# If the Portuguese option isn't available, it falls back to a standard English prompt for enabling/disabling voice control. Again, it sets the flags accordingly. 
# In both cases, if voice control is enabled, the `read_aloud` flag is set to True, indicating that read-aloud functionality should be active.

if 'portuguese' in voices[0].name.lower(): # Check if Portuguese language is available as a voice option (SAPI5).
    print('Ativar controle por voz? Aperte ENTER para não, ou qualquer outra tecla + ENTER para sim.')
    #read_aloud_fn('Ativar controle por voz? Aperte ENTER para não, ou qualquer outra tecla + ENTER para sim.')

    try:
        voice_mode = input()
    except:
        voice_mode = 'y' # Handle potential EOFError when input is not provided

    if voice_mode.lower() == '': # Based on user's choice, set voice control and interactive mode flags.
        voice_mode = False
        leaning_mode_interatcive = True
        print('Controle por voz desativado.')
        #read_aloud_fn('Controle por voz desativado.')
    else:
        voice_mode = True
        leaning_mode_interatcive = False
        print('Controle por voz ativado.')
        #read_aloud_fn('Controle por voz ativado.')
        read_aloud = True

    print()
    print('Abrindo interface no navegador...')
    #read_aloud_fn('Abrindo interface no navegador...')

else: # If 'portuguese' SAPI5 voice is not available
    try:
        voice_mode = input('Activate voice control? Press ENTER for no or any other key + ENTER for yes: ')
    except:
        voice_mode = 'y' # Handle potential EOFError when input is not provided
    
    if voice_mode.lower() == '':
        voice_mode = False
        leaning_mode_interatcive = True
        print('Voice control disabled.')
    else:
        voice_mode = True
        leaning_mode_interatcive = False
        print('Voice control activated.')
        read_aloud = True


# ===============================
# READ FILES WITH PROMPT EXAMPLES
# ===============================

# The provided code snippet is a Python script that reads two text files containing templates for user and system prompts, respectively. The prompts are separated by a special delimiter (`$-$-$`) in the files. The script then processes these templates to create a list of formatted strings for each type of prompt. Below is an annotated version of the code with comments for help maintenance:

with open('user_prompts.txt', encoding='utf-8', errors='ignore') as f:      # Open the file containing user prompts.
    temp = f.read()                                                         # Read the entire content of the file.
    examples = temp.split('$-$-$')                                          # Split the content into a list using `$-$-$` as a delimiter.
    examples = [f"""{x.strip()}""" for x in examples]                       # Remove leading/trailing whitespace from each prompt and format them as strings. The 'examples' variable now holds a list of user prompt templates.

with open('system_prompts.txt', encoding='utf-8', errors='ignore') as f:    # Open the file containing system prompts.
    temp = f.read()
    messages_text = temp.split('$-$-$')
    messages_text = [f"""{x.strip()}""" for x in messages_text]


# =======================
# TEXT GENERATOR FUNCTION
# =======================
            
# This main function generates next token in response to input context (system prompt + previous assistant response + user prompt + initial part of current assistant response).
# Function called by "Start Chat" button and by user speech in Voice Control Mode
# Parameters received from Gradio web interface MUST be in the same sequence as in 'inputs' list variable.
# Observations: To monitor inner function variables behavior, remember to select the corresponding mode (Lerning Mode, Fast Mode) before. Each mode has its exclusive pathway inside the code.
                        
def text_generator(
        system_prompt_p, # All '_p' parameters are binded to global variables
        infinite_loop_p,
        prev_answer,
        prompt_p,
        # current_ia_response_p, # To remove soon (4th element). Items greater then 4 must be down 1
        models,
        model_url_p,
        reset_mode_p,
        random_list_p,
        fast_mode_p,
        selected_voice_p,
        read_aloud_p,
        delay_next_token_p,
        loop_models_p,
        num_respostas,
        n_ctx, 
        max_tokens, 
        temperature, 
        stop_generation, 
        tfs_z, 
        top_p,
        min_p,
        top_k, 
        presence_penalty, 
        frequency_penalty, 
        repeat_penalty,
        prompt_template_p,
        vocabulary_p,
        ):
          
    # Global variables (used outside the function)
    global last_model
    global llm
    global resposta
    global model_path
    global para_tudo
    global tokens_score
    # global current_ia_response
    global stop_all
    global previous_answer
    global ultima_resposta
    global prompt
    global infinite_loop
    global read_aloud
    global x_bar
    global y_bar
    global color_bar
    global x_score
    global y_score
    global last_models_list
    global fast_mode
    global delay_next_token
    global system_prompt
    global random_list
    global prompt_template
    global reset_mode
    global selected_voice
    global engine
    global audio
    global vocabulary
    global full_text
    global next_token
    global model_metadata
    global previous_model_url

    click.play()
    print('Starting the funtion "text_generator"...')
    print()
    
    # Global variables bindings was necessary to avoid forbiden use of the same function parameters names
    fast_mode = fast_mode_p # '_p' is from text_generator function 'p'arameter
    delay_next_token = delay_next_token_p
    system_prompt = system_prompt_p
    # current_ia_response = current_ia_response_p
    prompt = prompt_p
    infinite_loop = infinite_loop_p
    loop_models = loop_models_p
    read_aloud = read_aloud_p
    random_list = random_list_p
    prompt_template = prompt_template_p
    reset_mode = reset_mode_p
    selected_voice = selected_voice_p
    vocabulary = vocabulary_p
    model_url = model_url_p


    # Check if no model is selected
    if models == []:

        # Check if "Model's URL for testing" field is filled
        if 'http' in model_url and previous_model_url != model_url: # True if the models's url (previous_model)url) is replaced by a different model url
            try:
                try:
                    del llm
                except:
                    pass
                llm = ''
                models = download_model(model_url)
                models = models.split('\\')[-1]
                previous_model_url = model_url # To avoid download the model every time it is called
                gc.collect()
            except:
                yield 'Error when trying to download model for testing.'
                return
        elif 'http' in model_url and previous_model_url == model_url:
            models = 'MODEL_FOR_TESTING.gguf'
        # llm = ''

    if prompt == '':                # To use in case of empty user prompt
        prompt = 'Hello!'

    if stop_generation == '':       # To avoid error, set the variable with an impossible character sequence
        stop_generation = "['$$$']"

    # Set the previous response sequence (in test)
    if infinite_loop == True:
        if ultima_resposta == '':   # This variable is set to '' when Clear Button is pressed (clean_output function)
            previous_answer = prev_answer
        else:
            previous_answer = ultima_resposta
    else:
        previous_answer = prev_answer


    # Models handling block. 'models' vairable must be passed forward as a list
    if models == None:              # When selected a directory without GGUF file
        yield 'Select a directory containing UGGF file.' # Use simple sentence
        return                      # Leaves the function
    
    if models == []:                # For the case when model is not selected
        yield 'Model not selected.' # Use simple sentence
        return                      # Leaves the function
    
    if isinstance(models, str):
        models = [models]
    
    if loop_models > 1:             # Multiply number of loops by the number of models sequence (Checkbox)
        models = models * loop_models
    
    if random_list == True and len(set(models)) >= 3: # Shuffles models order if >= 3 (Checkbox)
        models = random_list_fn(models) # Auxiliary function
    print()

    full_text = ''                  # Restart variable before load models.
    
    with open('full_text.txt', 'w', errors='ignore') as f: # Delete content of the file 'full_text.txt'
        pass


    # =================
    # LOOPS DESCRIPTION
    # =================

    # FOR LOOP OVER SELECTED MODELS (Model 1, Model 2...)                     1ST LOOP
    #      |
    #      ENDLESS WHILE LOOP (Until leave the text_generator function)       2ND LOOP
    #           |
    #           FOR LOOP OVER PROMPT LIST (Prompt 1, Prompt 1...)             3RD LOOP
    #                |
    #                FOR LOOP TOKEN GENERATION (Token 1, Token 2...)          4TH LOOP


    # ==========================================
    # FIRST LOOP - FOR LOOP OVER SELECTED MODELS
    # ==========================================

    pre_prompt = ''     # Required to store the 'pre_prompt' for use in each of the prompts in the prompt list
    final_prompt = ''   # Required to store the 'final_prompt' for use in each of the prompts in the prompt list

    # model_single_answer = True

    for n_model, model in enumerate(models):            # Loop over models list

        # back_first_loop = False
        
        # Extract model prompt template
        # try:                                            # try to get the corresponding prompt template for the selected model
        #     with open(fr'{model_path}\{model[:-5]}.txt', encoding='utf-8', errors='ignore') as f:
        #         temp = f.read()
        #         prompt_template = model + ' prompt template:\n' + temp # Variable to be displayed on web interface (Model prompt template field)
        #         temp = "f" + '"""' + temp + '"""'       # Format string before applying 'eval' function

        #         temp = temp.replace('#', '\#')          # Some models use '#' inside prompt templates. 'eval' function would ignore this. 

        #         # Replaces variables {system_prompt} and {prompt} using f-string. Returns a string
        #         # input_m = eval(temp)

        #         # try:
        #         #     input_m = eval(temp) # Replaces 'system_prompt' variable
        #         #     input_m = input_m.replace('$$$', '')    # <<<<<<<<<<<< TESTING
        #         #     print()
        #         # except Exception as e:
        #         #     yield traceback.format_exc() + '\n\nSingle backslash (\) must be replaced by double backslash (\\)\n colon (:) must be predeced by backslash (\:)'
        #         #     return
                
        #         # input_m = input_m.replace('$$$', '')    # <<<<<<<<<<<< TESTING
        #         # print()

        # except FileNotFoundError:                       # If model template TXT file not found
        #     yield f'To use Samantha IA you need 2 files in the same directory:\n1) Download a GGUF model file\n2) Create a TXT model template file\n\nGGUF file and/or prompt template file not found:\n{model_path}\{model[:-5]}.txt\n\nDownload the GGUF model file and/or create the file "{model[:-5]}.txt" and paste the corresponding prompt template inside it.'
        #     return
        
        num_control = 1                         # Controls number of responses generated by each mode
        load_start = time.time()                # Starts model loading time counting


        # ================================
        # SECOND LOOP - ENDLESS WHILE LOOP
        # ================================

        while True:

            # if back_first_loop == True:
            #     break

            para_tudo = False                                       # Reinitializes 'para_tudo' variable after it was set to True (para_tudo = True stop text generation)
            if last_model != model or llm == '' or loop_models > 1: # Check if model changed or was unloaded. If so, load new model. Force unload model if loop_model > 1
                try:                                                # Delete previous model from memory
                    del llm
                except:
                    pass
                last_model = model                                  # Update last_model variable


                # ==========
                # CREATE LLM
                # ==========

                try:                                                # Try to load model                    
                    llm = Llama(                                    # Instantiate Llama class passing the selected model (https://llama-cpp-python.readthedocs.io/en/latest/api-reference/)
                            model_path= model_path + '\\' + model,
                            n_gpu_layers=-1,                        # default: 0
                            main_gpu=0,
                            tensor_split=None,
                            vocab_only=False,
                            use_mmap=True,
                            use_mlock=False,
                            seed=4294967295,                        #-1,
                            n_ctx=n_ctx,                            # default: 512 <<<<<<<<<<<<<<<<<<<<<<<<<<<<< SET BY THE USER (NECESSARY TO RELOAD MODEL TO PRODUCE EFFECTS)
                            n_batch=512,                            # default: 512 Estava em 256
                            n_threads=None,                         # Estava em None
                            n_threads_batch=None,                   # Estava em None
                            rope_freq_base=0,
                            rope_freq_scale=0,
                            mul_mat_q=True,
                            f16_kv=True,
                            logits_all=False,
                            embedding=False,
                            last_n_tokens_size=64,                  # default 64. Estava em 512
                            lora_base=None,
                            lora_scale=1.0,
                            lora_path=None,
                            numa=False,
                            chat_format=None,                       # 'llama-2' (padrão), 'alpaca', 'vicuna', 'oasst_llama', 'openbuddy', 'redpajama-incite', 'snoozy', 'phind', 'open-orca'
                            chat_handler=None,
                            verbose=True,         
                        )
                except Exception as e:
                    yield 'Error on trying to load model. Try another model.' 
                    print(traceback.format_exc())
                    return
                                          
                model_metadata = str(llm.metadata).replace(',', '\n ') # Extract model's metadata and converts it to string
                
                temp = [llm.detokenize([x]) for x in range(llm._n_vocab)] # Get the model vocacubulary
                vocabulary = ''
                for n, x in enumerate(temp):
                    try:
                        vocabulary += f'{n})    {repr(x.decode())}\n'
                    except:
                        vocabulary += f'{n})    {repr(x)}\n'
            
            # if max_tokens == 0: # Change default End Of Sentence (EOS) token to allow unlimited text generation (until reach n_ctx)
            #     print()
            #     print('>>>>> EOS before:', llm._token_eos)
            #     llm._token_eos = 1_000_000 # Model vocabulary less than 50k tokens, so EOS will never be reached
            #     print('>>>>> EOS after:', llm._token_eos)
            #     print()

            if max_tokens == 0:
                max_tokens = None   
            
            # num_tokens = 0 # Starts tokens counting of the current response
            previous_token = [] # Stores 10 last tokens. Displayed on top of the output field

            # Adds model name to the current response. Text response starts here. 'resposta' is a cummulative text variable
            resposta += f'\n\n==========================================\n{num_control}) {model}:\n==========================================\n'

            # try:
            #     # with open(fr'{diretorio}\{model[:-5]}.txt', encoding='utf-8') as f: # Extract prompt template from TXT file
            #     with open(fr'{model_path}\{model[:-5]}.txt', encoding='utf-8', errors='ignore') as f: # Extract prompt template from TXT file
            #         temp = f.read()
            #         temp_2 = "f" + '"""' + temp + '"""' # 'temp_2' is used below
            
            # except Exception as e:
            #     yield 'Error on trying to load model prompt template TXT file. Check if it exists.' 
            #     print(traceback.format_exc())
            #     return


            # ===============
            # PROMPT SPLITTER
            # ===============
                
            # FINAL-PROMPT: Prompt to be used as the final prompt in a list of prompts, with the 'full_text' variable
            # Extract FINAL-PROMPT text from the prompt (text between [[ ]]). Final-prompt must be placed in the beginning of the text, BEFORE pre-prompt.
            
            if final_prompt == '':
                temp = r'\[\[[\r\n]*([\s\S]*?)[\r\n]*\]\]'
                # if len(re.findall(r'\[\[([\s\S]*?)\]\]', prompt)) >= 1:
                if len(re.findall(temp, prompt)) >= 1:
                    final_prompt = re.search(temp, prompt).group(0)
                    final_prompt = final_prompt.replace('[[', '').replace(']]', '')#[1:-1] # Delete []
                    final_prompt = final_prompt.replace('\n', ' ')
                    final_prompt = final_prompt + '\n\n'
                    prompt = re.sub(temp, '', prompt) # Delete pre-prompt phrase from the prompt text
                else:
                    final_prompt = ''
                
            # PRE-PROMPT: Prompt to be used for each each paragraph in a list of prompt separated by '\n'
            # Extract PRE-PROMPT text from the prompt (text between [ ]). Pre-prompt must be placed in the beginning of the text
            
            if pre_prompt == '': 
                # temp = re.findall(r'\[(.*?)\]', prompt)
                temp = re.findall(r'\[[\r\n]*([\s\S]*?)[\r\n]*\]', prompt)
                if len(temp) >= 1:
                    # pre_prompt = re.search(r'\[(.*?)\]', prompt).group(0)
                    pre_prompt = re.search(r'\[[\r\n]*([\s\S]*?)[\r\n]*\]', prompt).group(0)
                    pre_prompt = pre_prompt.replace('[', '').replace(']', '')#[1:-1] # Delete []
                    pre_prompt = pre_prompt.replace('\n', ' ')
                    pre_prompt = pre_prompt + '\n\n'
                    # prompt = re.sub(r'\[(.*?)\]', '', prompt) # Delete pre-prompt phrase from the prompt text
                    prompt = re.sub(r'\[[\r\n]*([\s\S]*?)[\r\n]*\]', '', prompt)
                else:
                    pre_prompt = ''


            # Split prompt criterias
            if '$$$' in prompt: # First: look for $$$ in the prompt text (priority)
                prompt_split = prompt.split('$$$\n') # Creates a list of prompts when $$$ is present on user input field

                # prompt_split = [x + '\n' + pre_prompt for x in prompt_split] # Include pre-prompt in each prompt splited with "$$$"
            
            else: # Second: separetes by '\n', if prompt text has no $$$ in the text
                prompt_split = prompt.split('\n')


            # Final cleanning process. Some codes works only in specific prompts (press Step-Over in VSCODE)
            prompt_split = [x.strip() for x in prompt_split] # Delete empty items from the prompt list
            prompt_split = [x for x in prompt_split if x != ''] # Delete empty items
            prompt_split = [x for x in prompt_split if x[:3] != '---'] # Delete items beginning wiht '---'
            prompt_split = [pre_prompt + x for x in prompt_split] # Add pre-prompt at the beginning of each prompt in the list
            prompt_split = [x.replace('$$$', '').strip() for x in prompt_split] # Delete '$$$' and leading spaces and new lines characters


            # MECANISMO QUE PERMITE A ELABORAÇÃO DE UMA RESPOSTA FINAL BASEADA EM TODAS AS RESPOSTAS ANTERIORES DOS MODELOS (FINAL-PROMPT)
            if final_prompt != '':

                with open('full_text.txt', 'r', errors='ignore') as f: # Delete content of the file 'full_text.txt'
                    temp = f.read()

                # prompt_split.append(final_prompt + 'full_text') # Add word 'full_text' to the variable 'final_prompt'. The word will be replaced by variable 'full_text'
                
                prompt_split.append(final_prompt + 'partial_text') # Add word 'full_text' to the variable 'final_prompt'. The word will be replaced by variable 'full_text'

            
            partial_text = ''
            
            with open('partial_text.txt', 'w', errors='ignore') as f: # Delete content of the file 'full_text.txt'
                pass


            # ======================================
            # THIRD LOOP - FOR LOOP OVER PROMPT LIST
            # ======================================

            for num_of_the_prompt, prompt_text in enumerate(prompt_split): # Prompt list. Runs current model over each prompt from the list
                
                # num_tokens = 1 # Starts tokens counting of the current response                
                # prompt_text = prompt_text.replace('{', '(').replace('}', ')') # To evoid NameError em eval(temp). Some texts has {} inside it
                # temp = temp_2.replace('{prompt}', prompt_text) # Replaces prompt with item from prompt list

                # temp = temp.replace('{current_ia_response}', current_ia_response)

                

                # full_text = full_text.replace('\n', '. ')

                # if 'full_text' in prompt_text:
                #     prompt_text = prompt_text.replace('full_text', full_text)

                # Text cleaning for audio reproduction. Remove characters inside [] and <>
                full_text = re.sub(r'\[.*?\]', '', full_text) 
                full_text = re.sub(r'<.*?>', '', full_text)


                if 'partial_text' in prompt_text:
                    prompt_text = prompt_text.replace('partial_text', partial_text + '\n$$$')

                # Text cleaning for audio reproduction. Remove characters inside [] and <>
                # full_text = re.sub(r'\[.*?\]', '', full_text) 
                # full_text = re.sub(r'<.*?>', '', full_text)

                # temp = temp.replace('full_text', full_text + '$$$') # $$$ joins paragraphs in only one prompt
                print()

                # User prompt character error handling (under test)
                # try:
                #     # temp = temp.replace(r'\\', r'/')#.replace(r':', '\:')
                #     # temp2 = temp.replace('#', '\#')          # Some models use '#' inside prompt templates. 'eval' function would ignore this. 
                #     input_m = eval(temp2)                    # Replaces 'system_prompt' variable
                # except Exception as e:
                #     yield traceback.format_exc() + '\n\nSingle backslash (\) must be replaced by double backslash (\\)\n colon (:) must be predeced by backslash (\:)'
                #     return

                # input_m = prompt_text

                # =============================

                # MAIN TRY BLOCK
                try: # For error treatement during tokens generation. Error is displayed on web interface and on terminal, but not crash the program
                    if reset_mode == True:
                        llm.reset()         # Reset model's internal parameters without unload it from memory.
                    start = 0
                    ultima_resposta = ''    # Restart variable for each new text generation cicle
                    
                    # After tests performed in JupyterLab with 'prompt_text' always present. If the fiel empty, the correspendent role is not inserted
                    if system_prompt == '' and previous_answer == '':# and current_ia_response == ''):
                        messages = [
                                    {'role': 'user', 'content': prompt_text},
                                    ]
                    
                    elif system_prompt == '' and previous_answer != '': # and current_ia_response == ''):
                        messages = [
                                    {'role': 'assistant', 'content': previous_answer},
                                    {'role': 'user', 'content': prompt_text},
                                    ]
                        
                    elif system_prompt != '' and previous_answer != '': # and current_ia_response == ''):
                        messages = [                                                        # Responses to prompt_text "Olá!"
                                    {'role': 'system', 'content': system_prompt},           # Requires text to avoid short responses like this: "Boa tarde! (If it's the afternoon) / Boa noite! (If it's evening or night).""
                                    {'role': 'assistant', 'content': previous_answer},      # Requires text to avoid short responses like this: "Boa tarde! Como posso ajudá-lo hoje?"
                                    {'role': 'user', 'content': prompt_text},               # Always present
                                    ]
                        
                    # elif (system_prompt == '' and previous_answer != '' and current_ia_response != ''):
                    #     messages = [
                    #                 {'role': 'assistant', 'content': previous_answer},
                    #                 {'role': 'user', 'content': prompt_text},
                    #                 {'role': 'assistant', 'content': current_ia_response},
                    #                 ]
                        
                    # elif (system_prompt != '' and previous_answer != '' and current_ia_response != ''):
                    #     messages = [                                                        # Responses to prompt_text "Olá!"
                    #                 {'role': 'system', 'content': system_prompt},           # Requires text to avoid short responses like this: "Boa tarde! (If it's the afternoon) / Boa noite! (If it's evening or night).""
                    #                 {'role': 'assistant', 'content': previous_answer},      # Requires text to avoid short responses like this: "Boa tarde! Como posso ajudá-lo hoje?"
                    #                 {'role': 'user', 'content': prompt_text},               # Always present
                    #                 {'role': 'assistant', 'content': current_ia_response},  # Requires text to avoid especial tokens and continuous generation: "<|assistant|> Olá! Como posso ajudar você hoje?"
                    #                 ]
                        
                    elif system_prompt != '' and previous_answer == '': # and current_ia_response == ''):
                        messages = [                                                        
                                    {'role': 'system', 'content': system_prompt},
                                    {'role': 'user', 'content': prompt_text},
                                    ]
                        
                    # elif (system_prompt == '' and previous_answer == '' and current_ia_response != ''):
                    #     messages = [                                                        
                    #                 {'role': 'user', 'content': prompt_text},
                    #                 {'role': 'assistant', 'content': current_ia_response},
                    #                 ]
                        
                    # Feedback loop activated. Insert 'previous_answer' right before 'user', independently the user position.
                    if infinite_loop == True and previous_answer == '': # Insert 'previous_answer' only if it was not inserted yet.
                        for n, k in enumerate(messages):
                            temp = next(iter(k))
                            if k[temp] == 'user':
                                print(n, k[temp])
                                messages.insert(n, {'role': 'assistant', 'content': previous_answer})
                                break

                        
                    print()
                    print('>>>>> SYSTEM MESSAGE:', system_prompt)
                    print()
                    print('>>>>> PREVIOUS RESPONSE:', previous_answer)
                    print()
                    print('>>>>> USER PROMPT:', prompt_text)
                    print()
                    # print('>>>>> CURRENT RESPONSE:', current_ia_response)
                    # print()
                    
                    # Variables used to create barblot with frequency of the tokens that are not the most likely
                    x_score = []
                    y_score = []
                    count = 1
                    total_time_start = time.time()


                    # ========================================
                    # FOURTH LOOP - FOR LOOP TOKENS GENERATION
                    # ========================================    
                    
                    # Loop to generate text, token by token. Model is loaded in memory here.
                    for nu, i in enumerate(llm.create_chat_completion(
                            messages = messages,
                            functions =  None,
                            function_call = None,
                            temperature = temperature,             # default: 0.2
                            top_p = top_p,                         # default: 0.95
                            min_p = min_p,                         # default: 0.05
                            top_k = top_k,                         # default: 40
                            stream = True,                         # default: False
                            stop = eval(stop_generation),          # default: None
                            max_tokens = max_tokens,               # default: 254 32k = 32768 None
                            presence_penalty = presence_penalty,   # default: 0
                            frequency_penalty = frequency_penalty, # default: 0
                            repeat_penalty = repeat_penalty,       # default: 1.1
                            tfs_z = tfs_z,                         # default: 1
                            mirostat_mode = 0,                     # default: 0
                            mirostat_tau = 5,
                            mirostat_eta = 0.1,
                            model = None,
                            logits_processor = None,
                            grammar = None,
                        )):
                       
                        #print(i)
                        
                        # Examples of i content:
                        # {'id': 'chatcmpl-d68c6c2c-2f94-4f1a-8abe-e257caaa36ce',
                        #  'model': 'D:\\samantha\\capybarahermes-2.5-mistral-7b.Q4_K_M.gguf',
                        #  'created': 1707853913,
                        #  'object': 'chat.completion.chunk',
                        #  'choices': [{'index': 0,
                        #               'delta': {'role': 'assistant'},
                        #               'finish_reason': None}]
                        # }

                        # {'id': 'chatcmpl-d68c6c2c-2f94-4f1a-8abe-e257caaa36ce',
                        #  'model': 'D:\\samantha\\capybarahermes-2.5-mistral-7b.Q4_K_M.gguf',
                        #  'created': 1707853913,
                        #  'object': 'chat.completion.chunk',
                        # 'choices': [{'index': 0,
                        #              'delta': {'content': 'Hello'},
                        #              'finish_reason': None}]
                        # }


                        # =========
                        # FAST MODE
                        # ========= 

                        if fast_mode == True:
                            try:
                                if nu == 0: # To sound only once at the beginning of text generation
                                    winsound.Beep(400, 500)
                                # Print token on terminal. # The first and last 'i' has no 'content' key and raise an error.
                                print(f'{nu})', round(time.time() - start, 2), repr(i['choices'][0]['delta']['content']))
                                
                                # Update 'resposta'
                                # if nu == 1 and current_ia_response != '': # nu == 1 is the first valid token
                                #     resposta += f"{current_ia_response}{i['choices'][0]['delta']['content']}"
                                # else:
                                resposta += i['choices'][0]['delta']['content']
                                
                                ultima_resposta += i['choices'][0]['delta']['content']
                                if para_tudo == True: # Stop / Next button
                                    break
                                if stop_all == True: # Stop All and Reset button
                                    som.play() # Assyncronous play (do not wait finish audio to proceed)
                                    stop_all = False
                                    llm.reset()
                                    yield resposta
                                    return
                                start = time.time() # Restart token generation time
                                continue
                            except:
                                print()
                                print("EXCEPTION:", i) # The first and last 'i' has no 'content' key and raise an error
                                print()
                                continue

                        # In Fast Mode, all text bellow is not executed


                        # ===========
                        # NORMAL MODE
                        # =========== 
                        
                        try:
                            current_token = i['choices'][0]['delta']['content']
                        except:
                            continue
                        try:
                            print(f'{nu})', round(time.time() - start, 2), repr(current_token))
                        except:
                            continue
                        if previous_token == []: # Executado apenas uma vez
                            winsound.Beep(600, 500)
                            load_stop = round((time.time() - load_start) / 60, 1)
                            input_encoded = len(llm.tokenize(prompt_text.encode())) + len(llm.tokenize(system_prompt.encode())) + len(llm.tokenize(previous_answer.encode())) #+ len(llm.tokenize(current_ia_response.encode()))
                        if stop_all == True: # Sai da função 'text_generator' quando o botão 'Stop All / Reset' é pressionado
                            som.play() # Assyncronous play (do not wait finish audio to proceed)
                            stop_all = False
                            llm.reset()
                            return


                        # =============
                        # LEARNING MODE
                        # =============

                        if delay_next_token != 'OFF':
                            # fast_mode = False
                            scores = llm.eval_logits
                            scores = scores[0]
                            zipped = zip(([llm.detokenize([x])] for x in range(llm._n_vocab)), scores) # [('a', 1), ('b', 2), ('c', 3)]
                            lista = list(zipped)
                            token_score = []
                            for n, x in enumerate(lista):
                                try:
                                    token_score.append([f'{n})    ' + "'" + x[0][0].decode() + "'    ", x[1], x[0][0].decode()])
                                except:
                                    pass
                            token_score_sorted = sorted(token_score, key=lambda x: x[1], reverse=True) # ["22867)    'lá'    ", 29.99230194091797, 'lá']
                            if top_k > 100:
                                top_k_bar = 100
                            else:
                                top_k_bar = top_k
                            x_bar = [l[0] for l in token_score_sorted[:top_k_bar]]
                            y_bar = [round(l[1], 2) for l in token_score_sorted[:top_k_bar]]
                            color_bar = ['Selected' if l[2] == current_token else 'No' for l in token_score_sorted[:top_k_bar]]
                            for n, l in enumerate(token_score_sorted[:top_k_bar]):
                                if l[2] == current_token and n != 0:
                                    x_score.append(str(count))
                                    y_score.append(n + 1)
                                    count += 1 # Count exceptions to the most likely token
                                    break
                                else:
                                    continue   
                            try:
                                token_score_sorted = [[x[0], '   (' + str(round(x[1], 2)) + ')     <<<  Selected'] if x[2] == current_token else [x[0], '   (' + str(round(x[1], 2)) + ')'] for x in token_score_sorted ]
                            except:
                                pass
                            token_score_sorted = token_score_sorted[:top_k] # top_k, 10
                            try:
                                tokens_score = ''.join([repr(x[0]) + x[1] + '\n' for x in token_score_sorted])
                            except:
                                pass
                            candidates = f'Candidates and scores for the next token in {llm._n_vocab} tokens vocabulary:\n'
                        else:
                            tokens_score = ''
                            candidates = ''

                        # ===================

                        # Try to extract token from dict object generated by the model. Em alguns loops o token não está presente. Por isso do try/except
                        try:
                            # if num_tokens == 1 and current_ia_response != '': # Para exibir ... em todas as respostas
                            #     resposta += f"{current_ia_response}{current_token}"
                            # else:
                            resposta += current_token
                            
                            ultima_resposta += current_token
                            # Tokens com pontuação mais alta                                
                            # text = ''.join([repr(x[0]) + x[1] + '\n' for x in token_score_sorted])
                            stop = round((time.time() - start), 1)
                            tt = round(time.time() - total_time_start, 1)

                            # <<<<<<<<<<<<<<<<

                            # Retorna resposta (já com o último token) e número parcial de tokens
                            yield f"""Previous tokens: '{repr("  ".join(previous_token[:10]))}'\n{candidates} {tokens_score} \n LLM load time:   {load_stop} min. {resposta} ({input_encoded} + {nu}, {stop}s)"""
                                                        
                            # <<<<<<<<<<<<<<<<

                            # Sai do loop quando o usuário aperta o botão Stop
                            if para_tudo == True:
                                # num_control = num_respostas # Se tiver executando loop de respostas, para todo o loop REMOVER PARA PERMITIR INTERROMPER APENAS O LOOP ATUAL
                                break
                            if delay_next_token != 'OFF':
                                if delay_next_token == 'NEXT TOKEN':
                                    while True:
                                        if next_token == True: # Controls NEXT TOKEN button infinite loop
                                            next_token = False
                                            break
                                        else:
                                            time.sleep(0.5)
                                else:
                                    time.sleep(delay_next_token)
                            # num_tokens += 1 # Atualiza número de tokens da resposta atual
                        except:
                            pass
                        try: # Atualiza token anterior
                            if len(previous_token) == 10:
                                previous_token.pop(0)
                            previous_token.append(current_token)
                        except:
                            pass
                        start = time.time() # Início do tempo do próximo token. Atualiza variável

                    # FAST MODE CONTINUES FROM HERE (COMMON PART FOR ALL MODES)
                    if fast_mode == True or (fast_mode == False and delay_next_token == 'OFF'): # Display response after Fast Generation Mode has finished
                        tt = round(time.time() - total_time_start, 1)
                        resposta = resposta + f'\n---------- ({nu} tokens, {tt}s)\n' # number of tokens from context window: llm.n_tokens len(llm.n_tokens) - len(llm._input_ids)
                        yield resposta
                    else: # Returns text in Learning Mode
                        yield f"""Previous tokens: '{repr("  ".join(previous_token[:10]))}'\n{candidates} {tokens_score} \n LLM load time:   {load_stop} min. {resposta} ({input_encoded} + {nu}, {stop}s)\n---------- ({tt}s)\n"""
                    
                    som.play() # Play notification sound to warn the end of response generation
                    while pygame.mixer.get_busy(): # Wait until notification sound ends to play (comment to make it assyncronous)
                        pass
                

                    # ==============
                    # TEXT TO SPEECH
                    # ==============
                    
                    # cleaned = re.sub(r'\[.*?\]', '', current_ia_response + ultima_resposta) # Text cleaning for audio reproduction. Remove characters inside [] and <>
                    cleaned = re.sub(r'\[.*?\]', '', ultima_resposta) # Text cleaning for audio reproduction. Remove characters inside [] and <>
                    
                    cleaned = re.sub(r'<.*?>', '', cleaned)
                    cleaned = cleaned.replace('**', '').replace('#', '')    # Do not speak bolded text in Markdown
                    try:                                                    # Delete previous audio file for allow the creation of a new one
                        os.remove('resposta.mp3')
                    except:
                        pass
                    if 'Portug' in selected_voice:
                        engine.setProperty('rate', 200)                     # Set rate for Portuguese voice (normal rate)
                    else:
                        engine.setProperty('rate', 115)                     # Set rate for others languages (slow down rate) 
                    for voice in voices:
                        if voice.name == selected_voice:                    # Set selected voice (interface widget) to create audio file
                            engine.setProperty('voice', voice.id)
                            print('Selected voice:', selected_voice)
                            break
                    engine.save_to_file(cleaned, 'resposta.mp3')            # Save audio file
                    engine.runAndWait()
                
                    # Read aloud the saved audio file with the previous Assistant response
                    if read_aloud == True:
                        audio = pygame.mixer.Sound('resposta.mp3')
                        audio.set_volume(1.0)
                        audio.play()

                # MAIN EXCEPT
                except Exception as e:
                    resposta = resposta + '\n\n' + '********************************\n' + traceback.format_exc() + '********************************\n\n' + 'No problem! You just reached the context window limit (n_ctx). Unload the model, increase the context window limit, and try again.\n\n'
                    yield resposta # Returns response with error message and display it on output interface
                    return
                
                # ============================= 
            
                if infinite_loop == True: # Update previous response. The existance of text in previous response affects the next text generation time
                    previous_answer = ultima_resposta
                    messages[1] = {'role': 'assistant', 'content': previous_answer}
                
                para_tudo = False # Reset variable
                
                full_text += ultima_resposta + '\n\n' # Add last response to full_text variable
                with open('full_text.txt', mode='w', encoding='utf-8', errors='ignore') as f:
                    f.write(full_text)

                partial_text += ultima_resposta + '\n\n' # Add last response to partial_text variable
                with open('partial_text.txt', mode='w', encoding='utf-8', errors='ignore') as f:
                    f.write(partial_text)

                # if infinite_loop == True: # Set variable to the current field value
                #     previous_answer = prev_answer

                # Leaves function if reponse contains this stop words
                if 'STOP_SAMANTHA' in ultima_resposta:
                    return
                
                
                # if model_single_answer == True: # To go back to the first loop (selected models)
                #     back_first_loop = True


                # ======================
                # CRITICAL LOOPS CONTROL
                # ======================

                # Controls the sequence of the four concatenated loops (MODEL -> ENDLESS -> PROMPTS -> TOKENS)
                if num_of_the_prompt < len(prompt_split) - 1:   # Continues loop for each prompt separeted by $$$
                    continue
                else:
                    if num_control < num_respostas:             # Break prompt list's for loop (go back to endless where loop)
                        break
                    elif num_control == num_respostas:          # Decides if goes to endless where loop or to models loop
                        if n_model < len(models) - 1:           # Leave prompt list's for loop (go back to endless where loop)
                            break
                        elif n_model == len(models) - 1:        # Leave the function
                            return
                if num_control < num_respostas:                 # Break prompt list's for loop (go back to endless where loop)
                    break           
            
            if n_model < len(models) - 1 and num_control == num_respostas: # Break endless while loop (go back to model loop)
                break

            num_control += 1





    para_tudo = False                                           # Reset variable

    # Final cleaning
    gc.collect()

        
# ===================
# AUXILIARY FUNCTIONS
# ===================

def random_list_fn(models): # Shuffles models list avoiding that equals itens get togueter (Created with Claude.ai)
    resultado = []
    contagens = Counter(models)
    elementos = list(contagens.keys())
    for elemento in elementos:
        resultado.extend([elemento] * contagens[elemento])
    while True:
        random.shuffle(resultado)
        tem_repeticao = False
        for i in range(len(resultado)-1):
            if resultado[i] == resultado[i+1]:
                tem_repeticao = True
                break
        if not tem_repeticao:
            break
    return resultado


def clean_output(): # Clear Output button: clear output text
    global resposta
    global ultima_resposta
    click.play()
    resposta = ''
    ultima_resposta = ''

    html_files = glob.glob('*.html') # Delete all html files in current folder
    for file in html_files:
        os.remove(file)

    # IN TEST
    with open('full_text.txt', 'w', errors='ignore') as f: # Delete content of the file 'full_text.txt'
        pass
    # IN TEST
    with open('partial_text.txt', 'w', errors='ignore') as f: # Delete content of the file 'partial_text.txt'
        pass
    
    try:
        os.remove('resposta.mp3')
    except:
        pass
    try:
        os.remove('full_text.mp3')
    except:
        pass

    return ''
    

def stop_running(): # Stop / Next button
    global para_tudo
    global audio
    global one_click
    if one_click == False:
        click.play()
    else:
        one_click = False
    para_tudo = True
    try:
        audio.stop() # AttributeError: 'NoneType' object has no attribute 'stop'
    except:
        pass
    return para_tudo


def stop_running_all(): # Stop All & Reset button
    global stop_all
    global audio
    global one_click
    if one_click == False:
        click.play()
    else:
        one_click = False
    stop_all = True
    try:
        audio.stop() # AttributeError: 'NoneType' object has no attribute 'stop'
    except:
        pass
    return stop_all


def update_previous_answer(): # Previous Response button
    click.play()
    return ultima_resposta


def update_audio_widget(*inputs): # Load audio widget with last message audio
    if os.path.isfile('resposta.mp3'):
        global engine
        click.play()
        # sel_voice = inputs[9]
        sel_voice = inputs[8]
        if 'Portug' in sel_voice: # Set rate for each voice
            engine.setProperty('rate', 200) # Slow down english speak
        else:
            engine.setProperty('rate', 115) # Normal rate for Portuguese
        for voice in voices: # Set selected voice to create audio file
            if voice.name == sel_voice:
                engine.setProperty('voice', voice.id)
                print('Selected voice:', sel_voice)
                break   
        # cleaned = re.sub(r'\[.*?\]', '', current_ia_response + ultima_resposta)  # Text cleaning for audio reproduction. Remove characters inside [] and <>
        cleaned = re.sub(r'\[.*?\]', '', ultima_resposta)  # Text cleaning for audio reproduction. Remove characters inside [] and <>
        
        
        cleaned = re.sub(r'<.*?>', '', cleaned)
        cleaned = cleaned.replace('**', '').replace('#', '') # Do not speak bolded text in Markdown
        try: # Delete previous audio file for allow the creation of a new one
            os.remove('resposta.mp3')
        except:
            pass
        engine.save_to_file(cleaned, 'resposta.mp3') # Save audio file
        engine.runAndWait()
        return 'resposta.mp3'
    else:
        return 'introducao.mp3'


def update_barplot_widget(): # Update barplot 1 with tokens scores distribution
    if fast_mode == True: # Hide barplot if fast_mode == True
        return gr.BarPlot(visible=False)
    if delay_next_token == 'OFF': # Controls barplot visibility
        show = False
    else:
        show = True
    df = pd.DataFrame( # Creates dataframe with Pandas
            {
                "token": x_bar,
                "score": y_bar,
                "color": color_bar
            }
        )
    return gr.BarPlot( # Returns barplot element
            df,
            x='token',
            y='score',
            color='color',
            title="Distribution of Tokens Probabilities",
            tooltip=["token", "score"],
            y_lim=[0, 30],
            width=500,
            height=150,
            interactive=True,
            visible= show,
            x_title="Top-k Tokens",
            y_title="Probability Score"
        )


# CREATE BARPLOT THAT SEQUENCIATE ON X AXIS ALL SELECTED TOKEN WITH ITS RESPECTIVE SCORE ON Y AXIS: https://www.youtube.com/watch?v=FdTRzgbBP8o


def update_barplot_widget_2(): # Update barplot 2 with unlikelly tokens frequency
    if fast_mode == True: # Hide barplot if fast_mode == True
        return gr.BarPlot(visible=False)
    if delay_next_token == 'OFF': # Controls barplot visibility
        show = False
    else:
        show = True
    df_2 = pd.DataFrame( # Creates dataframe with Pandas
            {
                "occurrence_number": x_score,
                "score": y_score,
                # "color": color_bar
            }
        )
    return gr.BarPlot( # Returns barplot element
            df_2,
            x='occurrence_number',
            y='score',
            color='score',
            title="Exceptions to the Most Likely Token",
            tooltip=["occurrence_number", "score"],
            y_lim=[0, 30],
            width=500,
            height=150,
            interactive=True,
            visible= show,
            x_title="Number of Occurrences",
            y_title="Probability Score"
        )


def open_browser(): # Open default browser with Gradio server on localhost in dark mode
    webbrowser.open('http://localhost:7860/?__theme=dark')


def update_template_field(): # Update model template field
    return prompt_template


def sel_model(): # Select model
    try:
        return models[0]
    except:
        return last_model
    

def update_vocabulary(): # Update model's tokens vocabulary
    return vocabulary


def update_metadata(): # Shows model's metadata on interface
    return model_metadata


def text_to_speech(*inputs): # Text to speech convertion
    global engine
    click.play()
    prompt_user = inputs[3]
    # sel_voice = inputs[9]
    sel_voice = inputs[8]
    if 'English' in sel_voice: # Set rate for each voice
        engine.setProperty('rate', 115) # Slow down english speak
    else:
        engine.setProperty('rate', 200) # Normal rate for Portuguese
    for voice in voices: # Set selected voice to create audio file
        if voice.name == sel_voice:
            engine.setProperty('voice', voice.id)
            print('Selected voice:', sel_voice)
            break   
    cleaned = re.sub(r'\[.*?\]', '', prompt_user) # Text cleaning for audio reproduction. Remove characters inside [] and <>
    cleaned = re.sub(r'<.*?>', '', cleaned)
    cleaned = cleaned.replace('**', '').replace('#', '') # Do not speak bolded text in Markdown
    cleaned = cleaned.replace('\n', ' ') # When copy and paste text from PDF file, the text use to come with '\n' at the end of every line
    cleaned = cleaned.replace('$$$', '')
    try: # Delete previous audio file for allow the creation of a new one
        os.remove('ia_response.mp3')
    except:
        pass
    engine.save_to_file(cleaned, 'ia_response.mp3') # Save audio file
    engine.runAndWait()
    return 'ia_response.mp3'


def unload_model():
    global llm
    click.play()
    try:
        del llm
        llm = ''
        print('Model deleted')
    except:
        pass


def split_text(text):
    text = text.replace('\n', ' ') # Paragraph
    palavras = text.split()
    tamanho_bloco = 110
    sobreposicao = 10
    partes = []
    inicio = 0 
    while inicio < len(palavras):
        fim = inicio + tamanho_bloco
        if fim > len(palavras):
            fim = len(palavras)
        parte = ' '.join(palavras[inicio:fim])
        partes.append(parte)
        inicio += tamanho_bloco - sobreposicao
    return '\n\n'.join(partes)


def extract_text():
    try:
        del root
        del tk
    except:
        pass
    import tkinter as tk
    click.play()

    root = tk.Tk()
    root.withdraw()
    root.attributes('-topmost', True) # Root window on the topmost
    while True: # IN TEST
        try:
            path = tk.filedialog.askopenfilename(
                title="Selecione um arquivo PDF",
                filetypes=[("Arquivos PDF", "*.pdf")]
            ) # Raising "RuntimeError: main thread is not in main loop"
            break
        except Exception as e:
            print('ERROR IN tk.filedialog:', traceback.format_exc())
            return
    if path == '':
        return
    path = path.replace('/', '\\')
    root.destroy()
    del root
    del tk
    with fitz.open(path) as pdf:
        text = ""
        total_pages = len(pdf)
        for page in pdf:
            text += f"\n\nPágina {page.number+1} de {total_pages}: "
            text += page.get_text().replace('\n', ' ')
        text = """[Generate a concise summary in Portuguese, one paragraph long, for the page below. Analyze carefully the textual content of the page. Generate a concise summary, faithfully capturing the main ideas. Each idea must be registered as a sentence in the paragraph. Start with the page number (ex: "Page 1:"). Generate the page summary in a single paragraph. Do not include comments and avoid unnecessary repetitions:]\n
[[Create a summary joining the text pages below. Distribute the text into paragraphs however you see fit. Do not mention page numbers neither include comments and avoid unnecessary repetitions. Start with the topic "Summary:":]]
        """ + text
    with open('text.txt', "w", errors='ignore') as f:
        f.write(text)

    for i in ['utf8', 'cp1254', 'latin1']:
        try:
            with open('text.txt', encoding=i) as f:   # , errors='ignore' utf8 cp1254
                return f.read()
        except:
            continue


def extract_full_text():
    try:
        del root
        del tk
    except:
        pass
    import tkinter as tk
    click.play()

    root = tk.Tk()
    root.withdraw()
    root.attributes('-topmost', True) # Root window on the topmost
    while True: # IN TEST
        try:
            path = tk.filedialog.askopenfilename(
                title="Selecione um arquivo PDF",
                filetypes=[("Arquivos PDF", "*.pdf")]
            ) # Raising "RuntimeError: main thread is not in main loop"
            break
        except Exception as e:
            print('ERROR IN tk.filedialog:', traceback.format_exc())
            return
    if path == '':
        return
    path = path.replace('/', '\\')
    root.destroy()
    del root
    del tk
    with fitz.open(path) as pdf:
        text = ""
        total_pages = len(pdf)
        for page in pdf:
            text += f"\n\nPágina {page.number+1} de {total_pages}: "
            text += page.get_text().replace('\n', ' ')
        text = """[Generate a concise summary in Portuguese, one paragraph long for each page below. Analyze carefully the textual content of the page. Generate a concise summary, faithfully capturing the main ideas. Each idea must be registered as a sentence in the paragraph. Start with the page number (ex: "Page 1:"), followed by the page summary. Generate the page summary in a single paragraph. Do not include comments and avoid unnecessary repetitions:]""" + text + '\n\n$$$'
    with open('text.txt', "w", errors='ignore') as f:
        f.write(text)

    for i in ['utf8', 'cp1254', 'latin1']:
        try:
            with open('text.txt', encoding=i) as f:   # , errors='ignore' utf8 cp1254
                return f.read()
        except:
            continue


def load_full_audio(*inputs):
    global engine
    click.play()
    # sel_voice = inputs[9]
    sel_voice = inputs[8]
    if 'English' in sel_voice: # Set rate for each voice
        engine.setProperty('rate', 115) # Slow down english speak
    else:
        engine.setProperty('rate', 200) # Normal rate for Portuguese
    for voice in voices: # Set selected voice to create audio file
        if voice.name == sel_voice:
            engine.setProperty('voice', voice.id)
            print('Selected voice:', sel_voice)
            break
    with open('full_text.txt', encoding='utf-8', errors='ignore') as f:
        full_text = f.read()
    cleaned = re.sub(r'\[.*?\]', '', full_text) # Text cleaning for audio reproduction. Remove characters inside [] and <>
    cleaned = re.sub(r'<.*?>', '', cleaned)
    cleaned = cleaned.replace('**', '').replace('#', '') # Do not speak bolded text in Markdown
    cleaned = cleaned.replace('\n', ' ') # When copy and paste text from PDF file, the text use to come with '\n' at the end of every line
    try: # Delete previous audio file for allow the creation of a new one
        os.remove('full_text.mp3')
    except:
        pass
    engine.save_to_file(cleaned, 'full_text.mp3') # Save audio file
    engine.runAndWait()
    return 'full_text.mp3'
 

def launch_notebook():
    """
    This function launches Jupyter Lab using the specified Python environment.
    
    It uses 'click' to play a sound indicating the action, then constructs 
    the path to the Jupyter Lab executable within the given Python environment,
    and finally opens it using 'subprocess.Popen'.
    """
    click.play()                    # Play a click sound
    # python_path = os.path.join(fr'{DIRETORIO_LOCAL}\miniconda3\envs\samantha\Scripts', "jupyter-lab.exe") # Define the path to the Jupyter Lab executable in the specified Python environment
    python_path = os.path.join(fr'{DIRETORIO_LOCAL}\miniconda3\envs\jupyterlab\Scripts', "jupyter-lab.exe") # Define the path to the Jupyter Lab executable in the specified Python environment
    
    subprocess.Popen([python_path]) # Open Jupyter Lab using the specified Python environment's executable path

        
def copy_code():
    click.play()
    padrao = r"```(.*?)\n(.*?)```"

    codigos = re.findall(padrao, ultima_resposta, re.DOTALL)

    # if infinite_loop == True: # If feedback loop is ON
    #     codigos = re.findall(padrao, previous_answer, re.DOTALL) # Copy code from previous response (after sinete sounds)
    # else:
    #     codigos = re.findall(padrao, ultima_resposta, re.DOTALL) # Copy code from output field (possible during code generation)

    resultado = []
    for codigo in codigos:
        linguagem, conteudo = codigo
        resultado.append(f"#{linguagem}\n{conteudo}")
    temp = "\n".join(resultado)
    pyperclip.copy(temp)

    # if read_aloud == True:
    #     try:
    #         run_code(temp)
    #     except Exception as e:
    #         print('ERROR in run_code function:', traceback.format_exc())
        

def copy_all_responses():
    click.play()
    pyperclip.copy(resposta)


def copy_last_response():
    click.play()
    pyperclip.copy(ultima_resposta)


def load_prompt_txt():
    try:
        del root
        del tk
    except:
        pass
    import tkinter as tk
    click.play()
    root = tk.Tk()
    root.withdraw()
    root.attributes('-topmost', True) # Root window on the topmost
    while True: # IN TEST
        try:
            path = tk.filedialog.askopenfilename(
                title="Selecione um arquivo TXT",
                filetypes=[("Arquivos TXT", "*.txt")]
            ) # Raising "RuntimeError: main thread is not in main loop"
            break
        except Exception as e:
            print('ERROR IN tk.filedialog:', traceback.format_exc())
            return
    path = path.replace('/', '\\')
    root.destroy()
    del root
    del tk
    if path == '':
        return '' # Em teste
    with open(path, 'r', encoding='utf-8', errors='ignore') as file:
        lines = file.readlines()
    cleaned_lines = []
    for line in lines:
        if not line.startswith('---'): # not line.startswith('#') and 
            cleaned_lines.append(line)
    cleaned_text = ''.join(cleaned_lines)
    return cleaned_text


def go_to_next_token():
    global next_token
    global one_click
    click.play()
    one_click = True # Used to unable click sound on STOP/NEXT and STOP ALL/RESET buttons
    next_token = True
 

def click_sound(examples): # Parameter included to avoid error in 'gr.Example()' element, that needs pass a input
    click.play()


def speech_to_text(*inputs):
    global engine
    global audio

    # sel_voice = inputs[9]
    sel_voice = inputs[8]

    for voice in voices: # Set selected voice to create audio file
        if voice.name == sel_voice:
            engine.setProperty('voice', voice.id)
            print('Selected voice:', sel_voice)
            break

    if 'English' in sel_voice: # Set rate for each voice
        engine.setProperty('rate', 115) # Slow down english speak
    else:
        engine.setProperty('rate', 200) # Normal rate for Portuguese


    # if read_aloud == False:
    #     new_fn = None
    # elif read_aloud == True:
    #     new_fn = speech_to_text

    # temp = inputs[9].value
    # prerequisites: as described in https://alphacephei.com/vosk/install and also python module `sounddevice` (simply run command `pip install sounddevice`)
    # Example usage using Dutch (nl) recognition model: `python test_microphone.py -m nl`
    # For more help run: `python test_microphone.py -h`

    click.play()

    q = queue.Queue()

    def int_or_str(text):
        """Helper function for argument parsing."""
        try:
            return int(text)
        except ValueError:
            return text

    def callback(indata, frames, time, status):
        """This is called (from a separate thread) for each audio block."""
        if status:
            print(status, file=sys.stderr)
        q.put(bytes(indata))

    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument(
        "-l", "--list-devices", action="store_true",
        help="show list of audio devices and exit")
    args, remaining = parser.parse_known_args()
    if args.list_devices:
        print(sd.query_devices())
        parser.exit(0)
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
        parents=[parser])
    parser.add_argument(
        "-f", "--filename", type=str, metavar="FILENAME",
        help="audio file to store recording to")
    parser.add_argument(
        "-d", "--device", type=int_or_str,
        help="input device (numeric ID or substring)")
    parser.add_argument(
        "-r", "--samplerate", type=int, help="sampling rate")
    parser.add_argument(
        "-m", "--model", type=str, help="language model; e.g. en-us, fr, nl; default is en-us")
    args = parser.parse_args(remaining)

    try:
        if args.samplerate is None:
            device_info = sd.query_devices(args.device, "input")
            # soundfile expects an int, sounddevice provides a float:
            args.samplerate = int(device_info["default_samplerate"])
            
        if args.model is None:
            if 'Portuguese' in sel_voice:
                model = Model(lang="pt") # <<<<<<<<<<<<<<<<<<<< Language:
            elif 'English' in sel_voice:
                model = Model(lang="en")
            else:
                model = Model(lang="en")
        else:
            model = Model(lang=args.model)

        if args.filename:
            dump_fn = open(args.filename, "wb")
        else:
            dump_fn = None

        with sd.RawInputStream(samplerate=args.samplerate, blocksize = 8000, device=args.device,
                dtype="int16", channels=1, callback=callback):
            print()
            print("=" * 80)
            print("Press Ctrl+C to stop the recording")
            print("=" * 80)

            rec = KaldiRecognizer(model, args.samplerate)

            saida = ''
            responder = False
            while True:
                data = q.get()
                if rec.AcceptWaveform(data):
                    output = rec.Result()
                    if '"text" : ""' in output:
                        continue
                    print(output[12:][:-2])
                    temp = json.loads(output)

                    # ====================================

                    # if 'Portuguese' in sel_voice:
                    #     if 'samantha' in temp['text'].lower() or\
                    #         ('sim' in temp['text'].lower() and responder == True) or\
                    #         ('não' in temp['text'].lower() and responder == True):

                    #         if temp['text'].lower() == 'samantha':
                    #             continue
                            
                    #         try: # Delete previous audio file for allow the creation of a new one
                    #             os.remove('voice.mp3')
                    #         except:
                    #             pass
                    #         if 'fechar' == temp['text'].replace('samantha', '').strip():
                    #             temp = 'fechando'
                    #         elif 'leia novamente' == temp['text'].replace('samantha', '').strip():
                    #             temp = 'Lendo novamente'
                    #         elif responder == False:
                    #             saida = temp['text'].replace('samantha', '').strip().capitalize()
                    #             temp = saida + '.\n' + 'Devo responder?'
                    #             responder = True
                    #         elif responder == True:
                    #             temp = temp['text'].replace('samantha', '').strip()
                    #             if 'sim' in temp:
                    #                 temp = 'Ok!'
                    #                 # responder = False
                                    
                    #                 yield saida # <<<<<<<<<<<<<<< SAÍDA

                    #             elif 'não' in temp:
                    #                 temp = 'Tudo bem.'
                    #                 # responder = False
                    #             responder = False
                    #         if temp == 'Lendo novamente':
                    #             engine.save_to_file('Lendo resposta anterior. ' + ultima_resposta, 'voice.mp3') # Save audio file
                    #             engine.runAndWait()
                    #             audio = pygame.mixer.Sound('voice.mp3') # Read aloud the saved audio file with the previous Assistant response
                    #             audio.set_volume(1.0)
                    #             audio.play()
                    #         else:
                    #             engine.save_to_file(temp, 'voice.mp3') # Save audio file
                    #             engine.runAndWait()
                    #             audio = pygame.mixer.Sound('voice.mp3') # Read aloud the saved audio file with the previous Assistant response
                    #             audio.set_volume(1.0)
                    #             audio.play()
                    #         if temp == 'fechando':
                    #             return


                    # TO FAST TALK IN PORTUGUESE
                    # =================================== 

                    if 'Portuguese' in sel_voice:
                        if 'samantha' in temp['text'].lower():
                            if temp['text'].lower() == 'samantha':
                                continue                      
                            saida = temp['text'].replace('samantha', '').strip().capitalize()
                            yield saida

                    # ====================================
                    # if 'English' in sel_voice:
                    #     if 'samantha' in temp['text'].lower() or\
                    #         ('yes' in temp['text'].lower() and responder == True) or\
                    #         ('no' in temp['text'].lower() and responder == True):
                    #         if temp['text'].lower() == 'samantha':
                    #             continue
                                                        
                    #         try: # Delete previous audio file for allow the creation of a new one
                    #             os.remove('voice.mp3')
                    #         except:
                    #             pass
                    #         if 'close' == temp['text'].replace('samantha', '').strip():
                    #             temp = 'closing'
                    #         elif 'read again' == temp['text'].replace('samantha', '').strip():
                    #             temp = 'Reading again'
                    #         elif responder == False:
                    #             saida = temp['text'].replace('samantha', '').strip().capitalize()
                    #             temp = saida + '.\n' + 'Should I respond?'
                    #             responder = True
                    #         elif responder == True:
                    #             temp = temp['text'].replace('samantha', '').strip()
                    #             if 'yes' in temp:
                    #                 temp = 'Ok!'
                    #                 responder = False
                                    
                    #                 yield saida # <<<<<<<<<<<<<<< SAÍDA

                    #             elif 'no' in temp:
                    #                 temp = 'No problem.'
                    #                 responder = False
                    #         if temp == 'Reading again':
                    #             engine.save_to_file('Reading previous response again. ' + ultima_resposta, 'voice.mp3') # Save audio file
                    #             engine.runAndWait()
                    #             audio = pygame.mixer.Sound('voice.mp3') # Read aloud the saved audio file with the previous Assistant response
                    #             audio.set_volume(1.0)
                    #             audio.play()
                    #         else:
                    #             engine.save_to_file(temp, 'voice.mp3') # Save audio file
                    #             engine.runAndWait()
                    #             audio = pygame.mixer.Sound('voice.mp3') # Read aloud the saved audio file with the previous Assistant response
                    #             audio.set_volume(1.0)
                    #             audio.play()
                    #         if temp == 'closing':
                    #             return
                            

                    # TO FAST TALK IN ENGLISH
                    # =================================== 

                    if 'English' in sel_voice:
                        if 'samantha' in temp['text'].lower():
                            if temp['text'].lower() == 'samantha':
                                continue                      
                            saida = temp['text'].replace('samantha', '').strip().capitalize()
                            yield saida                                                   

                if dump_fn is not None:
                    dump_fn.write(data)

    except KeyboardInterrupt:
        print("\nDone")
        parser.exit(0)
    except Exception as e:
        parser.exit(type(e).__name__ + ": " + str(e))


def extract_models_names(): # Load Model button: open window to choose directory with LLM files
    global model_path
    global models
    global last_models_list
    global last_diretorio
    global last_model
    click.play()
    
    # ==================================
    
    try: # This try/except was included for trying to solve an exporadic Tkinter error: "RuntimeError: main thread is not in main loop"
        del root
        del tk
    except:
        pass
    import tkinter as tk # To create a window for selecting directories and files. Imported here to avoid "Tcl_AsyncDelete: async handler deleted by the wrong thread" error
    root = tk.Tk()
    root.withdraw()
    root.attributes('-topmost', True) # Root window on the topmost
    while True: # IN TEST
        try:
            diretorio = tk.filedialog.askdirectory() # Raising "RuntimeError: main thread is not in main loop"
            break
        except Exception as e:
            print('ERROR IN tk.filedialog:', traceback.format_exc())
            del root
            del tk
            return gr.Dropdown(choices=last_models_list, value=models[0])
    root.destroy()
    del root
    del tk

    # ==================================

    diretorio = diretorio.replace('/', '\\')
    if diretorio == '':
        # SE TENTAR SELECIONAR DUAS VEZES E CANCELAR A SELEÇÃO, DÁ ERRO NA SEGUNDA (ERROR ONLY USING DEBUG MODE): "Tcl_AsyncDelete: async handler deleted by the wrong thread"
        try:
            if last_model == '':
                return gr.Dropdown(choices=last_models_list, value=models[0])
            else:
                return gr.Dropdown(choices=last_models_list, value=last_model)
        except:
            return gr.Dropdown(choices=[''], value='') # Included to avoid 'out of range' list error
    last_diretorio = diretorio
    model_path = diretorio
    temp = glob.glob(fr'{model_path}\*.gguf') # Create .uggf files path list to the selected directory. Update global variable (ok?)
    models = [i.split('\\')[-1] for i in temp] # Create list only with files names. Upadte global variable
    
    print()
    print('Models:')
    for n, i in enumerate(models):
        print(n + 1, i)
    print()
    last_models_list = models
    
    if len(models) == 1: # Update models dropdowm widget
        return gr.Dropdown(choices=models, value=models)
    elif len(models) > 1:
        return gr.Dropdown(choices=models, value=models[0])


def open_db_browser():

    click.play()                    # Play a click sound
    python_path = os.path.join(fr'{DIRETORIO_LOCAL}\DB Browser for SQLite', "DB Browser for SQLite.exe") # Define the path to the Jupyter Lab executable in the specified Python environment
    subprocess.Popen([python_path]) # Open DB Browser using the specified Python environment's executable path


def open_dtale():

    click.play()
    subprocess.run(['open_dtale.bat'], shell=True)


def download_model(url):

    # Download a model from url and save it in "Downloads" folde

    # Hugging Face Model URL
    # url = "https://huggingface.co/bartowski/DeepSeek-Coder-V2-Lite-Instruct-GGUF/resolve/main/DeepSeek-Coder-V2-Lite-Instruct-IQ2_M.gguf?download=true"

    # def download_and_rename_model(url):
    try:
        # 2) Extrair o caminho completo da pasta "Downloads"
        downloads_path = Path(os.path.expanduser("~")) / "Downloads"
        print(downloads_path)

        try:
            os.remove(downloads_path / "MODEL_FOR_TESTING.gguf")
        except Exception as e:
            print(e)
        
        # 3) Baixar o arquivo da URL
        response = requests.get(url, verify=False)
        if response.status_code != 200:
            raise Exception(f"Failed to download file. Status code: {response.status_code}")
        
        # Obter o nome original do arquivo da URL
        original_filename = os.path.basename(urlparse(url).path)
        
        # Caminho temporário para o arquivo baixado
        temp_file_path = downloads_path / original_filename
        
        # Salvar o arquivo baixado
        with open(temp_file_path, 'wb') as file:
            file.write(response.content)
            
        # 4) Renomear o arquivo ".gguf"
        new_file_path = downloads_path / "MODEL_FOR_TESTING.gguf"
        os.rename(temp_file_path, new_file_path)
        
        # 5) Retornar o caminho completo para o arquivo
        return str(new_file_path)
    
    finally:
        pass
        # Limpeza de memória
        if 'response' in locals():
            del response
        if 'file' in locals():
            del file
        gc.collect()  # Força a coleta de lixo

    # Exemplo de uso:
    # caminho_do_arquivo = download_and_rename_model(url)
    # print(f"O arquivo foi baixado e renomeado. Caminho: {caminho_do_arquivo}")

    # Limpeza adicional após o uso
    # gc.collect()

    # return caminho_do_arquivo


# # TO RUN CODE AUTOMATICALLY AFTER ITS GENERATION 
# def run_my_code(code: str): # Cria um arquivo .py no diretório local
#     if 'runthecode' in prompt.lower() or 'runthecode' in previous_answer.lower():
#         html_files = glob.glob('*.html')
#         for file in html_files:
#             os.remove(file)
#         file_name = "code_my_code.py"
#         with open(file_name, "w") as file:
#             file.write(code)
#         try:
#             subprocess.run(["python", file_name]) # Executa o arquivo .py via terminal com o interpretador do ambiente virtual atual
#         finally:
#             os.remove(file_name) # Remove o arquivo .py temporário (talvez melhor não apagar)


# ================
# GRADIO INTERFACE
# ================ 

# https://www.gradio.app/
  
# CSS code
css = """
#examples {color: #9CA3AF}
.prompt textarea {background-color: #0b0f19 !important}
.prompt textarea {color: #9CA3AF !important}
#prompt_id textarea {border-width: 1px !important}
#prompt_id textarea {border-color: #777777 !important}
"""


with gr.Blocks(css=css, title='Samantha IA') as demo: # AttributeError: Cannot call change outside of a gradio.Blocks context.
    
    # Imange
    # gr.HTML("""
    #         <img id="overlay-image" src="https://pngfre.com/wp-content/uploads/butterfly-27-1024x688.png" alt="Imagem no Canto Superior Esquerdo" style="position: absolute; top: 10px; left: 10px; width: 60px; height: auto; z-index: 9999;">
    #         """)
    
    # Page title
    gr.HTML(f'<h1 style="text-align: center; margin: -5px 0 0; color: #f3813f">{language["title"]}</h1>')
    gr.HTML(f'<h5 style="text-align: center; margin: -7px 0 0px"><b><span style="color: #9CA3AF;">{language["subtitle_1"]}</span></b></h5>')
    gr.HTML(f'<h6 style="text-align: center; margin: -7px 0 0px; font-size: 0.9em"><b><span style="color: #f3813f;">{language["warning"]}: </span></b><b><span style="color: #9CA3AF;">{language["subtitle_2"]}</span></b></h6>')
    gr.HTML(f"""<h6 style="text-align: right; margin: -7px 0 0px; font-size: 0.9em"><i><span style="color: #9CA3AF;">{language["subtitle_3"]}</span></i></h6>""")
    
    with gr.Row():
            

        # ====================
        # INPUT COMLUMN (LEFT)
        # ====================

        with gr.Column(scale=1):
            with gr.Row(): # Input buttons
                btn1 = gr.Button(language['btn1'], variant='primary')
                btn2 = gr.Button(language['btn2'])
                btn3 = gr.Button(language['btn3'])
            with gr.Row():
                btn4 = gr.Button(language['btn4'])
                btn5 = gr.Button(language['btn5'])
                btn6 = gr.Button(language['btn6'])

            # ATENTION! This list MUST follows the function 'text_generator' parameters sequence
            inputs = [
                gr.Textbox(value=system_prompt, lines=1, label='SYSTEM prompt', info=language['system_prompt_info'], elem_classes='prompt', interactive=True, show_copy_button=True),
                gr.Checkbox(value=infinite_loop, label='Feedback Loop', info=language["feedback_loop_info"], interactive=True),
                gr.Textbox(value=previous_answer, lines=1, label="ASSISTANT previous response (" + language['changeble'] + ")", info=language['assistant_previous_response_info'], elem_classes='prompt', interactive=True, show_copy_button=True),
                gr.Textbox(value=prompt, lines=1, label="USER prompt (" + language['text_to_speech'] + ")", info=language['user_prompt_info'], elem_classes='prompt', elem_id='prompt_id', interactive=True, show_copy_button=True),
                gr.Dropdown(choices=models, value=None, multiselect=True, allow_custom_value=True, label="Models selection", info=language['models_selection_info'], interactive=True),
                gr.Textbox(value=None, lines=1, label="Download model for testing", info=language['model_url_info'], elem_classes='prompt', interactive=True, show_copy_button=True),
                gr.Checkbox(value=reset_mode, label="Reset model", info=language['reset_model_info'], interactive=True),
                gr.Checkbox(value=random_list, label="Shuffle models", info=language['shuffle_models_order_info'], interactive=True),
                gr.Checkbox(value=fast_mode, label="Fast Mode", info=language['fast_mode_info'], interactive=True),
                gr.Dropdown(choices=[x.name for x in voices], value=selected_voice, multiselect=False, label="Voice selection", info=language['voice_selection_info'], interactive=True),                    
                gr.Checkbox(value=read_aloud, label="Read response aloud", info=language['read_aloud_info'], interactive=True),
                gr.Radio(['OFF', 0.3, 1, 5, 15, 30, 'NEXT TOKEN'], value='OFF', label='Learning Mode', info=language['learning_mode_info'], interactive=leaning_mode_interatcive),
                gr.Radio([1, 2, 3, 4, 5, 10, 100, 1000], value=1, label="Number of loops", info=language['number_of_loops_info'], interactive=True),
                gr.Radio([1, 2, 3, 4, 5, 10, 100, 1000], value=1, label="Number of responses", info=language['number_of_responses_info'], interactive=True),
                gr.Slider(0, 300_000, 4000, 64, label='n_ctx', info=language['n_ctx_info'], interactive=True),
                gr.Slider(0, 300_000, 4000, 1, label='max_tokens', info=language['max_tokens_info'], interactive=True),
                gr.Slider(0, 5, 0.2, 0.1, label='temperature', info=language['temperature_info'], interactive=True),
                gr.Textbox('["§§§"]', label='stop', info=language['stop_info'], interactive=True),
                gr.Slider(1e-5, 1, 1, 0.1, label='tfs_z', info=language['tfs_z_info'], interactive=True),
                gr.Slider(1e-6, 1, 0.95, 0.1, label='top_p', info=language['top_p_info'], interactive=True), # 1e-5 (0.00001) try to make refference to the probability of one single token
                gr.Slider(0, 1, 0.05, 0.01, label='min_p', info=language['min_p_info'], interactive=True), # 
                gr.Slider(1, 200_000, 40, 1, label='top_k', info=language['top_k_info'], interactive=True),
                gr.Slider(0, 10, 0, 0.1, label='presence_penalty', info=language['presence_penalty_info'], interactive=True),
                gr.Slider(0, 10, 0, 0.1, label='frequency_penalty', info=language['frequency_penalty_info'], interactive=True),
                gr.Slider(0, 10, 1.1, 0.1, label='repeat_penalty', info=language['repeat_penalty_info'], interactive=True),
                
                # gr.Textbox(value=prompt_template, lines=1, label='Model prompt template', info=language['model_prompt_template'], elem_classes='prompt'),

                gr.Textbox(value=model_metadata, label='Model metadata', info=language['model_metadata_info'], elem_classes='prompt'),
                gr.Textbox(value='', lines=1, label='Model vocabulary', info=language['model_vocabulary'], elem_classes='prompt')
            ]
            with gr.Row():
                btn_unload = gr.Button(language['btn_unload_model'])
                btn_unload.click(fn=unload_model, inputs=None, outputs=None)
                btn_files = gr.Button(language['btn_load_pdf_pages'])
                btn_files.click(fn=extract_text, inputs=None, outputs=inputs[3], queue=False)
                btn_notebook = gr.Button(language['btn_load_full_pdf'])
                btn_notebook.click(fn=extract_full_text, inputs=None, outputs=inputs[3], queue=False)
            
            with gr.Row():
                btn_load_system_prompt = gr.Button(language['btn_system_prompt'])
                btn_load_system_prompt.click(fn=load_prompt_txt, inputs=None, outputs=inputs[0], queue=False)
                btn_load_user_prompt = gr.Button(language['btn_user_prompt'])
                btn_load_user_prompt.click(fn=load_prompt_txt, inputs=None, outputs=inputs[3], queue=False)
                btn_y = gr.Button('')
                btn_y.click(fn=None, inputs=None, outputs=None, queue=True)
            
            gr.HTML('<br><h6><b>Exploratory Data Analysis (EDA):</b></h6>') # Useful Links

            with gr.Row():
                btn_x1 = gr.Button('DB Browser')
                btn_x1.click(fn=open_db_browser, inputs=None, outputs=None)
                btn_x2 = gr.Button('D-Tale')
                btn_x2.click(fn=open_dtale, inputs=None, outputs=None)
                btn_x3 = gr.Button('')
                btn_x3.click(fn=None, inputs=None, outputs=None)
                
            # with gr.Row():
            #     btn_x4 = gr.Button('')
            #     btn_x4.click(fn=, inputs=None, outputs=None)
            #     btn_x5 = gr.Button('')
            #     btn_x5.click(fn=None, inputs=None, outputs=None)
            #     btn_x6 = gr.Button('')
            #     btn_x6.click(fn=None, inputs=None, outputs=None)


            gr.HTML('<br><h6><b>Useful links:</b></h6>') # Useful Links


            gr.HTML("""<ul>
                        <li><a href="https://huggingface.co/models?search=gguf">GGUF Hugging Face Search Results</a></li>
                        <li><a href="https://chat.lmsys.org/">LLM Leaderboard</a></li>
                        <li><a href="https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard">Open LLM Benchmark</a></li>
                        <li><a href="https://huggingface.co/spaces/ggml-org/gguf-my-repo">GGUF My Repository</a></li>
                        <li><a href="https://www.google.com/search?q=google+tradutor">Google Translator</a></li>
                        <li><a href="https://nulpointerexception.com/2017/12/16/a-tutorial-to-understand-decision-tree-id3-learning-algorithm/">Decision Tree - Play Tennis Dataset</a></li>
                        <li><a href="https://huggingface.co/spaces/Xenova/the-tokenizer-playground">Tokenizer Playground</a></li>
                        <li><a href="https://huggingface.co/datasets/taesiri/arxiv_qa">Training Dataset Example</a></li>
                        <li><a href="https://llama-cpp-python.readthedocs.io/en/latest/api-reference/">llama-cpp-python API Reference</a></li>
                        <li><a href="https://github.com/abetlen/llama-cpp-python">llama-cpp-python on GitHub</a></li>
                        <li><a href="https://github.com/byroneverson/llm.cpp/blob/master/examples/main/README.md">llama.cpp examples on GitHub</a></li>
                        <li><a href="https://github.com/ggerganov/llama.cpp">llama.cpp</a></li>
                        <li><a href="https://github.com/unslothai/unsloth">Unsloth Finetunnig</a></li>
                        <li><a href="https://github.com/cg123/mergekit">LLM Mergekit</a></li>
                        <li><a href="https://huggingface.co/autotrain">AutoTrain Finetuning LLM</a></li>
                        <li><a href="https://huggingface.co/docs/hub/gguf">GGUF File</a></li>
                        <li><a href="https://platform.openai.com/docs/guides/prompt-engineering">OpenAI Prompt Engineering</a></li>
                        <li><a href="https://github.com/sqlitebrowser/sqlitebrowser/wiki/Using-the-Filters">DB Browser - Using Filters</a></li>
                        
                    </ul>""")
                        # <li><a href="https://huggingface.co/spaces/bigcode/bigcode-models-leaderboard">Big Code Models Leaderboard</a></li>
                        # <li><a href="https://huggingface.co/TheBloke">Hugging Face / TheBloke - LLM Repository</a></li>
                        # <li><a href="https://llm-leaderboard.streamlit.app/">LLM Leaderboard Unification</a></li>         
                        # <li><a href="https://huggingface.co/spaces/eduagarcia/open_pt_llm_leaderboard">Portuguese LLM Leaderboard</a></li>
                        

            gr.HTML('<br><h6><b>Tutorials:</b></h6>') # Tutorials
            gr.HTML("""<ul>
                    <li><a href="https://www.youtube.com/watch?v=wjZofJX0v4M&list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi&index=5">But what is a GPT? (3Blue 1Brown)</a></li>
                    <li><a href="https://www.youtube.com/watch?v=xU_MFS_ACrU">How do LLMs like ChatGPT work?</a></li>
                    <li><a href="https://www.youtube.com/watch?v=eMlx5fFNoYc">Visualizing Attention, a Transformer's Heart</a></li>
                    <li><a href="https://www.youtube.com/watch?v=zjkBMFhNj_g">Intro to Large Language Models</a></li>
                    <li><a href="https://www.youtube.com/watch?v=rEDzUT3ymw4">Neural Network in 1 Minute</a></li>
                    <li><a href="https://www.youtube.com/watch?v=kCc8FmEb1nY">Let's build GPT: from scratch, in code, spelled out</a></li>
                    <li><a href="https://www.promptingguide.ai/">Prompt Engineering Guide</a></li>
                    <li><a href="https://www.youtube.com/watch?v=XpoKB3usmKc">QLoRA—How to Fine-tune an LLM on a Single GPU</a></li>
                    <li><a href="https://www.youtube.com/watch?v=Ylz779Op9Pw">How to Improve LLMs with RAG</a></li>
                    </ul>""")
                    # https://www.youtube.com/watch?v=FdTRzgbBP8o
            gr.HTML('<br><h6><b>Installed Python Modules to Use with JupyterLab:</b></h6>') # Exploratory Data Analysis
            gr.HTML("""<ul>
                    <li><a href="https://seaborn.pydata.org/">Seaborn</a></li>
                    <li><a href="https://altair-viz.github.io/">Vega-Altair</a></li>
                    <li><a href="https://plotly.com/python/">Plotly</a></li>
                    <li><a href="https://pyvis.readthedocs.io/en/latest/">Pyvis</a></li>
                    <li><a href="https://networkx.org/documentation/stable/index.html">NetworkX</a></li>
                    <li><a href="https://github.com/fbdesignpro/sweetviz">Sweetviz</a></li>
                    <li><a href="https://github.com/man-group/dtale">D-Tale</a></li>
                    <li><a href="https://dataprep.ai/">DataPrep</a></li>
                    <li><a href="https://pandas.pydata.org/">Pandas</a></li>
                    <li><a href="https://pymupdf.readthedocs.io/en/latest/">PyMuPDF</a></li>
                    <li><a href="https://pypi.org/project/beautifulsoup4/">Beautifulsoup4</a></li>
                    </ul>""")
            
                    #<li><a href="https://playwright.dev/python/docs/intro">Playwright</a></li>
                    #<li><a href="https://github.com/ydataai/ydata-profiling">Pandas Profiling</a></li>
            
            gr.HTML('<br><h6><b>Accessibility:</b></h6>') # Exploratory Data Analysis
            gr.HTML("""<ul>
                    <li><a href="https://support.microsoft.com/en-us/windows/windows-keyboard-shortcuts-for-accessibility-021bcb62-45c8-e4ef-1e4f-41b8c1fc87fd">Windows keyboard shortcuts for accessibility</a></li>
                    <li><a href="https://support.microsoft.com/en-us/windows/appendix-b-narrator-keyboard-commands-and-touch-gestures-8bdab3f4-b3e9-4554-7f28-8b15bd37410a#WindowsVersion=Windows_11">Narrator keyboard commands and touch gestures</a></li>
                    </ul>""")
            
            
            # gr.HTML(f'<br><h6><b>Available GGUF models to download ({len(headings)}):</b></h6>')
            # gr.HTML(links)


        # =====================
        # OUTPUT COLUMN (RIGHT)
        # =====================
            
        with gr.Column(scale=1):
            with gr.Row():
                saida = gr.Textbox(value='', label="Assistant output", info=language['assistant_raw_output_info'], show_copy_button=True)
                outputs = [saida] # Primeiro elemento da tupla de saída da função 'text_generator' (token)
            with gr.Row():
                btn_next_token = gr.Button(language['btn_next_token'])
                btn_next_token.click(fn=go_to_next_token, inputs=None, outputs=None, queue=False) 
                btn_copy_code = gr.Button(language['btn_copy_code_blocks'])
                btn_copy_code.click(fn=copy_code, inputs=None, outputs=None, queue=False)
                btn_notebook = gr.Button(language['btn_open_jupyterlab'])
                btn_notebook.click(fn=launch_notebook, inputs=None, outputs=None, queue=False)
            with gr.Row():
                btn_last_response = gr.Button(language['btn_copy_last_response'])
                btn_last_response.click(fn=copy_last_response, inputs=None, outputs=None, queue=False)
                btn_all_responses = gr.Button(language['btn_copy_all_responses'])
                btn_all_responses.click(fn=copy_all_responses, inputs=None, outputs=None, queue=False)
                                
                # =================================
                
                # Voice control
                if voice_mode == True:
                    btn_voice = gr.Button(language['btn_voice_command'], variant='primary', visible=True)
                    btn_voice.click(fn=speech_to_text, inputs=inputs, outputs=inputs[3], queue=True, show_progress='hidden')
                    inputs[3].change(fn=text_generator, inputs=inputs, outputs=outputs, queue=True)
                elif voice_mode == False:
                    btn_voice = gr.Button('')

                # =================================
            
            with gr.Row():
                plot_1 = gr.BarPlot(visible=False) # Creates first plot that is updeted in the sequence (https://www.gradio.app/docs/barplot)
                demo.load(fn=update_barplot_widget, inputs=None, outputs=plot_1)
                saida.change(fn=update_barplot_widget, inputs=None, outputs=plot_1, show_progress='hidden', queue=False)
            with gr.Row():
                plot_2 = gr.BarPlot(visible=False) # Creates second plot that is updeted in the sequence
                demo.load(fn=update_barplot_widget_2, inputs=None, outputs=plot_2)
                saida.change(fn=update_barplot_widget_2, inputs=None, outputs=plot_2, show_progress='hidden', queue=False)
            with gr.Row():
                audio_widget = gr.Audio(value='introducao.mp3', type='filepath', autoplay=False, interactive=True, show_download_button=True, editable=True, show_share_button=True)
            with gr.Row():
                btn_gen_audio = gr.Button(language['btn_text_to_speech'])
                btn_gen_audio.click(fn=text_to_speech, inputs=inputs, outputs=audio_widget, queue=True)
                btn_audio = gr.Button(language['btn_last_response'])
                btn_audio.click(fn=update_audio_widget, inputs=inputs, outputs=audio_widget, queue=False)
                btn_full_audio = gr.Button(language['btn_all_responses'])
                btn_full_audio.click(fn=load_full_audio, inputs=inputs, outputs=audio_widget, queue=False)
            
            with gr.Row():
                gr.HTML("""<br><h5 style="text-align: left; margin: -5px 0 0; color: #f3813f">Models Repository:</h5>""")
                
            with gr.Row():
                gr.HTML("""<ul>
                        <li><a href="https://huggingface.co/models?sort=trending&search=gguf">Hugging Face GGUF Models</a></li>
                        </ul>""")
            
            with gr.Row():
                gr.HTML("""<br><h5 style="text-align: left; margin: -5px 0 0; color: #f3813f">Operating Tips:</h5>""")
            # with gr.Row():
            #     gr.HTML("""<h6 style="text-align: left;"><i><span style="color: #9CA3AF;">Key Concepts:&nbsp;&nbsp;&nbsp;Training Dataset / Prompt, Token, Token Vocabulary, Large Language Model (LLM), Training / Generation, Embedding Vectors, Embedding Matrix, Artificial Neural Networks (Layers, Weights and Bias), Ordered Token Vocabulary, Next Token Selection</span></i></h6>""")                      
            with gr.Row():
                gr.HTML("""<h6 style="text-align: left;"><i><span style="color: #9CA3AF;">Samantha's Parts:&nbsp;&nbsp;&nbsp;Server (AI processing) <-> Browser Interface (display and configuration)</span></i></h6>""")
            with gr.Row():
                gr.HTML('<h6 style="text-align: left;"><i><span style="color: #9CA3AF;">File Required:&nbsp;&nbsp;&nbsp;.GGUF Model File</span></i></h6>', elem_classes='prompt')
            # with gr.Row():
            #     gr.HTML(r'<h6 style="text-align: left;"><i><span style="color: #9CA3AF;">4) Model Prompt Template:&nbsp;&nbsp;&nbsp;special characters + {system_prompt} + {prompt}</span></i></h6>', elem_classes='prompt')
            with gr.Row():
                gr.HTML('<h6 style="text-align: left;"><i><span style="color: #9CA3AF;">Generation Phases:&nbsp;&nbsp;&nbsp;Model Loading (non stop) -> Thinking (non stop) -> Next Token Selection (stop)</span></i></h6>', elem_classes='prompt')
            with gr.Row():
                gr.HTML('<h6 style="text-align: left;"><i><span style="color: #9CA3AF;">Context Window:&nbsp;&nbsp;&nbsp;System Prompt + Previous Response + User Prompt + Current Response</span></i></h6>')
            with gr.Row():
                gr.HTML('<h6 style="text-align: left;"><i><span style="color: #9CA3AF;">Chaining Sequence:&nbsp;&nbsp;&nbsp;(Models List -> User Prompt List -> Number of Responses) -> Number of Loops</span></i></h6>')         
            # with gr.Row():
            #     gr.HTML('<h6 style="text-align: left;"><i><span style="color: #9CA3AF;">GPT:&nbsp;&nbsp;&nbsp;Choice of the next token according to the probability patterns extracted from the training texts</span></i></h6>')                     
            # with gr.Row():
            #     gr.HTML('<h6 style="text-align: left;"><i><span style="color: #9CA3AF;">Choice Probabilities:&nbsp;&nbsp;&nbsp;Deterministic (high score difference) X Sthocastic (low score difference)</span></i></h6>')                    
            # with gr.Row():
            #     gr.HTML('<h6 style="text-align: left;"><i><span style="color: #9CA3AF;">Tokenizer:&nbsp;&nbsp;&nbsp;Datasets (text) -> Tokens (text) -> Tokens Indexes (int) -> Model Vocabulary (int/text)</span></i></h6>')         
            # with gr.Row():
            #     gr.HTML('<h6 style="text-align: left;"><i><span style="color: #9CA3AF;">Embeddings Matrix:&nbsp;&nbsp;&nbsp;Tokens Indexes (int) -> Semantic/Sintatic Relations (vector) -> Matrix (feature table)</span></i></h6>')         
            # with gr.Row():
            #     gr.HTML('<h6 style="text-align: left;"><i><span style="color: #9CA3AF;">Math Representation:&nbsp;&nbsp;&nbsp;Human Language Semantic Universe (words all languages) <-> Mathematical Semantic Dimensions (same numeric repr)</span></i></h6>')         
            # with gr.Row():
            #     gr.HTML('<h6 style="text-align: left;"><i><span style="color: #9CA3AF;">Transformer:&nbsp;&nbsp;&nbsp; Initial Embeddings Matrix (table) -> Neural Network (self-attention) -> Context-Aware Embeddings (table) -> Tokens Scores (vocab)</span></i></h6>')     
            # with gr.Row():
            #     gr.HTML('<h6 style="text-align: left;"><i><span style="color: #9CA3AF;">Samplings/Penalties:&nbsp;&nbsp;&nbsp;Samplings (temperature/top-k/top-p) -> Penalties (presence/frequency/repeat) -> Stop Conditions</span></i></h6>')         
            # with gr.Row():
            #     gr.HTML('<h6 style="text-align: left;"><i><span style="color: #9CA3AF;">Summary:&nbsp;&nbsp;&nbsp;(Context Window (text) -> Tokens (vocab) -> Initial Embeddings Matrix (table) -> Transformer (self-attention) -> Context-Aware Embeddings (table) -> Tokens Scores (vocab) -> Sampling/Penalty) -> Stop Condition</span></i></h6>')         
            
            with gr.Row():
                gr.HTML("""<br><h5 style="text-align: left; margin: -5px 0 0; color: #f3813f">USER prompt examples</h5>""")
            with gr.Row():
                gr.Examples(fn=click_sound, run_on_click=True, examples=examples, label=None, examples_per_page=100, elem_id="examples", inputs=[inputs[3]])
            
            with gr.Row():
                gr.HTML('<br><h5 style="text-align: left; margin: -5px 0 0; color: #f3813f">SYSTEM prompt examples</h5>')
            with gr.Row():
                gr.Examples(fn=click_sound, run_on_click=True, examples=messages_text, label=None, examples_per_page=100, elem_id="examples", inputs=[inputs[0]])
        
        btn1.click(fn=text_generator, inputs=inputs, outputs=outputs, queue=True) # Input buttons actions (fucntion calls)
        btn2.click(fn=go_to_next_token, inputs=None, outputs=None, queue=False) # Bound to STOP / NEXT button
        btn2.click(fn=stop_running, inputs=None, outputs=None, queue=False)
        btn3.click(fn=clean_output, inputs=None, outputs=[saida], queue=True)
        # btn4.click(fn=extract_models_names, inputs=None, outputs=inputs[5])
        btn4.click(fn=extract_models_names, inputs=None, outputs=inputs[4])
        
        
        btn5.click(fn=go_to_next_token, inputs=None, outputs=None, queue=False) # Bound to STOP ALL / RESET button
        btn5.click(fn=stop_running_all, inputs=None, outputs=None, queue=False)
        btn6.click(fn=update_previous_answer, inputs=None, outputs=inputs[2], queue=False, show_progress='hidden')
        
        # saida.change(fn=update_template_field, inputs=None, outputs=inputs[-2], trigger_mode='always_last', queue=False, show_progress=False) 
        
        saida.change(fn=update_vocabulary, inputs=None, outputs=inputs[-1], trigger_mode='always_last', queue=True, show_progress=False)
        inputs[-1].change(fn=update_metadata, inputs=None, outputs=inputs[-2], trigger_mode='always_last', queue=True, show_progress=False)
        
        # inputs[-2].change(fn=update_vocabulary, inputs=None, outputs=inputs[-1], trigger_mode='always_last', queue=False)


def main():
    while True:  
        try:
            demo.queue()                # Put interface on queue
            open_browser()              # Open browser before endpoint generation (wait demo launch)
            demo.launch(share=False)
        except:
            continue


if __name__ == '__main__':
    main()
    
