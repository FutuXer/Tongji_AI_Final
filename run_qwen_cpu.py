from transformers import TextStreamer, AutoTokenizer, AutoModelForCausalLM

model_path = "./Qwen-7B-Chat"
prompt = "明明明明明白白白喜欢他，可她就是不说。 这句话里，明明和白白谁喜欢谁？"

tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(model_path, trust_remote_code=True, torch_dtype="auto").eval()

inputs = tokenizer(prompt, return_tensors="pt").input_ids
streamer = TextStreamer(tokenizer)
model.generate(inputs, streamer=streamer, max_new_tokens=300)



