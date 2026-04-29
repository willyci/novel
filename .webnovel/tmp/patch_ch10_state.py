import json
from datetime import datetime

p = r"C:/dev/webnovel/0.01-Degree/.webnovel/state.json"
s = json.load(open(p, encoding="utf-8"))

now = datetime.utcnow().isoformat()

# 1) Fix chapter_meta.0010 double-nesting (inner "0010" wraps the actual meta)
cm = s.setdefault("chapter_meta", {})
ch10 = cm.get("0010", {})
if isinstance(ch10, dict) and set(ch10.keys()) == {"0010"}:
    cm["0010"] = ch10["0010"]

# 2) progress: +2479 words, current_volume=3, volumes_completed contains Vol 2
prog = s["progress"]
prog["total_words"] = int(prog.get("total_words", 0)) + 2479
prog["current_volume"] = 3
vc = prog.setdefault("volumes_completed", [])
if 2 not in vc:
    vc.append(2)
prog["last_updated"] = now
for vp in prog.get("volumes_planned", []):
    if vp.get("volume_id") == 2 or vp.get("volume") == 2:
        vp["status"] = "completed"
    if vp.get("volume_id") == 3 or vp.get("volume") == 3:
        vp["status"] = "in_progress"

# 3) protagonist_state
ps = s["protagonist_state"]
ps["location"]["current"] = "Bunk, residential level, Kuiper Belt Asteroid Base (Sol 68 ~0200, observation port stars in frame)"
ps["location"]["last_chapter"] = 10
ps["power"]["bottleneck"] = (
    "Peter has decoded the cover story: project is the deliberate ablation of humanity by deflecting the "
    "Chicxulub impactor 67M years ago. He has the knowledge, access, and the one skill that could stop "
    "the plan. He has not decided to act. Cache deleted. The unwritten conditional remains the shape of "
    "a thing in the next room."
)
ps["emotional_state"] = "paralysis-under-knowledge: integrated belonging destroyed in private; performing for crew unchanged"

# 4) strand_tracker
st = s.setdefault("strand_tracker", {})
st["last_quest_chapter"] = 10
st["last_constellation_chapter"] = 10
st["current_dominant"] = "quest+constellation"
st["chapters_since_switch"] = 0
hist = st.setdefault("history", [])
hist.append({
    "chapter": 10,
    "strand": "quest+constellation",
    "note": (
        "Quest: catch-side-pass-1 refactor delivered Sol 65; Sol 66 0220 query result returns 67M years/Cretaceous; "
        "trajectory frame inversion identifies Chicxulub impactor as deflection target; 0.01-degree adjustment "
        "recontextualized as the entire point of the code; Sol 68 0140 cache deletion preserves optionality. "
        "Constellation: cover story collapses into actual plan -- Kerr/CTC/Casimir-cradle/Sun2.0/Kepler-7/von Neumann "
        "probe/0.01-degree all bind into ablation-of-humanity architecture; orbital interceptors confirmed nonexistent; "
        "coral fragment recontextualized engine-not-memento; Peter-Kessler mirror becomes monstrous in retrospect. "
        "Vol 2 close."
    )
})

# 5) Foreshadowing updates
fs = s.setdefault("plot_threads", {}).setdefault("foreshadowing", [])

def find(fid):
    for f in fs:
        if f.get("id") == fid:
            return f
    return None

closures = [
    ("F-CH8-PLANT-INTERCEPTORS",
     "Confirmed non-existent. Frame inversion of catch-side-pass-1 trajectory geometry exposes the same vectors as the "
     "Chicxulub impactor pre-impact deflection envelope; the orbital interceptors named by Kessler in Ch8 do not and "
     "never did exist."),
    ("F-CH9-PLANT-EPOCH-CLUSTER",
     "Sol 66 0220: catalogue match returns 67 million years / Cretaceous. The cluster-not-smear was the Chicxulub epoch."),
    ("F-CH9-PLANT-COMPARISON-TOOL-LOADING",
     "Sol 65 night: bar at 100%. Sol 66 0220: result line read three times; reference epoch barycentric center matched "
     "to Chicxulub catalogue; verified via two reruns (inverted-frame-stripped-metadata and naive)."),
]
for fid, payoff in closures:
    ent = find(fid)
    if ent:
        ent["phase"] = "paid_off"
        ent["resolved_chapter"] = 10
        ent["payoff_note"] = payoff
        ent["resolved_at"] = now

ent = find("F-CH9-PLANT-MIRIAM-CORAL")
if ent:
    ent["phase"] = "recontextualized"
    ent["recontextualized_chapter"] = 10
    ent["recontextualization_note"] = (
        "Coral fragment recontextualized: it is the engine of Kessler motivation, not a Miriam memento. Grief is real; "
        "the object signifies grief-into-action. Peter recognition Sol 67 late afternoon Nav Lab. Anchors Vol 3 "
        "moral-weight axis."
    )

carry_notes = [
    ("F-CH8-PLANT-THIRD-THING",
     "Sol 67 afternoon: Peter passes Kessler closed office door, strip of warm light underneath; Kessler is preparing "
     "the third thing. Reveals Ch11.",
     11),
    ("F-CH9-PLANT-PETER-KESSLER-MIRROR",
     "Mirror-recognition (Ch9) becomes monstrous in retrospect; Peter remembers seeing Kessler as a possible future "
     "self for two short sentences and does not finish the thought. Vol 3 climax-decision frame.",
     None),
    ("F-CH9-PLANT-KESSLER-WIFE",
     "Untouched in Ch10.",
     None),
]
for fid, note, ct in carry_notes:
    ent = find(fid)
    if ent:
        ent["carry_note_ch10"] = note
        if ct is not None:
            ent["carry_to"] = ct

new_plants = [
    {
        "id": "F-CH10-PLANT-PETER-PARALYSIS",
        "phase": "plant",
        "set_chapter": 10,
        "carry_to": [11, 12, 13, 14, 15],
        "visibility": "both",
        "note": ("Peter has knowledge, access, and the one skill that could stop the plan. He does not have certainty. "
                 "Not yet. Central Vol 3 question: what will Peter do?"),
    },
    {
        "id": "F-CH10-PLANT-EMPTY-SCREEN-CORNER",
        "phase": "plant",
        "set_chapter": 10,
        "carry_to": [11, 12, 13, 14, 15],
        "visibility": "reader",
        "note": ("Screen corner where the warning flag lived (Ch7-8) and the progress bar lived (Ch9-10) is now blank. "
                 "Motif retired to blank; Vol 3 may revisit if Peter reopens the comparison tool or re-instruments the integrator."),
    },
    {
        "id": "F-CH10-PLANT-OBSERVATION-PORT-STARS",
        "phase": "plant",
        "set_chapter": 10,
        "carry_to": [11, 12, 13, 14, 15],
        "visibility": "reader",
        "note": ("Sol 68 bunk: stars are exactly where they should be -- for now. Sets up Vol 3 Ch15 nothing-changed monitoring beat."),
    },
    {
        "id": "F-CH10-PLANT-INTEGRATION-WINDOW-FACE",
        "phase": "plant",
        "set_chapter": 10,
        "carry_to": [12],
        "visibility": "both",
        "note": ("Peter passed Vasquez Sol 67 integration window without his face changing. Sets up Ch12 code-review "
                 "trust: Vasquez does not yet suspect."),
    },
]

existing_ids = {f.get("id") for f in fs}
for np in new_plants:
    if np["id"] not in existing_ids:
        fs.append(np)

# 6) Open questions carried to Vol 3
oq = s.setdefault("open_questions", [])
def add_oq(q, carry_to):
    if not any(item.get("q") == q for item in oq):
        oq.append({"q": q, "carry_to": carry_to, "set_chapter": 10})
add_oq("What will Peter do?", "Vol3_central_axis")
add_oq("Can he insert anything into the code without Vasquez detecting it?", 12)
add_oq("How much time does he have? (Ch11 reveals D-10)", 11)
add_oq("What is the third thing?", 11)
add_oq("Does Kessler grief make him a monster?", "Vol3_thematic_axis")

# 7) Lexicon unlock event
lex = s.setdefault("lexicon_unlock_events", [])
if not any(e.get("chapter") == 10 and e.get("pov") == "Peter" for e in lex):
    lex.append({
        "chapter": 10,
        "pov": "Peter",
        "unlocked": ["Chicxulub", "Cretaceous", "dinosaurs", "extinct", "67 million years",
                     "sixty-seven million years", "0.01-degree adjustment"],
        "still_locked": ["K-Pg", "K-T"],
        "recorded_at": now,
    })

# 8) world_settings.power_system canonicalization
psw = s.setdefault("world_settings", {}).setdefault("power_system", [])
for i, item in enumerate(psw):
    if "Orbital interceptors" in item:
        psw[i] = "Orbital interceptors (Ch10 reveal: non-existent / cover-story fiction)"
if not any("0.01-degree adjustment" in x for x in psw):
    psw.append("0.01-degree adjustment (Ch10: asteroid-deflection mechanism, the entire point of the code)")

# Save
json.dump(s, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("OK_PATCHED")
print("current_chapter:", s["progress"]["current_chapter"])
print("total_words:", s["progress"]["total_words"])
print("current_volume:", s["progress"]["current_volume"])
print("volumes_completed:", s["progress"]["volumes_completed"])
print("strand current_dominant:", s["strand_tracker"]["current_dominant"])
print("strand last_quest_chapter:", s["strand_tracker"]["last_quest_chapter"])
print("strand last_constellation_chapter:", s["strand_tracker"]["last_constellation_chapter"])
print("protagonist.location.last_chapter:", s["protagonist_state"]["location"]["last_chapter"])
print("protagonist.emotional_state:", s["protagonist_state"]["emotional_state"])
print("chapter_meta[0010] keys:", list(s["chapter_meta"]["0010"].keys()))
print("foreshadowing total:", len(fs))
print("new_plants_added:", [np["id"] for np in new_plants if np["id"] in {f.get("id") for f in fs}])
