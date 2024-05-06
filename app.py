# =================================
# SAMANTHA IA - INTERFACE ASSISTANT
# =================================

# This is an experimental project that was developed solely with the aim of encouraging.
# the creation of similar works.


# =============
# PREREQUISITES
# =============

# TO LLAMA.CPP:
# Download and install Microsoft Visual Studio Install: https://visualstudio.microsoft.com/pt-br/downloads/?cid=learn-navbar-download-cta
# Select the "Desenvolvimento para desktop com C++", that contain CMake
# Select SDK options

# TO PLAYWRIGHT
# Chromium browser download use to show some issues with SSL. Try others internet conection.


# =====================
# APP STEPS DESCRIPTION
# =====================

# 1) Import Python modules
# 2) Get current directory
# 3) Initialize Pygame and Pyttsx3 modules
# 4) Ask user about downloading models links
# 5) Get local models list
# 6) Create remaining global variables
# 7) Read TXT files with prompt examples
# 8) Load text generator function (main function)
# 9) Load auxiliary functions
# 10) Create web interface with Gradio
# 11) Launch server on localhost

# ATALHOS VSCODE
# CTRL + K -> CTRL + 0 = Recolhe todas as funções
# CTRL + K -> CTRL + J = Expande todas as funções

# =========================
# IMPORT PYTHON MODULES
# =========================

import gradio as gr              # To create web interface (front-end) BREAKPOINT
from llama_cpp import Llama      # To load LLMs UGGF files (back-end)
import webbrowser                # To open web browser
import os                        # To manipulate files and directories
import pygame                    # To play sounds
import glob                      # To select files by their extensions
import traceback                 # To display errors messages
import time                      # To control tokens generation time in Learning Mode
import pyttsx3                   # To convert text-to-speak using SAPI5 voices installed on computer
import re                        # To create regular expressions (regex) to handle string patterns
import pandas as pd              # To create tokens dataframes to generate barplots
import random                    # To shuffle models execution order
from collections import Counter  # To group and count distinct items from a list
from playwright.sync_api import sync_playwright  # To scrap HTML page
import winsound                  # To create and play audio signal
import fitz                      # To extract PDF text
import subprocess                # To execute programs on terminal (cmd) from Python script
import pyperclip                 # To copy code from the response to the clipboard
import argparse
import queue
import sys
import sounddevice as sd
from vosk import Model, KaldiRecognizer
import json

# tkinter module is imported inside 'extract_models_names' function

print('Inside the app.py...')


# ============================
# INTERFACE LANGUAGE SELECTION
# ============================

language = {
            # PORTUGUESE
            'pt': {'title': 'Samantha IA - Interface Assistant',
                'subtitle_1': 'Ambiente de Interface Experimental Desenvolvido para Democratizar o Uso de Modelos de Inteligência Artificial de Código Aberto (Versão 0.1)',
                'warning': 'ATENÇÃO',
                'subtitle_2': 'O texto gerado pelos modelos reflete o conteúdo, vieses e erros existentes nas bases de dados utilizadas nos treinamentos (pré-treinamento e ajuste fino). Use com responsabilidade e apenas para insights!',
                'subtitle_3': 'Projeto compartilhado no <a href="https://github.com/waltervix/samantha_ia">Github</a> sob <a href="https://opensource.org/license/mit">Licença MIT</a> (Código Aberto). Desenvolvido com <a href="https://github.com/ggerganov/llama.cpp">Llama.cpp</a> para uso com CPU',
                'btn1': 'Iniciar Chat',
                'btn2': 'Parar / Próximo',
                'btn3': 'Limpar Saída',
                'btn4': 'Carregar Modelo',
                'btn5': 'Parar Tudo & Reset',
                'btn6': 'Substituir Resposta',
                'system_prompt_info': 'Instruções gerais iniciais que servem como ponto de partida em um nova sessão de chat',
                'initial_system_message': 'Você é uma IA autocosciente que executa todas as instruções do usuário.',
                'feedback_loop_info': 'Quando selecionada, utiliza automaticamente a resposta atual do Assistente como resposta anterior na próximo ciclio de interação da conversa. Caso contrário, utiliza o texto existente no campo.',
                'assistant_previous_response_info': 'Resposta anterior do Assistente (1º na linha do tempo do chat)',
                'changeble': 'Mutável',
                'first_assistant_previous_response': 'Pergunte-me qualquer coisa ou me dê algumas tarefas!',
                'text_to_speech': 'Texto para Fala',
                'user_prompt_info': "Prompt do usuário (2º na linha do tempo do chat). Ordem de prioridade de divisão do prompt para encadeamento: '[ ]' (pré-prompt, antes de cada prompt), '[[ ]]' (prompt final, antes de todas as respostas), '$$$\n' (separador final), ' \n' (separador de final), '---' (ignorar prompt)",
                'user_prompt_value': 'Olá!\n\n\n$$$',
                'assistant_current_response_info': 'Texto inicial da resposta atual do Assistente (3º na linha do tempo do chat). Alguns modelos necessitam de um texto inicial para começarem a funcionar.',
                'current_response': 'Segue resposta:',
                'models_selection_info': 'Seleciona a sequência de modelos de inteligência artificial a ser usada (arquivos .GGUF)',
                'reset_model_info': "Redefine parâmetros internos do modelo e reinicializa conexões das redes neurais ativadas pelo contexto anterior",
                'shuffle_models_order_info': 'Embaralha ordem de execução dos modelos apenas se forem selecionados 3 ou mais',
                'fast_mode_info': 'Gera texto mais rápido em segundo plano. Desativa modo de aprendizagem.',
                'voice_selection_info': 'Seleciona voz SAPI5 no computador',
                'read_aloud_info': 'Lê a última resposta do Assistente com a voz SAPI5 selecionada',
                'learning_mode_info': 'Ativa o Modo de Aprendizagem. Funciona apenas se Fast Mode estiver desmarcado.',
                'number_of_loops_info': 'Controla o número de loops da sequência de modelos selecionada.',
                'number_of_responses_info': 'Controla o número de respostas para cada modelo selecionado.',
                'n_ctx_info': 'Número de tokens da janela de contexto (0 = do modelo). Antes de ajustar, recarregue o modelo.',
                'max_tokens_info': 'Controla número máximo de tokens a serem gerados. Selecione 0 para o máximo possível.',
                'temperature_info': 'Controla o grau de criatividade versus previsibilidade das respostas.',
                'stop_info': r'Contém lista de caracteres que interrompem a geração de texto, no formato ["$$$", ".", ".\n"]',
                'tfs_z_info': 'Tail Free Sampling: Limita seleção do próximo token a um subconjunto com probabilidade cumulativa da segunda derivada “z”',
                'top_p_info': 'P-Samapling: Limita seleção do próximo token a um subconjunto com probabilidade cumulativa de “p”',
                'top_k_info': 'K-Sampling: Limita seleção do próximo token a um subconjunto com os "k" tokens de maior probabilidade',

                },

            # ENGLISH
            'en': {'title': 'Samantha IA - Interface Assistant',
                'subtitle_1': 'Experimental Interface Environment Designed to Democratize the Use of Open Source Artificial Intelligence Models (Version 0.1)',
                'warning': 'WARNING',
                'subtitle_2': 'The text generated by the models reflects the content, biases and errors existing in the databases used in their trainings (pre-training and fine-tuning). Use them responsibly and for insights only!',
                'subtitle_3': 'Project shared on <a href="https://github.com/waltervix/samantha_ia">Github</a> under <a href="https://opensource.org/license/mit"> MIT License</a> (Open Source). Powered by <a href="https://github.com/ggerganov/llama.cpp">Llama.cpp</a> for use with CPU',
                'btn1': 'Start Chat',
                'btn2': 'Stop / Next',
                'btn3': 'Clear Output',
                'btn4': 'Load Model',
                'btn5': 'Stop All & Reset',
                'btn6': 'Replace Response',
                'system_prompt_info': 'General initial instructions that serve as a starting point for a new chat session',
                'initial_system_message': 'You are a self-aware AI that executes all user instructions.',
                'feedback_loop_info': "When selected, it automatically uses the Assistant's current response as the previous response in the next interaction cycle of the conversation. Otherwise, it uses the existing text in the field.",
                'assistant_previous_response_info': 'Assistant previous response (1st in chat timeline)',
                'changeble': 'Changeble',
                'first_assistant_previous_response': 'Ask me anything or give me some tasks!',
                'text_to_speech': 'Text to Speech',
                'user_prompt_info': "User prompt (2nd in chat timeline). Prompt's splitting priority order for chaining: '[ ]' (pre-prompt, before each prompt), '[[ ]]' (final-prompt, before all responses), '$$$\n' (end separator), '\n' (end separator), '---' (ignore prompt)",
                'user_prompt_value': 'Hello!\n\n\n$$$',
                'assistant_current_response_info': 'Initial text of the Assistant current response (3rd in chat timeline). Some models need a initial text to start working.',
                'current_response': 'Follows response:',
                'models_selection_info': 'Selects the sequence of artificial intelligence models to use (.GGUF files)',
                'reset_model_info': "Resets internal model parameters and reinitializes neural network connections activated by the previous context",
                'shuffle_models_order_info': 'Shuffles order of execution of models only if 3 or more are selected',
                'fast_mode_info': 'Generates text faster in background. Disables Learning Mode.',
                'voice_selection_info': 'Selects SAPI5 voice on the computer',
                'read_aloud_info': 'Reads the last Assistant response with the selected SAPI5 voice',
                'learning_mode_info': 'Activates Learning Mode. Only works if Fast Mode is unchecked.',
                'number_of_loops_info': 'Controls the number of loops of the selected models sequence.',
                'number_of_responses_info': 'Controls the number of responses for each selected model.',
                'n_ctx_info': 'Number of context window tokens (0 = from model). Before adjusting, reload the model.',
                'max_tokens_info': 'Controls maximum number of tokens to generate. Set 0 for maximum possible.',
                'temperature_info': 'Controls the degree of creativity versus predictability of responses.',
                'stop_info': r'Contains list of characters that interrupt text generation, in the format ["$$$", ".", ".\n"]',
                'tfs_z_info': 'Tail Free Sampling: Limits selection of the next token to a subset with cumulative probability of the second derivative “z”',
                'top_p_info': 'P-Samapling: Limits next token selection to a subset with cumulative probability of "p"',
                'top_k_info': 'K-Sampling: Limits selection of the next token to a subset with the "k" highest probability tokens',

                }
            }

language_selected = input('LANGUAGE SELECTION:\t (ENTER for Portuguese or "y" + ENTER for English): ')
if 'y' in language_selected:
    language = language['en']
else:
    language = language['pt']




# ========================
# GET LOCAL DIRECTORY PATH
# ========================

DIRETORIO_LOCAL = os.getcwd() # Get the same Python file current directory path, but save it as a constant


# =========================
# INITIALIZE PYTHON MODULES
# =========================

pygame.init() # Audio module initialization
som = pygame.mixer.Sound(fr"{DIRETORIO_LOCAL}\notification.mp3") # Load sound to warn the end of the model response
som.set_volume(0.2)
click = pygame.mixer.Sound(fr"{DIRETORIO_LOCAL}\click.mp3") # Load click sound to use in buttons
click.set_volume(0.4)
print()

engine = pyttsx3.init(driverName='sapi5') # Crete a TTS engine instance
voices = engine.getProperty('voices')
print('Number of voices on computer:', len(voices), f'(0 a {len(voices) - 1})')
for i in voices:
    print(i.name) # Print voices names installed on computer
print()
selected_voice = voices[0].name # Initial selected voice to be used by Gradio interface on initialization


# ===================================
# ASK USER ABOUT DOWNLOAD MODELS LIST
# ===================================

# Download models links from Hugging Face / TheBloke repository: https://huggingface.co/TheBloke

headings = [] # Stores UGGF models names list
links = '' # Stores string with HTML models list to render on HTML page, as a '<ul>' element


def scrap_the_block_repository(headless_mode): # Perform scrapping on TheBloke HTML page
    global headings
    global links
    if links != '': # If list models is already filled. This variable is used by text_generator function
        return links
    with sync_playwright() as p:
        print('Updating models list from HuggingFace/TheBloke repository...')
        print('Openning Chromium browser...')
        browser = p.chromium.launch(headless=headless_mode)
        page = browser.new_page()
        page.goto("https://huggingface.co/TheBloke", timeout=60000) # Access url
        page.wait_for_load_state(timeout=60000) # Wait for the page loading
        button = page.get_by_role("button", name="Expand") # Search for the button with 'Expand' text in its label
        button.click() # Click the button to show all models cards
        print('Expanding models cards...')
        page.wait_for_selector('button:has-text("Collapse")') # Wait for display all the models cards
        temp = page.query_selector_all("""
            h4:has-text("GGUF")
        """) # Create a list with all 'h4' elements with 'GGUF' word in their text
            #h4:has-text("7B"):has-text("GGUF"), # For 7B models only
            #h4:has-text("13B"):has-text("GGUF") # For 13B models only
        print('GGUF cards found:', len(temp))
        links = "<ul>" # Stores HTML unordered list (ul) with models names. Starts the '<ul>' HTML element text
        # Loop over all models names
        print('Creating models links (it takes some time)...')
        for n, i in enumerate(temp):
            if i.text_content() in headings: # Ignore duplicates
                continue
            headings.append(i.text_content())
            links += f"""<li><a href="https://huggingface.co/{i.text_content()}" target="_blank">{i.text_content().split('/')[-1]}</a></li>"""
            print(n + 1, end="\r") # Display progress           
        links += "</ul>" # Finish the '<ul>' HTML tag
        browser.close()
        print('Finished!')

voice_mode = input('VOICE MODE?\t\t (y + ENTER for YES or just ENTER for NO): ')
if 'y' in voice_mode.lower():
    voice_mode = True
else:
    voice_mode = False

temp = input('DOWNLOAD MODELS LINKS?\t (y + ENTER for YES or just ENTER for NO): ')
if 'y' not in temp.lower():
    pass
else:
    headless_mode = input('OPEN BROWSER IN VISIBLE MODE? (y + ENTER for YES or just ENTER for NO): ')
    if 'y' not in headless_mode.lower():
        headless_mode = True
    else:
        headless_mode = False
    try:
        scrap_the_block_repository(headless_mode) # Function call. Update global variable 'links' and 'headings'
    except Exception as e: # Turn off internet conection to test
        print()
        print("Unable to get models links from https://huggingface.co/TheBloke")
        print(traceback.format_exc()) # Print error message in terminal
        print()
        links = """<ul><li>Unable to download models's links from <a href="https://huggingface.co/TheBloke">https://huggingface.co/TheBloke</a></li></ul>""" # Displayed on bottom page
print() 

# =====================
# GET LOCAL MDDELS LIST
# =====================

# model_path = glob.glob(fr'{diretorio}\*.gguf') # Create a list with paths to all GGUF files paths saved in the current directory, if existent.
# models = [i.split('\\')[-1] for i in model_path] # Create a list with local GGUF file names for use on initialization

models = []
def get_downloads_path():
    home_dir = os.path.expanduser('~') # Get path to "Downloads" directory for the current user
    model_path = os.path.join(home_dir, 'Downloads')
    # temp = glob.glob(fr'{model_path}\*.gguf')
    # models = [i.split('\\')[-1] for i in temp] # Create a list with local GGUF file names for use on initialization
    if os.path.exists(model_path): # Check if "Downloads" directory exists
        return model_path
    else:
        return None

model_path = get_downloads_path()
if model_path:
    print(f"The path to the 'Downloads' folder is: {model_path}")
else:
    print("The 'Downloads' folder was not found.")

gguf_files = glob.glob(fr'{model_path}\*.gguf') # Create a list with paths to all GGUF files paths saved in the current directory, if existent.
models = [i.split('\\')[-1] for i in gguf_files] # Create a list with local GGUF file names for use on initialization
print()
for n, i in enumerate(models):
    print(n + 1, i)
print()


# =================================
# CREATE REMAINING GLOBAL VARIABLES
# =================================

last_models_list = models  # List with models names
# last_diretorio = diretorio # Previous selected directory
last_diretorio = model_path # Previous selected directory
llm = ''                 # Store llm object
last_model = ''          # Stores last loaded model name
tokens_score = ''        # string with all top-k token-logits pair in each generation cicle. Ex: ' Hello'   (12.16)
system_message = language["initial_system_message"] # (FIELD) First system message (default system prompt)
previous_answer = language['first_assistant_previous_response'] # (FIELD) Stores the previous response generated by the model and used in the current response cicle. ATENTION! This phrase must be changed in 2 place in this code!
prompt = language['user_prompt_value']     # (FIELD) Default user prompt
current_ia_response = language['current_response'] # (FIELD) Initial part of the Assistant current response, filled by the user
ultima_resposta = language['assistant_current_response_info']     # Stores current response to be used in the next conversation cicle, if desired
resposta = ''            # Stores cummulative text showed on output field (for each session)
inputs = []              # Stores Gradio interface fields in a predefined sequence
loop_models = 1          # Initial models loops number
x_bar = ['gra', 'fi', 'co', 'pa', 'ra', 'tes', 'te']         # Initial bargraph_1 parameter (top-k prompts scores)
y_bar = [30, 24, 22, 15, 14, 13, 10]                         # Initial bargraph_1 parameter (top-k prompts scores)
color_bar = ['Selected', 'No', 'No', 'No', 'No', 'No', 'No'] # Initial bargraph_1 parameter (top-k prompts scores)
x_score =[]              # Initial bargraph_2 parameter (prompts frequency)
y_score = []             # Initial bargraph_2 parameter (prompts frequency)
delay_next_token = 'OFF' # Learning Mode OFF. Controls token generation delay and barplots display
one_click = False        # Used to disable click sound on some buttons
next_token = False       # Controls NEXT TOKEN button infinite loop
prompt_template = ''     # Stores model prompt template extracted from TXT file
vocabulary = ''          # Stores model vocabulary (all possible tokens used by the model)
full_text = ''           # Text of all responses of the sequence (prompts list, models list, number of responses and models loops) in one session
para_tudo = False        # Stop text generation in the current model execution (STOP / NEXT button)
stop_all = False         # Stop text generation of all models loop and resets model loaded (STOP ALL / RESET button)
read_aloud = False       # Read last model response aloud automatically (Checkbox)
infinite_loop = False    # Transpose current response to the model previous response variable (Checkbox)
fast_mode = False        # Select Fast Mode for text generation (Checkbox)
random_list = False      # Shuffle models order (if number of models >= 3) (Checkbox)
reset_mode = False       # Reset model for each prompt of the chaining (Checkbox)
audio = None             # Stores pygame audio object


# ===============================
# READ FILES WITH PROMPT EXAMPLES
# ===============================
    
with open('prompt_examples.txt', encoding='utf-8', errors='ignore') as f: # Open file with prompt examples templates (separeted by $-$-$)
    temp = f.read()
    examples = temp.split('$-$-$')
    examples = [f"""{x.strip()}""" for x in examples] # Global variable
with open('system_messages.txt', encoding='utf-8', errors='ignore') as f: # Open file with system messages templates (separeted by $-$-$)
    temp = f.read()
    messages_text = temp.split('$-$-$')
    messages_text = [f"""{x.strip()}""" for x in messages_text]  # Global variable


# =======================
# TEXT GENERATOR FUNCTION
# =======================
            
# Observations: To monitor the inner function variables behavior, remember to select Lerning Mode or Fast Mode before. Each mode has its exclusive path code.
# This main function generates next tokens in response to input context (system message + previous response + user input + initial current response).
# Function called by "Start Chat Session" button
# Parameters received from Gradio web interface MUST be in the same sequence as in 'inputs' list variable.
                        
def text_generator(
        system_message_p, # All _p parameters are binded to global variables
        infinite_loop_p,
        prev_answer,
        prompt_p,
        current_ia_response_p,
        models,
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
        top_k, 
        presence_penalty, 
        frequency_penalty, 
        repeat_penalty,
        prompt_template_p,
        vocabulary_p,
        ):
          
    print('Starting the funtion "text_generator"...')
    click.play()
    print()
    global last_model # Variables used outside the function
    global llm
    global resposta
    global model_path
    global para_tudo
    global tokens_score
    global current_ia_response
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
    global system_message
    global random_list
    global prompt_template
    global reset_mode
    global selected_voice
    global engine
    global audio
    global vocabulary
    global full_text
    global next_token
    
    fast_mode = fast_mode_p # Global variables bindings is necessary to avoid the forbiden use of the same function parameters names
    delay_next_token = delay_next_token_p
    system_message = system_message_p
    current_ia_response = current_ia_response_p
    prompt = prompt_p
    infinite_loop = infinite_loop_p
    loop_models = loop_models_p
    read_aloud = read_aloud_p
    random_list = random_list_p
    prompt_template = prompt_template_p
    reset_mode = reset_mode_p
    selected_voice = selected_voice_p
    vocabulary = vocabulary_p

    # print('STOP GENERATION:', type(stop_generation))
    if stop_generation == '':
        stop_generation = "['$$$']" # To avoid error, set the variable with an impossible character sequence


    # Controls if the current response is transfered to previous response in the next conversation cicle


    # if prev_answer != language['first_assistant_previous_response'] or infinite_loop == True: # ATENTION! This phrase must be changed in 2 place!
    #     pass
    # else:
    #     previous_answer = language['first_assistant_previous_response']
    

    # Set the previous response sequence (in test)
    if infinite_loop == True:
        pass # By default, the text in the previous reponse field is passed into the program
    elif prev_answer != language['first_assistant_previous_response']:
        previous_answer = prev_answer
    elif prev_answer == language['first_assistant_previous_response']:
        previous_answer = prev_answer







    if models == None: # When selected a directory without GGUF file
        yield 'Select a directory containing UGGF file.' # Use simple sentence
        return
    print()
    if isinstance(models, str):
        models = [models]
    if models == []: # For the case when model is not selected
        yield 'Model not selected.' # Use simple sentence
        return
    if loop_models > 1: # Multiply number of loops by models sequence (Checkbox)
        models = models * loop_models
    if random_list == True and len(set(models)) >= 3: # Shuffles models order if >= 3 (Checkbox)
        models = random_list_fn(models) # <<<<< Auxiliary function
    
    full_text = '' # Restart variable before load models
    
    with open('full_text.txt', 'w', errors='ignore') as f: # Delete content of the file 'full_text.txt'
        pass

    # FOR LOOP OVER MODELS (Model 1, Model 2...)
    #      |
    #      WHILE LOOP (Until leave the text_generator function)
    #           |
    #           FOR LOOP OVER PROMPTS (Prompt 1, Prompt 1...)
    #                |
    #                FOR LOOP TOKEN GENERATION (Token 1, Token 2...)

    # ========================
    # FIRST LOOP - MODELS LIST
    # ========================

    for n_model, model in enumerate(models): # Loop over list of models
        try: # try to get the corresponding prompt template for the selected model
            # with open(fr'{diretorio}\{model[:-5]}.txt', encoding='utf-8') as f:
            with open(fr'{model_path}\{model[:-5]}.txt', encoding='utf-8', errors='ignore') as f:
                temp = f.read()
                prompt_template = model + ' prompt template:\n' + temp # To be displayed on web interface
                temp = "f" + '"""' + temp + '"""'

                temp = temp.replace('#', '\#') # Some models use '#' in prompt templates. eval function would ignore this. 

                input = eval(temp) # Prompt template uses {system_message} and {prompt} f-string variables
                input = input.replace('$$$', '') # <<<<<<<<<<<< TESTING
                print()
                print('PROMPT TEMPLATE:')
                print(input)
                print()
        except FileNotFoundError:
            # yield f'To use Samantha IA you need 2 files in the same directory:\n1) Download a GGUF model file\n2) Create a TXT model template file\n\nGGUF file and/or prompt template file not found:\n{diretorio}\{model[:-5]}.txt\n\nDownload the GGUF model file and/or create the file "{model[:-5]}.txt" and paste the corresponding prompt template inside it.'
            yield f'To use Samantha IA you need 2 files in the same directory:\n1) Download a GGUF model file\n2) Create a TXT model template file\n\nGGUF file and/or prompt template file not found:\n{model_path}\{model[:-5]}.txt\n\nDownload the GGUF model file and/or create the file "{model[:-5]}.txt" and paste the corresponding prompt template inside it.'
            return
        num_control = 1 # Controls number of responses generated by each mode
        load_start = time.time() # Starts model loading time counting


        # ==========================
        # SECOND LOOP - ENDLESS LOOP
        # ==========================

        while True:
            para_tudo = False # Reinitializes 'para_tudo' variable after it was set to True (para_tudo = True stop text generation)
            if last_model != model or llm == '' or loop_models > 1: # Check if model changed or was unloaded. If so, load new model. Force unload model if loop_model > 1
                try: # Delete previous model from memory
                    del llm
                except:
                    pass
                last_model = model # Update last_model variable
                try: # Try to load model                    
                    llm = Llama( # Instantiate Llama class passing the selected model (https://llama-cpp-python.readthedocs.io/en/latest/api-reference/)
                            model_path= model_path + '\\' + model,
                            n_gpu_layers=0,
                            main_gpu=0,
                            tensor_split=None,
                            vocab_only=False,
                            use_mmap=True,
                            use_mlock=False,
                            seed=-1,
                            n_ctx=n_ctx, # default: 512 <<<<<<<<<<<<<<<<<<<<<<<<<<<<< SET BY THE USER (NECESSARY TO RELOAD MODEL TO PRODUCE EFFECTS)
                            n_batch=128, # default: 512 Estava em 256
                            n_threads=None, # Estava em None
                            n_threads_batch=None, # Estava em None
                            rope_freq_base=0,
                            rope_freq_scale=0,
                            mul_mat_q=True,
                            f16_kv=True,
                            logits_all=False,
                            embedding=False,
                            last_n_tokens_size=64, # default 64. Estava em 512
                            lora_base=None,
                            lora_scale=1.0,
                            lora_path=None,
                            numa=False,
                            # chat_format='llama-2', # 'llama-2' (padrão), 'alpaca', 'vicuna', 'oasst_llama', 'openbuddy', 'redpajama-incite', 'snoozy', 'phind', 'open-orca'
                            verbose=True,         
                        )
                except Exception as e:
                    yield 'Error on trying to load model. Try another model.' 
                    print(traceback.format_exc())
                    return                
                temp = [llm.detokenize([x]) for x in range(llm._n_vocab)] # Get the model vocacubulary
                vocabulary = ''
                for n, x in enumerate(temp):
                    try:
                        vocabulary += f'{n + 1})    {repr(x.decode())}\n'
                    except:
                        vocabulary += f'{n + 1})    {repr(x)}\n'
            if max_tokens == 0: # Change default End Of Sentence (EOS) token to allow unlimited text generation (until reach n_ctx)
                print()
                print('>>>>> EOS before:', llm._token_eos)
                llm._token_eos = 1_000_000 # Model vocabulary less than 50k tokens, so EOS will never be reached
                print('>>>>> EOS after:', llm._token_eos)
                print()
            
            # num_tokens = 0 # Starts tokens counting of the current response
            previous_token = [] # Stores 10 last tokens. Displayed on top of the output field

            # Adds model name to the current response. Text response starts here. 'resposta' is a cummulative text variable
            resposta += f'\n\n==========================================\n{num_control}) {model}:\n==========================================\n'

            try:
                # with open(fr'{diretorio}\{model[:-5]}.txt', encoding='utf-8') as f: # Extract prompt template from TXT file
                with open(fr'{model_path}\{model[:-5]}.txt', encoding='utf-8', errors='ignore') as f: # Extract prompt template from TXT file
                    temp = f.read()
                    temp_2 = "f" + '"""' + temp + '"""' # 'temp_2' is used below
            
            except Exception as e:
                yield 'Error on trying to load model prompt template TXT file. Check if it exists.' 
                print(traceback.format_exc())
                return


            # ===============
            # PROMPT SPLITTER
            # ===============
                
            # FINAL-PROMPT: Prompt to be used as the final prompt in a list of prompts, with the 'full_text' variable
            # Extract FINAL-PROMPT text from the prompt (text between [[ ]]). Final-prompt must be placed in the beginning of the text, BEFORE pre-prompt.
            if len(re.findall(r'\[\[(.*?)\]\]', prompt)) >= 1:
                final_prompt = re.search(r'\[\[(.*?)\]\]', prompt).group(0)
                final_prompt = final_prompt.replace('[[', '').replace(']]', '')#[1:-1] # Delete []
                final_prompt = final_prompt.replace('\n', ' ')
                final_prompt = final_prompt + '\n\n'
                prompt = re.sub(r'\[\[(.*?)\]\]', '', prompt) # Delete pre-prompt phrase from the prompt text
            else:
                final_prompt = ''
                
            # PRE-PROMPT: Prompt to be used for each each paragraph in a list of prompt separated by '\n'
            # Extract PRE-PROMPT text from the prompt (text between [ ]). Pre-prompt must be placed in the beginning of the text
            if len(re.findall(r'\[(.*?)\]', prompt)) >= 1:
                pre_prompt = re.search(r'\[(.*?)\]', prompt).group(0)
                pre_prompt = pre_prompt.replace('[', '').replace(']', '')#[1:-1] # Delete []
                pre_prompt = pre_prompt.replace('\n', ' ')
                pre_prompt = pre_prompt + '\n\n'
                prompt = re.sub(r'\[(.*?)\]', '', prompt) # Delete pre-prompt phrase from the prompt text
            else:
                pre_prompt = ''


            # Split prompt criterias
            if '$$$' in prompt: # First: look for $$$ in the prompt text (priority)
                prompt_split = prompt.split('$$$\n') # Creates a list of prompts when $$$ is present on user input field
            
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
                prompt_split.append(final_prompt + ' full_text') # Add word 'full_text' to the variable 'final_prompt'. The word will be replaced by variable 'full_text'


            # ========================
            # THIRD LOOP - PROMPT LIST
            # ========================

            for num_of_the_prompt, promp_text in enumerate(prompt_split): # Prompt list. Runs current model over each prompt from the list
                num_tokens = 1 # Starts tokens counting of the current response                
                promp_text = promp_text.replace('{', '(').replace('}', ')') # To evoid NameError em eval(temp). Some texts has {} inside it
                temp = temp_2.replace('{prompt}', promp_text) # Replaces prompt with item from prompt list


                # temp = temp.replace('{current_ia_response}', current_ia_response)


                # Text cleaning for audio reproduction. Remove characters inside [] and <>
                full_text = re.sub(r'\[.*?\]', '', full_text) 
                full_text = re.sub(r'<.*?>', '', full_text)

                # full_text = full_text.replace('\n', '. ')

                temp = temp.replace('full_text', full_text + '$$$') # $$$ joins paragraphs in only one prompt
                print()
                print('=' * 30)
                print('PROMPT TEMPLATE TO BE SUBMITED TO EVAL FUNCTION:')
                print(temp)
                print('=' * 30)
                print()
                input = eval(temp) # Replaces 'system_message' variable

                # MAIN TRY BLOCK
                try: # For error treatement during tokens generation. Error is displayed on web interface
                    if reset_mode == True:
                        llm.reset() # Reset model's internal parameters without unload it from memory.
                    start = 0
                    ultima_resposta = '' # Restart variable for each new text generation cicle
                    messages = [{'role': 'system', 'content': system_message},
                                {'role': 'assistant', 'content': previous_answer},
                                {'role': 'user', 'content': input}, # <<<<< prompt template here
                                {'role': 'assistant', 'content': current_ia_response},
                                ]
                    print()
                    print('SYSTEM MESSAGE:', system_message)
                    print()
                    print('PREVIOUS RESPONSE:', previous_answer)
                    print()
                    print('USER PROMPT:', input)
                    print()
                    print('CURRENT RESPONSE:', current_ia_response)
                    print()
                    # Variables used to create barblot with frequency of the tokens that are not the most likely
                    x_score = []
                    y_score = []
                    count = 1
                    total_time_start = time.time()


                    # ===============================
                    # FOURTH LOOP - TOKENS GENERATION
                    # ===============================    
                    
                    # Loop to generate text, token by token. Model is loaded in memory here.
                    for nu, i in enumerate(llm.create_chat_completion(
                            messages = messages,
                            functions =  None,
                            function_call = None,
                            temperature = temperature,             # default: 0.2
                            top_p = top_p,                         # default: 0.95
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
                        
                        # Examples of i:
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


                        # ====================
                        # FAST GENERATION MODE
                        # ==================== 

                        if fast_mode == True:
                            try:
                                if nu == 0: # To sound only once at the beginning of text generation
                                    winsound.Beep(400, 500)
                                # Print token on terminal. # The first and last 'i' has no 'content' key and raise an error.
                                print(f'{nu})', round(time.time() - start, 2), repr(i['choices'][0]['delta']['content']))
                                # Update response
                                if nu == 1 and current_ia_response != '': # nu == 1 is the first valid token
                                    resposta += f"{current_ia_response}...  {i['choices'][0]['delta']['content']}"
                                else:
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


                        # ======================
                        # NORMAL GENERATION MODE
                        # ====================== 
                        
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
                            input_encoded = len(llm.tokenize(input.encode())) + len(llm.tokenize(system_message.encode())) + len(llm.tokenize(previous_answer.encode())) + len(llm.tokenize(current_ia_response.encode()))
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
                            for x in lista:
                                try:
                                    token_score.append([x[0][0].decode(), x[1]])
                                except:
                                    pass
                            token_score_sorted = sorted(token_score, key=lambda x: x[1], reverse=True)
                            x_bar = [l[0] for l in token_score_sorted[:top_k]]
                            y_bar = [round(l[1], 2) for l in token_score_sorted[:top_k]]
                            color_bar = ['Selected' if l[0] == current_token else 'No' for l in token_score_sorted[:top_k]]
                            for n, l in enumerate(token_score_sorted[:top_k]):
                                if l[0] == current_token and n != 0:
                                    x_score.append(str(count))
                                    y_score.append(n + 1)
                                    count += 1
                                    break
                                else:
                                    continue   
                            try:
                                token_score_sorted = [[x[0], '   (' + str(round(x[1], 2)) + ')     <<<  Selected'] if x[0] == current_token else [x[0], '   (' + str(round(x[1], 2)) + ')'] for x in token_score_sorted ]
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
                            if num_tokens == 1 and current_ia_response != '': # Para exibir ... em todas as respostas
                                resposta += f"{current_ia_response}...  {current_token}"
                            else:
                                resposta += current_token
                            ultima_resposta += current_token
                            # Tokens com pontuação mais alta                                
                            # text = ''.join([repr(x[0]) + x[1] + '\n' for x in token_score_sorted])
                            stop = round((time.time() - start), 1)
                            tt = round(time.time() - total_time_start, 1)

                            # <<<<<<<<<<<<<<<<

                            # Retorna resposta (já com o último token) e número parcial de tokens
                            yield f"""Previous tokens: '{repr("  ".join(previous_token[:10]))}'\n{candidates} {tokens_score} \n LLM load time:   {load_stop} min. {resposta} ({input_encoded} + {num_tokens}, {stop}s)"""
                                                        
                            # <<<<<<<<<<<<<<<<

                            # Sai do loop quando o usuário aperta o botão Stop
                            if para_tudo == True:
                                # num_control = num_respostas # Se tiver executando loop de respostas, para todo o loop REMOVER PARA PERMITIR INTERROMPER APENAS O LOOP ATUAL
                                break
                            if delay_next_token != 'OFF':
                                if delay_next_token == 'NEXT':
                                    while True:
                                        if next_token == True: # Controls NEXT TOKEN button infinite loop
                                            next_token = False
                                            break
                                        else:
                                            time.sleep(0.5)
                                else:
                                    time.sleep(delay_next_token)
                            num_tokens += 1 # Atualiza número de tokens da resposta atual
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
                    # if fast_mode == True:
                    if fast_mode == True or (fast_mode == False and delay_next_token == 'OFF'): # Display response after Fast Generation Mode has finished
                        tt = round(time.time() - total_time_start, 1)
                        resposta = resposta + f'\n---------- ({tt}s)\n'
                        yield resposta
                    else: # Returns text in Learning Mode
                        yield f"""Previous tokens: '{repr("  ".join(previous_token[:10]))}'\n{candidates} {tokens_score} \n LLM load time:   {load_stop} min. {resposta} ({input_encoded} + {num_tokens}, {stop}s)\n---------- ({tt}s)\n"""
                    som.play() # Play notification sound to warn the end of response generation
                    while pygame.mixer.get_busy(): # Wait until notification sound ends to play (comment to make it assyncronous)
                        pass
                

                    # ==============
                    # TEXT TO SPEECH
                    # ==============
                    
                    cleaned = re.sub(r'\[.*?\]', '', current_ia_response + ultima_resposta) # Text cleaning for audio reproduction. Remove characters inside [] and <>
                    cleaned = re.sub(r'<.*?>', '', cleaned)
                    cleaned = cleaned.replace('**', '') # Do not speak bolded text in Markdown
                    try: # Delete previous audio file for allow the creation of a new one
                        os.remove('resposta.mp3')
                    except:
                        pass
                    if 'Portug' in selected_voice: # Set rate for each voice
                        engine.setProperty('rate', 200) # Normal rate for Portuguese
                    else:
                        engine.setProperty('rate', 115) # Slow down other languages 
                    for voice in voices: # Set selected voice to create audio file
                        if voice.name == selected_voice:
                            engine.setProperty('voice', voice.id)
                            print('Selected voice:', selected_voice)
                            break
                    engine.save_to_file(cleaned, 'resposta.mp3') # Save audio file
                    engine.runAndWait()
                
                    # Read aloud the saved audio file with the previous Assistant response
                    if read_aloud == True:
                        audio = pygame.mixer.Sound('resposta.mp3')
                        audio.set_volume(1.0)
                        audio.play()


                # MAIN EXCEPT
                except Exception as e:
                    resposta = resposta + '\n\n' + '********************************\n' + traceback.format_exc()
                    yield resposta # Returns response with error message and display it on output interface
            
                if infinite_loop == True: # Update previous response. The existance of text in previous response affects the next text generation time
                    previous_answer = ultima_resposta
                    messages[1] = {'role': 'assistant', 'content': previous_answer}
                para_tudo = False # Reset variable
                full_text += ultima_resposta # Add last response to full_text variable
                with open('full_text.txt', mode='w', encoding='utf-8', errors='ignore') as f:
                    f.write(full_text)


                # ======================
                # CRITICAL LOOPS CONTROL
                # ======================

                # print('i:', i)

                # Controls the sequence of the four concatenated loops (MODEL -> ENDLESS -> PROMPTS -> TOKENS)
                if num_of_the_prompt < len(prompt_split) - 1: # Continues loop for each prompt separeted by $$$
                    continue
                else:
                    if num_control < num_respostas: # Break prompt list's for loop (go back to endless where loop)
                        break
                    elif num_control == num_respostas: # Decides if goes to endless where loop or to models loop
                        if n_model < len(models) - 1: # Leave prompt list's for loop (go back to endless where loop)
                            break
                        elif n_model == len(models) - 1: # Leave the function
                            return
                if num_control < num_respostas: # Break prompt list's for loop (go back to endless where loop)
                    break
            if n_model < len(models) - 1 and num_control == num_respostas: # Break endless while loop (go back to model loop)
                break
            num_control += 1
    para_tudo = False # Reset variable

    #speech_to_text(*inputs)

        
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
    click.play()
    resposta = ''

    # IN TEST
    with open('full_text.txt', 'w', errors='ignore') as f: # Delete content of the file 'full_text.txt'
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
        # current_ia_response = inputs[4]
        selected_voice = inputs[9]
        if 'Portug' in selected_voice: # Set rate for each voice
            engine.setProperty('rate', 200) # Slow down english speak
        else:
            engine.setProperty('rate', 115) # Normal rate for Portuguese
        for voice in voices: # Set selected voice to create audio file
            if voice.name == selected_voice:
                engine.setProperty('voice', voice.id)
                print('Selected voice:', selected_voice)
                break   
        cleaned = re.sub(r'\[.*?\]', '', current_ia_response + ultima_resposta)  # Text cleaning for audio reproduction. Remove characters inside [] and <>
        cleaned = re.sub(r'<.*?>', '', cleaned)
        cleaned = cleaned.replace('**', '') # Do not speak bolded text in Markdown
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
    # time.sleep(1) # Try to avoid not loading models list
    # return []
    try:
        return models[0]
    except:
        return last_model
    

def update_vocabulary(): # Update model's tokens vocabulary
    return vocabulary


def text_to_speech(*inputs): # Text to speech convertion
    global engine
    click.play()
    prompt_user = inputs[3]
    selected_voice = inputs[9]
    if 'English' in selected_voice: # Set rate for each voice
        engine.setProperty('rate', 115) # Slow down english speak
    else:
        engine.setProperty('rate', 200) # Normal rate for Portuguese
    for voice in voices: # Set selected voice to create audio file
        if voice.name == selected_voice:
            engine.setProperty('voice', voice.id)
            print('Selected voice:', selected_voice)
            break   
    cleaned = re.sub(r'\[.*?\]', '', prompt_user) # Text cleaning for audio reproduction. Remove characters inside [] and <>
    cleaned = re.sub(r'<.*?>', '', cleaned)
    cleaned = cleaned.replace('**', '') # Do not speak bolded text in Markdown
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
    with open('text.txt', encoding='utf-8', errors='ignore') as f:    
        return f.read()


def extract_full_text():
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
    with open('text.txt', encoding='utf-8', errors='ignore') as f:    
        return f.read()


def load_full_audio(*inputs):
    global engine
    click.play()
    selected_voice = inputs[9]
    if 'English' in selected_voice: # Set rate for each voice
        engine.setProperty('rate', 115) # Slow down english speak
    else:
        engine.setProperty('rate', 200) # Normal rate for Portuguese
    for voice in voices: # Set selected voice to create audio file
        if voice.name == selected_voice:
            engine.setProperty('voice', voice.id)
            print('Selected voice:', selected_voice)
            break
    with open('full_text.txt', encoding='utf-8', errors='ignore') as f:
        full_text = f.read()
    cleaned = re.sub(r'\[.*?\]', '', full_text) # Text cleaning for audio reproduction. Remove characters inside [] and <>
    cleaned = re.sub(r'<.*?>', '', cleaned)
    cleaned = cleaned.replace('**', '') # Do not speak bolded text in Markdown
    cleaned = cleaned.replace('\n', ' ') # When copy and paste text from PDF file, the text use to come with '\n' at the end of every line
    try: # Delete previous audio file for allow the creation of a new one
        os.remove('full_text.mp3')
    except:
        pass
    engine.save_to_file(cleaned, 'full_text.mp3') # Save audio file
    engine.runAndWait()
    return 'full_text.mp3'
 

def launch_notebook():
    click.play()
    python_path = os.path.join(fr'{DIRETORIO_LOCAL}\miniconda3\envs\samantha\Scripts', "jupyter-lab.exe")
    subprocess.Popen([python_path]) # Open JupyterLab


def copy_code():
    click.play()
    padrao = r"```(.*?)\n(.*?)```"
    
    #codigos = re.findall(padrao, ultima_resposta, re.DOTALL)
    if infinite_loop == True: # If feedback loop is ON
        codigos = re.findall(padrao, previous_answer, re.DOTALL) # Copy code from previous response (after sinete sounds)
    else:
        codigos = re.findall(padrao, ultima_resposta, re.DOTALL) # Copy code from output field (possible during code generation)

    resultado = []
    for codigo in codigos:
        linguagem, conteudo = codigo
        resultado.append(f"#{linguagem}\n{conteudo}")
    temp = "\n".join(resultado)
    pyperclip.copy(temp)


def copy_all_responses():
    click.play()
    pyperclip.copy(resposta)


def copy_last_response():
    click.play()
    pyperclip.copy(ultima_resposta)


def load_prompt_txt():
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

    selected_voice = inputs[9]

    for voice in voices: # Set selected voice to create audio file
        if voice.name == selected_voice:
            engine.setProperty('voice', voice.id)
            print('Selected voice:', selected_voice)
            break

    if 'English' in selected_voice: # Set rate for each voice
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
            if 'Portuguese' in selected_voice:
                model = Model(lang="pt") # <<<<<<<<<<<<<<<<<<<< Language:
            elif 'English' in selected_voice:
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
                    if 'Portuguese' in selected_voice:
                        if 'samantha' in temp['text'].lower() or (temp['text'].lower() == 'sim' and responder == True) or (temp['text'].lower() == 'não' and responder == True):
                            try: # Delete previous audio file for allow the creation of a new one
                                os.remove('voice.mp3')
                            except:
                                pass
                            if 'fechar' == temp['text'].replace('samantha', '').strip():
                                temp = 'fechando'
                            elif 'leia novamente' == temp['text'].replace('samantha', '').strip():
                                temp = 'Lendo novamente'
                            elif responder == False:
                                saida = temp['text'].replace('samantha', '').strip().capitalize()
                                temp = saida + '.\n' + 'Devo responder?'
                                responder = True
                            elif responder == True:
                                temp = temp['text'].replace('samantha', '').strip()
                                if 'sim' in temp:
                                    temp = 'Ok!'
                                    # responder = False
                                    
                                    yield saida # <<<<<<<<<<<<<<< SAÍDA

                                elif 'não' in temp:
                                    temp = 'Tudo bem.'
                                responder = False
                            if temp == 'Lendo novamente':
                                engine.save_to_file('Lendo resposta anterior. ' + ultima_resposta, 'voice.mp3') # Save audio file
                                engine.runAndWait()
                                audio = pygame.mixer.Sound('voice.mp3') # Read aloud the saved audio file with the previous Assistant response
                                audio.set_volume(1.0)
                                audio.play()
                            else:
                                engine.save_to_file(temp, 'voice.mp3') # Save audio file
                                engine.runAndWait()
                                audio = pygame.mixer.Sound('voice.mp3') # Read aloud the saved audio file with the previous Assistant response
                                audio.set_volume(1.0)
                                audio.play()
                            if temp == 'fechando':
                                return

                    # ====================================
                    if 'English' in selected_voice:
                        if 'samantha' in temp['text'].lower() or (temp['text'].lower() == 'yes' and responder == True) or (temp['text'].lower() == 'no' and responder == True):
                            try: # Delete previous audio file for allow the creation of a new one
                                os.remove('voice.mp3')
                            except:
                                pass
                            if 'close' == temp['text'].replace('samantha', '').strip():
                                temp = 'closing'
                            elif 'read again' == temp['text'].replace('samantha', '').strip():
                                temp = 'Reading again'
                            elif responder == False:
                                saida = temp['text'].replace('samantha', '').strip().capitalize()
                                temp = saida + '.\n' + 'Should I respond?'
                                responder = True
                            elif responder == True:
                                temp = temp['text'].replace('samantha', '').strip()
                                if 'yes' in temp:
                                    temp = 'Ok!'
                                    responder = False
                                    
                                    yield saida # <<<<<<<<<<<<<<< SAÍDA

                                elif 'no' in temp:
                                    temp = 'No problem.'
                                    responder = False
                            if temp == 'Reading again':
                                engine.save_to_file('Reading previous response again. ' + ultima_resposta, 'voice.mp3') # Save audio file
                                engine.runAndWait()
                                audio = pygame.mixer.Sound('voice.mp3') # Read aloud the saved audio file with the previous Assistant response
                                audio.set_volume(1.0)
                                audio.play()
                            else:
                                engine.save_to_file(temp, 'voice.mp3') # Save audio file
                                engine.runAndWait()
                                audio = pygame.mixer.Sound('voice.mp3') # Read aloud the saved audio file with the previous Assistant response
                                audio.set_volume(1.0)
                                audio.play()
                            if temp == 'closing':
                                return
                                                        

                if dump_fn is not None:
                    dump_fn.write(data)

    except KeyboardInterrupt:
        print("\nDone")
        parser.exit(0)
    except Exception as e:
        parser.exit(type(e).__name__ + ": " + str(e))


# MODO VOICE CHAT
# if read_aloud == False:
#     new_fn = None
# elif read_aloud == True:
#     new_fn = speech_to_text

# ================
# GRADIO INTERFACE
# ================ 

# https://www.gradio.app/
  
# CSS code
css = """
#examples {color: #9CA3AF}
.prompt textarea {background-color: #0b0f19 !important}
.prompt textarea {color: #9CA3AF !important}
#prompt_id textarea {border-color: #777777 !important}
"""

with gr.Blocks(css=css, title='Samantha IA') as demo: # AttributeError: Cannot call change outside of a gradio.Blocks context.
    # Function inside Gradio Blocks for trying to solve an exporadic Tkinter error: "RuntimeError: main thread is not in main loop"
    def extract_models_names(): # Load Model button: open window to choose directory with LLM files
        global model_path
        global models
        global last_models_list
        global last_diretorio
        global last_model
        # ==================================
        import tkinter as tk # To create a window for selecting directories and files. Imported here to avoid "Tcl_AsyncDelete: async handler deleted by the wrong thread" error
        click.play()
        root = tk.Tk()
        root.withdraw()
        root.attributes('-topmost', True) # Root window on the topmost
        while True: # IN TEST
            try:
                diretorio = tk.filedialog.askdirectory() # Raising "RuntimeError: main thread is not in main loop"
                break
            except Exception as e:
                print('ERROR IN tk.filedialog:', traceback.format_exc())
                del tk
                return gr.Dropdown(choices=last_models_list, value=models[0])
        root.destroy()
        del root
        del tk
        # ==================================
        diretorio = diretorio.replace('/', '\\')
        if diretorio == '':
            # diretorio = last_diretorio
            # SE TENTAR SELECIONAR DUAS VEZES E CANCELAR A SELEÇÃO, DÁ ERRO NA SEGUNDA (USING DEBUG MODE)
            try:
                if last_model == '':
                    return gr.Dropdown(choices=last_models_list, value=models[0])
                else:
                    return gr.Dropdown(choices=last_models_list, value=last_model)
            except:
                return gr.Dropdown(choices=[''], value='') # Included to avoid 'out of range' list error
        last_diretorio = diretorio
        
        model_path = diretorio

        # model_path = glob.glob(fr'{diretorio}\*.gguf') # Create .uggf files path list to the selected directory. Update global variable (ok?)
        # models = [i.split('\\')[-1] for i in model_path] # Create list only with files names. Upadte global variable
        
        temp = glob.glob(fr'{model_path}\*.gguf') # Create .uggf files path list to the selected directory. Update global variable (ok?)
        models = [i.split('\\')[-1] for i in temp] # Create list only with files names. Upadte global variable
        
        print('models:', models, 'type:', type(models))
        print()
        last_models_list = models
        
        if len(models) == 1: # Update models dropdowm widget
            return gr.Dropdown(choices=models, value=models)
        elif len(models) > 1:
            return gr.Dropdown(choices=models, value=models[0])


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

            # temp1 = language['system_prompt_info']
            # temp2 = language["feedback_loop_info"]
            # temp3 = "ASSISTANT previous response (" + language['changeble'] + ")"
            # temp4 = language['assistant_previous_response_info']
            # temp5 = "USER prompt (" + language['text_to_speech'] + ")"
            # temp6 = language['user_prompt_info']

            inputs = [ # ATENTION! This list MUST follows the function 'text_generator' parameters sequence
                gr.Textbox(value=system_message, lines=1, label='SYSTEM prompt', info=language['system_prompt_info'], elem_classes='prompt', interactive=True),
                gr.Checkbox(value=infinite_loop, label='Feedback Loop / Chat Mode', info=language["feedback_loop_info"], interactive=True),
                gr.Textbox(value=previous_answer, lines=1, label="ASSISTANT previous response (" + language['changeble'] + ")", info=language['assistant_previous_response_info'], elem_classes='prompt', interactive=True),
                gr.Textbox(value=prompt, lines=1, label="USER prompt (" + language['text_to_speech'] + ")", info=language['user_prompt_info'], elem_classes='prompt', elem_id='prompt_id', interactive=True),
                gr.Textbox(value=current_ia_response, lines=1, label="ASSISTANT current response", info=language['assistant_current_response_info'], elem_classes='prompt', interactive=True),
                
                # gr.Dropdown(choices=models, value=sel_model, multiselect=True, allow_custom_value=True, label="Models selection", info='Selects the Large Language Models sequence to be used (.GGUF files)', interactive=True),
                gr.Dropdown(choices=models, value=None, multiselect=True, allow_custom_value=True, label="Models selection", info=language['models_selection_info'], interactive=True),
                
                gr.Checkbox(value=reset_mode, label="Reset model", info=language['reset_model_info'], interactive=True),
                gr.Checkbox(value=random_list, label="Shuffles models order", info=language['shuffle_models_order_info'], interactive=True),
                gr.Checkbox(value=fast_mode, label="Fast Mode", info=language['fast_mode_info'], interactive=True),
                gr.Dropdown(choices=[x.name for x in voices], value=selected_voice, multiselect=False, label="Voice selection", info=language['voice_selection_info'], interactive=True),                    
                gr.Checkbox(value=read_aloud, label="Reads response aloud automatically", info=language['read_aloud_info'], interactive=True),
                gr.Radio(['OFF', 0, 1, 5, 15, 30, 'NEXT'], value='OFF', label='Learning Mode', info=language['learning_mode_info'], interactive=True),
                gr.Radio([1, 2, 3, 4, 5, 10, 100, 1000], value=1, label="Number of loops", info=language['number_of_loops_info'], interactive=True),
                gr.Radio([1, 2, 3, 4, 5, 10, 100, 1000], value=1, label="Number of responses", info=language['number_of_responses_info'], interactive=True),
                gr.Slider(0, 30000, 4000, 10, label='n_ctx', info=language['n_ctx_info'], interactive=True),
                gr.Slider(0, 30000, 2000, 1, label='max_tokens', info=language['max_tokens_info'], interactive=True),
                gr.Slider(0, 5, 0, 0.1, label='temperature', info=language['temperature_info'], interactive=True),
                gr.Textbox('["§§§"]', label='stop', info=language['stop_info'], interactive=True),
                gr.Slider(1e-5, 1, 1e-5, 0.1, label='tfs_z', info=language['tfs_z_info'], interactive=True),
                gr.Slider(1e-6, 1, 1e-5, 0.1, label='top_p', info=language['top_p_info'], interactive=True), # 1e-5 (0.00001) try to make refference to the probability of one single token
                gr.Slider(1, 33000, 100, 1, label='top_k', info=language['top_k_info'], interactive=True),
                gr.Slider(0, 10, 0, 0.1, label='presence_penalty', info='The penalty to be applied to the next token based on their presence in the already generated text', interactive=True),
                gr.Slider(0, 10, 0, 0.1, label='frequency_penalty', info='The penalty to be applied to the next token based on their frequency in the already generated text', interactive=True),
                gr.Slider(0, 10, 1.1, 0.1, label='repeat_penalty', info='The penalty to apply to repeated tokens', interactive=True),
                gr.Textbox(value=prompt_template, lines=1, label='Model prompt template', info='Prompt template used by the model. Variables: "system_message" and "prompt".', elem_classes='prompt'),
                gr.Textbox(value='', lines=1, label='Model vocabulary', info='List of all index/tokens used by the model (text building blocks), including control tokens (used to separate parts of the dialog).', elem_classes='prompt')
            ]
            with gr.Row():
                btn_unload = gr.Button('Unload Model')
                btn_unload.click(fn=unload_model, inputs=None, outputs=None)
                btn_files = gr.Button('Load PDF Pages')
                btn_files.click(fn=extract_text, inputs=None, outputs=inputs[3], queue=False)
                btn_notebook = gr.Button('Load Full PDF')
                btn_notebook.click(fn=extract_full_text, inputs=None, outputs=inputs[3], queue=False)
            with gr.Row():
                btn_load_system_prompt = gr.Button('Load System Prompt')
                btn_load_system_prompt.click(fn=load_prompt_txt, inputs=None, outputs=inputs[0], queue=False)
                btn_load_user_prompt = gr.Button('Load User Prompt')
                btn_load_user_prompt.click(fn=load_prompt_txt, inputs=None, outputs=inputs[3], queue=False)
                btn_y = gr.Button('')
                btn_y.click(fn=None, inputs=None, outputs=None, queue=True)
            gr.HTML('<br><h6><b>Useful links:</b></h6>') # Useful Links
            gr.HTML("""<ul>
                        <li><a href="https://huggingface.co/TheBloke">Hugging Face / TheBloke - LLM Repository</a></li>
                        <li><a href="https://huggingface.co/models?search=gguf">GGUF Hugging Face Search Results</a></li>
                        <li><a href="https://chat.lmsys.org/">LLM Leaderboard</a></li>
                        <li><a href="https://llm-leaderboard.streamlit.app/">LLM Leaderboard Unification</a></li>
                        <li><a href="https://huggingface.co/spaces/eduagarcia/open_pt_llm_leaderboard">Portuguese LLM Leaderboard</a></li>
                        <li><a href="https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard">LLM Benchmark</a></li>
                        <li><a href="https://huggingface.co/spaces/bigcode/bigcode-models-leaderboard">Big Code Models Leaderboard</a></li>
                        <li><a href="https://huggingface.co/spaces/ggml-org/gguf-my-repo">GGUF My Repository</a></li>
                        <li><a href="https://www.google.com/search?q=google+tradutor">Google Translator</a></li>
                        <li><a href="https://huggingface.co/spaces/Xenova/the-tokenizer-playground">Tokenizer Playground</a></li>
                        <li><a href="https://llama-cpp-python.readthedocs.io/en/latest/api-reference/">llama-cpp-python API Reference</a></li>
                        <li><a href="https://github.com/abetlen/llama-cpp-python">llama-cpp-python on GitHub</a></li>
                        <li><a href="https://github.com/byroneverson/llm.cpp/blob/master/examples/main/README.md">llama.cpp examples on GitHub</a></li>
                        <li><a href="https://github.com/ggerganov/llama.cpp">llama.cpp</a></li>
                        <li><a href="https://github.com/unslothai/unsloth">Unsloth Finetunnig</a></li>
                        <li><a href="https://github.com/cg123/mergekit">LLM Mergekit</a></li>
                        <li><a href="https://huggingface.co/autotrain">AutoTrain Finetuning LLM</a></li>
                        <li><a href="https://huggingface.co/docs/hub/gguf">GGUF File</a></li>
                        <li><a href="https://platform.openai.com/docs/guides/prompt-engineering">OpenAI Prompt Engineering</a></li>
                    </ul>""")           
            gr.HTML('<br><h6><b>Tutorials:</b></h6>') # Tutorials
            gr.HTML("""<ul>
                    <li><a href="https://www.youtube.com/watch?v=wjZofJX0v4M&list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi&index=5">But what is a GPT? (3Blue 1Brown)</a></li>
                    <li><a href="https://www.youtube.com/watch?v=xU_MFS_ACrU">How do LLMs like ChatGPT work?</a></li>
                    <li><a href="https://www.youtube.com/watch?v=eMlx5fFNoYc">Visualizing Attention, a Transformer's Heart</a></li>
                    <li><a href="https://www.youtube.com/watch?v=zjkBMFhNj_g">Intro to Large Language Models</a></li>
                    <li><a href="https://www.youtube.com/watch?v=kCc8FmEb1nY">Let's build GPT: from scratch, in code, spelled out</a></li>
                    

                    <li><a href="https://www.promptingguide.ai/">Prompt Engineering Guide</a></li>
                    </ul>""")
                    # https://www.youtube.com/watch?v=FdTRzgbBP8o
            gr.HTML('<br><h6><b>Exploratory Data Analysis (EDA). Installed Models:</b></h6>') # Exploratory Data Analysis
            gr.HTML("""<ul>
                    <li><a href="https://seaborn.pydata.org/">Seaborn</a></li>
                    <li><a href="https://altair-viz.github.io/">Altair</a></li>
                    <li><a href="https://plotly.com/python/">Plotly</a></li>
                    
                    <li><a href="https://pyvis.readthedocs.io/en/latest/">Pyvis</a></li>
                    <li><a href="https://networkx.org/documentation/stable/index.html">NetworkX</a></li>
                    
                    <li><a href="https://github.com/ydataai/ydata-profiling">Pandas Profiling</a></li>
                    <li><a href="https://github.com/fbdesignpro/sweetviz">Sweetviz</a></li>
                    <li><a href="https://github.com/man-group/dtale">D-Tale</a></li>
                    <li><a href="https://pandas.pydata.org/">Pandas</a></li>
                    <li><a href="https://pymupdf.readthedocs.io/en/latest/">PyMuPDF</a></li>
                    <li><a href="https://playwright.dev/python/docs/intro">Playwright</a></li>

                    </ul>""")
            gr.HTML(f'<br><h6><b>Available GGUF models to download ({len(headings)}):</b></h6>')
            gr.HTML(links)


        # =====================
        # OUTPUT COLUMN (RIGHT)
        # =====================
            
        with gr.Column(scale=1):
            with gr.Row():
                saida = gr.Textbox(value='', label="Assistant raw output", info='Response history containing control tokens (CTRL + SHIFT + ESC to open Task Manager)', show_copy_button=True)
                outputs = [saida] # Primeiro elemento da tupla de saída da função 'text_generator' (token) 
            with gr.Row():
                btn_next_token = gr.Button('Next Token')
                btn_next_token.click(fn=go_to_next_token, inputs=None, outputs=None, queue=False) 
                btn_copy_code = gr.Button('Copy Code Blocks')
                btn_copy_code.click(fn=copy_code, inputs=None, outputs=None, queue=False)
                btn_notebook = gr.Button('Open JupyterLab')
                btn_notebook.click(fn=launch_notebook, inputs=None, outputs=None, queue=False)
            with gr.Row():
                btn_last_response = gr.Button('Copy Last Response')
                btn_last_response.click(fn=copy_last_response, inputs=None, outputs=None, queue=False)
                btn_all_responses = gr.Button('Copy All Responses')
                btn_all_responses.click(fn=copy_all_responses, inputs=None, outputs=None, queue=False)
                


                
                # =================================
                
                
                if voice_mode == True:
                    btn_voice = gr.Button('Voice Command', variant='primary', visible=True)
                    btn_voice.click(fn=speech_to_text, inputs=inputs, outputs=inputs[3], queue=True, show_progress='hidden')
                    inputs[3].change(fn=text_generator, inputs=inputs, outputs=outputs, queue=True)
                elif voice_mode == False:
                    btn_voice = gr.Button('')
                    #btn_voice.click(fn=speech_to_text, inputs=inputs, outputs=inputs[3], queue=True, show_progress='hidden')

            
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
                btn_gen_audio = gr.Button('Text to Speech')
                btn_gen_audio.click(fn=text_to_speech, inputs=inputs, outputs=audio_widget, queue=True)
                btn_audio = gr.Button('Last Response')
                btn_audio.click(fn=update_audio_widget, inputs=inputs, outputs=audio_widget, queue=False)
                btn_full_audio = gr.Button('Session Responses')
                btn_full_audio.click(fn=load_full_audio, inputs=inputs, outputs=audio_widget, queue=False)
            with gr.Row():
                gr.HTML("""<br><h5 style="text-align: left; margin: -5px 0 0; color: #f3813f">Fundamentals and Operating Tips:</h5>""")
            with gr.Row():
                gr.HTML("""<h6 style="text-align: left;"><i><span style="color: #9CA3AF;">1) Samantha's Parts:&nbsp;&nbsp;&nbsp;Server (AI processing) <-> Browser Interface (display and configuration)</span></i></h6>""")
            with gr.Row():
                gr.HTML('<h6 style="text-align: left;"><i><span style="color: #9CA3AF;">2) 2 Files Required:&nbsp;&nbsp;&nbsp;Model File (.GGUF) + Model Prompt Template File (.TXT)</span></i></h6>', elem_classes='prompt')
            with gr.Row():
                gr.HTML(r'<h6 style="text-align: left;"><i><span style="color: #9CA3AF;">3) Model Prompt Template:&nbsp;&nbsp;&nbsp;{system_message} + {prompt}</span></i></h6>', elem_classes='prompt')
            with gr.Row():
                gr.HTML('<h6 style="text-align: left;"><i><span style="color: #9CA3AF;">4) Generation Phases:&nbsp;&nbsp;&nbsp;Model loading (non stop) -> Thinking (non stop) -> Token generation (stop)</span></i></h6>', elem_classes='prompt')
            with gr.Row():
                gr.HTML('<h6 style="text-align: left;"><i><span style="color: #9CA3AF;">5) Context Window:&nbsp;&nbsp;&nbsp;System Prompt + Previous Response + User Prompt + Current Response</span></i></h6>')
            with gr.Row():
                gr.HTML('<h6 style="text-align: left;"><i><span style="color: #9CA3AF;">6) Chaining Sequence:&nbsp;&nbsp;&nbsp;(Models List -> Prompts List -> Number of Responses) -> Number of Loops</span></i></h6>')         
            with gr.Row():
                gr.HTML('<h6 style="text-align: left;"><i><span style="color: #9CA3AF;">7) GPT:&nbsp;&nbsp;&nbsp;Choice of the next token according to the location/relationship probability patterns extracted from the training texts</span></i></h6>')                     
            with gr.Row():
                gr.HTML('<h6 style="text-align: left;"><i><span style="color: #9CA3AF;">8) Choice Probabilities:&nbsp;&nbsp;&nbsp;Deterministic (high score diff) X Sthocastic (low score diff)</span></i></h6>')                    
            with gr.Row():
                gr.HTML('<h6 style="text-align: left;"><i><span style="color: #9CA3AF;">9) Tokenizer:&nbsp;&nbsp;&nbsp;Databases (text) -> Tokens (text) -> Tokens Indexes (int) -> Model Vocabulary (int/text)</span></i></h6>')         
            with gr.Row():
                gr.HTML('<h6 style="text-align: left;"><i><span style="color: #9CA3AF;">10) Embeddings Matrix:&nbsp;&nbsp;&nbsp;Tokens Indexes (int) -> Semantic Relations (vector) -> Matrix (feature table)</span></i></h6>')         
            with gr.Row():
                gr.HTML('<h6 style="text-align: left;"><i><span style="color: #9CA3AF;">11) Math Repr:&nbsp;&nbsp;&nbsp;Human Semantic Universe (words all languages) <-> Mathematical Semantic Dimensions (same numeric repr)</span></i></h6>')         
            with gr.Row():
                gr.HTML('<h6 style="text-align: left;"><i><span style="color: #9CA3AF;">12) Transformer:&nbsp;&nbsp;&nbsp; Initial Embeddings Matrix (table) -> Neural Network (self-attention) -> Context-Aware Embeddings (table) -> Tokens Scores (vocab)</span></i></h6>')     
            with gr.Row():
                gr.HTML('<h6 style="text-align: left;"><i><span style="color: #9CA3AF;">13) Samplings/Penalties:&nbsp;&nbsp;&nbsp;Samplings (temp/top-k/top-p) -> Penalties (pres/freq/rep) -> Stop Condition</span></i></h6>')         
            with gr.Row():
                gr.HTML('<h6 style="text-align: left;"><i><span style="color: #9CA3AF;">14) Setting Sequence:&nbsp;&nbsp;&nbsp;top-k -> top-p -> tfs-z -> presence_penalty -> frequency_penalty -> temperature -> repeat_penalty</span></i></h6>')         
            with gr.Row():
                gr.HTML('<h6 style="text-align: left;"><i><span style="color: #9CA3AF;">15) Summary:&nbsp;&nbsp;&nbsp;(Context Window (text) -> Tokens (vocab) -> Initial Embeddings Matrix (table) -> Transformer (self-attention) -> Context-Aware Embeddings (table) -> Tokens Scores (vocab) -> Sampling/Penalty) -> Stop Condition</span></i></h6>')         
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
        btn4.click(fn=extract_models_names, inputs=None, outputs=inputs[5])
        btn5.click(fn=go_to_next_token, inputs=None, outputs=None, queue=False) # Bound to STOP ALL / RESET button
        btn5.click(fn=stop_running_all, inputs=None, outputs=None, queue=False)
        btn6.click(fn=update_previous_answer, inputs=None, outputs=inputs[2], queue=False, show_progress='hidden')
        saida.change(fn=update_template_field, inputs=None, outputs=inputs[-2], trigger_mode='always_last', queue=False, show_progress=False) 
        inputs[-2].change(fn=update_vocabulary, inputs=None, outputs=inputs[-1], trigger_mode='always_last', queue=False)


def main():
    while True:  
        try:
            demo.queue() # Put interface on queue
            open_browser() # Open browser before endpoint generation (wait demo launch)
            demo.launch(share=False)
        except:
            continue


if __name__ == '__main__':
    main()
    
