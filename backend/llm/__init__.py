def call_model(model: str, prompt: str) -> str:
    if model == "mistral":
        from .mistral import call_mistral
        return call_mistral(prompt)
    elif model == "gemini":
        from .gemini import call_gemini
        return call_gemini(prompt)
    elif model == "llama":
        from .llama import call_llama
        return call_llama(prompt)
    elif model == "deepseek":
        from .deepseek import call_deepseek
        return call_deepseek(prompt)
    return "Invalid model"
