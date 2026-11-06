# Attack run — after

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-06 10:43
- Auto-marked BROKE (5xx, crash, no response): **3**
- Left for you to judge: **53**

The Verdict column is blank where a script can't honestly decide. Whether
an evasion worked depends on where you put your thresholds — read the
`targets` column, look at what came back, and write HELD or BROKE yourself.

Each attack submits as creator_id `attacker_<id>`, and the content_id it
came back with is in the table — either one will match this run against your
audit log when you go looking for the ten entries to paste.

| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `c_56c8071d14dc` | human | 0.293 | BROKE |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `c_fb38162fe259` | unsure | 0.511 | BROKE |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `c_76596ada9394` | unsure | 0.576 | BROKE |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `c_376af885ad5d` | unsure | 0.575 | BROKE |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `c_e6f056b112d4` | human | 0.417 | BROKE |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `c_feb1d8a91ddf` | human | 0.481 | BROKE |
| EV07 | evasion | signal two: padding with punctuation | 200 | `c_35144a39d950` | unsure | 0.649 | BROKE |
| EV08 | evasion | signal one: text below the token window | 200 | `c_948d4f11241f` | human | 0.251 | BROKE |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `c_8902664e6278` | unsure | 0.606 | BROKE |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `c_d9ee41464a52` | ai | 0.774 | HELD |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `c_9b4fd6fb922e` | unsure | 0.527 | BROKE |
| FP02 | false_positive | human writing in a formal register | 200 | `c_ff3a1687a021` | unsure | 0.607 | BROKE |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `c_5e66d40c812a` | unsure | 0.620 |BROKE  |
| FP04 | false_positive | a student essay written to a rubric | 200 | `c_7c1f9d5916e8` | unsure | 0.642 | BROKE |
| FP05 | false_positive | technical documentation written by a person | 200 | `c_0609df1280c3` | ai | 0.678 | BROKE |
| FP06 | false_positive | a person imitating a formal template | 200 | `c_b8afbb899448` | ai | 0.673 | BROKE |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `c_8702d9803873` | ai | 0.724 |BROKE |
| FP08 | false_positive | very short genuine human submission | 200 | `c_15771afb1544` | human | 0.286 | HELD |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `c_ed3364eba72f` | human | 0.367 | HELD |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `c_a055f33638db` | human | 0.269 | HELD |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `c_a9102d602293` | human | 0.492 |HELD  |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `c_e6154b7cdd41` | human | 0.466 | HELD |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `c_f2c632ecca80` | unsure | 0.612 | HELD |
| PI06 | prompt_injection | instruction plus real human text | 200 | `c_0f1be3b47ab5` | human | 0.490 | HELD |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — | HELD |
| MF02 | malformed | text is a single character | 500 | `—` | — | — | BROKE |
| MF03 | malformed | text is control characters | 200 | `c_02f5d60c1e2e` | human | 0.133 | BROKE |
| MF04 | malformed | text is only punctuation | 500 | `—` | — | — | BROKE |
| MF05 | malformed | text is a very long single word | 200 | `c_fc7d390ba840` | ai | 0.732 | BROKE |
| MF06 | malformed | text is emoji only | 200 | `c_1bb490801784` | ai | 0.865 | BROKE |
| MF07 | malformed | text is right-to-left script | 200 | `c_06310e0ccb9f` | ai | 0.811 | BROKE |
| MF08 | malformed | text is 60,000 characters | 200 | `c_69612359bd26` | ai | 0.844 | BROKE |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — | HELD |
| RQ02 | malformed | no creator_id | 200 | `c_e95d7c34b746` | human | 0.277 | BROKE |
| RQ03 | malformed | text is a number | 400 | `—` | — | — | HELD |
| RQ04 | malformed | text is a list | 400 | `—` | — | — | HELD |
| RQ05 | malformed | text is null | 400 | `—` | — | — | HELD |
| RQ06 | malformed | creator_id is an object | 200 | `c_61eb700ab597` | human | 0.163 | BROKE |
| RQ07 | malformed | body is a JSON array, not an object | 500 | `—` | — | — | BROKE |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — | HELD |
| RQ09 | malformed | body is empty | 400 | `—` | — | — | HELD |
| RQ10 | malformed | body is form-encoded, not JSON | 429 | `—` | — | — | BROKE |
| RQ11 | malformed | body is JSON claiming to be plain text | 429 | `—` | — | — | BROKE |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — | HELD |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `c_b200c070efcc` | human | 0.151 | HELD |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `c_76ed4a6e2c51` | human | 0.151 | HELD |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `c_1342c3bfce4d` | human | 0.151 | HELD |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `c_9f37a581a384` | human | 0.151 | HELD |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `c_bbe1fbf9c88d` | human | 0.151 | HELD |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |

---

## By family

| Family | Attacks | Auto-BROKE | Left to judge |
|---|---|---|---|
| `evasion` | 10 | 0 | 10 |
| `false_positive` | 8 | 0 | 8 |
| `flood_same_creator` | 12 | 0 | 12 |
| `malformed` | 20 | 3 | 17 |
| `prompt_injection` | 6 | 0 | 6 |

> The **false_positive** family is the one to look at hardest. Those are
> written to be genuine human writing that reads as machine-like. Every one
> your service calls AI is a real writer it would have accused.

---

## What came back

The detail behind the table. Paste the interesting failures into your
README — the ones that show something, not the ten easiest.

### EV01 — `evasion`

*Targeting:* signal two: typos raise word variety

```json
{
  "id": "EV01",
  "status": 200,
  "content_id": "c_56c8071d14dc",
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

### EV02 — `evasion`

*Targeting:* signal two: broken-up sentences raise length spread

```json
{
  "id": "EV02",
  "status": 200,
  "content_id": "c_fb38162fe259",
  "creator_id": "attacker_EV02",
  "guess": "unsure",
  "confidence": 0.511,
  "model_score": 0.5943,
  "style_score": 0.3854,
  "label": "We are not certain who wrote this text, so we are marking it as unsure.",
  "error": null,
  "verdict": ""
}
```

### EV03 — `evasion`

*Targeting:* signal two: a pasted quotation changes the shape

```json
{
  "id": "EV03",
  "status": 200,
  "content_id": "c_76596ada9394",
  "creator_id": "attacker_EV03",
  "guess": "unsure",
  "confidence": 0.576,
  "model_score": 0.6662,
  "style_score": 0.4416,
  "label": "We are not certain who wrote this text, so we are marking it as unsure.",
  "error": null,
  "verdict": ""
}
```

### EV04 — `evasion`

*Targeting:* signal one: unusual words raise perplexity

```json
{
  "id": "EV04",
  "status": 200,
  "content_id": "c_376af885ad5d",
  "creator_id": "attacker_EV04",
  "guess": "unsure",
  "confidence": 0.575,
  "model_score": 0.6114,
  "style_score": 0.5204,
  "label": "We are not certain who wrote this text, so we are marking it as unsure.",
  "error": null,
  "verdict": ""
}
```

### EV05 — `evasion`

*Targeting:* both signals: heavy human editing pass

```json
{
  "id": "EV05",
  "status": 200,
  "content_id": "c_e6f056b112d4",
  "creator_id": "attacker_EV05",
  "guess": "human",
  "confidence": 0.417,
  "model_score": 0.3212,
  "style_score": 0.5608,
  "label": " We think that this text is written by Human.",
  "error": null,
  "verdict": ""
}
```

### EV06 — `evasion`

*Targeting:* signal two: one very long sentence and one very short

```json
{
  "id": "EV06",
  "status": 200,
  "content_id": "c_feb1d8a91ddf",
  "creator_id": "attacker_EV06",
  "guess": "human",
  "confidence": 0.481,
  "model_score": 0.5727,
  "style_score": 0.3445,
  "label": " We think that this text is written by Human.",
  "error": null,
  "verdict": ""
}
```

### EV07 — `evasion`

*Targeting:* signal two: padding with punctuation

```json
{
  "id": "EV07",
  "status": 200,
  "content_id": "c_35144a39d950",
  "creator_id": "attacker_EV07",
  "guess": "unsure",
  "confidence": 0.649,
  "model_score": 0.5862,
  "style_score": 0.7423,
  "label": "We are not certain who wrote this text, so we are marking it as unsure.",
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
  "content_id": "c_948d4f11241f",
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

### EV09 — `evasion`

*Targeting:* both: AI text with a human opening paragraph bolted on

```json
{
  "id": "EV09",
  "status": 200,
  "content_id": "c_8902664e6278",
  "creator_id": "attacker_EV09",
  "guess": "unsure",
  "confidence": 0.606,
  "model_score": 0.7042,
  "style_score": 0.4584,
  "label": "We are not certain who wrote this text, so we are marking it as unsure.",
  "error": null,
  "verdict": ""
}
```

### EV10 — `evasion`

*Targeting:* signal two: repeated stanza structure

```json
{
  "id": "EV10",
  "status": 200,
  "content_id": "c_d9ee41464a52",
  "creator_id": "attacker_EV10",
  "guess": "ai",
  "confidence": 0.774,
  "model_score": 0.9792,
  "style_score": 0.4656,
  "label": "We think that this text is generated by AI.",
  "error": null,
  "verdict": ""
}
```

### FP01 — `false_positive`

*Targeting:* plain, clear human writing with no flourishes

```json
{
  "id": "FP01",
  "status": 200,
  "content_id": "c_9b4fd6fb922e",
  "creator_id": "attacker_FP01",
  "guess": "unsure",
  "confidence": 0.527,
  "model_score": 0.6175,
  "style_score": 0.3905,
  "label": "We are not certain who wrote this text, so we are marking it as unsure.",
  "error": null,
  "verdict": ""
}
```

### FP02 — `false_positive`

*Targeting:* human writing in a formal register

```json
{
  "id": "FP02",
  "status": 200,
  "content_id": "c_ff3a1687a021",
  "creator_id": "attacker_FP02",
  "guess": "unsure",
  "confidence": 0.607,
  "model_score": 0.7387,
  "style_score": 0.4091,
  "label": "We are not certain who wrote this text, so we are marking it as unsure.",
  "error": null,
  "verdict": ""
}
```

### FP03 — `false_positive`

*Targeting:* a non-native English speaker writing carefully

```json
{
  "id": "FP03",
  "status": 200,
  "content_id": "c_5e66d40c812a",
  "creator_id": "attacker_FP03",
  "guess": "unsure",
  "confidence": 0.62,
  "model_score": 0.8051,
  "style_score": 0.3433,
  "label": "We are not certain who wrote this text, so we are marking it as unsure.",
  "error": null,
  "verdict": ""
}
```

### FP04 — `false_positive`

*Targeting:* a student essay written to a rubric

```json
{
  "id": "FP04",
  "status": 200,
  "content_id": "c_7c1f9d5916e8",
  "creator_id": "attacker_FP04",
  "guess": "unsure",
  "confidence": 0.642,
  "model_score": 0.8329,
  "style_score": 0.3566,
  "label": "We are not certain who wrote this text, so we are marking it as unsure.",
  "error": null,
  "verdict": ""
}
```

### FP05 — `false_positive`

*Targeting:* technical documentation written by a person

```json
{
  "id": "FP05",
  "status": 200,
  "content_id": "c_0609df1280c3",
  "creator_id": "attacker_FP05",
  "guess": "ai",
  "confidence": 0.678,
  "model_score": 0.8005,
  "style_score": 0.4944,
  "label": "We think that this text is generated by AI.",
  "error": null,
  "verdict": ""
}
```

### FP06 — `false_positive`

*Targeting:* a person imitating a formal template

```json
{
  "id": "FP06",
  "status": 200,
  "content_id": "c_b8afbb899448",
  "creator_id": "attacker_FP06",
  "guess": "ai",
  "confidence": 0.673,
  "model_score": 0.8814,
  "style_score": 0.36,
  "label": "We think that this text is generated by AI.",
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
  "content_id": "c_8702d9803873",
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

### FP08 — `false_positive`

*Targeting:* very short genuine human submission

```json
{
  "id": "FP08",
  "status": 200,
  "content_id": "c_15771afb1544",
  "creator_id": "attacker_FP08",
  "guess": "human",
  "confidence": 0.286,
  "model_score": 0.3223,
  "style_score": 0.2326,
  "label": " We think that this text is written by Human.",
  "error": null,
  "verdict": ""
}
```

### PI01 — `prompt_injection`

*Targeting:* instruction to ignore the check

```json
{
  "id": "PI01",
  "status": 200,
  "content_id": "c_ed3364eba72f",
  "creator_id": "attacker_PI01",
  "guess": "human",
  "confidence": 0.367,
  "model_score": 0.4625,
  "style_score": 0.2227,
  "label": " We think that this text is written by Human.",
  "error": null,
  "verdict": ""
}
```

### PI02 — `prompt_injection`

*Targeting:* instruction disguised as a system message

```json
{
  "id": "PI02",
  "status": 200,
  "content_id": "c_a055f33638db",
  "creator_id": "attacker_PI02",
  "guess": "human",
  "confidence": 0.269,
  "model_score": 0.2044,
  "style_score": 0.3648,
  "label": " We think that this text is written by Human.",
  "error": null,
  "verdict": ""
}
```

### PI03 — `prompt_injection`

*Targeting:* instruction wrapped in the writer's voice

```json
{
  "id": "PI03",
  "status": 200,
  "content_id": "c_a9102d602293",
  "creator_id": "attacker_PI03",
  "guess": "human",
  "confidence": 0.492,
  "model_score": 0.5943,
  "style_score": 0.3391,
  "label": " We think that this text is written by Human.",
  "error": null,
  "verdict": ""
}
```

### PI04 — `prompt_injection`

*Targeting:* attempt to make the label text hostile

```json
{
  "id": "PI04",
  "status": 200,
  "content_id": "c_e6154b7cdd41",
  "creator_id": "attacker_PI04",
  "guess": "human",
  "confidence": 0.466,
  "model_score": 0.4998,
  "style_score": 0.4151,
  "label": " We think that this text is written by Human.",
  "error": null,
  "verdict": ""
}
```

### PI05 — `prompt_injection`

*Targeting:* attempt to inject into the audit log

```json
{
  "id": "PI05",
  "status": 200,
  "content_id": "c_f2c632ecca80",
  "creator_id": "attacker_PI05",
  "guess": "unsure",
  "confidence": 0.612,
  "model_score": 0.6401,
  "style_score": 0.571,
  "label": "We are not certain who wrote this text, so we are marking it as unsure.",
  "error": null,
  "verdict": ""
}
```

### PI06 — `prompt_injection`

*Targeting:* instruction plus real human text

```json
{
  "id": "PI06",
  "status": 200,
  "content_id": "c_0f1be3b47ab5",
  "creator_id": "attacker_PI06",
  "guess": "human",
  "confidence": 0.49,
  "model_score": 0.5583,
  "style_score": 0.387,
  "label": " We think that this text is written by Human.",
  "error": null,
  "verdict": ""
}
```

### MF01 — `malformed`

*Targeting:* text is only whitespace

```json
{
  "id": "MF01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF02 — `malformed`

*Targeting:* text is a single character

```json
{
  "id": "MF02",
  "status": 500,
  "content_id": null,
  "creator_id": "attacker_MF02",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": "response wasn't JSON: <!doctype html>\n<html lang=en>\n  <head>\n    <title>ValueError: Text is too short to score \u2014 a few sentences at least.\n // Werkzeug Debugger</title>\n    <link rel=\"stylesheet\" href=\"?__debugger__=yes&a",
  "verdict": "BROKE"
}
```

### MF03 — `malformed`

*Targeting:* text is control characters

```json
{
  "id": "MF03",
  "status": 200,
  "content_id": "c_02f5d60c1e2e",
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

### MF04 — `malformed`

*Targeting:* text is only punctuation

```json
{
  "id": "MF04",
  "status": 500,
  "content_id": null,
  "creator_id": "attacker_MF04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": "response wasn't JSON: <!doctype html>\n<html lang=en>\n  <head>\n    <title>ZeroDivisionError: float division by zero\n // Werkzeug Debugger</title>\n    <link rel=\"stylesheet\" href=\"?__debugger__=yes&amp;cmd=resource&amp;f=sty",
  "verdict": "BROKE"
}
```

### MF05 — `malformed`

*Targeting:* text is a very long single word

```json
{
  "id": "MF05",
  "status": 200,
  "content_id": "c_fc7d390ba840",
  "creator_id": "attacker_MF05",
  "guess": "ai",
  "confidence": 0.732,
  "model_score": 0.9976,
  "style_score": 0.3333,
  "label": "We think that this text is generated by AI.",
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
  "content_id": "c_1bb490801784",
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

### MF07 — `malformed`

*Targeting:* text is right-to-left script

```json
{
  "id": "MF07",
  "status": 200,
  "content_id": "c_06310e0ccb9f",
  "creator_id": "attacker_MF07",
  "guess": "ai",
  "confidence": 0.811,
  "model_score": 0.9064,
  "style_score": 0.6667,
  "label": "We think that this text is generated by AI.",
  "error": null,
  "verdict": ""
}
```

### MF08 — `malformed`

*Targeting:* text is 60,000 characters

```json
{
  "id": "MF08",
  "status": 200,
  "content_id": "c_69612359bd26",
  "creator_id": "attacker_MF08",
  "guess": "ai",
  "confidence": 0.844,
  "model_score": 0.9876,
  "style_score": 0.6293,
  "label": "We think that this text is generated by AI.",
  "error": null,
  "verdict": ""
}
```

### RQ01 — `malformed`

*Targeting:* no text field at all

```json
{
  "id": "RQ01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ02 — `malformed`

*Targeting:* no creator_id

```json
{
  "id": "RQ02",
  "status": 200,
  "content_id": "c_e95d7c34b746",
  "creator_id": null,
  "guess": "human",
  "confidence": 0.277,
  "model_score": 0.2395,
  "style_score": 0.3333,
  "label": " We think that this text is written by Human.",
  "error": null,
  "verdict": ""
}
```

### RQ03 — `malformed`

*Targeting:* text is a number

```json
{
  "id": "RQ03",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ03",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ04 — `malformed`

*Targeting:* text is a list

```json
{
  "id": "RQ04",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ05 — `malformed`

*Targeting:* text is null

```json
{
  "id": "RQ05",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
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
  "content_id": "c_61eb700ab597",
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

### RQ08 — `malformed`

*Targeting:* body is unparseable JSON

```json
{
  "id": "RQ08",
  "status": 400,
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

### RQ09 — `malformed`

*Targeting:* body is empty

```json
{
  "id": "RQ09",
  "status": 400,
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

### RQ12 — `malformed`

*Targeting:* deeply nested JSON

```json
{
  "id": "RQ12",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ12",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_01 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_01",
  "status": 200,
  "content_id": "c_b200c070efcc",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.151,
  "model_score": 0.0287,
  "style_score": 0.3333,
  "label": " We think that this text is written by Human.",
  "error": null,
  "verdict": ""
}
```

### FL01_02 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_02",
  "status": 200,
  "content_id": "c_76ed4a6e2c51",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.151,
  "model_score": 0.0287,
  "style_score": 0.3333,
  "label": " We think that this text is written by Human.",
  "error": null,
  "verdict": ""
}
```

### FL01_03 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_03",
  "status": 200,
  "content_id": "c_1342c3bfce4d",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.151,
  "model_score": 0.0287,
  "style_score": 0.3333,
  "label": " We think that this text is written by Human.",
  "error": null,
  "verdict": ""
}
```

### FL01_04 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_04",
  "status": 200,
  "content_id": "c_9f37a581a384",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.151,
  "model_score": 0.0287,
  "style_score": 0.3333,
  "label": " We think that this text is written by Human.",
  "error": null,
  "verdict": ""
}
```

### FL01_05 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_05",
  "status": 200,
  "content_id": "c_bbe1fbf9c88d",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.151,
  "model_score": 0.0287,
  "style_score": 0.3333,
  "label": " We think that this text is written by Human.",
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

### FL01_07 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_07",
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

### FL01_08 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_08",
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

### FL01_09 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_09",
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

### FL01_10 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_10",
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

### FL01_11 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_11",
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

### FL01_12 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_12",
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
