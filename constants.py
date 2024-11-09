PROMPTS = [
    "What kind of chart is this?",
    "What are the varibles in this chart?",
    "What is the relationship between the variables in this chart?",
    "What is the trend in this chart?"]

MODEL = "llama3.2-vision"

CSV_FILENAME = "analysis_results.csv"

FIELDNAMES = ['Image ID', PROMPTS[0], PROMPTS[1], PROMPTS[2], PROMPTS[3]]

SYSTEM_PROMPT = "You are an expert in reading graphs and understanding the data from it."
