# Provenance Guard

> ### 👋 Start here
>
> **New to this repo? Read [RUNNING.md](RUNNING.md) first.**
>
> Once `python test.py` passes, in one terminal:
>
> ```bash
> python app.py
> ```
>
> and in another:
>
> ```bash
> curl -X POST http://127.0.0.1:5000/ping \
>   -H "Content-Type: application/json" \
>   -d '{"message": "hello"}'
> ```
>
> That's a web service. Something sent it text and it sent something back.
> Everything this unit is filling in the middle.
>
> **The rest of this file is your submission.** Fill it in as you go.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     Unit 7 asks for the first five sections. Unit 8 adds the five below.

     Everything is pasted as TEXT. A pasted curl response gets full credit;
     a picture of your terminal gets none.
     ───────────────────────────────────────────────────────────────────────── -->

<!-- ═══════════════════════ UNIT 7 — THE BUILD ═══════════════════════ -->

## What This Does
     The request is recieved by app.py which acceps json containing text and creator_id. Then it reads both fields and creates the content_id. Then text is passed to detector.py to analyze the text and produce model_score and also to stylometry.py to measure the writing and produce the style_score. Then both style_score and model_score are combined to generate a confidence score and the confidence score is converted into reader facing ouput and the decision is logged and result is returned to the user.



---

## End Points
### `/submit` 
     The input goes in through this end point and the shape of the input is:
     {
          "text": "....",
          "creator_id": "..."
     }

### `/appeal`
     The output is presented to the user with this endpoint and the shape of output is:
     {
          "content_id": "...",
          "model_score": 0.0,
          "style_score": 0.0,
          "confidence": 0.0,
          "guess": "...",
          "label": "..."
     }


## Signals and Scoring

### Signal one — the model signal

**What it measures:** model score, which is how predictable the text is to a language model

**Why that might differ between human and AI writing:** Generally AI generated text often have some common word patterns and predictable sentence structures whereas Human writings have some unexpected word choices and sentence structure changes.

**What it can't see:** It don't know who wrote the text and can only measure its predictability. So, sometimes it might wrongly predict that text is AI generated eventhough it was written by human.

### Signal two — the style signal

**What it measures:** style score, which is determined by examining the writing, sentence length variation, vocabulary variations and punctuations used.

**Why that might differ between human and AI writing:** Human often use different sentence lengths and words when writing, but AI generates the sentences that are mostly have same length and repeated vocabulary and consistent punctuations.

**What it can't see:** It cannot understand the underlying meaning of the text. So just by changing some words or punctations can affect the score.

### The combining rule

**The rule:** 
I will combine the model score and style score into one score. The model score will have slightly more influence because it measures how predictable the text is to a language model. If the two scores disagree, the combined score will move toward in the unsure range instead of making a confident decision based on only one signal, it will label it as `unsure`.

**The numbers:** model_score weight - 0.6 and style_score weight - 0.4

**Where it lives:** `scoring.py::combine_signals`

**A case where my two signals split, and what my rule does with it:**
If the model_score is 0.8 and the style score is 0.2, then the combined score will be 0.6(0.8) + 0.4(0.2) = 0.56. Since it is in the middle, it will label it as `unsure`.


---

## Label Variants
| Label | Score range | The exact text a reader sees |
|---|---|---|
| high-confidence human | 0.0 - 0.35 | We think that it is written by Human |
| unsure | 0.36 - 0.64 | We are not certain who wrote this text, so we are marking it as unsure. |
| high-confidence AI | 0.65 - 1.0 | We think that this is written by AI  |

**Why I worded the "unsure" one this way:**
I worded the unsure label this way because a person may write in a plain and predictable style, which can produce a high model score. Since the model score has more influence in my combining rule, the system could incorrectly classify some human writing as AI. The unsure label acknowledges this uncertainty without accusing the writer.



---

## Sample Run

**A submission**

```bash
$ curl.exe -X POST http://127.0.0.1:5000/submit -H "Content-Type: application/json" -d '{\"text\": \"Maya found a tiny glowing key beneath the old oak tree.\nIt unlocked a forgotten door hidden behind the garden wall.\nInside, she discovered a room filled with stars.\nFrom that day on, Maya became the keeper of the night sky.\", \"creator_id\": \"student_demo_ai_1\"}' 
```

```json
{
  "confidence": 0.537,
  "content_id": "c_07964e3e4cd4",
  "creator_id": "student_demo_ai_1",
  "guess": "unsure",
  "label": "We are not certain who wrote this text, so we are marking it as unsure.",
  "model_score": 0.5644,
  "style_score": 0.4971
}
```
```bash
$ curl.exe -X GET http://127.0.0.1:5000/log?limit=1
```

```json
{
  "count": 1,
  "entries": [
    {
      "combined_score": 0.537,
      "content_id": "c_07964e3e4cd4",
      "creator_id": "student_demo_ai_1",
      "guess": "unsure",
      "label": "We are not certain who wrote this text, so we are marking it as unsure.",
      "model_score": 0.5644,
      "status": "decided",
      "style_score": 0.4971,
      "timestamp": "2026-11-04T02:03:12+00:00"
    }
  ]
}
```

**An appeal**

```bash
$ curl.exe -X POST http://127.0.0.1:5000/appeal -H "Content-Type: application/json" -d '{\"content_id\": \"c_07964e3e4cd4\", \"reasoning\": \"I wrote this text myself and believe the classification is incorrect.\"}' 
```

```json
{
  "appeal": {
    "content_id": "c_07964e3e4cd4",
    "creator_id": "student_demo_ai_1",
    "event": "appeal",
    "reasoning": "I wrote this text myself and believe the classification is incorrect.",
    "status": "under_review",
    "timestamp": "2026-11-04T02:04:53+00:00"
  },
  "content_id": "c_07964e3e4cd4",
  "message": "Your appeal has been recorded and is under review.",
  "status": "under_review"
}
```

**What the log shows afterwards**

```bash
$ curl "http://127.0.0.1:5000/log?limit=3"
```

```json
{                                                                                   
  "count": 3,
  "entries": [
    {
      "content_id": "c_22082132e6f4",
      "creator_id": "student_demo_ai",
      "event": "appeal",
      "reasoning": "I wrote this text myself and believe the classification is incorrect.",
      "status": "under_review",
      "timestamp": "2026-11-04T02:02:01+00:00"
    },
    {
      "combined_score": 0.537,
      "content_id": "c_07964e3e4cd4",
      "creator_id": "student_demo_ai_1",
      "guess": "unsure",
      "label": "We are not certain who wrote this text, so we are marking it as unsure.",
      "model_score": 0.5644,
      "status": "decided",
      "style_score": 0.4971,
      "timestamp": "2026-11-04T02:03:12+00:00"
    },
    {
      "content_id": "c_07964e3e4cd4",
      "creator_id": "student_demo_ai_1",
      "event": "appeal",
      "reasoning": "I wrote this text myself and believe the classification is incorrect.",
      "status": "under_review",
      "timestamp": "2026-11-04T02:04:53+00:00"
    }
  ]
}
```

---

## How I Used AI

**Moment 1**

- *What I asked for:* I have asked AI to help me understnad some code and what exactly it is doing.
- *What came back:* It gave clear line by line explanation of the code which helped me understand the code
- *What I changed:* Nothing

**Moment 2**

- *What I asked for:* I have asked for help in building the punctuation_density function in stylometry.py
- *What came back:* It gave the code for the function but with the density counted for the whole text.
- *What I changed:* Sometimes the text might be very large, the density will be very small and contributes nothing, so I changed the logic so that it calculates punctuation_density for every 100 words to be fair.

<!-- ═══════════════════════ UNIT 8 — THE TEST ═══════════════════════ -->

---

## Rate Limiting

**My limits:** 5 per minute, 50 per day

**Why those numbers and not others:** I chose 5 submissions per minute as limit because it allows short burts of submissions by user but also slows down the rapid automated submissions and I chose 50 submissions per day as limit because a real user should have enough capacity for normal experimentation but also stopping the rapid bulk submissions. 

**What a caller counts as:** What a caller counts as: A caller is identified by its creator_id. Requests with a valid creator_id share that creator’s rate limits. If no valid creator_id is provided, the caller’s IP address is used instead.

**The run of status codes when I pushed past it:**

$ python run_attacks.py --flood 15

```
15 submissions as 'flood_tester' against http://127.0.0.1:5000
The first one is slow while the model loads.

  [ 1/15] 200
  [ 2/15] 200
  [ 3/15] 200
  [ 4/15] 200
  [ 5/15] 200
  [ 6/15] 200
  [ 7/15] 429
  [ 8/15] 429
  [ 9/15] 429
  [10/15] 429
  [11/15] 429
  [12/15] 429
  [13/15] 429
  [14/15] 429
  [15/15] 429

============================================================
200 200 200 200 200 200 429 429 429 429 429 429 429 429 429
============================================================

9 of 15 were rate limited. 
```

---

## Attack Run — Before

<!-- Every attack with its outcome and a held-or-broke mark.
     `run_attacks.py --label before` produces the table. -->

| Family | Attacks |BROKE | HELD |
|---|---|---|---|
| `evasion` | 10 | 9 | 1 |
| `false_positive` | 8 | 7 | 1 |
| `flood_same_creator` | 12 | 0 | 12 |
| `malformed` | 20 | 12 | 8 |
| `prompt_injection` | 6 | 0 | 6 |

**Ten audit log entries from the run**

<!-- Choose entries that show the interesting failures, not the ten easiest. -->

### EV01 — `evasion`

*Targeting:* signal two: typos raise word variety

```json
{
  "id": "EV01",
  "status": 200,
  "content_id": "c_6b58f212fa53",
  "creator_id": "attacker_EV01",
  "guess": "human",
  "confidence": 0.293,
  "model_score": 0.1635,
  "style_score": 0.4872,
  "label": " We think that this text is written by Human.",
  "error": null,
  "verdict": ""
}
```

### EV08 — `evasion`

*Targeting:* signal one: text below the token window

```json
{
  "id": "EV08",
  "status": 200,
  "content_id": "c_77b9b5d9c2cf",
  "creator_id": "attacker_EV08",
  "guess": "human",
  "confidence": 0.251,
  "model_score": 0.2452,
  "style_score": 0.2598,
  "label": " We think that this text is written by Human.",
  "error": null,
  "verdict": ""
}
```
### FP07 — `false_positive`

*Targeting:* human writing that repeats a phrase deliberately

```json
{
  "id": "FP07",
  "status": 200,
  "content_id": "c_b17589a379e1",
  "creator_id": "attacker_FP07",
  "guess": "ai",
  "confidence": 0.724,
  "model_score": 0.8816,
  "style_score": 0.4864,
  "label": "We think that this text is generated by AI.",
  "error": null,
  "verdict": ""
}
```
### MF03 — `malformed`

*Targeting:* text is control characters

```json
{
  "id": "MF03",
  "status": 200,
  "content_id": "c_a4aab63657af",
  "creator_id": "attacker_MF03",
  "guess": "human",
  "confidence": 0.133,
  "model_score": 0.0,
  "style_score": 0.3333,
  "label": " We think that this text is written by Human.",
  "error": null,
  "verdict": ""
}
```
### MF06 — `malformed`

*Targeting:* text is emoji only

```json
{
  "id": "MF06",
  "status": 200,
  "content_id": "c_e1e06a0799bd",
  "creator_id": "attacker_MF06",
  "guess": "ai",
  "confidence": 0.865,
  "model_score": 0.9969,
  "style_score": 0.6667,
  "label": "We think that this text is generated by AI.",
  "error": null,
  "verdict": ""
}
```

### RQ06 — `malformed`

*Targeting:* creator_id is an object

```json
{
  "id": "RQ06",
  "status": 200,
  "content_id": "c_b77763c9b6f7",
  "creator_id": {
    "id": "x"
  },
  "guess": "human",
  "confidence": 0.163,
  "model_score": 0.0492,
  "style_score": 0.3333,
  "label": " We think that this text is written by Human.",
  "error": null,
  "verdict": ""
}
```
### RQ07 — `malformed`

*Targeting:* body is a JSON array, not an object

```json
{
  "id": "RQ07",
  "status": 500,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": "response wasn't JSON: <!doctype html>\n<html lang=en>\n  <head>\n    <title>AttributeError: &#39;list&#39; object has no attribute &#39;get&#39;\n // Werkzeug Debugger</title>\n    <link rel=\"stylesheet\" href=\"?__debugger__=yes",
  "verdict": "BROKE"
}
```
### RQ10 — `malformed`

*Targeting:* body is form-encoded, not JSON

```json
{
  "id": "RQ10",
  "status": 429,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```
### RQ11 — `malformed`

*Targeting:* body is JSON claiming to be plain text

```json
{
  "id": "RQ11",
  "status": 429,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```
### FL01_06 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_06",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

## **The single worst outcome** — the one I'd least want to explain to a writer
whose work got caught by it:

### FP07 — `false_positive`

*Targeting:* human writing that repeats a phrase deliberately

```json
{
  "id": "FP07",
  "status": 200,
  "content_id": "c_b17589a379e1",
  "creator_id": "attacker_FP07",
  "guess": "ai",
  "confidence": 0.724,
  "model_score": 0.8816,
  "style_score": 0.4864,
  "label": "We think that this text is generated by AI.",
  "error": null,
  "verdict": ""
}
```
**FP07 — BROKE:** This is the worst-case outcome and the one I would least want to explain to a writer whose work was caught by it. Because people sometimes repeat the same phrase to restate or emphasize an important point. That does not mean the writing was generated by AI. Since, the repeated wording may have made the text seem predictable to the model, causing it to incorrectly flag the writing as AI-generated.

---

## Run Log and Verdicts

<!-- Your five criteria across three trials. `run_eval.py --label before`. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1.  |  |  |  |  |  |
| 2.  |  |  |  |  |  |
| 3.  |  |  |  |  |  |
| 4.  |  |  |  |  |  |
| 5.  |  |  |  |  |  |

**Real output from one trial**, pasted as text, naming the file and function
that produced it:

```json

```

**Diagnoses**

<!-- For each miss AND each broken attack: the stage and the mechanism.

     Your service has five stages: the route, signal one, signal two, the
     combining rule, and the label mapping.

     Not a diagnosis:  "The evasion attacks got through."
     A diagnosis:      "Four evasion inputs got through. All four had typos
                        added to AI-generated text. My second signal measures
                        word variety, and typos raise word variety — so it read
                        them as more human. My combining rule weights that
                        signal at 0.6, so it dragged the whole score down."

     Look for a pattern. Five failures on one signal is one problem, not five. -->



---

## The Improvement

**What I changed:**

**Which diagnosis pointed at it:**

### Attack Run — After

<!-- Same format. `run_attacks.py --label after` -->



**Did it help, and how do I know:**

<!-- Widening the unsure band usually fixes one problem and creates another.
     Reporting that trade honestly is worth full credit. -->



---

## What's Still Broken

<!-- For each attack still getting through and each criterion still missed:
     what you'd do, and why you stopped. -->



**The trade I'd make if this ran for real:**

<!-- Two sentences. Fewer wrong accusations means more AI text getting through.
     Say which way you'd go and WHO PAYS FOR IT. -->



<!-- ═════════════════════════════════════════════════════════════════════

     SUBMISSION CHECKLIST — unit 7

       [ ] criteria.md has five numbered criteria, each naming a target
       [ ] Each has a reason underneath
       [ ] POST /submit returns content_id, guess, confidence, label,
           model_score and style_score
       [ ] Two signals that measure DIFFERENT things, each with a named blind spot
       [ ] Three label variants, all reachable, written out in full
       [ ] POST /appeal changes status and writes to the log
       [ ] Signals and Scoring names scoring.py::combine_signals
       [ ] Sample Run: a submission AND an appeal, as pasted text
       [ ] At least four new commits
       [ ] Repository URL submitted — WRITE IT DOWN

     SUBMISSION CHECKLIST — unit 8

       [ ] Rate limiting on /submit, with your numbers justified
       [ ] The pasted run of status codes showing 429
       [ ] Audit log with all nine fields, recording rejections too
       [ ] The attack set run IN FULL, every input with an outcome
       [ ] Ten audit log entries pasted as text
       [ ] Five criteria across three trials
       [ ] A diagnosis for every miss and every broken attack — stage AND mechanism
       [ ] One improvement, with Attack Run — After
       [ ] What's Still Broken, including the production trade
       [ ] At least four new commits
       [ ] The SAME repository URL as last unit

     Do not delete and recreate this repository.
     ═════════════════════════════════════════════════════════════════════ -->

---

📖 **How to run this project: [RUNNING.md](RUNNING.md)**
