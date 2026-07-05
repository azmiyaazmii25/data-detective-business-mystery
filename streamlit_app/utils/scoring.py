def get_rank(score):
    if score < 20:
        return "🟤 Rookie Analyst"
    elif score < 50:
        return "🔵 Junior Analyst"
    elif score < 100:
        return "🟢 Senior Analyst"
    elif score < 150:
        return "🟣 Lead Data Detective"
    else:
        return "🟡 Chief Analytics Officer"