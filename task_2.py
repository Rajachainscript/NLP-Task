import string

def clean_and_tokenize(text):
    translator = str.maketrans('', '', string.punctuation)
    cleaned_text = text.lower().translate(translator)
    return set(cleaned_text.split())


def simplified_lesk(sentence, target_word, word_senses):

    if not word_senses or target_word not in word_senses:
        return None

    sentence_words = clean_and_tokenize(sentence)

    if target_word.lower() in sentence_words:
        sentence_words.remove(target_word.lower())
    best_sense = None
    max_overlap = -1
    for sense_key, sense_info in word_senses[target_word].items():
        gloss = sense_info['gloss']
        gloss_words = clean_and_tokenize(gloss)


        overlap = len(sentence_words & gloss_words)


        if overlap > max_overlap:
            max_overlap = overlap
            best_sense = sense_key

    return best_sense



word_senses = {
    "bank": {
        "financial_institution": {
            "gloss": "a financial establishment that invests money deposited by customers, pays it out when required, and lends money to borrowers. also called a place where money is kept for savings or investment."
        },
        "river_side": {
            "gloss": "the land alongside or sloping down to a river or lake. often covered in vegetation like grass or trees."
        },
        "rely": {
            "gloss": "to depend on or trust someone or something for support or help."
        },
        "array": {
            "gloss": "a systematic arrangement of objects, usually in rows and columns. for example, a bank of computers or a bank of switches."
        }
    },
    "crane": {
        "bird": {
            "gloss": "a tall, long-legged, long-necked bird, often with a graceful appearance. species include the sandhill crane and the whooping crane."
        },
        "machine": {
            "gloss": "a large, tall machine used for moving heavy objects by suspending them from a projecting arm or beam. common on construction sites."
        },
        "stretch": {
            "gloss": "to stretch out one""s body or neck, especially to see something better. like craning your neck to see over a crowd."
        }
    },
    "match": {
        "contest": {
            "gloss": "a organized sports game or competition between two individuals or teams. for example, a football match or a boxing match."
        },
        "fire_lighter": {
            "gloss": "a short, slender piece of wood or cardboard coated on one end with a chemical that ignites when rubbed against a rough surface. used for lighting fires."
        },
        "compatible": {
            "gloss": "a person or thing that is equal to or corresponds to another in quality, size, or value. they are a good match for each other."
        },
        "correspond": {
            "gloss": "to have the same pattern, color, or design; to be equal or harmonious. the curtains match the paint."
        }
    },
    "bat": {
        "animal": {
            "gloss": "a flying mammal with wings formed from a membrane stretched between the limbs and body. most are nocturnal and use echolocation."
        },
        "sports_equipment": {
            "gloss": "a wooden or metal club used in sports like baseball or cricket to hit the ball. typically has a rounded, often cylindrical, hitting surface."
        },
        "flutter": {
            "gloss": "to flutter or wink rapidly, as in \"she didn't bat an eyelid\" meaning she showed no surprise or reaction."
        }
    },
    "light": {
        "illumination": {
            "gloss": "the natural agent that stimulates sight and makes things visible. emitted by sources like the sun, lamps, or fire."
        },
        "not_heavy": {
            "gloss": "of little weight; not heavy. easy to lift or carry. for example, a light package or a light meal."
        },
        "pale_color": {
            "gloss": "of a color: pale, containing a lot of white. for example, light blue as opposed to dark blue."
        },
        "ignite": {
            "gloss": "to set something on fire; to begin to burn. to light a candle or a match."
        }
    }
}



test_cases = [
    ("I need to go to the bank to withdraw some cash for the deposit.", 'bank'),
    ("The children played on the muddy bank of the river, skipping stones.", 'bank'),
    ("You can bank on her to finish the project on time; she's very reliable.", 'bank'),
    ("The server room contained a large bank of blinking lights and drives.", 'bank'),

    ("We saw a beautiful sandhill crane wading in the marsh at dawn.", 'crane'),
    ("The construction crew used a massive crane to lift the steel beam into place.", 'crane'),
    ("She had to crane her neck to see the stage over the tall people in front of her.", 'crane'),

    ("The championship match between the two teams was incredibly intense.", 'match'),
    ("He struck the match against the box to light the campfire.", 'match'),
    ("We need to find a donor whose blood type is a match for the patient.", 'match'),
    ("Your socks don't match your shirt; one is blue and the other is green.", 'match'),

    ("A single bat flying with wings and go  eat thousands of insects in one night.", 'bat'),
    ("The hitter to hit the cricket ball and  bat with all his might and connected for a run.", 'bat'),
    ("She heard the shocking news and didn't even bat an eye.", 'bat'),

    ("The sun provides light and warmth to the Earth.", 'light'),
    ("This suitcase is very light; I can carry it easily.", 'light'),
    ("She painted her room a pleasant light yellow color.", 'light'),
    ("Could you please light the candles on the birthday cake?", 'light'),
    ("The financial transaction was completed securely.", 'bank'),
    ("A light breeze blew.", 'light'),
    ("We need a match for the game and the fire.", 'match'),
    ("This is a completely unrelated sentence about programming.", 'bank'),
    ("The river's bank was eroded after the storm.", 'bank'),
    ("The BANK is closed on Sundays.", 'bank'),
]

for sentence, target  in test_cases:
    result = simplified_lesk(sentence, target, word_senses)
    print(f"Sentence: {sentence}\nTarget: {target}\nPredicted: {result}")
