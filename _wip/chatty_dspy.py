# %%
from dotenv import load_dotenv
load_dotenv()

def calculator(formula: str):
    "A calculator that will evaluate any basic python arithmetic, one-liner"
    return eval(formula)

chat = Chat(
    model = 'claude-sonnet-4-20250514',
    sp="You are a helpful assistant",
    hist=[
        "My name is Max",
        "I don't like that name"
    ],
    tools = calculator
)
chat('What :O ?')
# Prediction ...
# %%
# this is stateful and well come in the chat history afte 4 previous messages, when it run input and output added to history
chat('what is 2 + 10')
# Prediction ...

# %%
import dspy
from attachments.dspy import Attachments
from typing import List, Optional

# This signature is designed to be stateless.
class ChatSignature(dspy.Signature):
    __doc__ = "System prompt goes here"
    # in
    prompt = dspy.InputField()
    user_attachments: Optional[Attachments] = dspy.InputField()
    tools: Optional[List[function]] = dspy.InputField()
    history: Optional[List[str]] = dspy.InputField()
    not_trained_system_prompts: Optional[str] = dspy.InputField()
    # out
    assistants_reply: str = dspy.OutputField()


# %%
ChatSignature

# %%
completions = adapter(lm, lm_kwargs=config, signature=signature, demos=demos, inputs=kwargs)

ChatSignature(user_prompt = "hello")
# %%

chat = dspy.Predict(ChatSignature)

#example
response1 = chat(
    user_prompt = "Hello",
).assistants_reply

# second turn

response2 = chat(
    user_prompt = "Hello",
    history = dspy.History([{response1.assistants_reply])
).assistants_reply



#maybe but there is something between this and dspy
# %%
# Creating a chat object with a system prompt and a history
mychat = chat(
    system_prompt = "You are a helpful assistant",
    history = ["hello, my name is max","hello max my name is AI"]
)

# %%
# Creating a chat object with a system prompt and a history
mychat = chat(
    system_prompt = "You are a helpful assistant",
    history = ["hello, my name is max","hello max my name is AI"]
)
# mychat will be stateful so:
mychat("nice to meet you")
# would return itself, but would print prominently the ai reply and
# if called by something looking for a string it would return the ai response
# and the mychat[ ] would work as a list of messages, odd (user), even assistant.
# mychat.full_history would have the message json full object
# mychat[0] = rewrite the first message
# mychat.system_prompt rewrite the sys_prompt
# mychat.run() checks if anythin has changed since last run (system_prompt or a message) and intelligently rerun the assistant's parts
# mychat.copy() duplicates it and 'deconnect' completely.
# mychat.branch() branches off so a change to original mychat earlier on changes that too.
# mychat.tools.append() adds tools




# %%
from fastcore import *
adapter = dspy.Adapter
print(adapter)
# %%
class VanillaAdatper(dspy.Adapter):


# %%
class PrettyAdatper(dspy.Adapter):
    def __repr__(self):
        cls_name = self.__class__.__name__
        names = [x for x in dir(self) if not (x.startswith('__') and x.endswith('__'))]
        tagged = []
        for name in names:
            value = getattr(self, name)
            if callable(value):
                tagged.append(f"{name} (method)")
            else:
                tagged.append(f"{name} (attribute: {value!r})")
        return f"<{cls_name}: " + ", ".join(tagged) + ">"

PrettyAdatper()



# %%
tst
lambda a: a + 2

# %%

class MyClass:
    a=1
    def add2(self):
        return self.a + 1

tst = MyClass()
tst.a = 10
tst.add2()
tst
# %%
class MyClassy:
    a = 1
    def add2(self):
        return self.a + 1
    def __repr__(self):
        cls_name = self.__class__.__name__
        names = [x for x in dir(self) if not (x.startswith('__') and x.endswith('__'))]
        tagged = []
        for name in names:
            value = getattr(self, name)
            if callable(value):
                tagged.append(f"{name} (method)")
            else:
                tagged.append(f"{name} (attribute: {value!r})")
        return f"<{cls_name}: " + ", ".join(tagged) + ">"

tst = MyClassy()
tst.a = 10
print(tst)
# %%
import inspect, textwrap, ast

def _auto_repr(self):
    """A friendly, readable __repr__ for your objects."""
    cls_name = self.__class__.__name__

    def _is_not_implemented(func):
        try:
            src = textwrap.dedent(inspect.getsource(func)).strip()
        except (OSError, TypeError):
            return False
        if src in {"pass", "..."} or "NotImplemented" in src:
            return True
        try:
            tree = ast.parse(src)
            body = tree.body[0].body
            return len(body) == 1 and isinstance(body[0], ast.Pass)
        except Exception:
            return False

    names = [n for n in dir(self) if not (n.startswith('__') and n.endswith('__'))]

    pub_attrs, priv_attrs, pub_meths, priv_meths = [], [], [], []

    for name in names:
        obj = getattr(self, name)
        if callable(obj):
            tag = name + "()"
            if _is_not_implemented(obj):
                tag += "  # Not implemented"
            (pub_meths if not name.startswith('_') else priv_meths).append(tag)
        else:
            tag = f"{name}={obj!r}"
            (pub_attrs if not name.startswith('_') else priv_attrs).append(tag)

    # Helper for section formatting
    def block(title, items):
        if not items:
            return ""
        return f"{title}:\n  " + "\n  ".join(items)

    # Build the card, showing only non-empty sections
    sections = [
        block("Public attributes", pub_attrs),
        block("Private attributes", priv_attrs),
        block("Public methods", pub_meths),
        block("Private methods", priv_meths),
    ]
    shown = "\n\n".join(s for s in sections if s)

    return f"<{cls_name}>\n{shown}" if shown else f"<{cls_name}>"

# ---------------------------------------------------------------------------
# OPTION 1 ── Mix‑in (inherit explicitly)
# ---------------------------------------------------------------------------
class AutoReprMixin:
    __repr__ = _auto_repr


class Adapter2(dspy.Adapter, AutoReprMixin):
    ...

Adapter2()
# %%
help(Adapter2)
