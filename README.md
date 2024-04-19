
![v](https://img.shields.io/badge/version-0.1.1-blue) ![v](https://img.shields.io/badge/updated-April%2018,%20%202023-green)

https://github.com/matiassingers/awesome-readme?tab=readme-ov-file#Examples

<br><br>
# 🛠️ Installing Samantha

To use Samantha IA you will need:
<br><br>
* Install [Visual Studio](https://visualstudio.microsoft.com/pt-br/vs/community/) (free community version) on your computer. Download it and select only the option **Desktop development with C++** (administrator privileges required):

  ![cmake](https://github.com/controlecidadao/samantha_ia/blob/main/images/cmake2.png)
<br><br>
* Download the repository zip file clicking [here](https://github.com/controlecidadao/samantha_ia/archive/refs/heads/main.zip) and unpack it on your machine:

   ![directory](https://github.com/controlecidadao/samantha_ia/blob/main/images/directory.png)
<br><br>
* Double click on `install_samantha_ia.bat` to start installation (Windows may ask you to confirm the origin of the file):

   ![directory](https://github.com/controlecidadao/samantha_ia/blob/main/images/install.png)

  >_This is the critical part of the installation. If everything goes well, the process will complete without displaying error messages in the terminal._<br>
  >_However, during the tests the causes of error identified were:_<br>
  >_a) lack of prior installation of Visual Studio (resolved with installation)_<br>
  >_b) blocking Playwright browser downloads due to corporate internet access restrictions (resolved by using the internet at home or on a cell phone)_

<br><br>
# ⬇️ Downloading Large Language Models (LLM)

Samantha needs 2 files to work:
* model file (.gguf)
* prompt template file (.txt)
<br><br>

### Downloading Open Source Models (.gguf File)

Open souce models files can be downloaded from the [Hugging Face's model search engine](https://huggingface.co/models?sort=trending&search=gguf), using `gguf` as the search parameter.

You can also go to a specific repository and see all the `gguf` models available for download and testing, like [TheBloke](https://huggingface.co/TheBloke).

The models are displayed on cards like this:

  ![model_card](https://github.com/controlecidadao/samantha_ia/blob/main/images/model_card.png)

To download the template, click on the card to open the corresponding page. Locate the **Model card** and **Files and versions** tabs:

  ![tabs](https://github.com/controlecidadao/samantha_ia/blob/main/images/tabs.png)

Click on the **Files and versions** tab and download a model that fits in your available RAM space. To check your available memory, open Task Manager by pressing `CTRL + SHIFT + ESC` and click on **Performance** tab.

We suggest the model with **Q4_K_M** (4-bit quantization) in its name (put the mouse over the download button to view the file name).

<br>
As a rule, the larger the model size, the greater the accuracy of the generated texts:
<br><br>

  ![ram](https://github.com/controlecidadao/samantha_ia/blob/main/images/ram.png)

<br>
To check your free RAM, open Task Manager:
<br><br>

![task](https://github.com/controlecidadao/samantha_ia/blob/main/images/task_manager.png)

Download the chosen template and save it to your computer.
<br><br>

### Creating Model Prompt Template (.txt File)

After downloading the model, you must create a `.txt` file with the same name as the model and save it in the **same directory**.

Example:<br><br>
Model file name:&emsp;&emsp;&emsp;&emsp;&nbsp;&nbsp; `WizardLM-2-7B.Q4_K_M.gguf`<br>
Prompt template file name: `WizardLM-2-7B.Q4_K_M.txt`

To create an empty `.txt` file, right-click on a blank area within the directory and select the **New** > **Text Document** options. Now, right-click on the `.txt` file and rename it with the same name as the model.

Finally, locate the model-specific prompt template and paste it inside the `.txt` file. This prompt template is usually on the model page.

>_This is a critical part of the initial settings. If you use the wrong prompt template, model will not generate text correctlly._<br>

Examples:<br><br>
Prompt template: **ChatML**
```
<|im_start|>system
{system_message}<|im_end|>`
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
{system_message}</s>
<|user|>
{prompt}</s>
<|assistant|>
```

Prompt template: **Llama-2-Chat**
```
[INST] <<SYS>>
{system_message}
<</SYS>>
{prompt} [/INST]
```

Prompt template: **Instruction-Input-Response**
```
### Instruction:
{system_message}

### Input:
{prompt}

### Response:
```

Prompt template: **Mistral**
```
[INST] {prompt} [/INST]
```

Prompt template: **Unknown**
```
{prompt}
```

For each `.gguf` file downloaded, a new `.txt` file must be created.
<br><br>

### Your First Models

* [TheBloke/rocket-3B-GGUF](https://huggingface.co/TheBloke/rocket-3B-GGUF)

* [MaziyarPanahi/WizardLM-2-7B-GGUF](https://huggingface.co/MaziyarPanahi/WizardLM-2-7B-GGUF)

<br><br>
# 🧠 Using Samantha

To use Samantha IA you will need:


<br><br><br><br>
Samantha IA works locally and needs an internet connection only to download models.
