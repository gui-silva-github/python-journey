import wikipedia

wikipedia.set_lang('pt')
result = wikipedia.summary("excel")
display(result)