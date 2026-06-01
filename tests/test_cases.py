SCORE_TEST_CASES = [

    {
    "name": "vibe_positive",
    "text": "а есть вайб?"
    },

    {
        "name": "vibe_negative",
        "text": "а нет вайба?"
    },

    {
        "name": "want_to_play_dota",
        "text": "в доту охота"
    },

    {
        "name": "need_to_gather",
        "text": "надо собраться"
    },

    {
        "name": "need_to_gather_and_play",
        "text": "надо собраться покатать"
    },

    {
        "name": "who_will_join_question",
        "text": "кто будет?"
    },

    {
        "name": "who_will_join_statement",
        "text": "кто будет"
    },

    {
        "name": "who_will_join_dota_question",
        "text": "кто будет в доту?"
    },

    {
        "name": "who_will_join_dota_statement",
        "text": "кто будет в доту"
    },

    {
        "name": "who_in_dota_question",
        "text": "кто в доту?"
    },

    {
        "name": "who_in_dota_statement",
        "text": "кто в доту"
    },

    {
        "name": "where_is_everyone",
        "text": "а че где все?"
    },
    
    {
        "name": "simple_dota_invite",
        "text": "го дота"
    },

    {
        "name": "minecraft_question",
        "text": "когда в майн?"
    },

    {
        "name": "dota_with_urgency",
        "text": "через 20 минут в доту"
    },

    {
        "name": "vibe_invite",
        "text": "есть вайб на доту после 12?"
    },

    {
        "name": "need_one_player",
        "text": "нужен еще один в леталку"
    },

    {
        "name": "discord_gathering",
        "text": "го в дс на факторио"
    },

    {
        "name": "positive_response",
        "text": "я в деле"
    },

    {
        "name": "soon_response",
        "text": "буду через 15 минут"
    },

    {
        "name": "negative_response",
        "text": "не могу сегодня"
    },

    {
        "name": "game_news",
        "text": "вышел новый патч для доты"
    },

]



ACTION_TEST_CASES = [

    {
        "name": "ignore_case",
        "score": 1
    },

    {
        "name": "watch_lower_boundary",
        "score": 5
    },

    {
        "name": "watch_middle",
        "score": 7
    },

    {
        "name": "notify_boundary",
        "score": 10
    },

    {
        "name": "notify_high",
        "score": 20
    }
]


SESSION_TEST_CASES = [

    {
        "name": "simple_dota_gathering",

        "messages": [
            "го дота",
            "я",
            "через 20 минут буду"
        ]
    },

    {
        "name": "minecraft_gathering",

        "messages": [
            "когда в майн?",
            "я бы зашел",
            "можно вечером"
        ]
    },

    {
        "name": "lethal_gathering",

        "messages": [
            "че гоу в леталку",
            "можно",
            "буду через 10 минут",
            "я тоже"
        ]
    },

    {
        "name": "failed_gathering",

        "messages": [
            "го дота",
            "не могу",
            "я пас"
        ]
    },

    {
        "name": "discord_gathering",

        "messages": [
            "го факторио",
            "создавай лобби",
            "го в дс",
            "буду"
        ]
    }
]