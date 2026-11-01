def stock_analysis_prompt(data):
	return "".join(
	   [
		f"analyze thus stock data and tell me if you see any patterns.",
		f"Here is the data: {data}",
		f"Give me your response in numbered bullet points",
	   ]
	)
