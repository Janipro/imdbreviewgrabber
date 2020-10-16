# ----------------------------------------------------------------------
# This is a hobby project made to get better with python as a language
# and it's modules. I will keep it updated as long as it's not too much
# work. Feel free to add any features or make suggestions!
# ----------------------------------------------------------------------


import time
import selenium
from selenium import webdriver

# Check to see if modules have been imported correctly
if not webdriver:
    print("Could not import webdriver module!")
if not time:
    print("Could not import time module!")


def search_for_movie(browser, movie):
    """This will be our search in the imdb movie database"""
    element = browser.find_element_by_id("suggestion-search")
    print("Found search bar!")
    if element:
        element.send_keys(movie)
        time.sleep(1)  # Sleep is introduced to let the user see what is going on!
        try:
            result = browser.find_element_by_class_name("react-autosuggest__suggestions-list")
            print("Found movie!")
            print("Trying first result!")
            option = result.find_element_by_id("react-autowhatever-1--item-0")
            option.click()
            time.sleep(1)
            current_url = browser.current_url
            browser.get(current_url[0:37] + "reviews?ref_=tt_ov_rt")  # All review pages have identical ending href
            time.sleep(1)
        except selenium.common.exceptions.NoSuchElementException:
            print("Had to manually search for result")
            element.submit()
            time.sleep(1)
            try:
                first_result = browser.find_element_by_class_name("result_text")
                if first_result:
                    first_result.click()
            except selenium.common.exceptions.NoSuchElementException:
                print("No movie found...")
                print("Try again? y/n")
                ans = input()
                if ans == "y":
                    browser.quit()
                    return main()
                else:
                    raise SystemExit


def save_reviews_to_file(browser, movie, amount):
    """We need to handle spoiler warnings, as they do not show the full review"""
    reviews = browser.find_elements_by_css_selector(".imdb-user-review")
    while len(reviews) < amount:
        extend = browser.find_element_by_class_name("load-more-data")
        extend.click()
        time.sleep(2)
        reviews = browser.find_elements_by_css_selector(".imdb-user-review")

    expandables = browser.find_elements_by_class_name("text.show-more__control.clickable")
    if expandables:
        for i in range(len(expandables)-1):
            expandables[i].click()
        time.sleep(1)

    spoilers = browser.find_elements_by_class_name("spoiler-warning")
    if spoilers:
        button = browser.find_elements_by_class_name("expander-icon-wrapper.spoiler-warning__control")
        for i in range(len(spoilers)-1):
            button[i].click()  # Spoiler_warning == False (?)
        time.sleep(1)

    if not reviews:
        print("This movie has no reviews..")
        print("Try again? y/n")
        ans = input()
        if ans == "y":
            browser.quit()
            return main()
        else:
            raise SystemExit

    print("Found " + str(len(reviews)) + " reviews!" + "\n" + "Selecting " + str(amount) + " of them.")
    ratings = browser.find_elements_by_class_name("rating-other-user-rating")
    usernames = browser.find_elements_by_class_name("display-name-link")
    texts = browser.find_elements_by_class_name("text.show-more__control")
    titles = browser.find_elements_by_class_name("title")

    # If no file exists, we create an empty file
    try:
        print("Creating file: " + movie + ".txt")
        f = open("./result/" + movie + ".txt", "x")
        f.close()
    except FileExistsError:
        print("Found file already..." + "\n" + "Updating...")

    with open("./result/" + movie + ".txt", mode="w") as file:
        for i in range(amount):
            username = usernames[i].text
            rating = ratings[i].text
            title = titles[i].text
            text = texts[i].text
            file.write("User: " + username + "\n" + "Rating: " + rating + "\n" + "Title: " + title + "\n" + text)
            file.write("\n" * 2)

        # The program closes after 2 seconds for convenience
        time.sleep(2)
        print("Done!")
        raise SystemExit


def main():
    print("Search for a movie: ")
    movie = input()
    print("How many reviews do you want to grab?")
    amount = int(input())

    # Make sure to add chromedriver to PATH before using the app!
    browser = webdriver.Chrome("./files/chromedriver.exe")
    browser.get("https://www.imdb.com")
    time.sleep(1)
    search_for_movie(browser, movie)
    save_reviews_to_file(browser, movie, amount)


main()

