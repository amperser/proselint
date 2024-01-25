"""Redundancy."""

from __future__ import annotations

from proselint.checks import ResultCheck
from proselint.checks import preferred_forms_check


def check(text: str) -> list[ResultCheck]:
    """Suggest the preferred forms."""
    err = "redundancy.wallace"
    msg = "Redundancy. Use '{}' instead of '{}'."

    redundancies = [
        ["rectangular", ["rectangular in shape"]],
        ["audible", ["audible to the ear"]],
    ]
    return preferred_forms_check(text, redundancies, err, msg)


def check_garner(text: str) -> list[ResultCheck]:
    """Suggest the preferred forms.

    source:     Garner's Modern American Usage
    source_url: http://bit.ly/1T4alrY
    """
    err = "redundancy.garner"
    msg = "Redundancy. Use '{}' instead of '{}'."

    redundancies = [
        ["adequate", ["adequate enough"]],
        ["admitted", ["self-admitted"]],
        ["affidavit", ["sworn affidavit"]],
        ["agreement", ["mutual agreement"]],
        ["alumnus", ["former alumnus"]],
        ["antithetical", ["directly antithetical"]],
        ["approximately", ["approximately about"]],
        ["associate", ["associate together(?: in groups)?"]],
        ["bivouac", ["temporary bivouac", "bivouac camp"]],
        ["blend", ["blend together"]],
        ["but", ["but nevertheless"]],
        ["charged with...", ["accused of a charge"]],
        ["circumstances of", ["circumstances surrounding"]],
        ["circumstances", ["surrounding circumstances"]],
        ["close", ["close proximity"]],
        ["collaborate", ["collaborate together"]],
        ["collaborator", ["fellow collaborator"]],
        ["collaborators", ["fellow collaborators"]],
        ["collocated", ["collocated together"]],
        ["colleagues", ["fellow colleagues"]],
        ["combine", ["combine together"]],
        ["complacent", ["self-complacent"]],
        ["confessed", ["self-confessed"]],
        ["connect", ["connect together"]],
        ["consensus", ["(?:general )?consensus of opinion"]],
        ["consolidate", ["consolidate together"]],
        ["continues to", ["still continues to"]],
        ["contradictory", ["mutually contradictory"]],
        ["cooperation", ["mutual cooperation"]],
        ["couple", ["couple together"]],
        ["crisis", ["serious crisis"]],
        ["eliminate", ["entirely eliminate"]],
        ["especially", ["most especially"]],
        ["fact", ["actual fact"]],
        ["facts", ["true facts"]],
        ["forecast", ["future forecast"]],
        ["founding fathers", ["founding forefathers"]],
        ["free", ["free and gratis"]],
        ["free", ["free gratis"]],
        ["full", ["completely full"]],
        ["fundamentals", ["basic fundamentals"]],
        ["gift", ["free gift"]],
        ["innovation", ["new innovation"]],
        ["interact", ["interact with each other"]],
        ["large", ["large-size"]],
        ["meld", ["meld together"]],
        ["merge", ["merge together"]],
        ["mingle", ["mingle together"]],
        ["mix", ["mix together"]],
        ["mutual feelings", ["mutual feelings for eachother"]],
        ["mutual respect", ["mutual respect for each other"]],
        ["native citizen", ["native-born citizen"]],
        ["necessity", ["absolute necessity"]],
        ["obvious", ["blatantly obvious"]],
        ["pause", ["pause for a moment"]],
        ["planning", ["advance planning"]],
        ["plans", ["future plans"]],
        ["pooled", ["pooled together"]],
        ["potable water", ["potable drinking water"]],
        ["potable water", ["potable drinking water"]],
        ["recruit", ["new recruit"]],
        ["reelected", ["reelected for another term"]],
        ["refer", ["refer back"]],
        ["regress", ["regress back"]],
        ["repay them", ["repay them back"]],
        ["repay", ["repay back"]],
        ["repeat", ["repeat again"]],
        ["repeat", ["repeat back"]],
        ["repeat", ["repeat the same"]],
        ["repeated", ["repeated the same"]],
        ["reprieve", ["temporary reprieve"]],
        ["respite", ["brief respite"]],
        ["retirement", ["retiral", "retiracy"]],
        ["retreat", ["retreat back"]],
        ["return", ["return back"]],
        ["scrutinize", ["closely scrutinize"]],
        ["software", ["software program"]],
        ["surrounded", ["surrounded on all sides"]],
        ["the nation", ["the whole entire nation"]],
        ["throughout the", ["throughout the entire"]],
        ["timpani", ["timpani drum"]],
        ["twins", ["pair of twins"]],
        ["vacancy", ["unfilled vacancy"]],
        ["various", ["various different"]],
        ["veteran", ["former veteran"]],
        ["visible", ["visible to the eye"]],
        ["vocation", ["professional vocation"]],
        ["while", ["while at the same time"]],
    ]

    return preferred_forms_check(text, redundancies, err, msg)


def check_nordquist(text: str) -> list[ResultCheck]:
    """Suggest the preferred forms.

    source:     Richard Nordquist
    source_url: http://grammar.about.com/bio/Richard-Nordquist-22176.htm
    """
    err = "redundancy.nordquist"
    msg = "Redundancy. Use '{}' instead of '{}'."

    redundancies = [
        ["essential", ["absolutely essential"]],
        ["necessary", ["absolutely necessary"]],
        ["a.m.", ["a.m. in the morning"]],
        ["p.m.", ["p.m. at night"]],
    ]
    return preferred_forms_check(text, redundancies, err, msg)


def check_atd_1(text: str) -> list[ResultCheck]:
    """Check for redundancies from After the Deadline.

    NOTE: this was one of the slowest Checks,
          so it was segmented to even the load for parallelization
    """
    err = "after_the_deadline.redundancy"
    msg = "Redundancy. Use '{}' instead of '{}'."

    redundancies = [
        ["Bō", ["Bo Staff"]],
        ["Challah", ["Challah bread"]],
        ["Hallah", ["Hallah bread"]],
        ["Challah", ["Challah bread"]],
        ["I", ["I myself", "I personally"]],
        ["Mount Fuji", ["Mount Fujiyama"]],
        ["Milky Way", ["Milky Way galaxy"]],
        ["Rio Grande", ["Rio Grande river"]],
        ["adage", ["old adage"]],
        ["add", ["add a further", "add an additional"]],
        ["advance", ["advance forward"]],
        ["alternative", ["alternative choice"]],
        ["amaretto", ["amaretto almond"]],
        ["annihilate", ["completely annihilate"]],
        ["anniversary", ["annual anniversary"]],
        ["anonymous", ["unnamed anonymous"]],
        ["as", ["equally as"]],
        ["ascend", ["ascend up"]],
        ["ask", ["ask the question"]],
        ["assemble", ["assemble together"]],
        ["at present the", ["at the present time the"]],
        ["at this point", ["at this point in time"]],
        ["attach", ["attach together"]],
        ["autumn", ["autumn season"]],
        ["bald", ["bald-headed"]],
        ["balsa", ["balsa wood"]],
        ["belongings", ["personal belongings"]],
        ["benefits", ["desirable benefits"]],
        ["bento", ["bento box"]],
        ["best", ["best ever"]],
        ["bit", ["tiny bit"]],
        ["blend", ["blend together"]],
        ["bond", ["common bond"]],
        ["bonus", ["added bonus", "extra bonus"]],
        ["bouquet", ["bouquet of flowers"]],
        ["breakthrough", ["major breakthrough"]],
        ["bride", ["new bride"]],
        ["brief", ["brief in duration"]],
        ["bruin", ["bruin bear"]],
        ["hot", ["burning hot"]],
        ["cacophony", ["cacophony of sound"]],
        ["cameo", ["brief cameo", "cameo appearance"]],
        ["cancel", ["cancel out"]],
        ["cash", ["cash money"]],
        ["chai", ["chai tea"]],
        ["chance", ["random chance"]],
        ["charm", ["personal charm"]],
        ["circle", ["circle around", "round circle"]],
        ["circulate", ["circulate around"]],
        ["classify", ["classify into groups"]],
        ["classmates", ["fellow classmates"]],
        ["cliche", ["old cliche", "overused cliche"]],
        ["climb", ["climb up"]],
        ["clock", ["time clock"]],
        ["collaborate", ["collaborate together"]],
        ["collaboration", ["joint collaboration"]],
        ["colleague", ["fellow colleague"]],
        ["combine", ["combine together"]],
        ["commute", ["commute back and forth"]],
        ["compete", ["compete with each other"]],
        ["comprise", ["comprise of"]],
        ["comprises", ["comprises of"]],
        ["conceived", ["first conceived"]],
        ["conclusion", ["final conclusion"]],
        ["confer", ["confer together"]],
        ["confrontation", ["direct confrontation"]],
        # ["confused",          ["confused state"]],
        ["connect", ["connect together", "connect up"]],
        ["consensus", ["consensus of opinion", "general consensus"]],
        ["consult", ["consult with"]],
        ["conversation", ["oral conversation"]],
        ["cool", ["cool down"]],
        ["cooperate", ["cooperate together"]],
        ["cooperation", ["mutual cooperation"]],
        ["copy", ["duplicate copy"]],
        ["core", ["inner core"]],
        ["cost", ["cost the sum of"]],
        ["could", ["could possibly"]],
        ["coupon", ["money-saving coupon"]],
        ["created", ["originally created"]],
        ["crisis", ["crisis situation"]],
        ["crouch", ["crouch down"]],
        ["currently", ["now currently"]],
        ["custom", ["old custom", "usual custom"]],
        ["danger", ["serious danger"]],
        ["dates", ["dates back"]],
        ["decision", ["definite decision"]],
        ["depreciate", ["depreciate in value"]],
        ["descend", ["descend down"]],
        ["destroy", ["totally destroy"]],
        ["destroyed", ["completely destroyed"]],
        ["destruction", ["total destruction"]],
        ["details", ["specific details"]],
        ["dilemma", ["difficult dilemma"]],
        ["disappear", ["disappear from sight"]],
        ["discovered", ["originally discovered"]],
        ["dive", ["dive down"]],
        ["done", ["over and done with"]],
        ["drawing", ["illustrated drawing"]],
        ["drop", ["drop down"]],
        ["dune", ["sand dune"]],
        ["during", ["during the course of"]],
        ["dwindle", ["dwindle down"]],
        ["dwindled", ["dwindled down"]],
        ["every", ["each and every"]],
        ["earlier", ["earlier in time"]],
        [
            "eliminate",
            [
                "completely eliminate",
                "eliminate altogether",
                "entirely eliminate",
            ],
        ],
        ["ember", ["glowing ember"]],
        ["embers", ["burning embers"]],
        ["emergency", ["emergency situation", "unexpected emergency"]],
        ["empty", ["empty out"]],
        ["enclosed", ["enclosed herein"]],
        ["end", ["final end"]],
        ["engulfed", ["completely engulfed"]],
        ["enter", ["enter in", "enter into"]],
        ["equal", ["equal to one another"]],
        ["eradicate", ["eradicate completely"]],
        ["essential", ["absolutely essential"]],
        [
            "estimated at",
            [
                "estimated at about",
                "estimated at approximately",
                "estimated at around",
            ],
        ],
        ["etc.", ["and etc."]],
        ["evolve", ["evolve over time"]],
        ["exaggerate", ["over exaggerate"]],
        ["exited", ["exited from"]],
        ["experience", ["actual experience", "past experience"]],
        ["experts", ["knowledgeable experts"]],
        ["extradite", ["extradite back"]],
        ["face the consequences", ["face up to the consequences"]],
        ["face the fact", ["face up to the fact"]],
        ["face the challenge", ["face up to the challenge"]],
        ["face the problem", ["face up to the problem"]],
        ["facilitate", ["facilitate easier"]],
        ["fact", ["established fact"]],
        ["facts", ["actual facts", "hard facts", "true facts"]],
        ["fad", ["passing fad"]],
        ["fall", ["fall down"]],
        ["fall", ["fall season"]],
        ["feat", ["major feat"]],
        ["feel", ["feel inside"]],
        ["feelings", ["inner feelings"]],
        ["few", ["few in number"]],
        ["filled", ["completely filled", "filled to capacity"]],
        ["first", ["first of all"]],
        ["first time", ["first time ever"]],
        ["fist", ["closed fist"]],
        ["fly", ["fly through the air"]],
        ["focus", ["focus in", "main focus"]],
        ["follow", ["follow after"]],
        ["for example", ["as for example"]],
        # ["foremost",          ["first and foremost"]],
        ["forever", ["forever and ever"]],
        ["free", ["for free"]],
        ["friend", ["personal friend"]],
        ["friendship", ["personal friendship"]],
        ["full", ["full to capacity"]],
        ["fundamentals", ["basic fundamentals"]],
        ["fuse", ["fuse together"]],
        ["gather", ["gather together", "gather up"]],
        ["get up", ["get up on his feet", "get up on your feet"]],
        ["gift", ["free gift"]],
        ["gifts", ["free gifts"]],
        ["goal", ["ultimate goal"]],
        # ["graduate",          ["former graduate"]],
        ["grow", ["grow in size"]],
        ["guarantee", ["absolute guarantee"]],
        ["gunman", ["armed gunman"]],
        ["gunmen", ["armed gunmen"]],
        ["habitat", ["native habitat"]],
        ["had done", ["had done previously"]],
        ["halves", ["two equal halves"]],
        # ["has",               ["has got"]],
        # ["have",              ["have got"]],
        ["haven", ["safe haven"]],
        # ["he",                ["he himself"]],
        ["heat", ["heat up"]],
        ["history", ["past history"]],
        ["hoist", ["hoist up"]],
        ["hole", ["empty hole"]],
        ["honcho", ["head honcho"]],
    ]
    return preferred_forms_check(text, redundancies, err, msg)


def check_atd_2(text: str) -> list[ResultCheck]:
    """Check for redundancies from After the Deadline.

    NOTE: this was one of the slowest Checks,
      so it was segmented to even the load for parallelization
    """
    err = "after_the_deadline.redundancy"
    msg = "Redundancy. Use '{}' instead of '{}'."

    redundancies = [
        ["ice", ["frozen ice"]],
        ["ideal", ["perfect ideal"]],
        ["identical", ["same identical"]],
        ["identification", ["positive identification"]],
        ["imports", ["foreign imports"]],
        ["impulse", ["sudden impulse"]],
        ["in fact", ["in actual fact"]],
        ["in the yard", ["outside in the yard"]],
        ["inclusive", ["all inclusive"]],
        ["incredible", ["incredible to believe"]],
        ["incumbent", ["present incumbent"]],
        # ["indicted",          ["indicted on a charge"]],
        ["industry", ["private industry"]],
        ["injuries", ["harmful injuries"]],
        ["innovation", ["new innovation"]],
        ["innovative", ["innovative new", "new innovative"]],
        # ["input",             ["input into"]],
        ["instinct", ["natural instinct", "naturally instinct"]],
        ["integrate", ["integrate together", "integrate with each other"]],
        [
            "interdependent",
            ["interdependent on each other", "mutually interdependent"],
        ],
        ["introduced", ["introduced for the first time"]],
        ["invention", ["new invention"]],
        ["kneel", ["kneel down"]],
        ["knots", ["knots per hour"]],
        # ["last",              ["last of all"]],
        # ["later",             ["later time"]],
        ["lift", ["lift up"]],
        ["lingers", ["still lingers"]],
        ["look to the future", ["look ahead to the future"]],
        ["love triangle", ["three-way love triangle"]],
        ["maintained", ["constantly maintained"]],
        ["manually", ["manually by hand"]],
        ["marina", ["boat marina"]],
        ["may", ["may possibly"]],
        ["meet", ["meet together", "meet with each other"]],
        ["memories", ["past memories"]],
        ["merge", ["merge together"]],
        ["merged", ["merged together"]],
        ["meshed", ["meshed together"]],
        ["midnight", ["twelve midnight"]],
        ["migraine", ["migraine headache"]],
        ["minestrone", ["minestrone soup"]],
        ["mix", ["mix together"]],
        ["moment", ["brief moment", "moment in time"]],
        ["monopoly", ["complete monopoly"]],
        ["mural", ["wall mural"]],
        ["mutual respect", ["mutual respect for each other"]],
        ["mutually dependent", ["mutually dependent on each other"]],
        ["mystery", ["unsolved mystery"]],
        # ["naked",             ["bare naked"]],
        ["nape", ["nape of her neck"]],
        ["necessary", ["absolutely necessary"]],
        ["never", ["never at any time"]],
        ["noon", ["12 noon", "12 o'clock noon", "high noon", "twelve noon"]],
        ["nostalgia", ["nostalgia for the past"]],
        ["number of", ["number of different"]],
        ["opening", ["exposed opening"]],
        ["my opinion", ["my personal opinion"]],
        ["opposites", ["exact opposites", "polar opposites"]],
        ["opposite", ["exact opposite", "polar opposite"]],
        ["orbits", ["orbits around"]],
        ["outcome", ["final outcome"]],
        ["panacea", ["universal panacea"]],
        ["pending", ["now pending"]],
        ["penetrate", ["penetrate through"]],
        ["persists", ["still persists"]],
        ["pioneer", ["old pioneer"]],
        ["plan", ["plan ahead", "plan in advance", "proposed plan"]],
        ["planning", ["advance planning", "forward planning"]],
        ["plans", ["future plans"]],
        ["plan", ["future plan"]],
        ["point", ["point in time"]],
        ["point", ["sharp point"]],
        ["postpone", ["postpone until later"]],
        ["pouring rain", ["pouring down rain"]],
        ["preview", ["advance preview"]],
        ["previously listed", ["previously listed above"]],
        ["probed", ["probed into"]],
        ["proceed", ["proceed ahead"]],
        ["prosthesis", ["artificial prosthesis"]],
        # ["protrude",          ["protrude out"]],
        ["proverb", ["old proverb"]],
        # ["proximity",         ["close proximity"]],
        ["put off", ["put off until later"]],
        # ["raise",             ["raise up"]],
        ["re-elect", ["re-elect for another term"]],
        ["reason is", ["reason is because"]],
        ["recur", ["recur again"]],
        ["recurrence", ["future recurrence"]],
        ["refer", ["refer back"]],
        ["reflect", ["reflect back"]],
        # ["relevant",          ["highly relevant"]],
        ["remain", ["continue to remain"]],
        ["remains", ["still remains"]],
        ["replica", ["exact replica"]],
        ["reply", ["reply back"]],
        # ["requirements",      ["necessary requirements"]],
        ["reservations", ["advance reservations"]],
        ["retreat", ["retreat back"]],
        ["revert", ["revert back"]],
        ["round", ["round in shape"]],
        ["rule of thumb", ["rough rule of thumb"]],
        ["rumor", ["unconfirmed rumor"]],
        ["rustic", ["rustic country"]],
        ["same", ["exact same", "precise same", "same exact"]],
        ["sanctuary", ["safe sanctuary"]],
        ["satisfaction", ["full satisfaction"]],
        ["scrutinize", ["scrutinize in detail"]],
        ["scrutiny", ["careful scrutiny", "close scrutiny"]],
        ["secret", ["secret that cannot be told"]],
        ["seek", ["seek to find"]],
        ["separated", ["separated apart from each other"]],
        ["share", ["share together"]],
        ["shiny", ["shiny in appearance"]],
        ["sincere", ["truly sincere"]],
        ["sink", ["sink down"]],
        ["skipped", ["skipped over"]],
        # ["slow",              ["slow speed"]],
        # ["small",             ["small size"]],
        ["soft", ["soft in texture", "soft to the touch"]],
        ["sole", ["sole of the foot"]],
        ["some time", ["some time to come"]],
        ["speck", ["small speck"]],
        ["speed", ["rate of speed"]],
        ["spell out", ["spell out in detail"]],
        ["spiked", ["spiked upward", "spiked upwards"]],
        ["spring", ["spring season"]],
        ["stranger", ["anonymous stranger"]],
        ["studio audience", ["live studio audience"]],
        ["subway", ["underground subway"]],
        ["sufficient", ["sufficient enough"]],
        ["summer", ["summer season"]],
        ["sure", ["absolutely sure"]],
        ["surprise", ["unexpected surprise"]],
        ["surround", ["completely surround"]],
        ["surrounded", ["surrounded on all sides"]],
        ["tall", ["tall in height", "tall in stature"]],
        ["telepathy", ["mental telepathy"]],
        ["ten", ["ten in number"]],
        ["these", ["these ones"]],
        # ["they",              ["they themselves"]],
        ["those", ["those ones"]],
        ["trench", ["open trench"]],
        ["truth", ["honest truth"]],
        ["tundra", ["frozen tundra"]],
        ["ultimatum", ["final ultimatum"]],
        # ["undeniable",        ["undeniable truth"]],
        ["undergraduate", ["undergraduate student"]],
        # ["unintentional",     ["unintentional mistake"]],
        ["vacillate", ["vacillate back and forth"]],
        ["veteran", ["former veteran"]],
        ["visible", ["visible to the eye"]],
        ["warn", ["warn in advance"]],
        ["warning", ["advance warning"]],
        ["water heater", ["hot water heater"]],
        ["in which we live", ["in which we live in"]],
        ["winter", ["winter season"]],
        ["witness", ["live witness"]],
        ["yakitori", ["yakitori chicken"]],
        ["yerba mate", ["yerba mate tea"]],
        ["yes", ["affirmative yes"]],
    ]

    return preferred_forms_check(text, redundancies, err, msg)
