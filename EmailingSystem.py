from nylas import APIClient
import datetime
import random

#these variables need to be updated using the nylas dashboard
CLIENT_ID = "2zoibek2fkz4g7761hzz7j9tq"
CLIENT_SECRET = "c2gsp2d61b2kcdo8cp5ko75gr"
ACCESS_TOKEN = "FeP5GffLRVEE5L6XGUupnh9IOX5lkF"

nylas = APIClient(
    CLIENT_ID,
    CLIENT_SECRET,
    ACCESS_TOKEN,
)


def email_user(email, name, message):
    today = datetime.date.today()

    # Textual month, day and year
    today_date = today.strftime("%B %d, %Y")


    funny_img1 = "TrainerImages/great_job2.jpeg"
    funny_img2 = "TrainerImages/you_rock.jpeg"
    funny_images = [funny_img1, funny_img2]
    random_img = random.randint(0, 1)

    attachment = open(funny_images[random_img], 'rb')
    file = nylas.files.create()
    file.filename = 'complete1.jpg'
    file.stream = attachment
    file.save()
    attachment.close()

    draft = nylas.drafts.create()
    draft.subject = "Performance Summary"

    # Email message as a strigfied HTML
    greeting = "<p style=\"font-size:30px; text-align: center; color:Red;\"> <b>Amazing Workout " + name + "! </b> </p> <br>"
    performance_summary = "<p style=\"font-size:20px; text-align: center;\"><b>Here is your Performance Summary<b> for "
    message = today_date + ":<br><br>" + message

    draft.body = greeting + performance_summary + message
    draft.to = [{'name': name, 'email': email}]
    draft.attach(file)
    draft.send()


def main():
    message="This is a test message like a demo email"
    email_user("rspraneethchandra@gmail.com", "Sai", message)


# if __name__ == "__main__":
    # main()

