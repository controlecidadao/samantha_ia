
![v](https://img.shields.io/badge/version-0.1.1-blue) ![v](https://img.shields.io/badge/updated-April%2018,%20%202023-green)

https://github.com/matiassingers/awesome-readme?tab=readme-ov-file#Examples

<br><br>
## 💻 Installing Samantha

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
## 💻 Loading Large Language Models (LLM)

Samantha needs 2 files to work:
* model file (.gguf)
* prompt template file (.txt)

### Downloading Models

Models files can be downloaded from the [Hugguing Face search engine](https://huggingface.co/models?sort=trending&search=gguf), using `gguf` as the search parameter.

You can also go to a specific repository and see all the `gguf` models available for download and testing, like [TheBloke](https://huggingface.co/TheBloke).



<br><br><br><br>
Samantha IA works locally and needs an internet connection only to download models.
