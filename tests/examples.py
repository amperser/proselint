"""
Example data for checks.

This is a single-export module containing `data`. `data` is a tuple of tuples
with the following structure:
    0. module name (string)
    1. examples that should fail (tuple of strings)
    2. examples that should pass (tuple of strings)
"""

data: tuple[tuple[str, tuple[str, ...], tuple[str, ...]], ...] = (
    (
        "annotations",
        ("Add it to the TODO list.",),
        ("Smoke phrase with nothing flagged.", "Add it to the to do list."),
    ),
    (
        "archaism",
        ("I want to sleep, perchance to dream.",),
        (
            "Smoke phrase with nothing flagged.",
            "I want to sleep, and maybe dream.",
        ),
    ),
    (
        "hedging",
        (
            "I would argue that this is a good test.",
            "You could say that, so to speak.",
        ),
        ("Smoke phrase with nothing flagged.",),
    ),
    (
        "lexical_illusions",
        (
            "Paris in the the springtime.",
            "You should know that that that was wrong.",
            "She had coffee at the Foo bar bar.",
            "She she coffee at the Foo-bar.",
            "After I write i write i write.",
            "That is an echo is an echo",
            "Don't miss the biggest illusion miss the biggest illusion.",
        ),
        (
            "Smoke phrase with nothing flagged.",
            "And he's gone, gone with the breeze",
            "You should know that that sentence wasn't wrong.",
            "She had had dessert on the balcony.",
            "The practitioner's side",
            "An antimatter particle",
            "The theory",
            "She had coffee at the Foo-bar bar.",
            "Don't just play the game - play the game.",
            "Green greenery",
        ),
    ),
    (
        "malapropisms",
        ("Found in the Infinitesimal Universe.",),
        ("Smoke phrase with nothing flagged.",),
    ),
    (
        "mixed_metaphors",
        (
            "The project produced a huge bottleneck.",
            "Writing tests is not rocket surgery.",
        ),
        ("Smoke phrase with nothing flagged.",),
    ),
    (
        "mondegreens",
        ("..and Lady Mondegreen.",),
        (
            "Smoke phrase with nothing flagged.",
            "... and laid him on the green.",
        ),
    ),
    (
        "needless_variants",
        ("It was an extensible telescope.",),
        ("Smoke phrase with nothing flagged.",),
    ),
    (
        "nonwords",
        ("The test was good irregardless.",),
        ("Smoke phrase with nothing flagged.",),
    ),
    (
        "oxymorons",
        ("He needed an exact estimate.", "Are we advancing backward?"),
        ("Smoke phrase with nothing flagged.",),
    ),
    (
        "skunked_terms",
        ("I gave an impassionate defence of the situation.",),
        ("Smoke phrase with nothing flagged.",),
    ),
    (
        "uncomparables",
        (
            "The item was more unique.",
            "This sentence is very unique.",
            "This sentence is very\nunique.",
            "Kind of complete.",
            "An increasingly possible future.",
            "It was the least possible outcome.",
        ),
        (
            "Smoke phrase with nothing flagged.",
            "Every perfect instance.",
            "A more perfect union.",
            "A more possible future.",
            "But is it at least possible?",
            "It's at least possible for that thing to exist",
            (
                "It is at least possible of achievement and that our actions"
                "are at least possible contributions to bringing it about."
            ),
            (
                "It should be at least possible for the Department to improve"
                "its position and for the citizens generally to"
                "enjoy prosperity."
            ),
        ),
    ),
    (
        "cliches.hell",
        ("I was at xyz and then all hell broke loose again.",),
        ("Smoke phrase with nothing flagged.",),
    ),
    (
        "cliches.misc",
        (
            "Worse than a fate worse than death.",
            "Since last year, he's got his hands full.",
            "The thought leader is here to influence.",
            "He's a chip off the old block.",
            "You sound like a broken record.",
            "You gave me a crash course in xyz.",
            "You always had a green thumb.",
            "You know the score.",
            "You payed out of pocket for years.",
            "I feel sick as a dog since yesterday.",
            "I feel sick as a dog.",
            "You, me and that uphill battle.",
            "You, me and that uphill battle with him.",
            "Will wonders never cease?",
            "It's a matter of concern.",
        ),
        ("Smoke phrase with nothing flagged.", "No cliches here."),
    ),
    (
        "dates_times.am_pm",
        (
            "It happened at 7 am.",
            "It happened at 7a.m.",
            "It happened at 12 a.m.",
            "It happened at 12 p.m.",
            "It happened at 7a.m. in the morning.",
        ),
        (
            "Smoke phrase with nothing flagged.",
            "It happened at 7 a.m.",
            "On Wed, Sep 21, 2016 at 11:42 AM -0400, X wrote:",
            "It happened at 7 a.m.",
            "It happened at noon.",
            "It happened at 7 a.m.",
        ),
    ),
    (
        "dates_times.dates",
        (
            "It happened in the 90's.",
            "It happened in the 1980's.",
            "It happened from 2000-2005.",
            "It happened in August, 2008.",
            "It happened in August of 2008.",
            "The 50's were swell.",
            "From 1999-2002, Sally served as chair of the committee.",
        ),
        (
            "Smoke phrase with nothing flagged.",
            "It happened in the 90s.",
            "It happened in the 1980s.",
            "It happened from 2000 to 2005.",
            "It happened in August 2008.",
            "It happened in August 2008.",
        ),
    ),
    (
        "misc.apologizing",
        ("To say something more research is needed.",),
        ("Smoke phrase with nothing flagged.",),
    ),
    (
        "misc.back_formations",
        ("It is an improprietous use.",),
        ("Smoke phrase with nothing flagged.",),
    ),
    (
        "misc.but",
        (
            'But I never start with the word "but".',
            "But why are you like that.",
            "This is a paragraph.\n\nBut this starts a new paragraph",
            "Some text here.\n\nBut wait, there's more",
        ),
        (
            "Smoke phrase with nothing flagged.",
            (
                'I never start with the word "but",'
                "\nbut might use it after a linebreak."
            ),
            "Butter is the best.",
            "This is cool! But that not so much.",
            "Is this cool? But that not so much.",
        ),
    ),
    (
        "misc.capitalization",
        (
            "It goes back to the stone age.",
            "A nice day during Winter.",
            "A nice day in june.",
            "It happened on friday.",
        ),
        (
            "Smoke phrase with nothing flagged.",
            "Smoke Stone Age with nothing flagged.",
            "Smoke winter with nothing flagged",
        ),
    ),
    (
        "misc.composition",
        (
            "His story is not honest.",
            "Her story is a strange one.",
            "He had not succeeded.",
            "He had not succeeded with that.",
        ),
        ("Smoke phrase with nothing flagged.",),
    ),
    (
        "misc.currency",
        ("It cost $10 dollars.",),
        ("Smoke phrase with nothing flagged.",),
    ),
    (
        "misc.debased",
        ("This leaves much to be desired.",),
        ("Smoke phrase with nothing flagged.",),
    ),
    (
        "misc.greylist",
        (
            "She should utilize her knowledge.",
            "This is obviously an inadvisable word to use obviously.",
            "I utilize a hammer to drive nails into wood.",
            "Do you know anyone who *needs* to utilize the word utilize?",
        ),
        ("Smoke phrase with nothing flagged.",),
    ),
    (
        "misc.illogic",
        (
            "We should preplan the trip.",
            "To coin a phrase from him, No diggity",
            "Not Without your collusion you won't'.",
            "it fills a much-needed gap",
        ),
        ("Smoke phrase with nothing flagged.",),
    ),
    (
        "misc.inferior_superior",
        ("It was more inferior than the alternative.",),
        ("Smoke phrase with nothing flagged.",),
    ),
    (
        "misc.institution_name",
        ("I went to the Virginia Polytechnic and State University.",),
        ("Smoke phrase with nothing flagged.",),
    ),
    (
        "misc.latin",
        ("And ceteris paribus, it was good.",),
        ("Smoke phrase with nothing flagged.",),
    ),
    (
        "misc.many_a",
        ("There were many a day I thought about it.",),
        ("Smoke phrase with nothing flagged.",),
    ),
    (
        "misc.metadiscourse",
        ("It's based on the rest of this article.",),
        ("Smoke phrase with nothing flagged.",),
    ),
    (
        "misc.narcissism",
        (
            (
                "In recent years, an increasing number of scientists"
                " have studied the problem in detail."
            ),
        ),
        ("Smoke phrase with nothing flagged.",),
    ),
    (
        "misc.not_guilty",
        ("She is not guilty beyond a reasonable doubt.",),
        ("Smoke phrase with nothing flagged.",),
    ),
    (
        "misc.phrasal_adjectives",
        ("There were across the board discounts.", "He ran swiftly-fast."),
        (
            "Smoke phrase with nothing flagged.",
            "The not-so-hotly-contested result was fine.",
        ),
    ),
    (
        "misc.false_plurals",
        ("There were several phenomenons.", "I give you many kudos."),
        ("Smoke phrase with nothing flagged.",),
    ),
    (
        "misc.preferred_forms",
        (
            "It was almost haloween.",
            "He is Chief Justice of the Supreme Court of the United States.",
            "Meantime, I had tea.",
            "He jumped off of the couch.",
            "In the meanwhile, something happened.",
            "She went to bed; meantime, I had tea.",
        ),
        (
            "Smoke phrase with nothing flagged.",
            "Meanwhile, I had tea.",
            "A 4th order low-pass with a roll-off of 24 db/octave",
            "In the meantime, something happened.",
            "She went to bed; meanwhile, I had tea.",
        ),
    ),
    (
        "misc.pretension",
        ("We need to reconceptualize the project.",),
        ("Smoke phrase with nothing flagged.",),
    ),
    (
        "misc.professions",
        ("I really need a shoe repair guy.",),
        ("Smoke phrase with nothing flagged.",),
    ),
    (
        "misc.scare_quotes",
        ("What was the 'take-home message'?",),
        ("Smoke phrase with nothing flagged.",),
    ),
    (
        "misc.suddenly",
        ("Suddenly, it all made sense.",),
        ("Smoke phrase with nothing flagged.",),
    ),
    (
        "misc.tense_present",
        (
            "I did it on accident honestly.",
            "I did it On accident honestly.",
            "Told you something between you and i.",
            "Told you something between you and I.",
            "I feel nauseous.",
        ),
        (
            "Smoke phrase with nothing flagged.",
            "I did it by accident honestly.",
        ),
    ),
    (
        "misc.waxed",
        ("They really could wax poetically.",),
        (
            "Smoke phrase with nothing flagged.",
            "Wax me if you can.",
            "He waxed poetic.",
        ),
    ),
    (
        "misc.whence",
        ("Go back from whence you came!",),
        ("Smoke phrase with nothing flagged.",),
    ),
    (
        "redundancy.misc",
        (
            "The table was rectangular in shape.",
            "It was blatantly obvious what to do next.",
            "Taking the package was absolutely essential.",
            "He often repeated the old adage.",
            "Associate together in groups.",
        ),
        ("Smoke phrase with nothing flagged.",),
    ),
    (
        "redundancy.ras_syndrome",
        ("Please enter your PIN number.",),
        ("Smoke phrase with nothing flagged.",),
    ),
    (
        "spelling.able_atable",
        ("There was a demonstratable difference.",),
        ("Smoke phrase with nothing flagged.",),
    ),
    (
        "spelling.able_ible",
        ("It was a sensable decision.",),
        ("Smoke phrase with nothing flagged.",),
    ),
    (
        "spelling.ally_ly",
        ("She was accidently fired.",),
        ("Smoke phrase with nothing flagged.",),
    ),
    (
        "spelling.ance_ence",
        ("The resistence was futile.",),
        ("Smoke phrase with nothing flagged.",),
    ),
    (
        "spelling.athletes",
        ("One of the greats: Cal Ripkin.",),
        ("Smoke phrase with nothing flagged.",),
    ),
    (
        "spelling.ely_ly",
        ("She was completly unprepared.",),
        ("Smoke phrase with nothing flagged.",),
    ),
    (
        "spelling.em_im_en_in",
        ("We shall imbark on a voyage.",),
        ("Smoke phrase with nothing flagged.",),
    ),
    (
        "spelling.er_or",
        ("She met with the invester.",),
        ("Smoke phrase with nothing flagged.",),
    ),
    (
        "spelling.in_un",
        ("The plan was unfeasible.",),
        ("Smoke phrase with nothing flagged.",),
    ),
    (
        "spelling.misc",
        ("I like this alot.", "I stay 'til sundown."),
        ("Smoke phrase with nothing flagged.",),
    ),
    (
        "spelling.ve_of",
        ("This could of been the third test.",),
        ("Smoke phrase with nothing flagged.",),
    ),
    (
        "terms.animal_adjectives",
        ("It was some bird-like creature.",),
        ("Smoke phrase with nothing flagged.",),
    ),
    (
        "terms.denizen_labels",
        ("He was definitely a Hong Kongite.",),
        ("Smoke phrase with nothing flagged.",),
    ),
    (
        "terms.eponymous_adjectives",
        ("The writing wasn't Shakespearian.",),
        ("Smoke phrase with nothing flagged.",),
    ),
    (
        "terms.venery",
        ("There was a group of alligators.", "There was a bunch of wombats."),
        (
            "Smoke phrase with nothing flagged.",
            "There was a congregation of alligators.",
            "There was a wisdom of wombats.",
        ),
    ),
    (
        "typography.diacritical_marks",
        ("He saw the performance by Beyonce.",),
        ("Smoke phrase with nothing flagged.",),
    ),
    (
        "typography.symbols",
        (
            "The long and winding road...",
            "Show me the money! (C)",
            "Show me the money! (c)",
            "The Fresh Maker (TM)",
            "The Fresh Maker (tm)",
            "Just Do It (R)",
            "Just Do It (r)",
            "This is a sentence.   This is another.",
            "It is obvious that 2 x 2 = 4.",
            'This is "another sentence". How faulty.',
            '"This should produce an error", he said.',
            'Alas, "it should here too".',
        ),
        (
            "Smoke phrase with nothing flagged.",
            "This is “a sentence”. Look at it.",
            "“This should produce no error”, he said.",
            "A 'singular' should not, though.",
        ),
    ),
    (
        "weasel_words",
        ("The book was very interesting.",),
        (
            "Smoke phrase with nothing flagged.",
            "Very well, Headmaster, thank you.",
            "The discovery and development of new approaches.",
        ),
    ),
    (
        "restricted.elementary",
        (
            "Cells make up your body.",
            "I love clowns.",
            "I hate cells and clowns.",
        ),
        (
            "A boy and his goat went to a farm.",
            "I am tired.",
            "Your body is made of water.",
        ),
    ),
    (
        "restricted.top1000",
        ("I am tired.", "I hate broccoli.", "I am tired and hate broccoli."),
        (
            "I am blonde.",
            "I'm gonna listen to music tonight.",
            "I will go to sleep because I have school.",
        ),
    ),
    (
        "industrial_language.airlinese",
        (
            "This is your captain speaking. We will be taking off momentarily.",
            "We deplaned promptly after.",
        ),
        (
            "Smoke phrase with nothing flagged.",
            "Did that car just hydroplane?",
            "I know how to operate a planing mill.",
        ),
    ),
    (
        "industrial_language.bureaucratese",
        ("I hope the report meets with your approval.",),
        ("Smoke phrase with nothing flagged.",),
    ),
    (
        "industrial_language.chatspeak",
        ("BRB getting coffee.",),
        ("Smoke phrase with nothing flagged.",),
    ),
    (
        "industrial_language.commercialese",
        ("We regret to inform you of this.",),
        ("Smoke phrase with nothing flagged.",),
    ),
    (
        "industrial_language.corporate_speak",
        ("We will circle back around to it.",),
        ("Smoke phrase with nothing flagged.", "We will discuss it later."),
    ),
    (
        "industrial_language.jargon",
        ("I agree it's in the affirmative.",),
        ("Smoke phrase with nothing flagged.",),
    ),
    (
        "social_awareness.lgbtq",
        (
            "He was a homosexual man.",
            "My sexual preference is for women.",
            "I once met a fag.",
        ),
        (
            "Smoke phrase with nothing flagged.",
            "They were a gay couple.",
            "I once met a gay man.",
            "Homosexual.",
        ),
    ),
    (
        "social_awareness.nword",
        ("Have i used the n-word?",),
        ("Smoke phrase with nothing flagged.",),
    ),
    (
        "social_awareness.sexism",
        (
            "The legal team had two lawyers and a lady lawyer.",
            "Oh chairperson - why so sad.",
            "You get the mailperson.",
        ),
        (
            "Smoke phrase with nothing flagged.",
            "Hello Mr. Birdperson. You look good.",
            "Hello Mr. birdperson. still looking good.",
        ),
    ),
    (
        "spelling.consistency",
        (
            "The centre of the arts is the art center.",
            "The most chocolatey cake had the chocolaty frosting.",
        ),
        (
            "Smoke phrase with nothing flagged.",
            "The centre for the arts is the art centre.",
            "The center for the arts is the art center.",
        ),
    ),
    (
        "typography.punctuation",
        (
            "This is bad.  Not consistent. At all.",
            "See Smith et. al.",
            "So exaggerated!!!",
            "Really??",
            "What is going on?!",
            "What is going on!?",
            "I'm really excited!!",
            "I'm really excited! Really!",
            "Sally sells seashells and they were too expensive!!!!",
            "Sally sells seashells and they were too expensive! They were not!",
            "Why does Sally sell such expensive seashells??",
            "Why does Sally sell such expensive seashells????",
        ),
        (
            "Smoke phrase with nothing flagged.",
            "This is good. Only one space each time. Every time.",
            "A cat can sleep 20.5 hours a day.",
            "I asked the Prof. what to do",
            "Sally sells seashells and they were too expensive!",
            "Why does Sally sell such expensive seashells?",
        ),
    ),
    (
        "psychology",
        (
            "The defendant took a lie detector test.",
            "The effect was highly signficant at p = 0.00.",
            "I've been practicing mental telepathy.",
        ),
        ("Smoke phrase with nothing flagged.",),
    ),
)
