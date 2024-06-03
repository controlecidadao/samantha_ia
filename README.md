
![v](https://img.shields.io/badge/version-0.1.1-blue) 
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
![v](https://img.shields.io/badge/updated-April%2018,%20%202023-green)

![banner](https://github.com/controlecidadao/samantha_ia/blob/main/images/banner.png)



## Experimental Interface Environment Designed to Democratize the Use of Open Source Large Language Models (LLM)

### Welcome to Samantha IA: The Interface Assistant for Open Source Artificial Intelligence Models

In an era where artificial intelligence is becoming increasingly accessible, we introduce Samantha, an AI interface designed to democratize the use of large language models through open source technology. Her mission is to empower individuals and organizations alike, enabling them to harness the power of AI models.

Samantha was designed to allow **text reverse prompt engineering with self-improvement feedback loop**. This technique helps small large language models (LLM) to generate more accurate responses by transferring to the model the task of creating the final prompt based on the user's initial instructions, adding intermediate layers to the prompt construction process.

Thanks to its **emergent behavior**, with the right prompt and proper hyperparameter configuration, even small models can generate big responses!


<br><br>

# 🎯 Key Features of Samantha

- **Open Source Foundation**: Built upon [Llama.cpp](https://github.com/ggerganov/llama.cpp) and [Gradio](https://www.gradio.app/) , under [MIT license](https://opensource.org/license/mit), Samantha runs seamlessly on standard computers, even without a GPU.
  
- **Offline Capability**: Samantha operates independently of the internet, requiring connectivity only for the initial download of model files. This ensures privacy and security for your data processing needs.

- **Unlimited and Free Use**: Samantha's open-source nature allows for unrestricted use without any costs or limitations, making it accessible to everyone.

- **Accessibility for People with Disabilities**: The system is designed to be user-friendly and accessible for people with physical disabilities. With features like voice interaction through text-to-speech and speech-to-text, users can interact with Samantha without relying solely on visual interfaces. This inclusive design ensures that AI technology is available to everyone, regardless of their abilities.

- **Extensive Model Selection**: With access to [thousands](https://huggingface.co/models?sort=trending&search=gguf) of open-source models, users can experiment with various AI capabilities, each tailored to different tasks and applications.

- **Customizable Parameters**: Users have full control over model hyperparameters such as temperature, top-k, top-p, and max_tokens, allowing for fine-tuned responses that suit specific requirements.

- **Interactive Experience**: Samantha's chaining functionality enables users to generate endless texts by chaining prompts and models, facilitating complex interactions between different AI systems without human intervention.

- **Learning Insights**: A feature called 'Learning mode' lets users observe the model's decision-making process, providing insights into how it selects output tokens based on their probability scores (logits).

- **Voice Interaction**: Samantha supports offline text-to-speech with SAPI5 voices and speech-to-text with [Vosk](https://alphacephei.com/vosk/), making it accessible and user-friendly for everyone.

- **Document Handling**: The system can load small PDF and TXT files, and instructions can be inputted or loaded via a TXT file for convenience.

- **Versatile Text Input**: Four fields for prompt insertion allow users to interact with the system effectively, including system prompt, previous response, user prompt, and initial text to guide the model's response.

- **Code Integration**: Automatic extraction of code blocks from responses, along with pre-installed [JupyterLab](https://jupyter.org/), enables users to execute generated code swiftly for immediate results.

- **Data Analysis Tools**: A suite of data analysis tools like [Pandas](https://pandas.pydata.org/), [Numpy](https://numpy.org/), [Seaborn](https://seaborn.pydata.org/), [Vega-Altair](https://altair-viz.github.io/), [Plotly](https://plotly.com/python/), [Dash](https://plotly.com/examples/), [Sweetviz](https://pypi.org/project/sweetviz/), [D-Tale](https://github.com/man-group/dtale), [NetworkX](https://networkx.org/), [Pyvis](https://pyvis.readthedocs.io/en/latest/index.html), [PyMuPDF](https://pypi.org/project/PyMuPDF/)  and [Beautiful Soup](https://beautiful-soup-4.readthedocs.io/en/latest/) are available within JupyterLab for comprehensive analysis and visualization.

- **Performance Optimized**: To ensure smooth performance on CPUs, Samantha maintains a limited chat history to the previous response only.

**Our Vision:**
Samantha is more than just an AI interface; it's a movement towards a future where artificial intelligence is not a privilege but a tool for all. We envision a world where individuals can leverage AI to enhance their productivity, creativity, and decision-making without barriers. Join us in this journey to democratize AI and make it a force for good in our daily lives.

**Use Responsibly:**
As we embrace the power of these models, let's remember that the generated text reflects the content, biases, and errors present in their training datasets. We encourage responsible use of Samantha for insights only, always keeping ethical considerations at the forefront of our interactions with AI.

Users should be aware that the responses generated by AI are derived from the training of its large language models on a vast corpus of text data. The exact sources or processes used by the AI to generate its outputs cannot be precisely cited or identified. The content produced by the AI is not a direct quotation or compilation from specific sources. Instead, it reflects the patterns, statistical relationships, and knowledge that the AI's neural networks have learned and encoded during the training process on the broad data corpus. The responses are generated based on this learned knowledge representation, rather than being retrieved verbatim from any particular source material. While the AI's training data may have included authoritative sources, its outputs are its own synthesized expressions of the learned associations and concepts.

**Objective:**
The primary objective with Samantha is to inspire and empower others to create similar systems and to educate users on the utilization of AI. Our goal is to foster a community of developers and enthusiasts who can take the knowledge and tools used in Samantha to further innovate and contribute to the field of open source AI. By doing so, we aim to cultivate a culture of collaboration and sharing, ensuring that the benefits of AI are accessible to all, regardless of their technical background or financial resources. We believe that by enabling more people to build and understand AI applications, we can collectively drive progress and address societal challenges with informed and diverse perspectives. Let's work together to shape a future where AI is a positive transformative force for humanity.

🙏 **Special Thanks** to Georgi Gerganov and the whole team working on [llama.cpp](https://github.com/ggerganov/llama.cpp) for making all of this possible.

<br><br>

# 🛠️ Installing and Running Samantha

To use Samantha IA you will need:
<br><br>
* Install [Visual Studio](https://visualstudio.microsoft.com/pt-br/vs/community/) (free community version) on your computer. Download it, run it, and select only the option **Desktop development with C++** (administrator privileges required):

  ![cmake](https://github.com/controlecidadao/samantha_ia/blob/main/images/cmake2.png)
<br><br>
* Download the zip file from the repository by clicking [here](https://github.com/controlecidadao/samantha_ia/archive/refs/heads/main.zip) and unzip it to your computer:

   ![directory](https://github.com/controlecidadao/samantha_ia/blob/main/images/directory.png)
<br><br>
* Double click on `install_samantha_ia.bat` file to start installation (Windows may [ask](https://i.stack.imgur.com/wa3KQ.png) you to confirm the origin of the file. Click on 'More info' and confirm):

   ![directory](https://github.com/controlecidadao/samantha_ia/blob/main/images/install.png)<br><br>

  >_This is the critical part of the installation. If everything goes well, the process will complete without displaying error messages in the terminal._<br>
  >_However, during the tests the causes of error identified were:_<br>
  >_a) lack of prior installation of Visual Studio (resolved with installation)_<br>
  >_b) blocking Playwright browser downloads due to corporate internet access restrictions (resolved by using the internet at home or on a cell phone)_

<br>

* Once installed, open Samantha by double clicking on `open_samantha.bat` file (Windows may [ask](https://i.stack.imgur.com/wa3KQ.png) you to confirm the origin of the file. Click on 'More info' and confirm):<br>

  ![directory](https://github.com/controlecidadao/samantha_ia/blob/main/images/open_samantha.png)<br><br>

<br>

# ⬇️ Downloading Large Language Models (LLM)

Samantha needs 1 file to generate texts:
* AI Model file (.gguf)
<!--* Prompt template file (.txt)-->
<br>

### Downloading Open Source Model Files (.gguf)

Open souce model files can be downloaded from the [Hugging Face's model search engine](https://huggingface.co/models?sort=trending&search=gguf), using `gguf` as the search parameter.

You can also go to a specific repository and see all the `gguf` models available for downloading and testing, like [TheBloke](https://huggingface.co/TheBloke) repository.
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

We suggest to download the model with **Q4_K_M** (4-bit quantization) in its name (put the mouse over the download button to view the complete file name). As a rule, the larger the model size, the greater the accuracy of the generated texts:
<br><br>

  ![ram](https://github.com/controlecidadao/samantha_ia/blob/main/images/ram.png)

<br>

If the downloaded model doesn't fit into the available RAM space, your hard drive will be used, impacting performance.

Download the chosen model and save it to your computer.
<br><br>

<!--
### Creating Model Prompt Template File (.txt)

After downloading the model, you must create a `.txt` file with the **same name** as the model and save it in the **same directory**.

Example:<br><br>
Model file name:&emsp;&emsp;&emsp;&emsp;&nbsp;&nbsp; `WizardLM-2-7B.Q4_K_M.gguf`<br>
Prompt template file name: `WizardLM-2-7B.Q4_K_M.txt`

To create an empty `.txt` file, right-click on a blank area within the directory and select the **New** > **Text Document** options. Now, right-click on the `.txt` file and rename it with the same name as the model.

Finally, locate the model-specific prompt template and paste it inside the `.txt` file. This prompt template is usually on the model page.<br><br>

>_This is a critical part of the initial settings. If you use the wrong prompt template, model will not generate text correctlly._<br>

<br>Here are some prompt template examples. Texts in curly braces `{system_prompt}` and `{prompt}` must be included by the user:<br><br>
Prompt template: **ChatML**
```
<|im_start|>system
{system_prompt}<|im_end|>
<|im_start|>user
{prompt}<|im_end|>
<|im_start|>assistant
```

Prompt template: **Orca-Vicuna**
```
SYSTEM: {system_message}
USER: {prompt}
ASSISTANT:
```

Prompt template: **Alpaca**
```
Below is an instruction that describes a task. Write a response that appropriately completes the request.

### Instruction:
{prompt}

### Response:
```

Prompt template: **Zephyr**
```
<|system|>
{system_prompt}</s>
<|user|>
{prompt}</s>
<|assistant|>
```

Prompt template: **Llama-2-Chat**
```
[INST] <<SYS>>
{system_prompt}
<</SYS>>
{prompt} [/INST]
```

Prompt template: **Llama-3**
```
<|begin_of_text|><|start_header_id|>system<|end_header_id|>

{system_prompt}<|eot_id|><|start_header_id|>user<|end_header_id|>

{prompt}<|eot_id|><|start_header_id|>assistant<|end_header_id|>
```

Prompt template: **Instruction-Input-Response**
```
### Instruction:
{system_prompt}

### Input:
{prompt}

### Response:
```

Prompt template: **Mistral**
```
[INST] {prompt} [/INST]
```

Prompt template: **Microsoft Phi-3**
```
<|user|>
{prompt}<|end|>
<|assistant|>
```

Prompt template: **Unknown**
```
{prompt}
```

For each `.gguf` file downloaded, a new `.txt` file must be created.
<br><br>
-->

### Your First Models

* [PrunaAI/Phi-3-mini-128k-instruct-GGUF-Imatrix-smashed](https://huggingface.co/PrunaAI/Phi-3-mini-128k-instruct-GGUF-Imatrix-smashed/tree/main) (**3.8 billion** parameters model from Microsoft, fine-tunned by PrunaAI)

* [TheBloke/CapybaraHermes-2.5-Mistral-7B-GGUF](https://huggingface.co/TheBloke/CapybaraHermes-2.5-Mistral-7B-GGUF) ( **7 billion** parameters model from Mistral)

* [MaziyarPanahi/WizardLM-2-7B-GGUF](https://huggingface.co/MaziyarPanahi/WizardLM-2-7B-GGUF) (**7 billion** parameters model from Microsoft)

* [lmstudio-community/Meta-Llama-3-8B-Instruct-GGUF](https://huggingface.co/lmstudio-community/Meta-Llama-3-8B-Instruct-GGUF) (**8 billion** parameters model from Meta)

<br><br>
# 🧠 Using Samantha

To start running Samantha IA:

* Double click on `open_samantha_ia.bat` file (Windows may ask you to confirm the origin of the file) and wait a few seconds:

   ![run](https://github.com/controlecidadao/samantha_ia/blob/main/images/run.png)

  A terminal window will open. This is the **server-side** of Samantha IA.

  After answering the questions, Samantha IA will open in a new browser tab. This is the **browser-side**.

<br><br>
# 📝 Future Improvements

As an experimental project, Samantha has points to be improved:

* Create an isolated virtual environment for use with Jupyterlab to allow the installation of other Python libraries and avoid conflicts with the libraries used by Samantha;

* Try other offline speech-to-text libraries with better accuracy;

<br><br><br><br>

https://github.com/matiassingers/awesome-readme?tab=readme-ov-file#Examples
