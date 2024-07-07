
![v](https://img.shields.io/badge/version-0.1.0-blue) 
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
![v](https://img.shields.io/badge/updated-June%2030,%20%202024-green)

![banner](https://github.com/controlecidadao/samantha_ia/blob/main/images/banner.png)



## Samantha Interface Assistant: Experimental Environment Designed to Democratize the Use of Open Source Large Language Models (LLM)

### Welcome to Samantha: The Interface Assistant for Open Source Artificial Intelligence Models

<br>

Samantha is an interface assistant for open source artificial intelligence models developed under [Open Science](https://www.unesco.org/en/open-science) principles for use on common computers (without GPU). The program runs the LLM locally, free of charge and unlimitedly, without the need for an internet connection, except to download the models. Its objective is to democratize knowledge about the use of open source AIs and demonstrate that, using the appropriate technique, even small models are capable of producing responses similar to those of larger proprietary ones. Her mission is to help explore the boundaries of (realy) open AI models.

<br>

The system allows the sequential loading of models (one model at a time) and adjustment of their hyperparameters, allowing the response generated by the previous model to be analyzed by the subsequent model to generate the next response, in an unlimited number of interaction cycles between LLMs without human intervention. Each model can only interact with the answer provided by the immediately preceding model. Each new response replaces the previous one. You can also use just one model and have it interact with its previous response over an unlimited number of text generation cycles.

<br>

Samantha Interface Assistant was designed to explore **reverse prompt engineering with self-improvement feedback loop**. This technique helps small large language models (LLM) to generate more accurate responses by transferring to the model the task of creating the final prompt and corresponding response based on the user's initial instructions, adding intermediate layers to the prompt construction process.

<br>

Thanks to **emergent behavior**, with the right prompt and proper hyperparameter configuration, even small models can generate big responses!
<br><br><br>

<p align="center">
  <a href="https://youtu.be/vt5fpE0bzSY">
    <img src="https://i.sstatic.net/Vp2cE.png" alt="Watch the video">
  </a>
</p>

<br><br>

# 🎯 Key Features of Samantha

<br>

✅ **Open Source Foundation**: Built upon [Llama.cpp](https://github.com/ggerganov/llama.cpp) and [Gradio](https://www.gradio.app/) , under [MIT license](https://opensource.org/license/mit), Samantha runs on standard computers, even without a dedicated Graphics Processing Unit (GPU).<br><br>
  
✅ **Offline Capability**: Samantha operates independently of the internet, requiring connectivity only for the initial download of model files. This ensures privacy and security for your data processing needs.<br><br>

✅ **Unlimited and Free Use**: Samantha's open-source nature allows for unrestricted use without any costs or limitations, making it accessible to everyone.<br><br>

<!-- **Accessibility for People with Disabilities**: The system is designed to be user-friendly and accessible for people with physical disabilities. With features like voice interaction through text-to-speech and speech-to-text, users can interact with Samantha without relying solely on visual interfaces. This inclusive design ensures that AI technology is available to everyone, regardless of their abilities.-->

✅ **Extensive Model Selection**: With access to [thousands](https://huggingface.co/models?sort=trending&search=gguf) of open-source models (Microsoft, Google, Meta etc.), users can experiment with various AI capabilities, each tailored to different tasks and applications.<br><br>

✅ **Customizable Parameters**: Users have control over model hyperparameters such as temperature, top-k, top-p, among others, allowing for responses that suit specific requirements.<br><br>

✅ **Interactive Experience**: Samantha's chaining functionality enables users to generate endless texts by chaining prompts and models, facilitating complex interactions between different LLMs without human intervention.<br><br>

✅ **Learning Insights**: A feature called 'Learning Mode' lets users observe the model's decision-making process, providing insights into how it selects output tokens based on their probability scores (logits) and hyperparameter settings.<br><br>

✅ **Voice Interaction**: Samantha supports offline text-to-speech with SAPI5 voices and speech-to-text with [Vosk](https://alphacephei.com/vosk/) (English and Portuguese), making it accessible and user-friendly for everyone.<br><br>

✅ **Audio feedback**: Provides audible alerts to the user, signaling the beginning and end of the text generation phase by the model.<br><br>

✅ **Document Handling**: The system can load small PDF and TXT files, and chaining instructions/prompts can be inputted or loaded via a TXT file for convenience.<br><br>

✅ **Versatile Text Input**: Fields for prompt insertion allow users to interact with the system effectively, including system prompt, previous response and user prompt to guide the model's response.<br><br>

✅ **Code Integration**: Automatic extraction of code blocks from model's response, along with pre-installed [JupyterLab](https://jupyter.org/), enables users to execute generated code swiftly for immediate results.<br><br>

✅ **Data Analysis Tools**: A suite of data analysis tools like [Pandas](https://pandas.pydata.org/), [Numpy](https://numpy.org/), [Seaborn](https://seaborn.pydata.org/), [Vega-Altair](https://altair-viz.github.io/), [Plotly](https://plotly.com/python/), [Dash](https://plotly.com/examples/), [Sweetviz](https://pypi.org/project/sweetviz/), [D-Tale](https://github.com/man-group/dtale), [DataPrep](https://dataprep.ai/), [NetworkX](https://networkx.org/), [Pyvis](https://pyvis.readthedocs.io/en/latest/index.html), [DB Browser](https://sqlitebrowser.org/about/), [PyMuPDF](https://pypi.org/project/PyMuPDF/)  and [Beautiful Soup](https://beautiful-soup-4.readthedocs.io/en/latest/) are available within JupyterLab for comprehensive analysis and visualization (for a complete list of Python available libraries, type `!pip list` in a JupyterLab cell).<br><br>

✅ **Performance Optimized**: To ensure smooth performance on CPUs, Samantha maintains a limited chat history to just the previous response, reducing the model's context window size.<br>

<br>

**Our Vision:**
Samantha is more than just an AI interface; it's a [Open Science](https://www.unesco.org/en/open-science) movement towards a future where artificial intelligence is not a privilege but a tool for all. One can envision a world where individuals can leverage AI to enhance their productivity, creativity, and decision-making without barriers. Join us in this journey to democratize AI and make it a force for good in our daily lives.

<br>

**Use Responsibly:**
As one embrace the power of these models, let's remember that the generated text reflects the content, biases, errors and improprieties present in their training datasets. We encourage responsible use of Samantha for insights only, always keeping ethical considerations at the forefront of our interactions with AI algorithms, which are just a mathematical model that generates coherent texts from the sequencing of words (tokens) based on the probability extracted from the training texts.

<br>

Users should be aware that the responses generated by AI are derived from the training of its large language models on a vast corpus of text data. The exact sources or processes used by the AI to generate its outputs cannot be precisely cited or identified. The content produced by the AI is not a direct quotation or compilation from specific sources. Instead, it reflects the patterns, statistical relationships, and knowledge that the AI's neural networks have learned and encoded during the training process on the broad data corpus. The responses are generated based on this learned knowledge representation, rather than being retrieved verbatim from any particular source material. While the AI's training data may have included authoritative sources, its outputs are its own synthesized expressions of the learned associations and concepts.

<br>

**Objective:**
The primary objective with Samantha is to inspire others to create similar systems and to educate users on the utilization of AI. Our goal is to foster a community of developers and enthusiasts who can take the knowledge and tools to further innovate and contribute to the field of open source AI. By doing so, the aim to cultivate a culture of collaboration and sharing, ensuring that the benefits of AI are accessible to all, regardless of their technical background or financial resources. It is believed that by enabling more people to construct and comprehend AI applications, we can collectively drive progress and address societal challenges with informed and diverse perspectives. Let's work together to shape a future where AI is a positive and inclusive force for humanity.

<br>

🙏 **Special Thanks** to Georgi Gerganov and the whole team working on [llama.cpp](https://github.com/ggerganov/llama.cpp) for making all of this possible, as well to [ableten](https://github.com/abetlen/llama-cpp-python) by his amazing Python bidings for the Gerganov C++ library.

<br><br>

# 🛠️ Installing and Running Samantha

To use Samantha you will need:
<br><br>
* Install [Visual Studio](https://visualstudio.microsoft.com/pt-br/vs/community/) (free community version) on your computer. Download it, run it, and select only the option **Desktop development with C++** (administrator privileges required):

  ![cmake](https://github.com/controlecidadao/samantha_ia/blob/main/images/cmake2.png)
<br><br>
* Download the zip file from the repository by clicking [here](https://github.com/controlecidadao/samantha_ia/archive/refs/heads/main.zip) and unzip it to your computer:

   ![directory](https://github.com/controlecidadao/samantha_ia/blob/main/images/directory.png)
<br><br>
* Double click on `install_samantha_ia.bat` file to start installation (Windows may ask you to confirm the origin of the `.bat` file. Click on 'More info' and confirm):

   ![directory](https://github.com/controlecidadao/samantha_ia/blob/main/images/install.png)<br><br>

  >_This is the critical part of the installation. If everything goes well, the process will complete without displaying error messages in the terminal._<br>

  <br>
  The installation process takes several minutes.

<br>

* Once installed, open Samantha by double clicking on `open_samantha.bat` file (Windows may ask you again to confirm the origin of the `.bat` file. Click on 'More info' and confirm):<br>

  ![directory](https://github.com/controlecidadao/samantha_ia/blob/main/images/open_samantha.png)<br><br>

<br>

# ⬇️ Downloading Large Language Models (LLM)

Samantha needs just 1 `.gguf` model file to generate text.
<br>

### Downloading Open Source Model Files (.gguf)

Open souce model files can be downloaded from the [Hugging Face's model search engine](https://huggingface.co/models?sort=trending&search=gguf), using `gguf` as the search parameter.

You can also go to a specific repository and see all the `.gguf` models available for downloading and testing.
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

We suggest to download the model with **Q4_K_M** (4-bit quantization) in its name (put the mouse over the download button to view the complete file name). As a rule, the larger the model size, the greater the accuracy of the generated text:
<br>

If the downloaded model doesn't fit into the available RAM space, your hard drive will be used, impacting performance.

Download the chosen model and save it to your computer or copy the download link and paste it inside Samantha's _Download model for testing_ field.
<br><br>

### Your First Testing Models

Note that each model has its own characteristics, presenting significantly different responses depending on its size, internal architecture, training method, predominant language of the training database, user prompt and hyperparameter adjustment, and it is necessary to test its performance for the desired task. Some models may not (yet) be loaded by Samantha due to their technical characteristics.

* [llmware/bling-phi-3-gguf](https://huggingface.co/llmware/bling-phi-3-gguf) (**3.8 billion** parameters model created by [Microsoft](https://huggingface.co/microsoft), fine-tunned by [llmware](https://huggingface.co/llmware))

Where to find models to test: [Huggingface GGUF Models](https://huggingface.co/models?sort=trending&search=gguf)

<br><br>
# 🧠 Starting Samantha

To start running Samantha:

* Double click on `open_samantha_ia.bat` file (Windows may ask you to confirm the origin of the `.bat` file) located inside the unziped folder and wait a few seconds:

   ![run](https://github.com/controlecidadao/samantha_ia/blob/main/images/run.png)

  A terminal window will open. This is the Samantha's **server-side**.

  After answering the questions, the interface will open in a new browser tab. This is the Samantha's **browser-side**.


* Open Microsoft Task Management by pressing CTRL + SHIFT + ESC to monitor memory usage.

<br><br>
# ▶️ Video Tutorials

Learn how to use Samantha.<br>

<br>

<details>
<summary>Installing Samantha</summary>

<br>
You can add text within a collapsed section. 
<br><br>
  
```python
   print("Hello World")
```
<br>

[![Watch the video](https://i.sstatic.net/Vp2cE.png)](https://youtu.be/vt5fpE0bzSY)

</details>


<br><br>
# 📝 Version History

Project version history and future improvements.

<br>

<details>
<summary>Code Versions</summary>
<br>

**Version 0.1.0 (2024/06/30):**
* Initial test version.
<br>

**Future improvements:**
* Find out why models (Qwen, Llama, Gemma) load faster in the Jupyterlab environment and try to reproduce in the Samantha environment.
* Try other lightweight offline Speech-to-Text libraries with better accuracy.
* Refactor the code to make it more accessible.
<br>

</details>



<br><br><br><br>

<!--https://github.com/matiassingers/awesome-readme?tab=readme-ov-file#Examples-->
