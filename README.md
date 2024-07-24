
![v](https://img.shields.io/badge/version-0.1.0-blue) 
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
![v](https://img.shields.io/badge/updated-July%2017,%20%202024-green)

![banner](https://github.com/controlecidadao/samantha_ia/blob/main/images/banner.png)



## Samantha Interface Assistant: Experimental Environment Designed to Democratize the Use of Open Source Large Language Models (LLM)

### ✨ Welcome to Samantha: An Interface Assistant for Open Source Artificial Intelligence

<br>

Samantha is an interface assistant for open source artificial intelligence models developed under [Open Science](https://www.unesco.org/en/open-science) principles (open methodology, open source, open data, open access, open peer review and open educational resources) for use on common Windows computers (without GPU). The program runs the LLM locally, free of charge and unlimitedly, without the need for an internet connection, except to download [GGUF](https://pypi.org/project/llama-cpp-python/) models or when required by the execution of the code created by the models (i.e. for data analysis 📊). Its objective is to democratize knowledge about the use of AI and demonstrate that, using the appropriate technique, even small models are capable of producing responses similar to those of larger proprietary ones. Her mission is to help explore the boundaries of (realy) open AI models.

<br>

Samantha is being developed 🧬 to assist in the exercise of social control of the public administration 🔍, considering the worrisome current scenario of the growing loss of citizens' trust in external control institutions, resulting from the destructuring of the technical staff of the courts of accounts. However, its features allow it to be used by anyone interested in exploring open-source artificial intelligence models, especially programmers.

<br>

The system allows the sequential loading of a list of prompts and models (one model at a time to save memory), as well as the adjustment of their hyperparameters, allowing the response generated by the previous model to be feedbacked and analyzed by the subsequent model to generate the next response, in an unlimited number of interaction cycles between LLMs without human intervention. Models can only interact with the answer provided by the immediately preceding model, so each new response replaces the previous one. You can also use just one model and have it interact with its previous response over an unlimited number of text generation cycles ♾️.
<br><br>

🔗 Some chaining examples **_without using_** Samantha's response **Feedback Loop** feature:

  * **(model_1) responds (prompt_1) X number of responses:** used to monitor model's deterministic or stochastic behavior with help of the Learning Mode, as well as to generate multiple diverse responses with stochastic settings.

  * **(model_1) responds (prompt_1, prompt_2, prompt_n):** used to execute multiples instructions sequencially with the same model.

  * **(model_1, model_2, model_n) respond (prompt_1):** used to compare models' responses for the same single prompt. Useful for comparing different models, as well as quantized versions of the same model.

  * **(model_1, model_2, model_n) respond (prompt_1, prompt_2, prompt_n):** used to compare models' responses for a list of prompts, as well as to execute a sequence of instructions using disctinct models. By using the Single Response per Model feature, each model can also respond to only one specific prompt.
<br><br>

🔗 Some chaining examples **_using_** Samantha's response **Feedback Loop** feature:

  * **(model_1) responds (prompt_1) X number of responses:** Used to improve model's previous response through a fixed user instruction using the same model, as well as to generate a continuous dialog using a single model.

  * **(model_1) responds (prompt_1, prompt_2, prompt_n):** used to improve model's previous response through multiples user instructions sequencially with the same model. Each prompt is used to refine the previous response.

  * **(model_1, model_2, model_n) respond (prompt_1):** Used to improve previous model's response using disctinct models, as well as to generate a dialog between different models.

  * **(model_1, model_2, model_n) respond (prompt_1, prompt_2, prompt_n):** Used to execute a sequence of instructions using disctinct models (Single Response per Model feature).
<br><br>


👉 **Chaining Sequence Template:   ( [models list] -> respond -> ( [user prompt list] X number of responses) ) X number of loops**
<br><br>

Sequencing of prompts and models allows the generation of long responses by fractioning the user input instruction 🧩. Every partial response fits in the model's response length defined in the training process.
<br><br>

As an open source tool for automatic self-interaction between AI models, Samantha Interface Assistant was designed to explore **reverse prompt engineering with self-improvement feedback loop** 🔁. This technique helps small large language models (LLM) to generate more accurate responses by transferring to the model the task of creating the final prompt and corresponding response based on the user's initial imprecise instructions, adding intermediate layers to the prompt construction process. Samantha doesn't have a hidden system prompt like it does with proprietary models. All instructions are controlled by the user.
<br><br>

🎲 Thanks to **emergent behavior**, with the right prompt and proper hyperparameter configuration, even small models working together can generate big responses!
<br><br><br>

<p align="center">
  <a href="https://youtu.be/vt5fpE0bzSY">
    <img src="https://i.sstatic.net/Vp2cE.png" alt="Watch the video">
  </a>
</p>

<br>

🌎 **A Small Step:** Samantha is just a movement towards a future where artificial intelligence is not a privilege but a tool for all in a world where individuals can leverage AI to enhance their productivity, creativity, and decision-making without barriers, walking a journey to democratize AI and make it a force for good in our daily lives.

<br>

⚠️ **Use Responsibly:**
The generated text reflects the content, biases, errors and improprieties present in their training datasets. We encourage responsible use of Samantha and for insights only, always keeping ethical considerations at the forefront of our interactions with AI algorithms, which are complex mathematical models that generates coherent texts from the sequencing of words (tokens) based on the probability patterns extracted from the training texts.

<br>

🦾 **The Instrumental Nature of AI:** Recognizing the technological monopoly of artificial intelligence as a possible instrument of domination and the expansion of social inequalities represents a challenge at this inflection point in history. Noting the flaws of the smaller models during the text generation process aids in this understanding by comparing them with the claimed perfection of the larger proprietary models. It is necessary to reposition things in their proper places and question the romantic reductionist view of attributing human characteristics - such as intelligence - to a technology produced by the human intellect. For this reason, it is essential to demystify artificial intelligence through a didactic approach to how this novel "word calculator" works. Certainly, the dopamine of the initial charm artificially created by the market will not withstand the generation of a few hundred tokens (token is the name given to the basic building block of texts that an LLM uses to understand and generate text. A token may be an entire word or part of a word).

<br>

✏️ **Text Generation Considerations:**
Users should be aware that the responses generated by AI are derived from the training of its large language models on a vast corpus of text data. The exact sources or processes used by the AI to generate its outputs cannot be precisely cited or identified. The content produced by the AI is not a direct quotation or compilation from specific sources. Instead, it reflects the patterns, statistical relationships, and knowledge that the AI's neural networks have learned and encoded during the training process on the broad data corpus. The responses are generated based on this learned knowledge representation, rather than being retrieved verbatim from any particular source material. While the AI's training data may have included authoritative sources, its outputs are its own synthesized expressions of the learned associations and concepts.

<br>

🎯 **Objective:**
The primary objective with Samantha is to **inspire** 💡 others to create similar - and much better ones, to be sure - systems and to educate users on the utilization of AI. Our goal is to foster a community of developers and enthusiasts who can take the knowledge and tools to further innovate and contribute to the field of open source AI. By doing so, the aim to cultivate a culture of collaboration and sharing, ensuring that the benefits of AI are accessible to all, regardless of their technical background or financial resources. It is believed that by enabling more people to construct and comprehend AI applications, we can collectively drive progress and address **societal challenges** with informed and diverse perspectives. Let's work together to shape a future where AI is a **positive and inclusive force for humanity**. See [UNESCO's Ethics of Artificial Intelligence Recommendations](https://www.unesco.org/en/artificial-intelligence/recommendation-ethics?hub=32618).

<br>

**On the Shoulders of Giants:**
 Special thanks 🙏 to Georgi Gerganov and the whole team working on [llama.cpp](https://github.com/ggerganov/llama.cpp) for making all of this possible, as well as to [Andrei Bleten](https://github.com/abetlen/llama-cpp-python) by his amazing Python bidings for the Gerganov C++ library.

<br><br>





## 📌 Samantha's Key Features

<details>
<summary>Features</summary>

<br><br>
✅ **Open Source Foundation:** Built upon [Llama.cpp](https://github.com/ggerganov/llama.cpp) and [Gradio](https://www.gradio.app/) , under [MIT license](https://opensource.org/license/mit), Samantha runs on standard computers, even without a dedicated Graphics Processing Unit (GPU).<br><br>
  
✅ **Offline Capability:** Samantha operates independently of the internet, requiring connectivity only for the initial download of model files or when required by the execution of the code created by the models. This ensures privacy and security for your data processing needs. Your sensitive data is not shared via the internet with companies through confidentiality agreements.<br><br>

✅ **Unlimited and Free Use:** Samantha's open-source nature allows for unrestricted use without any costs or limitations, making it accessible to everyone in everywhere.<br><br>

<!-- **Accessibility for People with Disabilities**: The system is designed to be user-friendly and accessible for people with physical disabilities. With features like voice interaction through text-to-speech and speech-to-text, users can interact with Samantha without relying solely on visual interfaces. This inclusive design ensures that AI technology is available to everyone, regardless of their abilities.-->

✅ **Extensive Model Selection:** With access to [thousands](https://huggingface.co/models?sort=trending&search=gguf) of foundation and fine-tuned open-source models, users can experiment with various AI capabilities, each tailored to different tasks and applications, allowing to chain the sequence of models that best meet your needs.<br><br>

✅ **Copy and paste LLMs:** To try out a sequence of `gguf` models, just copy their download links from any Hugging Face repository and paste inside Samantha to run them right away in sequence.<br><br>

✅ **Customizable Parameters:** Users have control over model hyperparameters such as **context window** length (n_ctx, max_tokens), **token sampling** (temperature, tfs_z, top-k, top-p, min_p, typical_p), **penalties** (presence_penalty, frequency_penalty, repeat_peanlty) and **stop words**, allowing for responses that suit specific requirements, with deterministic or stochastic behavior.<br><br>

✅ **Interactive Experience:** Samantha's chaining functionality enables users to generate endless texts by chaining prompts and models, facilitating complex interactions between different LLMs without human intervention.<br><br>

✅ **Learning Insights:** A feature called 'Learning Mode' lets users observe the model's decision-making process, providing insights into how it selects output tokens based on their probability scores (logits) and hyperparameter settings. A list of the least likely selected tokens is also generated.<br><br>

✅ **Voice Interaction:** Samantha supports simple voice commands with offline speech-to-text [Vosk](https://alphacephei.com/vosk/) (English and Portuguese) and text-to-speech with SAPI5 voices, making it accessible and user-friendly.<br><br>

✅ **Audio feedback:** The interface provides audible alerts to the user, signaling the beginning and end of the text generation phase by the model.<br><br>

✅ **Document Handling:** The system can load small PDF and TXT files. Chaining instructions/prompts can be inputted via a TXT file for convenience.<br><br>

✅ **Versatile Text Input:** Fields for prompt insertion allow users to interact with the system effectively, including system prompt, previous model response and user prompt to guide the model's response.<br><br>

✅ **Code Integration:** Automatic extraction of code blocks from model's response, along with pre-installed [JupyterLab](https://jupyter.org/) in an isolated virtual environment, enables users to execute generated code swiftly for immediate results.<br><br>

✅ **Data Analysis Tools:** A suite of data analysis tools like [Pandas](https://pandas.pydata.org/), [Numpy](https://numpy.org/), [SciPy](https://scipy.org/), [Scikit-Learn](https://scikit-learn.org/stable/index.html#), [Seaborn](https://seaborn.pydata.org/), [Vega-Altair](https://altair-viz.github.io/), [Plotly](https://plotly.com/python/), [Dash](https://plotly.com/examples/), [Sweetviz](https://pypi.org/project/sweetviz/), [D-Tale](https://github.com/man-group/dtale), [DataPrep](https://dataprep.ai/), [NetworkX](https://networkx.org/), [Pyvis](https://pyvis.readthedocs.io/en/latest/index.html), [Selenium](https://selenium-python.readthedocs.io/), [PyMuPDF](https://pypi.org/project/PyMuPDF/) and [Beautiful Soup](https://beautiful-soup-4.readthedocs.io/en/latest/) are available within JupyterLab for comprehensive analysis and visualization (for a complete list of all Python available libraries, use a prompt like **_"create a Python code that print all modules installed. Separate each module with \<br\> tag."_** and press Run Code button. The result will be displayed in a browser popup). Integration with [DB Browser](https://sqlitebrowser.org/about/) is also available.<br><br>

✅ **Performance Optimized:** To ensure smooth performance on CPUs, Samantha maintains a limited chat history to just the previous response, reducing the model's context window size to save memory and computational resources.<br>

</details>





<br><br>
## 🛠️ Installing Samantha

<details>
<summary>Instructions</summary>

<br><br>
To use Samantha you will need:
<br><br>
* Install [Visual Studio](https://visualstudio.microsoft.com/pt-br/vs/community/) (free community version) on your computer. Download it, run it, and select only the option **Desktop development with C++** (administrator privileges required):

  ![cmake](https://github.com/controlecidadao/samantha_ia/blob/main/images/cmake2.png)
<br><br>
* Download the zip file from Samantha's repository by clicking [here](https://github.com/controlecidadao/samantha_ia/archive/refs/heads/main.zip) and unzip it to your computer. Select the drive where you want to install the program:

   ![directory](https://github.com/controlecidadao/samantha_ia/blob/main/images/directory.png)
<br><br>
* Open `samantha_ia-main` directory and double click on `install_samantha_ia.bat` file to start installation. Windows may ask you to confirm the origin of the `.bat` file. Click on 'More info' and confirm. We encorage to inspect the code of all files:

   ![directory](https://github.com/controlecidadao/samantha_ia/blob/main/images/install.png)<br><br>

  >_This is the critical part of the installation. If everything goes well, the process will complete without displaying error messages in the terminal._<br>

  <br>
  
  The installation process takes several minutes and should end with the creation of two virtual environments: `samantha` and `jupyterlab`.

<br>

* Once installed, open Samantha by double clicking on `open_samantha.bat` file. Windows may ask you again to confirm the source of the `.bat` file. This authorisation is required only the first time you run the program. Click on 'More info' and confirm:<br>

  ![directory](https://github.com/controlecidadao/samantha_ia/blob/main/images/open_samantha.png)<br><br>

  A terminal window will open. This is the Samantha's **server-side**.

  After answering the initial questions (interface language and voice control options - voice control is not suitable for first use), the interface will open in a new browser tab. This is the Samantha's **browser-side**:

  <br>

  ![directory](https://github.com/controlecidadao/samantha_ia/blob/main/images/interface_english.png)<br><br>

  With the browser window opened, Samantha is ready to go.

</details>





<br><br>
## 👟 Testing a Model in 5 Steps

<details>
<summary>Instructions</summary>

<br><br>
Samantha needs just a `.gguf` model file to generate text. Follow these steps to perform a simple model test with Samantha:
<br><br>

1) Open Microsoft Task Management by pressing `CTRL + SHIFT + ESC` and check available memory. Close some programs if necessary to free memory.

2) Visit [Hugging Face](https://huggingface.co/models?library=gguf&sort=trending&search=gguf) repository and click on the card to open the corresponding page. Locate the _Files and versions_ tab and choose a `gguf` model that fits in your available memory.
   
4) Right click over the model download link icon and copy its url.

5) Paste the model url into Samantha's _Download Models for Testing_ field.

6) Insert a prompt into _USER Prompt_ field and press `Enter` (keep the $$$ sign at the end of your prompt). The model will be downloaded and the response will be generated using a deterministic settings. You can track this process via Task Management.

<br>

Every new model downloaded via this copy and paste procedure will replace the previous one to save hard drive space.

You can also download the model and save it permanently to your computer. For more datails, see the section below.

</details>





<br><br>
## ⬇️ Downloading Large Language Models (LLM)

<details>
<summary>Instructions</summary>

<br>

### Downloading Open Source Model Files (.gguf)

Open souce model can be downloaded from [Hugging Face](https://huggingface.co/models?sort=trending&search=gguf), using `gguf` as the search parameter. You can combine two words like `gguf code`.

You can also go to a specific repository and see all the `.gguf` models available for downloading and testing, like [https://huggingface.co/bartowski](https://huggingface.co/bartowski)
<br><br>

The models are displayed on cards like this:

![model_card](https://github.com/controlecidadao/samantha_ia/blob/main/images/model_card.png)
<br><br>

To download the model, click on the card to open the corresponding page. Locate the **Model card** and **Files and versions** tabs:

![tabs](https://github.com/controlecidadao/samantha_ia/blob/main/images/tabs.png)
<br><br>

After that, click on the **Files and versions** tab and download a model that fits in your available RAM space. To check your available memory, open Task Manager by pressing `CTRL + SHIFT + ESC`, click on **Performance** tab (1) and select **Memory** (2):

<br>

![task](https://github.com/controlecidadao/samantha_ia/blob/main/images/task_manager.png)
<br><br>

We suggest to download the model with **Q4_K_M** (4-bit quantization) in its link name (put the mouse over the download button to view the complete file name in the link like this: `https://huggingface.co/NousResearch/Hermes-2-Pro-Llama-3-8B-GGUF/resolve/main/Hermes-2-Pro-Llama-3-8B-Q4_K_M.gguf?download=true`). As a rule, the larger the model size, the greater the accuracy of the generated text.
<br>

If the downloaded model doesn't fit into the available RAM space, your hard drive will be used, impacting performance.

Download the chosen model and save it to your computer or just copy the download link and paste it inside Samantha's _Download model for testing_ field. Watch video tutorials in the section below for more details.
<br><br>

### Your First Testing Models

Note that each model has its own characteristics, presenting significantly different responses depending on its size, internal architecture, training method, predominant language of the training database, user prompt and hyperparameter adjustment, and it is necessary to test its performance for the desired task. **Some models may not (yet) be loaded due to their technical characteristics or incompatibility with the current version of the [llama.cpp Python binding](https://github.com/abetlen/llama-cpp-python) used by Samantha**.

* [llmware/bling-phi-3-gguf](https://huggingface.co/llmware/bling-phi-3-gguf) (**3.8 billion** parameters model created by [Microsoft](https://huggingface.co/microsoft) and fine-tunned by [llmware](https://huggingface.co/llmware))

Where to find models to test: [Huggingface GGUF Models](https://huggingface.co/models?sort=trending&search=gguf)<br><br>

The quality of a model can be assessed using four basic criteria:

  * **Degree of understanding** of the explicit and implicit instructions contained in the user prompt;

  * **Degree of precision in the decision-making** process to fill in the gaps in the context of the user prompt and to resolve ambiguities, required to generate the response;

  * **Degree of adherence** to these instructions;

  * **Quality of the response** (structure and content) in relation to the user's expectations for the problem submitted to the model, considering the technique used to create the prompt and the adjustment of the model's hyperparameters.
</details>





<br><br>
## 🧠 Samantha's Controls & Settings

### Interface Left Column (input):

<details>
<summary>Start chat (button)</summary>
<br>

Starts a chat session, sending all input texts (system prompt, assistant previous response and user prompt) to the server, as well as the settings adjusted by the user.

Keyboard shortcut: Press "Enter" anywhere on the page.

<br><br>
</details>

<details>
<summary>Stop / Next (button)</summary>
<br>

Interrupts the token generation process for the current model, starting the execution of the next model in the sequence, if any.

It also stops playback of the currently playing audio when in speech autoplay mode (_Read response aloud_ checkbox selected).

<br><br>
</details>

<details>
<summary>Clear history (button)</summary>
<br>

Clears the history of the current chat session.

<br><br>
</details>

<details>
<summary>Load model (button)</summary>
<br>

Allows you to select the directory where the models available for loading are saved.

Default: "Downloads" folder

You can select any directory that contains models. In this case, the models contained in the selected directory will be listed in the _Model selection_ dropdown field.

<br><br>
</details>

<details>
<summary>Stop all & reset (button)</summary>
<br>

Stops the sequence of running models and resets internal settings of the last loaded model.

<br><br>
</details>

<details>
<summary>Replace response (button)</summary>
<br>

Replaces the text in the _Assistant previous response_ field with the text of the last response generated by the model.

<br><br>
</details>


<details>
<summary>System prompt (textbox)</summary>
<br>

In the context of Large Language Models (LLMs), a **system prompt** is a special type of instruction given to the model at the beginning of a conversation or task. 

Think of it as setting the stage for the interaction. It provides the LLM with crucial information about its role, the desired persona, and the overall context of the conversation.

Here's how it works:

1. **Defining the Role:** The system prompt clearly defines the LLM's role in the interaction. 
    * For example, it might instruct the model to act as a helpful assistant, a creative writer, a factual summarizer, or even a character in a story.

2. **Setting the Tone and Persona:**  The system prompt can also establish the desired tone and persona for the LLM's responses. 
    * It could be formal, informal, humorous, serious, or any other style depending on the intended use case.

3. **Providing Contextual Information:** The system prompt can offer background information relevant to the conversation or task. 
    * This helps the LLM understand the user's needs and provide more accurate and relevant responses.

**Benefits of Using System Prompts:**

* **Improved Consistency:** System prompts ensure that the LLM consistently adheres to a specific role and style throughout the interaction.
* **Enhanced Accuracy:** By providing context and instructions, system prompts help the LLM generate more accurate and relevant responses.
* **Tailored Experiences:** Different system prompts can be used to create tailored experiences for users based on their needs and preferences.

**Example:**

Let's say you want to use an LLM to write a poem in the style of Shakespeare. A suitable system prompt would be:

"You are William Shakespeare, a renowned poet from Elizabethan England. Write a sonnet about the beauty of a summer day."

By providing this system prompt, you guide the LLM to generate a response that reflects Shakespeare's language, style, and thematic interests.

Not all models support system prompt. Test to find out. Put "x = 2 + 2" in the system prompt field and ask the model the value of "x" in the user prompt field. If the model gets the value of "x" right, system prompt is available.

<br><br>
</details>

<details>
<summary>Feedback loop (checkbox)</summary>
<br>

When activated, it automatically considers the response generated by the model in the current conversation cycle as being the model's previous response in the next cycle, allowing feedback from the system. 

Any text entered by the user in the _Assistant previous response_ field is only considered in the first cycle after activating this feature. In the following cycles, the model's response internally replaces the previous response, but without deleting the text contained in that field, which can be reused in a new chat session. You can monitor the content of the assistant previous response via terminal.

In turn, when deactivated, it always uses the text contained in the _Assistant previous response_ field as the previous response, unless the text is preceded by “---”.

To internally clear the model's previous response, press the _Clear History_ button. It is recommended to press the _Clear History_ button before each new conversation when this feature is activated.

<br><br>
</details>

<details>
<summary>Assistant previous response loop (textbox)</summary>
<br>

Stores the text considered by the model to be your previous response in the current conversation cycle.

Used to allow feedback on the responses generated by the model.

To ignore text in this field, include "---" at the beginning of the text.

<br><br>
</details>

<details>
<summary>User prompt (textbox)</summary>
<br>

Main interface field, receives the list of user prompts that will be submitted to the model sequentially.

Each item in the list must be separated from the next one by a line break (SHIFT + ENTER or "\n") or by the symbols "$$$", if the items are made up of text with line breaks.

You can import a TXT file containing a list of prompts.

"---" before a prompt list item causes the system to ignore that item.

Text positioned within single square brackets ("[" and "]") is added to the beginning of each prompt list item, simulating a system prompt.

Text positioned within double square brackets ("[[" and "]]") is added as the last item in the prompt list. In this case, all responses generated by the model in the current chat session are concatenated and added to the end of this item, allowing the model to analyze them together.

If the model generates "STOP_SAMANTHA", it stops token generation and exits the loop.

**Example:**<br>
[You are a poet that writes only in Portuguese]<br>
Create a sentence about love<br>
Create a sentence about life<br>
---Create a sentence about time (_this instruction is ignored_)<br>
[[Create a paragraph in English that summarizes the ideas contained in the following sentences:]]<br>
(_previous responses are concatenated here_)<br>

**Model responses sequence:**<br>
"O amor é um fogo que arde no meu peito, uma chama que me guia através da vida."<br>
"A vida é um rio que flui sem parar, levando-nos para além do que conhecemos."<br>
Love and life are intertwined forces that shape our existence. Love burns within us like a fire, guiding us through life's journey with passion and purpose. Meanwhile, life itself is a dynamic and ever-changing river, constantly flowing and carrying us beyond the familiar and into the unknown. Together, love and life create a powerful current that propels us forward, urging us to explore, discover, and grow.

<br><br>
</details>

<details>
<summary>Model selection (dropdown)</summary>
<br>

Dropdown list of models saved on the computer and available for text generation.

The default location for saving models is the "Downloads" directory.

You can select multiples models (even repeated) to create a sequence of models to respond the user prompts.

The last model downloaded from a link is saved as _MODEL_FOR_TESTING_ and is displayed in this list.

<br><br>
</details>

<details>
<summary>Download model for testing (textbox)</summary>
<br>

Receives a list of links to the models that will be downloaded and executed sequencially.

Links preceded by "---" will be ignored.

Only works if no model is selected in _Model selection_ field.

<br><br>
</details>

<details>
<summary>Single response per model (checkbox)</summary>
<br>

Activates a single response per model. 

Prompts that exceed the number of models or models that exceed the number of prompts are ignored. 

Disables _Number of loops_ and _Number of responses_ checkboxes.

<br><br>
</details>

<details>
<summary>Reset model (checkbox)</summary>
<br>

Reinitializes the internal state of the model, eliminating the influence of the previous context.

<br><br>
</details>

<details>
<summary>Shuffle models (checkbox)</summary>
<br>

Shuffles the execution order of the models if 3 or more models are selected.

<br><br>
</details>

<details>
<summary>Fast mode (checkbox)</summary>
<br>

Generates text faster in the background without displaying the addition of each token in the interface.

Disables Learning Mode.

<br><br>
</details>

<details>
<summary>Voice selection (dropdown)</summary>
<br>

Selects the language of the computer's SAPI5 voice that will read the responses generated by the model.

<br><br>
</details>

<details>
<summary>Read response aloud (checkbox)</summary>
<br>

Activates automatic reading mode for responses generated by the model using the language selected in the _Voice selection_ field.

<br><br>
</details>

<details>
<summary>Learning mode (radio buttons)</summary>
<br>

Activates Learning Mode.

Displays barplots with token scores.

Only works if Fast Mode is unchecked. 

**Items:**<br>

**OFF:** Learning mode disabled.<br>
**0, 0.3, 1, 3, 10:** Time in seconds.<br>
**NEXT TOKEN:** Allows you to control the response generation process, token by token, via _NEXT TOKEN_ button.<br>

<br><br>
</details>

<details>
<summary>Number of loops (radio buttons)</summary>
<br>

number of repetitions of the selected model sequence.

<br><br>
</details>

<details>
<summary>Number of responses (radio buttons)</summary>
<br>

Number of responses to be generated by each selected model.

<br><br>
</details>

<details>
<summary>n_ctx (slider)</summary>
<br>

Teste

<br><br>
</details>

<details>
<summary>max_tokens (slider)</summary>
<br>

Teste

<br><br>
</details>

<details>
<summary>Stop (textbox)</summary>
<br>

Teste

<br><br>
</details>

<details>
<summary>temperature (slider)</summary>
<br>

Teste

<br><br>
</details>

<details>
<summary>tfs_z (slider)</summary>
<br>

Teste

<br><br>
</details>

<details>
<summary>top_p (slider)</summary>
<br>

Teste

<br><br>
</details>

<details>
<summary>min_p (slider)</summary>
<br>

Teste

<br><br>
</details>

<details>
<summary>typical_p (slider)</summary>
<br>

Teste

<br><br>
</details>

<details>
<summary>top_k (slider)</summary>
<br>

Teste

<br><br>
</details>

<details>
<summary>presence_penalty (slider)</summary>
<br>

Teste

<br><br>
</details>

<details>
<summary>frequency_penalty (slider)</summary>
<br>

Teste

<br><br>
</details>

<details>
<summary>repeat_penalty (slider)</summary>
<br>

Teste

<br><br>
</details>

<details>
<summary>Show model's vocabulary (checkbox)</summary>
<br>

Teste

<br><br>
</details>

<details>
<summary>Unload model (button)</summary>
<br>

Teste

<br><br>
</details>

<details>
<summary>PDF pages (button)</summary>
<br>

Teste

<br><br>
</details>

<details>
<summary>PDF full (button)</summary>
<br>

Teste

<br><br>
</details>

<details>
<summary>TXT system prompt (button)</summary>
<br>

Teste

<br><br>
</details>

<details>
<summary>TXT user prompt (button)</summary>
<br>

Teste

<br><br>
</details>

<details>
<summary>Copy HF links (button)</summary>
<br>

Teste

<br><br>
</details>

<details>
<summary>DB Browser (button)</summary>
<br>

Teste

<br><br>
</details>

<details>
<summary>D-Tale (button)</summary>
<br>

Teste

<br><br>
</details>

<!--<details>
<summary>(button)</summary>
<br>

Teste

<br><br>
</details>-->

<details>
<summary>Useful links (links)</summary>
<br>

Teste

<br><br>
</details>

<details>
<summary>Tutorials (links)</summary>
<br>

Teste

<br><br>
</details>

<details>
<summary>Installed Python modules to use with JupyterLab (links)</summary>
<br>

Teste

<br><br>
</details>

<details>
<summary>Accessibility (links)</summary>
<br>

Teste

<br><br>
</details>

<br>






### Interface Right Column (output):

<details>
<summary>Assistant output (textbox)</summary>
<br>

Teste

<br><br>
</details>

<details>
<summary>Next token (button)</summary>
<br>

Teste

<br><br>
</details>

<details>
<summary>Copy code blocks (button)</summary>
<br>

Teste

<br><br>
</details>

<details>
<summary>Open Jupyterlab (button)</summary>
<br>

Teste

<br><br>
</details>

<details>
<summary>Copy last response (button)</summary>
<br>

Teste

<br><br>
</details>

<details>
<summary>Copy all response (button)</summary>
<br>

Teste

<br><br>
</details>

<details>
<summary>Run code (button)</summary>
<br>

Teste

<br><br>
</details>

<details>
<summary>Response in HTML (button)</summary>
<br>

Teste

<br><br>
</details>

<details>
<summary>Responses in HTML (button)</summary>
<br>

Teste

<br><br>
</details>

<details>
<summary>Voice control (button)</summary>
<br>

Teste

<br><br>
</details>

<details>
<summary>Audio player (widget)</summary>
<br>

Teste

<br><br>
</details>

<details>
<summary>Text to speech (button)</summary>
<br>

Teste

<br><br>
</details>

<details>
<summary>Last response (button)</summary>
<br>

Teste

<br><br>
</details>

<details>
<summary>All responses (button)</summary>
<br>

Teste

<br><br>
</details>

<details>
<summary>Models repositories (links)</summary>
<br>

Teste

<br><br>
</details>

<details>
<summary>Operating tips (tips)</summary>
<br>

Teste

<br><br>
</details>

<details>
<summary>User prompt examples (prompts)</summary>
<br>

Teste

<br><br>
</details>

<details>
<summary>System prompt examples (prompts)</summary>
<br>

Teste

<br><br>
</details>















context window length (n_ctx, max_tokens), token sampling (temperature, tfs_z, top-k, top-p, min_p, typical_p), penalties (presence_penalty, frequency_penalty, repeat_peanlty) and stop words,


### Initial Settings

Samantha's initial settings is **deterministic**. As a rule, this means that for the same prompt, you'll get always the same answer, even when applying penalties to exclude repeated tokens (penalties does not affect the model deterministic behavior).<br> 

Used to assess training database biases. 

Some models tend to loop (repeat the same text indefinitely) when using highly deterministic adjustments, selecting tokens with the highest probability score. 

In turn, for **stochastic* behavior, suited for creative content, in which model selects tokens with different probability scores, adjust the hyperparameters accordingly.
<br><br>

**Deterministic settings (default):**<br>
* temperature (0)
* tfs_z (0)
* top_p (0)
* min_p (1)
* typical_p (0)
* top_k (40)
* presence_penalty (0)
* frequency_penalty (0)
* repeat_penalty (1.1).
<br><br>

**Stochastic settings:** <br>
* temperature (0.2)
* tfs_z (1)
* top_p (0.9)
* min_p (0.05)
* typical_p (1)
* top_k (40)
* presence_penalty (0)
* frequency_penalty (0)
* repeat_penalty (1.1)

</details>

<br><br>
## ▶️ Video Tutorials

<details>
<summary>Click to open</summary>

<br><br>
You can add text within a collapsed section. 
<br><br>
  
```python
   print("Hello World")
```
<br>

[![Watch the video](https://i.sstatic.net/Vp2cE.png)](https://youtu.be/vt5fpE0bzSY)

</details>

<br><br>
## 🪄 Samantha's Tips and Tricks

<details>
<summary>Click to open</summary>

<br><br>
* Tip 1
</details>


<br><br>
## 📝 Version History and Future Improvements

<details>
<summary>Click to open</summary>

 <br><br>
**Code Versions:**

Version 0.1.0 (2024-07-15):
* Initial beta version.
<br>

**Future improvements:**
* Try other lightweight offline Speech-to-Text libraries with better speech recognition accuracy.
* Refactor the code to make it more accessible.
<br>
Suggestions are always welcome!

</details>
<br><br>

<!--https://github.com/matiassingers/awesome-readme?tab=readme-ov-file#Examples-->
