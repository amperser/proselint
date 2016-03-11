# -*- coding: utf-8 -*-
"""Redundancy.

---
layout:     post
source:     After the Deadline
source_url: http://open.afterthedeadline.com/download/download-source-code/
title:      redundancy
date:       2016-03-09 22:33:00
categories: writing
---

Points out use redundant phrases.

"""
from proselint.tools import memoize, preferred_forms_check


@memoize
def check(text):
    """Suggest the preferred forms."""
    err = "after_the_deadline.redundancy"
    msg = "Redundancy. Use '{}' instead of '{}'."

    redundancies = [
        [u"Bō",               ["Bo Staff"]],
        ["Challah",           ["Challah bread"]],
        ["Hallah",            ["Hallah bread"]],
        ["I",                 ["I myself", "I personally"]],
        ["Mount Fuji",        ["Mount Fujiyama"]],
        ["Milky Way",         ["Milky Way galaxy"]],
        ["Rio Grande",        ["Rio Grande river"]],
        ["a.m.",              ["a.m. in the morning"]],
        ["adage",             ["old adage"]],
        ["add",               ["add a further", "add an additional"]],
        ["advance",           ["advance forward"]],
        ["alternative",       ["alternative choice"]],
        ["always",            ["always and forever"]],
        ["amaretto",          ["amaretto almond"]],
        ["ambush",            ["veiled ambush"]],
        ["annihilate",        ["completely annihilate"]],
        ["anniversary",       ["annual anniversary"]],
        ["anonymous",         ["unnamed anonymous"]],
        ["approval",          ["favorable approval"]],
        ["as",                ["equally as"]],
        ["ascend",            ["ascend up"]],
        ["ask",               ["ask the question"]],
        ["assemble",          ["assemble together"]],
        ["at the present the", ["at the present time the"]],
        ["at this point",     ["at this point in time"]],
        ["attach",            ["attach together"]],
        ["autumn",            ["autumn season"]],
        ["baby",              ["little baby"]],
        ["bad",               ["awful bad"]],
        ["bald",              ["bald-headed"]],
        ["balsa",             ["balsa wood"]],
        ["began",             ["first began"]],
        ["beginning",         ["new beginning"]],
        ["belongings",        ["personal belongings"]],
        ["benefits",          ["desirable benefits"]],
        ["bento",             ["bento box"]],
        ["best",              ["best ever"]],
        ["bit",               ["tiny bit"]],
        ["black",             ["pitch black"]],
        ["blend",             ["blend together"]],
        ["bond",              ["common bond"]],
        ["bonus",             ["added bonus", "extra bonus"]],
        ["bouquet",           ["bouquet of flowers"]],
        ["breakthrough",      ["major breakthrough"]],
        ["bride",             ["new bride"]],
        ["brief",             ["brief in duration"]],
        ["bruin",             ["bruin bear"]],
        ["burning",           ["burning hot"]],
        ["but",               ["but however", "but nevertheless"]],
        ["cacophony",         ["cacophony of sound"]],
        ["cameo",             ["brief cameo", "cameo appearance"]],
        ["cancel",            ["cancel out"]],
        ["cash",              ["cash money"]],
        ["cease",             ["cease and desist"]],
        ["chai",              ["chai tea"]],
        ["chance",            ["random chance"]],
        ["charm",             ["personal charm"]],
        ["circle",            ["circle around", "round circle"]],
        ["circulate",         ["circulate around"]],
        ["classify",          ["classify into groups"]],
        ["classmates",        ["fellow classmates"]],
        ["cliche",            ["old cliche", "overused cliche"]],
        ["climb",             ["climb up"]],
        ["clock",             ["time clock"]],
        ["collaborate",       ["collaborate together"]],
        ["collaboration",     ["joint collaboration"]],
        ["colleague",         ["fellow colleague"]],
        ["combine",           ["combine together"]],
        ["commute",           ["commute back and forth"]],
        ["compete",           ["compete with each other"]],
        ["comprises",         ["comprises of"]],
        ["conceived",         ["first conceived"]],
        ["conclusion",        ["final conclusion"]],
        ["confer",            ["confer together"]],
        ["confrontation",     ["direct confrontation"]],
        ["confused",          ["confused state"]],
        ["connect",           ["connect together", "connect up"]],
        ["connected",         ["interconnected"]],
        ["consensus",         ["consensus of opinion", "general consensus"]],
        ["construction",      ["new construction"]],
        ["consult",           ["consult with"]],
        ["conversation",      ["oral conversation"]],
        ["cool",              ["cool down"]],
        ["cooperate",         ["cooperate together"]],
        ["cooperation",       ["mutual cooperation"]],
        ["copy",              ["duplicate copy"]],
        ["core",              ["inner core"]],
        ["cost",              ["cost the sum of"]],
        ["could",             ["could possibly"]],
        ["coupon",            ["money-saving coupon"]],
        ["created",           ["originally created"]],
        ["crisis",            ["crisis situation"]],
        ["crouch",            ["crouch down"]],
        ["curative",          ["curative process"]],
        ["currently",         ["now currently"]],
        ["custom",            ["old custom", "usual custom"]],
        ["danger",            ["serious danger"]],
        ["dates",             ["dates back"]],
        ["decision",          ["definite decision"]],
        ["depreciate",        ["depreciate in value"]],
        ["descend",           ["descend down"]],
        ["destroy",           ["totally destroy"]],
        ["destroyed",         ["completely destroyed"]],
        ["destruction",       ["total destruction"]],
        ["details",           ["specific details"]],
        ["dilemma",           ["difficult dilemma"]],
        ["disappear",         ["disappear from sight"]],
        ["discovered",        ["originally discovered"]],
        ["dive",              ["dive down"]],
        ["done",              ["over and done with"]],
        ["down",              ["downward"]],
        ["drawing",           ["illustrated drawing"]],
        ["drop",              ["drop down"]],
        ["dune",              ["sand dune"]],
        ["during",            ["during the course of"]],
        ["dwindle",           ["dwindle down"]],
        ["dwindled",          ["dwindled down"]],
        ["each",              ["each and every"]],
        ["earlier",           ["earlier in time"]],
        ["eliminate",         ["completely eliminate", "eliminate altogether",
                               "entirely eliminate"]],
        ["ember",             ["glowing ember"]],
        ["embers",            ["burning embers"]],
        ["emergency",         ["emergency situation", "unexpected emergency"]],
        ["empty",             ["empty out"]],
        ["enclosed",          ["enclosed herein"]],
        ["end",               ["final end"]],
        ["engulfed",          ["completely engulfed"]],
        ["enter",             ["enter in", "enter into"]],
        ["equal",             ["equal to one another"]],
        ["eradicate",         ["eradicate completely"]],
        ["essential",         ["absolutely essential"]],
        ["estimated at",      ["estimated at about",
                               "estimated at approximately",
                               "estimated at around"]],
        ["etc.",              ["and etc."]],
        ["evolve",            ["evolve over time"]],
        ["exaggerate",        ["over exaggerate"]],
        ["exited",            ["exited from"]],
        ["experience",        ["actual experience", "past experience"]],
        ["experts",           ["knowledgeable experts"]],
        ["extradite",         ["extradite back"]],
        ["face",              ["face up to"]],
        ["facilitate",        ["facilitate easier"]],
        ["fact",              ["established fact"]],
        ["facts",             ["actual facts", "hard facts", "true facts"]],
        ["fad",               ["passing fad"]],
        ["fall",              ["fall down", "fall season"]],
        ["feat",              ["major feat"]],
        ["feel",              ["feel inside"]],
        ["feelings",          ["inner feelings"]],
        ["few",               ["few in number"]],
        ["filled",            ["completely filled", "filled to capacity"]],
        ["first",             ["first of all"]],
        ["first time",        ["first time ever"]],
        ["fist",              ["closed fist"]],
        ["fit",               ["fit enough"]],
        ["fly",               ["fly through the air"]],
        ["focus",             ["focus in", "main focus"]],
        ["follow",            ["follow after"]],
        ["for example",       ["as for example"]],
        ["foremost",          ["first and foremost"]],
        ["forever",           ["forever and ever"]],
        ["free",              ["for free"]],
        ["friend",            ["personal friend"]],
        ["friendship",        ["personal friendship"]],
        ["full",              ["full to capacity"]],
        ["fundamentals",      ["basic fundamentals"]],
        ["fuse",              ["fuse together"]],
        ["gather",            ["gather together", "gather up"]],
        ["get up",            ["get up on his feet", "get up on your feet"]],
        ["gift",              ["free gift"]],
        ["gifts",             ["free gifts"]],
        ["goal",              ["ultimate goal"]],
        ["graduate",          ["former graduate"]],
        ["grow",              ["grow in size"]],
        ["guarantee",         ["absolute guarantee"]],
        ["gunman",            ["armed gunman"]],
        ["gunmen",            ["armed gunmen"]],
        ["habitat",           ["native habitat"]],
        ["had done",          ["had done previously"]],
        ["halves",            ["two equal halves"]],
        ["has",               ["has got"]],
        ["have",              ["have got"]],
        ["haven",             ["safe haven"]],
        ["he",                ["he himself"]],
        ["heat",              ["heat up"]],
        ["history",           ["past history"]],
        ["hoist",             ["hoist up"]],
        ["hole",              ["empty hole"]],
        ["honcho",            ["head honcho"]],
        ["hurry",             ["hurry up"]],
        ["ice",               ["frozen ice"]],
        ["ideal",             ["perfect ideal"]],
        ["identical",         ["same identical"]],
        ["identification",    ["positive identification"]],
        ["imports",           ["foreign imports"]],
        ["impulse",           ["sudden impulse"]],
        ["in",                ["inward", "situated in"]],
        ["in fact",           ["in actual fact"]],
        ["in the distance",   ["off in the distance"]],
        ["in the yard",       ["outside in the yard"]],
        ["inclusive",         ["all inclusive"]],
        ["incredible",        ["incredible to believe"]],
        ["incumbent",         ["present incumbent"]],
        ["indicted",          ["indicted on a charge"]],
        ["industry",          ["private industry"]],
        ["injuries",          ["harmful injuries"]],
        ["innovation",        ["new innovation"]],
        ["innovative",        ["innovative new", "new innovative"]],
        ["input",             ["input into"]],
        ["instinct",          ["natural instinct", "naturally instinct"]],
        ["integrate",         ["integrate together",
                               "integrate with each other"]],
        ["interdependent",    ["interdependent on each other",
                               "mutually interdependent"]],
        ["into",              ["inward into"]],
        ["introduced",        ["introduced for the first time"]],
        ["introduced a",      ["introduced a new"]],
        ["invention",         ["new invention"]],
        ["investigation",     ["thorough investigation"]],
        ["join",              ["join together"]],
        ["kinds",             ["different kinds"]],
        ["kneel",             ["kneel down"]],
        ["knots",             ["knots per hour"]],
        ["lag",               ["lag behind"]],
        ["last",              ["last of all"]],
        ["later",             ["later time"]],
        ["left",              ["left behind", "leftward"]],
        ["lift",              ["lift up"]],
        ["lingers",           ["still lingers"]],
        ["look to the future", ["look ahead to the future"]],
        ["love triangle",     ["three-way love triangle"]],
        ["made of",           ["made out of"]],
        ["maintained",        ["constantly maintained"]],
        ["manually",          ["manually by hand"]],
        ["many",              ["many different"]],
        ["marina",            ["boat marina"]],
        ["mask",              ["face mask"]],
        ["may",               ["may possibly"]],
        ["media",             ["mass media"]],
        ["meet",              ["meet together", "meet up",
                               "meet with each other"]],
        ["memories",          ["past memories"]],
        ["merge",             ["merge together"]],
        ["merged",            ["merged together"]],
        ["meshed",            ["meshed together"]],
        ["midnight",          ["twelve midnight"]],
        ["midway",            ["midway between"]],
        ["might",             ["might possibly"]],
        ["migraine",          ["migraine headache"]],
        ["minestrone",        ["minestrone soup"]],
        ["miss",              ["miss out on"]],
        ["mix",               ["mix together"]],
        ["moment",            ["brief moment", "moment in time"]],
        ["monopoly",          ["complete monopoly"]],
        ["mural",             ["wall mural"]],
        ["mutual respect",    ["mutual respect for each other"]],
        ["mutually dependent", ["mutually dependent on each other"]],
        ["mystery",           ["unsolved mystery"]],
        ["naked",             ["bare naked"]],
        ["nape",              ["nape of her neck"]],
        ["necessary",         ["absolutely necessary"]],
        ["necessities",       ["basic necessities"]],
        ["never",             ["never at any time", "never before"]],
        ["none",              ["none at all"]],
        ["noon",              ["12 noon", "12 o'clock noon", "high noon",
                               "twelve noon"]],
        ["nostalgia",         ["nostalgia for the past"]],
        ["now",               ["right now"]],
        ["now and then",      ["every now and then"]],
        ["number of",         ["number of different"]],
        ["on",                ["onto", "onward", "up on top", "up on top of"]],
        ["open",              ["open up"]],
        ["opening",           ["exposed opening"]],
        ["opinion",           ["personal opinion"]],
        ["opposites",         ["exact opposites", "polar opposites"]],
        ["or",                ["or alternatively"]],
        ["orbits",            ["orbits around"]],
        ["out",               ["outward"]],
        ["outcome",           ["final outcome"]],
        ["output",            ["output out of"]],
        ["outside",           ["outside of"]],
        ["over",              ["over top", "over top of", "over with",
                               "right over"]],
        ["over and over",     ["over and over again"]],
        ["palm",              ["palm of the hand"]],
        ["panacea",           ["universal panacea"]],
        ["part of",           ["integral part of"]],
        ["parts",             ["component parts"]],
        ["pass",              ["free pass"]],
        ["pending",           ["now pending"]],
        ["penetrate",         ["penetrate into", "penetrate through"]],
        ["per",               ["as per"]],
        ["period",            ["period of time", "time period"]],
        ["persists",          ["still persists"]],
        ["pick",              ["pick and choose"]],
        ["pioneer",           ["old pioneer"]],
        ["pizza",             ["pizza pie"]],
        ["plan",              ["plan ahead", "plan in advance",
                               "proposed plan"]],
        ["planning",          ["advance planning", "forward planning"]],
        ["plans",             ["future plans"]],
        ["plunge",            ["plunge down"]],
        ["point",             ["point in time", "sharp point"]],
        ["postpone",          ["postpone until later"]],
        ["pouring rain",      ["pouring down rain"]],
        ["pregnant",          ["very pregnant"]],
        ["present",           ["present time"]],
        ["pretenses",         ["false pretenses"]],
        ["preview",           ["advance preview"]],
        ["previously listed", ["previously listed above"]],
        ["probed",            ["probed into"]],
        ["proceed",           ["proceed ahead"]],
        ["prosthesis",        ["artificial prosthesis"]],
        ["protest",           ["protest against"]],
        ["protrude",          ["protrude out"]],
        ["proverb",           ["old proverb"]],
        ["proximity",         ["close proximity"]],
        ["public",            ["general public"]],
        ["pursue",            ["pursue after"]],
        ["put off",           ["put off until later"]],
        ["quiet",             ["peace and quiet"]],
        ["raise",             ["raise up"]],
        ["range",             ["dynamic range"]],
        ["re-elect",          ["re-elect for another term"]],
        ["reason",            ["reason why"]],
        ["reason is",         ["reason is because"]],
        ["recently",          ["just recently"]],
        ["record",            ["all-time record", "new record"]],
        ["records",           ["past records"]],
        ["recruit",           ["new recruit"]],
        ["recur",             ["recur again"]],
        ["recurrence",        ["future recurrence"]],
        ["refer",             ["refer back"]],
        ["reflect",           ["reflect back"]],
        ["regardless",        ["irregardless"]],
        ["relevant",          ["highly relevant"]],
        ["remain",            ["continue to remain"]],
        ["remains",           ["still remains"]],
        ["repeat",            ["repeat again"]],
        ["replica",           ["exact replica"]],
        ["reply",             ["reply back"]],
        ["reprieve",          ["temporary reprieve"]],
        ["requirements",      ["necessary requirements"]],
        ["reservations",      ["advance reservations"]],
        ["residents",         ["local residents"]],
        ["result",            ["end result"]],
        ["retreat",           ["retreat back"]],
        ["revert",            ["revert back"]],
        ["right",             ["rightward"]],
        ["rise",              ["rise up"]],
        ["round",             ["round in shape"]],
        ["routine",           ["regular routine"]],
        ["rule of thumb",     ["rough rule of thumb"]],
        ["rumor",             ["unconfirmed rumor"]],
        ["rustic",            ["rustic country"]],
        ["same",              ["exact same", "precise same", "same exact"]],
        ["sanctuary",         ["safe sanctuary"]],
        ["satisfaction",      ["full satisfaction"]],
        ["scrutinize",        ["scrutinize in detail"]],
        ["scrutiny",          ["careful scrutiny", "close scrutiny"]],
        ["secret",            ["secret that cannot be told"]],
        ["seek",              ["seek out", "seek to find"]],
        ["separated",         ["separated apart from each other"]],
        ["share",             ["share together"]],
        ["shiny",             ["shiny in appearance"]],
        ["shut",              ["shut down"]],
        ["sincere",           ["truly sincere"]],
        ["sink",              ["sink down"]],
        ["skipped",           ["skipped over"]],
        ["slow",              ["slow speed"]],
        ["small",             ["small size"]],
        ["snow",              ["white snow"]],
        ["so",                ["so therefore"]],
        ["soaked",            ["soaked to the skin"]],
        ["soda",              ["soda pop"]],
        ["soft",              ["soft in texture", "soft to the touch"]],
        ["sole",              ["sole of the foot"]],
        ["some time",         ["some time to come"]],
        ["space",             ["empty space"]],
        ["speck",             ["small speck"]],
        ["speed",             ["rate of speed"]],
        ["spell out",         ["spell out in detail"]],
        ["spiked",            ["spiked upward", "spiked upwards"]],
        ["spliced",           ["spliced together"]],
        ["spring",            ["spring season"]],
        ["stacked",           ["stacked together"]],
        ["start",             ["start off", "start out", "start out"]],
        ["started",           ["first started"]],
        ["stranger",          ["anonymous stranger"]],
        ["studio audience",   ["live studio audience"]],
        ["subject",           ["subject matter"]],
        ["subway",            ["underground subway"]],
        ["sufficient",        ["sufficient enough"]],
        ["summary",           ["brief summary", "short summary"]],
        ["summer",            ["summer season"]],
        ["sure",              ["absolutely sure"]],
        ["surprise",          ["unexpected surprise"]],
        ["surround",          ["completely surround"]],
        ["surrounded",        ["surrounded on all sides"]],
        ["swoop",             ["swoop down"]],
        ["talking",           ["talking out loud"]],
        ["tall",              ["tall in height", "tall in stature"]],
        ["tantrum",           ["temper tantrum"]],
        ["tear",              ["tear apart"]],
        ["telepathy",         ["mental telepathy"]],
        ["ten",               ["ten in number"]],
        ["teriyaki",          ["teriyaki barbecue"]],
        ["the same",          ["one and the same"]],
        ["these",             ["these ones"]],
        ["they",              ["they themselves"]],
        ["those",             ["those ones"]],
        ["time",              ["high time"]],
        ["to",                ["in order to", "so as to"]],
        ["to ask",            ["to ask a question", "to ask for assistance",
                               "to ask for help"]],
        ["together",          ["together at the same time"]],
        ["total",             ["sum total"]],
        ["treatment",         ["therapeutic treatment"]],
        ["trench",            ["open trench"]],
        ["trend",             ["current trend"]],
        ["truth",             ["honest truth"]],
        ["tube",              ["hollow tube"]],
        ["tuna",              ["tuna fish"]],
        ["tundra",            ["frozen tundra"]],
        ["twins",             ["a pair of twins", "pair of twins"]],
        ["ultimatum",         ["final ultimatum"]],
        ["undeniable",        ["undeniable truth"]],
        ["undergraduate",     ["undergraduate student"]],
        ["unintentional",     ["unintentional mistake"]],
        ["unique",            ["really unique", "somewhat unique",
                               "totally unique", "very unique"]],
        ["unit",              ["single unit"]],
        ["up",                ["upward"]],
        ["usual",             ["per usual"]],
        ["vacillate",         ["vacillate back and forth"]],
        ["veteran",           ["former veteran"]],
        ["visible",           ["visible to the eye"]],
        ["void",              ["null and void"]],
        ["warm",              ["warm up"]],
        ["warn",              ["warn in advance"]],
        ["warning",           ["advance warning"]],
        ["water heater",      ["hot water heater"]],
        ["we",                ["we ourselves"]],
        ["weather",           ["weather conditions", "weather situation"]],
        ["whence",            ["from whence"]],
        ["whether",           ["as to whether", "whether or not"]],
        ["which we live",     ["in which we live in"]],
        ["why",               ["why come"]],
        ["winter",            ["winter season"]],
        ["witness",           ["live witness"]],
        ["write",             ["write down"]],
        ["written",           ["written down"]],
        ["yakitori",          ["yakitori chicken"]],
        ["yerba mate",        ["yerba mate tea"]],
        ["yes",               ["affirmative yes"]],
    ]

    return preferred_forms_check(text, redundancies, err, msg)


@memoize
def check_redundant_acronym_syndrome(text):
    """Suggest the preferred forms."""
    err = "after_the_deadline.redundancy.ras"
    msg = "RAS syndrome. Use '{}' instead of '{}'."

    redundancies = [
        ["ABS",               ["ABS brakes", "ABS braking system"]],
        ["ACT",               ["ACT test"]],
        ["CD",                ["CD disc"]],
        ["GOP",               ["GOP party"]],
        ["GRE",               ["GRE exam"]],
        ["HIV",               ["HIV virus"]],
        ["ISBN",              ["ISBN number"]],
        ["LCD",               ["LCD display"]],
        ["PC",                ["PC computer"]],
        ["PIN",               ["PIN number"]],
        ["RAM",               ["RAM memory"]],
        ["RSVP",              ["please RSVP"]],
        ["SAT",               ["SAT test"]],
        ["UPC",               ["UPC code"]],
    ]

    return preferred_forms_check(text, redundancies, err, msg)
