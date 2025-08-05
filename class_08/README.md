# 🔍 `tool_use_behavior` — Detailed Explanation (Roman Urdu + English)

## 🔧 `tool_use_behavior = "run_llm_again"`

### 📖 Roman Urdu:
Is ka matlab hai ke jab AI koi tool use karega (jaise `add(5, 3)`), to tool ka result LLM ko dobara diya jayega — taki wo result ko explain kare, ya context add kare.

### 📘 English:
After the tool is used, the LLM runs again to interpret or explain the result.  
✅ Great when you want the LLM to say things like: **"The answer is 8."**

---

## ⛔ `tool_use_behavior = "stop_on_first_tool"`

### 📖 Roman Urdu:
Yeh keh raha hai: agar koi tool call ho gaya, to usi ka result final hai.  
LLM ko dobara mat chalao. Sirf tool ka output hi user ko dikhao.

### 📘 English:
As soon as a tool is called, that result is returned directly.  
The LLM does **not** get a chance to add explanation.  
✅ Good for fast or simple responses.

---

## 🧠 `tool_use_behavior = ["add", "multiply"]`

### 📖 Roman Urdu:
Agar yeh specific tools (`add`, `multiply`) use ho gaye, to un par LLM ko dobara mat chalao.  
Lekin agar koi aur tool (jaise `explain_math_term`) use hua, to us par LLM chalay.

### 📘 English:
If one of the listed tools is used, then stop there and return the result.  
For other tools not in the list, allow LLM to continue processing.

---
