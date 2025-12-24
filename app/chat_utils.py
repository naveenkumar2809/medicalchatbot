from euriai.langchain import create_chat_model


def get_chat_model(model_name: str = "gpt-4.1-nano", temperature: float = 0.7, api_key: str = None) :

    return create_chat_model(api_key="euri-aef1e2c55f3601e410523a5ae7de67b120e93bf23ff135e0096cfc6063aaf9cd",
            model_name=model_name,
            temperature=temperature)

def ask_chat_model(chat_model, prompt: str):
    response = chat_model.invoke(prompt)
    return response.content