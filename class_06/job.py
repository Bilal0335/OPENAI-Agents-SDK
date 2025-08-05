# from agents import Runner, set_tracing_disabled
# from my_agent.job_agent import job_recommender_agent
# from user_data_type.job_data import Userdata

# set_tracing_disabled(disabled=True)

# # 1. Get user input step-by-step
# print("👋 Welcome to the Job Recommender Assistant")

# # Block until name is entered
# while True:
#     name = input("Enter your name: ").strip()
#     if name:
#         break
#     print("⚠️ Name cannot be empty. Please enter your name.")

# # Other inputs
# age = int(input("Enter your age: "))
# role = input("Enter your role (e.g., Developer, Designer, Student): ")
# skills = input("Enter your skills (comma separated): ")
# experience = int(input("Enter your years of experience: "))

# # 2. Create context
# user = Userdata(
#     name=name,
#     age=age,
#     role=role,
#     skills=skills,
#     experience_years=experience
# )

# # 3. Run agent
# print("\n🤖 Running assistant...\n")
# res = Runner.run_sync(
#     starting_agent=job_recommender_agent,
#     input="Can you suggest a job for me?",
#     context=user
# )

# # 4. Show output
# print(f"👋 Welcome {user.name}!")
# print("Agent says:")
# print(res.final_output)



from agents import Runner, set_tracing_disabled
from my_agent.job_agent import job_recommender_agent
from user_data_type.job_data import Userdata  # Make sure the class name matches

set_tracing_disabled(disabled=True)

print("👋 Welcome to the Job Recommender Assistant")

# Block until name is entered
while True:
    name = input("Enter your name: ").strip()
    if name:
        break
    print("⚠️ Name cannot be empty. Please enter your name.")

# Validate age (must be an integer)
while True:
    age_input = input("Enter your age: ").strip()
    if age_input.isdigit():
        age = int(age_input)
        break
    print("⚠️ Please enter a valid number for age.")

# Role input (not empty)
while True:
    role = input("Enter your role (e.g., Developer, Designer, Student): ").strip()
    if role:
        break
    print("⚠️ Role cannot be empty.")

# Skills input (not empty)
while True:
    skills = input("Enter your skills (comma separated): ").strip()
    if skills:
        break
    print("⚠️ Skills cannot be empty.")

# Validate experience (must be an integer)
while True:
    exp_input = input("Enter your years of experience: ").strip()
    if exp_input.isdigit():
        experience = int(exp_input)
        break
    print("⚠️ Please enter a valid number for experience.")

# 2. Create user context
user = Userdata(
    name=name,
    age=age,
    role=role,
    skills=skills,
    experience_years=experience
)

# 3. Run agent
print("\n🤖 Running assistant...\n")
res = Runner.run_sync(
    starting_agent=job_recommender_agent,
    input="Can you suggest a job for me?",
    context=user
)

# 4. Output
print(f"\n👋 Welcome {user.name}!")
print("Agent says:")
print(res.final_output)
