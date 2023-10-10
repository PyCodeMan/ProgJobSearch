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
        data = soup.find(tag, class_=html_cls).text
        return data.replace('  ', '')


def scraping():

    freelancer = Burses("https://www.freelancer.com/jobs/python/")
    freelancer_data = freelancer.scrape(freelancer.resp_text, "p", "JobSearchCard-primary-description")

    freelance = Burses("https://freelance.ru/project/search/pro?c=&c%5B%5D=4&q=&m=or&e=&a=0&a=1&v=0&f=&t=&o=0&b=")
    freelance_data = freelance.scrape(freelance.resp_text, "a", "description")

    guru = Burses("https://www.guru.com/d/jobs/c/programming-development/")
    guru_data = guru.scrape(guru.resp_text, "p", "jobRecord__desc")
    
    order_texts = f'\n\n\n{freelancer_data} \n\nLink to order: https://www.freelancer.com/jobs/python/\
    \n\n\n{freelance_data} \n\nLink to order: https://freelance.ru/project/search/pro?c=&c%5B%5D=4&q=&m=or&e=&a=0&a=1&v=0&f=&t=&o=0&b=\
    \n\n\n{guru_data} \n\nLink to order: https://www.guru.com/d/jobs/c/programming-development/ \n\n\n'
    return order_texts


def update_manually():

    user_answer = input("\nUpdate order texts? Y/N \n\n")
    if user_answer.lower() == "y":
        print("\n" + "Loading...")
        time.sleep(10)
        print(scraping())
        update_manually()
    elif user_answer.lower() == "n":
        print("\n" + "Exit to the menu...\n\n\n")
        main()
    else:
        print("Invalid input")
        update_manually()


def main():

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
                print(scraping())
                print(f'Wait {count} minutes...\n\n\n')
                time.sleep(count*60)
            else:
                print('End. Exit to main menu...\n\n\n')
                main()
        except ValueError:
            print("\nYou enter a not number. Exit to the menu...\n\n\n")
            main()
    
    elif user_answer == "2":
        update_manually()
    
    elif user_answer == "3":
        print('\n\n' + '''We are a team of developers, creating open source software to help people around the world solve their problems and improve the quality of life.
We strive to ensure that our products are available to everyone who needs them, and that our work is available to the public.
We believe in the power of community and encourage everyone to join us in creating a better world. Thanks for choosing us!''' + '\n\n')
        main()
    
    elif user_answer == "4":
        print("""
\n\nTelegram: @iNeonYT | @PyCodeMan \n
Coding Telegram: t.me/acodebeta \n
GitHub: https://github.com/ACodeBeta \n
Mail: codebeta@mail.ru
\n
""")
        main()
    
    elif user_answer == "5":
        print("\nProgramm finished...")
    
    else:
        print("\n\nInvalid input\n\n")
        main()


if __name__ == '__main__':
    main()