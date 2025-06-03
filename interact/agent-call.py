import dotenv
dotenv.load_dotenv()  # May skip if you have exported environment variables.
from vertexai import agent_engines

agent_engine_id = "6025438069421768704"
user_input = "Double check this: Earth is further away from the Sun than Mars."

print("Connecting to Agent Engine", agent_engine_id)
agent_engine = agent_engines.get(agent_engine_id)
print("Connected to agent engine ", agent_engine.name)
print("Creating a user session ")
session = agent_engine.create_session(user_id="new_user")
print("session created",session)
for event in agent_engine.stream_query(
    user_id=session["userId"], session_id=session["id"], message=user_input
):
    for part in event["content"]["parts"]:
        print(part["text"])