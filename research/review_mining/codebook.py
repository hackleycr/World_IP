"""Theme codebook for Steam review text. Each theme is a case-insensitive regex.

Themes are grouped by the design pillar they inform (see docs/design/01-pillars.md).
Matching is lexical: no negation handling ("not grindy" still matches "grind").
Accuracy is measured by hand-coding samples (see validate.py / validation results).
"""
import re

THEMES = {
    # Pillar 1: reward vs. effort
    "grind_repetition": (
        "P1", r"\bgrind\w*|\brepetitive|\brepetition|\btedious|\bchores?\b|\bbusywork|\bpadd(ed|ing)\b"),
    "progress_loss_devaluation": (
        "P1", r"\b(lost|lose|losing|loses|wiped?|reset\w*)\b.{0,25}\b(progress|saves?|items?|gear|"
              r"everything|hours|character|world)\b|\bnerf\w*|\bpower creep|\bsunset\w*|\bwipes?\b"),
    "rng_luck": (
        "P1", r"\brng\b|\bluck\b|\bunlucky|\bgacha|\bloot ?box|\bdrop rates?\b"),
    "monetization": (
        "P1", r"micro ?transactions?|\bmtx\b|pay[ -]?to[ -]?win|\bp2w\b|battle ?pass|cash shop|\bpredatory|"
              r"\boverpriced|\bmonetiz\w*"),
    "rewarding_satisfying": (
        "P1", r"\brewarding|\bsatisf(ying|action)|\bpay-?off|sense of (accomplishment|achievement|progress)"),
    # Pillar 2: world change and permanence
    "permanence_consequence": (
        "P2", r"\bpermadeath|\bpermanent\w*|\bconsequences?\b|\birreversib\w*|save[ -]?scum\w*|\bhardcore\b|"
              r"\bone life\b|\bperma[ -]?death"),
    "destruction_world_change": (
        "P2", r"\bdestr(oy|uct)\w*|\bterraform\w*|\breshap\w*|\bdemolish\w*|\bcollaps\w*|\bdig(ging)?\b"),
    # Pillar 3: discovery and rule understanding
    "discovery_curiosity": (
        "P3", r"\bdiscover\w*|\bcurio(us|sity)|\bmyster(y|ies|ious)|\bexplor\w*|\bsecrets?\b|\baha\b|"
              r"\beureka|\bfigur(e|ed|ing) (it |things |stuff )?out|\bsense of wonder"),
    "learning_curve_opacity": (
        "P3", r"learning curve|\bconfus\w*|\bno tutorial|\bbad tutorial|\bwiki\b|\boverwhelm\w*|\bobtuse|"
              r"\bopaque|\bcryptic|\bunclear|hard to (understand|learn|get into)|\bunintuitive|\bnot explained"),
    "depth_systems": (
        "P3", r"\bdepth\b|\bin-?depth|\bcomplex\w*|\bmechanics\b|\bsystems\b|\bstrateg\w*|\boptimi[sz](e|ing)\b|"
              r"\bmin-?max\w*|\bsynerg\w*"),
    "creativity_building": (
        "P3", r"\bbuild(ing|s)?\b|\bcreat(e|ive|ivity|ions?)\b|\bsandbox|\bfreedom\b|\bautomat\w*|\bfactor(y|ies)|"
              r"\bdesign(ing)? (your|my) own"),
    "emergence_simulation": (
        "P3", r"\bphysics\b|\bsimulat\w*|\bemergen\w*|\binteract(ion|ions|s)?\b|chain reaction|\bchemistry|"
              r"\bsystemic"),
    # Engagement and retention
    "addictive_time_sink": (
        "ENG", r"\baddict\w*|one more (run|turn|day|game)|time sink|can'?t stop|lost track of time|"
               r"\b\d{3,}(,\d{3})?\+? ?(hours|hrs|h)\b"),
    "replayability_variety": (
        "ENG", r"\breplay\w*|every run|each run|\bprocedural\w*|randomly generated|\bvariety\b|"
               r"different every"),
    "content_runs_out": (
        "ENG", r"\bnot enough content|\bnothing to do|\bran out of|\bend ?game\b|\bdead game|\bno updates|"
               r"\babandon\w*|\btoo short|\bshort game"),
    # Context themes
    "difficulty": (
        "CTX", r"\bdifficult\w*|\bchalleng\w*|\bpunishing|\bbrutal\b|\bunfair\w*|\btoo (hard|easy)"),
    "frustration_stuck": (
        "CTX", r"\bstuck\b|\bfrustrat\w*|\brage\b|\bannoying|\bgave up|\bgive up"),
    "bugs_performance": (
        "CTX", r"\bbug(s|gy)?\b|\bcrash\w*|\blag\w*|\bfps\b|\bperformance|\boptimi[sz](ation|ed)\b|\bstutter\w*|"
               r"\bservers?\b"),
    "social_multiplayer": (
        "CTX", r"\bfriends?\b|\bco-?op\b|\bmultiplayer|\bcommunity\b|\bonline\b"),
    "story_presentation": (
        "CTX", r"\bstory\b|\bnarrative|\batmospher\w*|\bmusic\b|\bsoundtrack|\bart ?style|\bbeautiful|"
               r"\bcharacters\b|\bwriting\b"),
    "developer_updates": (
        "CTX", r"\bdevs?\b|\bdevelopers?\b|\bupdates?\b|\bpatch\w*"),
    "relaxing_cozy": (
        "CTX", r"\brelax\w*|\bchill\b|\bcozy|\bcosy|\bcalm\w*|\bwholesome"),
}

COMPILED = {k: re.compile(p, re.I | re.S) for k, (_, p) in THEMES.items()}
PILLAR = {k: v[0] for k, v in THEMES.items()}


def code(text):
    """Return the set of themes whose pattern matches the text."""
    return {k for k, rx in COMPILED.items() if rx.search(text or "")}
