from supabase import create_client

SUPABASE_URL = "https://qmvwgzvnbiyadnlsvnkr.supabase.co"
SUPABASE_KEY = "sb_publishable_yEaJq55BMdRBzScaiJ54rg_li3TWoV5"

supabase = create_client(
    SUPABASE_URL,
    SUPABASE_KEY
)

def authenticate_user(username, password):

    result = (
        supabase
        .table("users")
        .select("*")
        .eq("username", username)
        .eq("password", password)
        .execute()
    )

    # print(result.data)

    return len(result.data) > 0

def add_user(username, password):
    try:
        supabase.table("users").insert({
            "username": username,
            "password": password
        }).execute()
    except Exception as e:
        print(e)

def get_user_settings(username):

    result = (
        supabase
        .table("settings")
        .select("*")
        .eq("username", username)
        .execute()
    )

    if result.data:
        return result.data[0]

    return {
        "check_shield" : False,
        "auto_colloseum": False,
        "auto_gathering": False,
        "auto_training": False,
        "auto_healing": False,
        "auto_collecting": False,
    }

def save_settings(
    username,
    check_shield,
    auto_colosseum,
    auto_gathering,
    auto_training,
    auto_healing,
    auto_collecting
):

    supabase.table("settings").upsert({

        "username": username,

        "check_shield": check_shield,
        "auto_colosseum": auto_colosseum,
        "auto_gathering": auto_gathering,
        "auto_training": auto_training,
        "auto_healing": auto_healing,
        "auto_collecting": auto_collecting

    }).execute()
    # print(response)

def update_shield_status(
    username,
    shield_active,
    shield_time,
    shield_seconds
):

    supabase.table(
        "account_status"
    ).upsert({

        "username": username,
        "shield_active": shield_active,
        "shield_time": shield_time,
        "shield_seconds" : shield_seconds

    }).execute()

def get_shield_status(username):

    result = (
        supabase
        .table("account_status")
        .select(
            "shield_active,shield_time"
        )
        .eq(
            "username",
            username
        )
        .execute()
    )

    if result.data:
        return result.data[0]

    return None