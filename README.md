# Speech Search Engine with Whisper


[![LAI](https://bit.ly/3xTcccO)][#app-gallery]

[#app-gallery]: https://01gdsrn3rf7qgev31g8gvea1gh.litng-ai-03.litng.ai/view/home

This app is a simulation of a Voice search feature provided by search engines like Google, DuckDuckGo using OpenAI's [Whisper](https://openai.com/blog/whisper/) model.

This ⚡ [Lightning app](lightning.ai) ⚡ was generated automatically with:

```bash
lightning init app LAI_voice_search_openai_whisper_demo
```

## Sample output
![Sample output](assets\demo_output.PNG)

## To run LAI_voice_search_openai_whisper_demo

First, install LAI_voice_search_openai_whisper_demo (warning: this app has not been officially approved on the lightning gallery):

```bash
lightning install app https://github.com/theUser/LAI_voice_search_openai_whisper_demo
```

Once the app is installed, run it locally with:

```bash
lightning run app LAI_voice_search_openai_whisper_demo/app.py
```



Run it on the [lightning cloud](lightning.ai) with:

```bash
lightning run app LAI_voice_search_openai_whisper_demo/app.py --cloud
```

## to test and link

Run flake to make sure all your styling is consistent (it keeps your team from going insane)

```bash
flake8 .
```

To test, follow the README.md instructions in the tests folder.

## Steps followed to build such a feature in this minimal app

* Obtain the Speech-to-text (transcription) output using Whisper
* Use this transcribed output string as an input for [duckduckgo search](https://github.com/deedy5/duckduckgo_search)
* Once the web search results are obtained, render using HTML

## FAQ

* Why upload audio and not use the microphone like a sane person?
Ans: The original intention was to use the mic but due to a small [bug](https://github.com/gradio-app/gradio/issues/2325) in gradio Audio component, it does not work as expected. The file upload mechanism does work but is temporary, this shall be changed to mic once the gradio bug is resolved.

* Why use DuckDuckGo(DDG) and not Google search?
Ans: Google has a lot of rate limiting applied and frequent searches via code lead to getting blocked resulting in status code: 429 - Too many requests. Apparently DDG does not have super strict rate limiting. 

* Why Lightning.ai ?
Ans: Provisioning the infra and deployment is automated, all one needs to do is focus on business logic. Also HF spaces are too crowded with mutiple such demos.


## TODOs
- [] Update code to accept microphone input as soon as Gradio bug is resolved
- [] Write relevant tests
- [] Add comments and prepare code for submission to Lightning Gallery


