from anime_manager import AnimeManager


def my_clear_console():
    print("\n\n\n\n\n" * 6)


def get_user_input():
    ask = True
    while ask:
        print("-----------------------------------------------------------------------------------------------------\n")
        choice = (input("Enter the ID of the anime you want to watch to check the anime's info.\n"
                        "Enter 'n' to go to the 'Next Page'\n"
                        "Enter 'b' to go to the 'Previous Page'\n"
                        "Enter 'exit' to close the app.\n- ")).lower()
        try:
            anime_id = int(choice)
            if 0 <= anime_id <= len(anime_manager.current_anime_chunk) - 1:
                ask = False
                anime_manager.set_current_anime(anime_id)
                anime_manager.anime_page()
                choice_ask_download = anime_manager.ask_download()
                if choice_ask_download == 'y':
                    choice_ask_typology = anime_manager.ask_typology()
                    if choice_ask_typology != -1:
                        anime_manager.download_anime_episodes(choice_ask_typology)
                    else:
                        input("Operation cancelled.\nPress Enter to continue...")
            else:
                print("[MAIN 26] Error!!! Invalid anime ID!")
        except ValueError as e:
            if choice == 'n':
                ask = False
                anime_manager.next_page()
            elif choice == 'b':
                ask = False
                anime_manager.previous_page()
            elif choice == 'exit':
                ask = False
                anime_manager.exit()
            else:
                print(f"[MAIN 38] Error!!! Invalid command!\n"
                      f"Technical Error: {e}")


on = True

anime_manager = AnimeManager()

while anime_manager.current_page != -1:
    my_clear_console()
    print(f"Current page = {anime_manager.current_page}")
    for index, anime in enumerate(anime_manager.current_anime_chunk):
        print(f"{index}) {anime}")
    get_user_input()
    print("------------------------------------------------------------------------")
