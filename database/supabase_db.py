from supabase import create_client
from datetime import datetime

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

def add_user(email, username, password):

    try:

        print("Creating user...")

        result = supabase.table("users").insert({
            "email": email,
            "username": username,
            "password": password,
            "role": "user",
            "email_verified": False
        }).execute()

        print("USER RESULT:")
        print(result)

        supabase.table("settings").insert({
            "username": username,
            "train_troop" : "T1 Infantry"
        }).execute()

        supabase.table("account_status").insert({
            "username": username,
            "shield_active": False,
            "shield_time": "",
            "shield_seconds": 0
        }).execute()

        print("User created successfully")

    except Exception as e:
        print("ERROR:")
        print(e)

def get_user_settings(username):

    result = (
        supabase
        .table("settings")
        .select("*")
        .eq("username", username)
        .execute()
    )
    # print(result.data)

    if result.data:
        return result.data[0]

    return {
        "check_shield" : False,
        "auto_colloseum": False,
        "auto_gathering": False,
        "auto_training": False,
        "auto_healing": False,
        "auto_collecting": False
    }

def save_settings(
    username,
    check_shield,
    auto_colosseum,
    auto_gathering,
    auto_training,
    auto_healing,
    auto_collecting,
    train_troop
):

    supabase.table("settings").upsert({

        "username": username,

        "check_shield": check_shield,
        "auto_colosseum": auto_colosseum,
        "auto_gathering": auto_gathering,
        "auto_training": auto_training,
        "auto_healing": auto_healing,
        "auto_collecting": auto_collecting,
        "train_troop": train_troop


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
        "shield_seconds": shield_seconds,
        "last_updated": datetime.utcnow().isoformat()

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


#---------------------------------
# unique username and emial for registration
#---------------------------------
def username_exists(username):

    result = (
        supabase
        .table("users")
        .select("username")
        .eq("username", username)
        .execute()
    )

    return len(result.data) > 0

def email_exists(email):

    result = (
        supabase
        .table("users")
        .select("email")
        .eq("email", email)
        .execute()
    )

    return len(result.data) > 0

