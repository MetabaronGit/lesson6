# 1 agent - 2 men
# 1 man - 20 min

name = "Zebediah"
agents = 3
names = "Bob Jim Becky Pat Miles Piles kuba"

name = name.lower()
names = names.lower()
name_list = names.split()
name_list.append(name)
name_list.sort()
order = name_list.index(name)
que = dict()
for i in range(1, agents + 1):
    que.setdefault(f"{i}", list())

print(name_list)
print(order)

agent_nr = 1
AGENT_WORK = 2
next_agent = 1
for i in range(1, order + 2):
    que[f"{agent_nr}"].append(name_list.pop(0))
    actual_agent = agent_nr
    next_agent += 1
    if next_agent > AGENT_WORK:
        next_agent = 1
        agent_nr += 1
        if agent_nr > agents:
            agent_nr = 1
print(que)
print(actual_agent)
print(len(que.get(f"{actual_agent}")) * 20)