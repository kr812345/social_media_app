import subprocess

# Run the service corresponding to the user_app
def run_user_service():
    subprocess.Popen(["C:/Users/krish/OneDrive/Documents/Coding/sem-3/BD_7/version_2_social_media_app_main_ver/version_2/social_media_app/v_env/Scripts/python.exe", "user_app/app.py"])

# Run the service corresponding to the post_app
def run_post_service():
    subprocess.Popen(["C:/Users/krish/OneDrive/Documents/Coding/sem-3/BD_7/version_2_social_media_app_main_ver/version_2/social_media_app/v_env/Scripts/python.exe", "post_app/app.py"])

# Run the service corresponding to the dm_app
def run_DM_service():
    subprocess.Popen(["C:/Users/krish/OneDrive/Documents/Coding/sem-3/BD_7/version_2_social_media_app_main_ver/version_2/social_media_app/v_env/Scripts/python.exe","dm_app/app.py"])

if __name__ == '__main__':
    run_user_service()
    run_post_service()
    run_DM_service()

    # Graceful Termination of the two subprocesses
    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("\nTerminating both the processes. Alvida!")
