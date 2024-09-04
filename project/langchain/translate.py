import os
import sys

apiKey = "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"
openAiApiKey = "sk-WfT1jLBsFiZO81uTCa09Cc9945Ea458bBf68F8134865F03f"
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = apiKey
os.environ["OPENAI_API_KEY"] = openAiApiKey
os.environ["OPENAI_BASE_URL"] = "https://xiaoai.plus/v1"
from langchain_openai import ChatOpenAI

model = ChatOpenAI(model="gpt-3.5-turbo")

from langchain_core.output_parsers import StrOutputParser
parser = StrOutputParser()

from langchain_core.prompts import ChatPromptTemplate
systemTemplate = "Translate the professional meaning of the term ({text}) into {language} in the computer industry. Please output detail."
promptTemplate = ChatPromptTemplate.from_messages(
    [("system", systemTemplate), ("user", "{text}")]
)

text = "input your word!"
if len(sys.argv) > 1:
    text = sys.argv[1]
print(text)

# 利用提示模板来触发模型
chain = promptTemplate | model | parser
templateOutput = chain.invoke({"language": "Chinese", "text": text})
print(templateOutput)
