import os
from LAI_voice_search_openai_whisper_demo.components.ddg_search_component import Search
from LAI_voice_search_openai_whisper_demo.components.openai_whisper_demo import WhisperSearch


### tests for the web search class
def test_search_function():
    web_crawler = Search()
    keywords = 'capital of India'
    

    computed_answers = web_crawler.search(keywords=keywords, html=False)
    for i in range(len(computed_answers)):
        assert isinstance(computed_answers[i], dict)
        assert set(computed_answers[i].keys()) == set(['title', 'body', 'href'])




### tests for the openai whisper class (audio + search)
def test_whisper_predict_function():
    # note: This test may or may note pass if any other model is used (small/medium etc)
    voice_to_search = WhisperSearch()
    audio_sample_with_precomputed_outputs = [
        {'audio_file_path': '../resources/jackhammer.wav', 'output': 'The still smell of old beer lingers.'},
        {'audio_file_path': '../resources/42_ans_to_everything_english.wav', 'output': 'is 40 to the answer to everything.'},
        {'audio_file_path': '../resources/meaning_of_life.wav', 'output': 'What is the meaning of life?'},
    ]

    for i in range(len(audio_sample_with_precomputed_outputs)):
        text = voice_to_search.predict(audio_sample_with_precomputed_outputs[i]['audio_file_path'])
        assert text == audio_sample_with_precomputed_outputs[i]['output']

