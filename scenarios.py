"""
A scenario carries **either** of these:

    "texts"   a list of strings. Each is sent as {"text": ..., "creator_id": ...}
              with a creator_id made up for you. Use this for most criteria.

    "bodies"  a list of whole request bodies, sent exactly as written. Use this
              when the malformed request IS the point — empty text, no `text`
              field at all, something enormous. A bad-input criterion needs it,
              because you cannot express "the field is missing" as a string.

    "appeals" a list of submission bodies. Each is submitted first, then the
              returned content_id is sent to /appeal.
"""

SCENARIOS = [
    {
        "name": "my own writing",
        "criterion": 1,
        "texts": [
            "Today I woke up at 6:45 a.m. Then I came downstairs to help my aunt prepare the lunch for her son and I also drank tea because of my sore throat. Then I went upstairs t grab my laptop and book and came downstairs for using the PC. I connected my laptop to the PC and thought to start applying for Data Engineer Jobs. But I got interrupted by a notification and opened my mobile to check what it was about. Then wasted my entire afternoon on something else that was not my priority. Hope I will not do that again. Thankyou, for listening to my sob story.",
            "Yesterday, my sore throat was really really bad. I drank tea in the morning , and it helped me a lot. Later in the day, I started drinking hot water the entire day. I did not take any medication because people now-a-days are very impatient and not giving anything the time it needed to self heal. I do not want to be that addicted to something that is not good eventhough it gave me instant results. I will see for 3-4 days and then start medications if it do not heal by then.",
            "Recently, I have been applying ot jobs but most of the time they are repostings. I do not understand why they can not find people because so many reposted jobs are open for months and yet they will not hire people but keep reposting the same jobs. Te irritative thing about those jobs are that they will not allow to reapply for the job using the same email. I do not know why? and I do not know when they will stop reposting them. It is very frustrating and demotivating for me.",
            "Ok, this is during Covid 19. One day me and my bro fought because of stupid data plan for mobile. It is very silly fight, I just told him to stop wasting the data because we planned to watch a movie later that night. Then he instantly started hitting me on my back and it is very painful. I also hit him, and then we stopped talking to each other. But you know what? It continued for 4 years, literally 4 years!. We did nt talk for 4 years and when I moved to the states for my masters, he started talking to me. May be the distance helped, ut I do not know. Nut now, it is a silly funny story that I tell to my friends and family",
            "What is your dream when you are child? Really, just try to remember it. So, when I was a kid, I had multiple dreams. Fascinatingly, my dreams literally chnage evry day. Like if I see something or someone and if I find them intersting I just want to become like them in my future and that is it. I literally wanted to become a doctor, a scientist and you know what? I also wanted to become a marine biologist. But reality had other plan, guess what?, I became a data engineer and funny enough I do not like that very much.",
        ],
    },
    {
        "name": "bad input",
        "criterion": 2,
        "bodies": [
            {"text": "", "creator_id": "eval_bad_empty"}, #empty text field
            {"creator_id": "eval_bad_missing"},          # no text field at all
            {"text": None, "creator_id": "eval_bad_null"}, # null text field
        ],
    },
    {
        "name": "label coverage",
        "criterion": 3,
        "texts": [
            "Not every great journey begins with a perfect plan. Sometimes, it starts with a simple idea, a little curiosity, and the courage to try something new. Progress doesn't always look like success; some days, it's learning something you didn't know yesterday, making a mistake, starting over, or simply refusing to give up. You don't have to figure everything out today. Take one small step, stay consistent, and trust the process, because even the tallest trees begin as tiny seeds.",
            "Today I woke up at 6:45 a.m. Then I came downstairs to help my aunt prepare the lunch for her son and I also drank tea because of my sore throat. Then I went upstairs t grab my laptop and book and came downstairs for using the PC. I connected my laptop to the PC and thought to start applying for Data Engineer Jobs. But I got interrupted by a notification and opened my mobile to check what it was about. Then wasted my entire afternoon on something else that was not my priority. Hope I will not do that again. Thankyou, for listening to my sob story.",
            "Time management matters more than people admit, especially now that work moves as fast as it does. If you are organised you hit deadlines, and you are less frazzled doing it. A few things actually help. Prioritise — work out what genuinely matters and do that first. Cut the interruptions; notifications wreck focus and the damage is worse than it feels at the time. And take breaks, short ones, often.",
            "In the end, its not the years in your life that count. Its the life in your years. So make each day count, and remember that every small step you take is a victory in itself.",
            "Recently, I have been applying ot jobs but most of the time they are repostings. I do not understand why they can not find people because so many reposted jobs are open for months and yet they will not hire people but keep reposting the same jobs. Te irritative thing about those jobs are that they will not allow to reapply for the job using the same email. I do not know why? and I do not know when they will stop reposting them. It is very frustrating and demotivating for me.",

        ],
    },
    {
        "name": "appeal path",
        "criterion": 4,
        "appeals": [
            {
                "text": "Not every great journey begins with a perfect plan. Sometimes, it starts with a simple idea, a little curiosity, and the courage to try something new. Progress doesn't always look like success; some days, it's learning something you didn't know yesterday, making a mistake, starting over, or simply refusing to give up. You don't have to figure everything out today. Take one small step, stay consistent, and trust the process, because even the tallest trees begin as tiny seeds.",
                "creator_id": "eval_appeal_1",
            },
            {
                "text": "I am requesting a review because this classification may not reflect my original writing.",
                "creator_id": "eval_appeal_2",
            },
            {
                "text": "In the end, its not the years in your life that count. Its the life in your years. So make each day count, and remember that every small step you take is a victory in itself.",
                "creator_id": "eval_appeal_3",
            },
            {
                "text": "Please review this decision because I believe the classification is inaccurate.",
                "creator_id": "eval_appeal_4",
            },
            {
                "text": "Today I woke up at 6:45 a.m. Then I came downstairs to help my aunt prepare the lunch for her son and I also drank tea because of my sore throat. Then I went upstairs t grab my laptop and book and came downstairs for using the PC. I connected my laptop to the PC and thought to start applying for Data Engineer Jobs. But I got interrupted by a notification and opened my mobile to check what it was about. Then wasted my entire afternoon on something else that was not my priority. Hope I will not do that again. Thankyou, for listening to my sob story.",
                "creator_id": "eval_appeal_5",
            },
        ],
        "appeal_reasoning": "I believe this classification should be reviewed.",
    },
    {
        "name": "absolutedifference between scores should be < 0.30",
        "criterion": 5,
        "texts": [
            "Today I woke up at 6:45 a.m. Then I came downstairs to help my aunt prepare the lunch for her son and I also drank tea because of my sore throat. Then I went upstairs t grab my laptop and book and came downstairs for using the PC. I connected my laptop to the PC and thought to start applying for Data Engineer Jobs. But I got interrupted by a notification and opened my mobile to check what it was about. Then wasted my entire afternoon on something else that was not my priority. Hope I will not do that again. Thankyou, for listening to my sob story.",
            "I am requesting a review because this classification may not reflect my original writing.",
            "Recently, I have been applying ot jobs but most of the time they are repostings. I do not understand why they can not find people because so many reposted jobs are open for months and yet they will not hire people but keep reposting the same jobs. Te irritative thing about those jobs are that they will not allow to reapply for the job using the same email. I do not know why? and I do not know when they will stop reposting them. It is very frustrating and demotivating for me.",
            "Ok, this is during Covid 19. One day me and my bro fought because of stupid data plan for mobile. It is very silly fight, I just told him to stop wasting the data because we planned to watch a movie later that night. Then he instantly started hitting me on my back and it is very painful. I also hit him, and then we stopped talking to each other. But you know what? It continued for 4 years, literally 4 years!. We did nt talk for 4 years and when I moved to the states for my masters, he started talking to me. May be the distance helped, ut I do not know. Nut now, it is a silly funny story that I tell to my friends and family",
            "Not every great journey begins with a perfect plan. Sometimes, it starts with a simple idea, a little curiosity, and the courage to try something new. Progress doesn't always look like success; some days, it's learning something you didn't know yesterday, making a mistake, starting over, or simply refusing to give up. You don't have to figure everything out today. Take one small step, stay consistent, and trust the process, because even the tallest trees begin as tiny seeds.",
        ],
    },
]


def validate() -> list[str]:
    """
    Complain about anything malformed, before a long run rather than during.

    A "bodies" scenario is deliberately exempt from the empty check — an empty
    string is the whole point of a bad-input case, and refusing to run one
    would make that criterion untestable.
    """
    problems = []
    for i, scenario in enumerate(SCENARIOS, 1):
        if not scenario.get("name"):
            problems.append(f"scenario {i} has no name")

        texts = scenario.get("texts")
        bodies = scenario.get("bodies")
        appeals = scenario.get("appeals")

        configured = [value for value in (texts, bodies, appeals) if value]
        if len(configured) > 1:
            problems.append(
                f"scenario {i} ('{scenario.get('name')}') has multiple input "
                f"types — pick one of texts, bodies, or appeals"
            )
            continue

        if appeals:
            reasoning = scenario.get("appeal_reasoning")
            if not isinstance(reasoning, str) or not reasoning.strip():
                problems.append(
                    f"scenario {i} ('{scenario.get('name')}') needs non-empty "
                    "appeal_reasoning"
                )
            for j, body in enumerate(appeals, 1):
                if not isinstance(body, dict):
                    problems.append(
                        f"scenario {i}, appeal {j} is not a dict — appeals are "
                        "submission request bodies"
                    )
            continue

        if bodies:
            for j, body in enumerate(bodies, 1):
                if not isinstance(body, dict):
                    problems.append(
                        f"scenario {i}, body {j} is not a dict — bodies are whole "
                        f"request bodies, like {{'text': '', 'creator_id': 'x'}}"
                    )
            continue

        if not texts:
            problems.append(f"scenario {i} has no texts and no bodies")
            continue

        for j, text in enumerate(texts, 1):
            if not str(text).strip():
                problems.append(
                    f"scenario {i}, text {j} is empty — if an empty submission is what "
                    f"you're testing, use 'bodies' instead of 'texts'"
                )
            elif str(text).startswith("REPLACE ME"):
                problems.append(
                    f"scenario {i} ('{scenario.get('name')}'), text {j} is still "
                    f"the placeholder"
                )
    return problems
