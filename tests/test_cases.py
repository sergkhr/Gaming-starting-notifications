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
    # gpt made tests, he decided that inviter is not participant - will check later
    {
        "name": "simple_dota_gathering",
        "messages": [
            {"text": "го дота", "user_id": "u1", "user_name": "User 1"},
            {"text": "я", "user_id": "u2", "user_name": "User 2"},
            {"text": "через 20 минут буду", "user_id": "u3", "user_name": "User 3"},
        ],
        "expected_sessions": 1,
        "expected_messages": 3,
        "expected_participants": {"u2", "u3"},
        "expected_declined_users": set(),
    },
    {
        "name": "minecraft_gathering",
        "messages": [
            {"text": "когда в майн?", "user_id": "u1", "user_name": "User 1"},
            {"text": "я бы зашел", "user_id": "u2", "user_name": "User 2"},
            {"text": "можно вечером", "user_id": "u3", "user_name": "User 3"},
        ],
        "expected_sessions": 1,
        "expected_messages": 3,
        "expected_participants": {"u2", "u3"},
        "expected_declined_users": set(),
    },
    {
        "name": "lethal_gathering",
        "messages": [
            {"text": "че гоу в леталку", "user_id": "u1", "user_name": "User 1"},
            {"text": "можно", "user_id": "u2", "user_name": "User 2"},
            {"text": "буду через 10 минут", "user_id": "u3", "user_name": "User 3"},
            {"text": "я тоже", "user_id": "u4", "user_name": "User 4"},
        ],
        "expected_sessions": 1,
        "expected_messages": 4,
        "expected_participants": {"u2", "u3", "u4"},
        "expected_declined_users": set(),
    },
    {
        "name": "failed_gathering",
        "messages": [
            {"text": "го дота", "user_id": "u1", "user_name": "User 1"},
            {"text": "не могу", "user_id": "u2", "user_name": "User 2"},
            {"text": "я пас", "user_id": "u3", "user_name": "User 3"},
        ],
        "expected_sessions": 1,
        "expected_messages": 3,
        "expected_participants": set(),
        "expected_declined_users": {"u2", "u3"},
    },
    {
        "name": "discord_gathering",
        "messages": [
            {"text": "го факторио", "user_id": "u1", "user_name": "User 1"},
            {"text": "создавай лобби", "user_id": "u2", "user_name": "User 2"},
            {"text": "го в дс", "user_id": "u3", "user_name": "User 3"},
            {"text": "буду", "user_id": "u4", "user_name": "User 4"},
        ],
        "expected_sessions": 1,
        "expected_messages": 4,
        "expected_participants": {"u4"},
        "expected_declined_users": set(),
    },
    {
        "name": "vibe_only_should_not_attach (wdym gpt?)",
        "messages": [
            {"text": "го дота", "user_id": "u1", "user_name": "User 1"},
            {"text": "жестко", "user_id": "u2", "user_name": "User 2"},
        ],
        "expected_sessions": 1,
        "expected_messages": 1,
        "expected_participants": set(),
        "expected_declined_users": set(),
    },
    {
        "name": "vibe_answer",
        "messages": [
            {"text": "го дота", "user_id": "u1", "user_name": "User 1"},
            {"text": "вайб", "user_id": "u2", "user_name": "User 2"},
        ],
        "expected_sessions": 1,
        "expected_messages": 2,
        "expected_participants": {"u2"},
        "expected_declined_users": set(),
    },
]