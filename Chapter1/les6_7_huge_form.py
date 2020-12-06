from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# link_huge_form = "http://suninjuly.github.io/huge_form.html"


def main(browser, link_huge_form):
    dict_text = {
        'First name:': 'first_name',
        'Last name:': 'last_name',
        'E-mail:': 'e@e-mail.edu',
        'Country:': 'USSR',
        'City:': 'Smolensk',
        'Street:': 'Lenina',
        'Your pets:': 'Fox',
        'Favorite movies:': 'Serial',
        'Favorite artists:': 'All Metal',
        'Favorite albums:': 'Sehnsucht',
        'Favorite cars:': 'leg\'s',
        'Your hobbies:': 'Rollerblading',
        'Your favorite books:': 'technical',
        'What is your favorite sports?': 'sport sleep',
        'What do you do on your weekends?': 'working',
        'Do you like travelling?': 'Yep',
        'Do you like Disney cartoons?': 'Yep',
        'How old are you?': '30',
        'Blood type:': '-',
        'Favorite color:': 'Green',
        'Favorite food:': 'meat',
        'Favorite cake:': 'tiramisu',
        'Favorite magazine:': 'online',
        'Favorite radio station:': 'Maximum',
        'Favorite actor:': 'Tenth',
        'Favorite actress:': 'Odri',
        'Text field:': 'Any text',
        'one or the other: QA/QC': 'both',
        'one or the other: jira/teamcity': 'both',
        'one or the other: severity/priority': 'urgency XD',
        'one or the other: bug/defect': 'Bug',
        'one or the other: python/java': 'Python',
        "First thing when you hear 'python':": 'Monty',
        "First thing when you hear 'selenium':": '34',
        "First thing when you hear 'pigeons'": 'toilet bowl flying',
        "First thing when you hear 'pinguins':": 'Tux',
        "First thing when you hear 'Trump':": 'pofig',
        "First thing when you hear 'yellow':": 'submarine',
        "First thing when you hear 'harry potter':": 'avada kedavra',
        "First thing when you hear 'socks':": 'put on'
    }
    try:
        # browser = webdriver.Firefox()
        browser.get(link_huge_form)

        # get list of field headers
        texts = browser.find_elements(By.CSS_SELECTOR, ".first_block")
        d = [x.text for x in texts]
        d = d[0].split("\n\n")

        # get list of input fields
        elements = browser.find_elements(By.TAG_NAME, "input")

        # input value in text field
        num_list_element = 0
        for element in elements:
           element.send_keys(dict_text[d[num_list_element]])
           num_list_element += 1

        # click on "Submit" button
        button = browser.find_element(By.CLASS_NAME, "btn")
        button.click()

        # get
        alert = browser.switch_to.alert
        text_alert = alert.text
        answer_value = text_alert[(text_alert.index(': ')) + 2:]
        time.sleep(1)
        alert.accept()

    finally:
        time.sleep(2)
        # browser.quit()

    return answer_value

if __name__ == '__main__':
    main()
