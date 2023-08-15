import requests as req
import time
from bs4 import BeautifulSoup

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'
headers = {"User-agent": user_agent}

class Burses:
    def __init__(self, url):
        self.url = url
        self.resp = req.get(url)
        self.resp_text = self.resp.text
    def scrape(self, resp_text, tag, html_cls):
        soup = BeautifulSoup(self.resp_text, "lxml")
        data = str(soup.find(tag, class_=html_cls))
        return data

def scraping():
    
    freelancer = Burses("https://www.freelancer.com/jobs/python/")
    freelancer_data = freelancer.scrape(freelancer.resp_text, "p", "JobSearchCard-primary-description").replace("</p>", "")
    freelancer_data_lenght = len(freelancer_data[141:])
    print("\n" + "\n" + "\n" + freelancer_data[141:freelancer_data_lenght] + "..." + "\n" + "\n" + "Link to order: https://www.freelancer.com/jobs/python/" + "\n" + "\n" + "\n")

    freelance = Burses("https://freelance.ru/project/search/pro?c=&c%5B%5D=4&q=&m=or&e=&a=0&a=1&v=0&f=&t=&o=0&b=")
    freelance_data = freelance.scrape(freelance.resp_text, "a", "description").replace("</a>", "").replace('<a class="description" href="/projects/bot-telegramm-pochasovaya-oplata-1516022.html" target="_blank" title="Фрагмент описания">', '')
    print(freelance_data + "\n" + "\n" + "Link to order: https://freelance.ru/project/search/pro?c=&c%5B%5D=4&q=&m=or&e=&a=0&a=1&v=0&f=&t=&o=0&b=" + "\n" + "\n" + "\n")

    guru = Burses("https://www.guru.com/d/jobs/c/programming-development/")
    guru_data = guru.scrape(guru.resp_text, "p", "jobRecord__desc").replace("</p>", "").replace('<p class="jobRecord__desc" v-pre="">', '')
    print(guru_data + "\n" + "\n" + "Link to order: https://www.guru.com/d/jobs/c/programming-development/" + "\n" + "\n" + "\n")

    toogit = Burses("https://www.toogit.com/find-freelance-jobs")
    toogit_data = toogit.scrape(toogit.resp_text, "div", "mb20 text-truncate-wrap").replace("</div>", "")
    print(toogit_data[38:] + "\n" + "\n" + "Link to order: https://www.toogit.com/find-freelance-jobs" + "\n" + "\n" + "\n")

while True:
    
    print("Select option:\n\
    1. Automatic updating of order texts\n\
    2. Updating order texts manually\n\
    3. About us\n\
    4. Links\n\
    5. Exit\n")

    user_answer = input("What is your choice?\n\n")
    
    if user_answer == "1":
        second_user_answer = input("\n\n" + "At what time interval should the order texts be updated?\
 Enter the number of minutes. Keep in mind that automatically the order texts will be updated 6 times.\
 It is recommended to update the order texts every ten minutes. Enter any other symbol other than a number to exit the menu\n\n")
        try:
            count = int(second_user_answer)
            print("\n\n" + "Loading...")
            for i in range(6):
                scraping()
                print("Loading...")
                time.sleep(count*60)
        except ValueError:
            print("\nYou enter a not number. Exit to the menu...\n\n\n")
        except:
            print("\n" + "Error. Please, check your internet connection, or let me know on my GitHub\n\n\n")

    elif user_answer == "2":
        while True:
            user_answer = input("\nUpdate order texts? Y/N \n\n")
            if user_answer.lower() == "y":
                print("\n" + "Loading...")
                time.sleep(10)
                try:
                    scraping()
                except:
                    print("\n" + "Error. Please, check your internet connection, or let me know on my GitHub")
            elif user_answer.lower() == "n":
                print("\n" + "Script stopped\n\n\n")
                break
            else:
                print("Invalid input")

    elif user_answer == "3":
        print('\n\nWe are a team of developers, creating open source software to help people around the world solve their problems and improve the quality of life. We strive to ensure that our products are available to everyone who needs them, and that our work is available to the public. We believe in the power of community and encourage everyone to join us in creating a better world. Thanks for choosing us!\n\n')

    elif user_answer == "4":
        print("""
\n\nTelegram: @iNeonYT | @PyCodeMan \n
Coding Telegram: t.me/acodebeta \n
GitHub: https;//github.com/ACodeBeta \n
Mail: codebeta@mail.ru
\n
""")

    elif user_answer == "5":
        print("\nProgramm finished...")
        break

    else:
        print("Invalid input")
