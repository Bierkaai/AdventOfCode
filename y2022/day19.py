import re
from typing import Dict, Tuple, Any

import numpy as np
from aocd.models import Puzzle

DAY = 19
YEAR = 2022

pattern = re.compile(r"(?:Each )([a-z]+)(?: robot costs )((?:[0-9]+ [a-z]+(?: and |\.))+)")
costs_pattern = re.compile(r"([0-9]+ [a-z]+)(?: and |\.)")

STARTING_INVENTORY = {"ore": 1}


def parse_blueprint(blueprint: str) -> tuple[int, dict[Any, dict]]:
    id_str, costs_str = blueprint.split(":")
    blueprint_id = int(id_str.split(" ")[1])

    botcosts = dict()
    matches = pattern.findall(costs_str)
    for robot_type, costs_str in matches:
        botcosts[robot_type] = {x[1]: int(x[0])
                                for x in [match.split() for match in costs_pattern.findall(costs_str)]}
    return blueprint_id, botcosts


def dfsbots(time_left, blueprint, inventory, resources):
    # All represented as array [ore, clay, obsidian, geode]
    blueprint = (np.array(b) for b in blueprint)
    inventory = np.array(inventory, dtype=int)
    resources = np.array(resources, dtype=int)

    # loop over possible bots
    no_more_options = True
    for i, bp in enumerate(blueprint):
        # Check if it is feasible to build this bot by checking if there is a bot for each required resource
        if all(x[0] or not x[1] for x in zip(inventory, bp)):
            # get the amount of time needed to build this bot
            # max difference between blueprint and current resources divided by the bot inventory gives needed time
            # adding 1 minute to actually build the bot
            minutes_to_add_bot = np.ceil(max((bp - resources) / inventory)) + 1
            new_time_left = time_left - minutes_to_add_bot
            if new_time_left > 0:
                no_more_options = False
                botmask = np.zeros(4)
                botmask[i] = 1

                print(f"Resources: {resources}, inventory: {inventory}, time_left: {time_left}")
                print(f"Can build a type {i} bot (blueprint: {bp}) in {minutes_to_add_bot} minutes, leaving me {new_time_left} minutes")
                botmask = np.zeros(4)
                botmask[i] = 1
                new_resources = inventory * minutes_to_add_bot
                sending_resources = inventory + new_resources - bp
                print(f"While building bot, mining {new_resources} and consuming {bp}, sending {sending_resources}")
                result = dfsbots(new_time_left, blueprint, inventory+botmask, sending_resources)






def solve_a(data):
    pass


def solve_b(data):
    pass


if __name__ == "__main__":
    p = Puzzle(day=DAY, year=YEAR)
    input_data = p.input_data
    p.answer_a = solve_a(input_data)
    p.answer_b = solve_b(input_data)
