# ----------------------------------------------------------------------
# This is a hobby project made to get better with python as a language
# and it's modules. I will keep it updated as long as it's not too much
# work. Feel free to add any features or make suggestions!
# ----------------------------------------------------------------------


import time
from selenium import webdriver

# Check to see if modules have been imported correctly
if not webdriver:
    print("Could not import webdriver module!")
if not time:
    print("Could not import time module!")


def search_for_movie(browser, movie):
    """This will be our search in the imdb movie database"""
    try:
        element = browser.find_element_by_id("suggestion-search")
        print("Found search bar!")
        if element:
            print("Found movie!")
            element.send_keys(movie)
            time.sleep(1)  # Sleep is introduced to let the user see what is going on!
            result = browser.find_element_by_class_name("react-autosuggest__suggestions-list")
            if result:
                print("Trying first result!")
                option = result.find_element_by_id("react-autowhatever-1--item-0")
                option.click()
                time.sleep(1)
                current_url = browser.current_url
                browser.get(current_url[0:37] + "reviews?ref_=tt_ov_rt")  # All review pages have identical ending href
                time.sleep(1)
            else:
                print("Had to manually search for result")
                element.submit()
    except ModuleNotFoundError as message:
        print("We couldn't find the search bar!")
        raise SystemExit(message)


def save_reviews_to_file(browser, movie):
    """If no file exists, we create an empty file"""
    try:
        print("Creating file" + movie + ".txt")
        f = open(movie + ".txt", "x")
        f.close()
    except FileExistsError:
        print("Found file already.")

    with open(movie + ".txt", mode="w") as file:
        # We need to handle spoiler warnings, as they do not show the full review
        button = browser.find_element_by_class_name("expander-icon-wrapper.spoiler-warning__control")
        if button:
            button.click()  # Spoiler_warning == False (?)
            time.sleep(1)
        text = browser.find_element_by_class_name("text.show-more__control")
        print("Found review!")

        # Sometimes the text class is not found
        if not text:
            time.sleep(1)
            text = browser.find_element_by_class_name("text.show-more__control")  # Maybe now
        rating = browser.find_element_by_class_name("rating-other-user-rating")
        to_write = text.text
        to_rate = rating.text
        file.writelines(to_rate + "\n" + to_write)

        # The program closes after 5 seconds for convenience
        time.sleep(5)
        browser.quit()


def main():
    print("Search for a movie: ")
    movie = input()

    # Make sure to add chromedriver to PATH before using the app!
    browser = webdriver.Chrome("./files/chromedriver.exe")
    browser.get("https://www.imdb.com")
    time.sleep(1)
    search_for_movie(browser, movie)
    save_reviews_to_file(browser, movie)


main()

