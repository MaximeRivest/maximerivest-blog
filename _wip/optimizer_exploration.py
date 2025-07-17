# %%
from dspy import *
translator = Predict("french -> english")
translator.set_lm(LM("gpt-4.1"))
translator(french = "Allo")
# %%
translator.set_lm(LM("gemini/gemini-2.5-flash-lite-preview-06-17"))
translator(french = "J'aime les animaux")
# %%
configure(lm = LM("gpt-4.1-nano"))

trainingset = [
    Example(french="Salut", english="Hi").with_inputs("french"),
    Example(french="Je suis dans le champs", english="I am wrong").with_inputs("french"),
    Example(french="L'IA semble utile", english="AI seems useful").with_inputs("french"),
    Example(french="La fleur est rose", english="The flower is pink").with_inputs("french"),
    Example(french="Il était une fois un chat", english="Once upon a time, there was a cat.").with_inputs("french"),
    Example(french="Bonjour, comment ça va?", english="Hello, how are you?").with_inputs("french")
    ]

def translation_judge(example, prediction, trace=None):
    judge = Predict("input_french, groundtruth_english, prediction_english -> prediction_vs_groundtruth_similarity: int")
    judge.set_lm(LM("gpt-4.1-nano"))
    return judge(input_french = example.french, groundtruth_english = example.english, prediction_english = prediction.english).score

optimizer = MIPROv2(metric = translation_judge, auto="light")
translator_opt = optimizer.compile(translator, trainset = trainingset, requires_permission_to_run = False)

translator_opt(french = "J'aime les animaux")
#%%
