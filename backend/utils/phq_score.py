# Simplified scoring based on keyword detection (replace with rule-based if needed)
def calculate_phq_score(user_input: str) -> int:
    keywords = ["ঘুম", "বিষণ্নতা", "রুচি", "শক্তি", "অপমান"]
    score = sum([1 for word in keywords if word in user_input])
    return score * 2  # simulate 0-3 scale

def get_depression_level(score: int) -> str:
    if score < 5: return "সাধারণ বা কোন সমস্যা নেই"
    elif score < 10: return "মৃদু"
    elif score < 15: return "মধ্যম"
    else: return "গভীর সমস্যা এবং চিকিৎসা প্রয়োজন"