import datetime as dt
import smtplib
import random
import pandas

# set my email and user
my_email = "enteremailhere@email.com"
my_pass = "password"

# read the csv and turn it into a dictionary that's able to be worked with...
birthdays = pandas.read_csv("birthdays.csv")
birthdays_dict = birthdays.to_dict(orient="records")

# instructor's method for birthday dictionary
# birthdays_dicts = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in birthdays.iterrows()}


# grab today's date and month
now = dt.datetime.now()
today = now.date()
current_day = today.day
current_month = today.month

# instructor's way of today's date
# todays_tuple = (today.month, today.day)

# sets random letter to use for letter_(1,2,3).txt
letter_num = random.randint(1, 3)

for index in range(0, len(birthdays_dict)):

    if birthdays_dict[index]["day"] == current_day and birthdays_dict[index]["month"] == current_month:
        name = birthdays_dict[index]["name"]

        with open(f"./letter_templates/letter_{letter_num}.txt") as letter_file:
            letter = letter_file.read()
            placeholder = "[NAME]"
            if placeholder in letter:
                finished_letter = letter.replace("[NAME]", name)

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_pass)
            connection.sendmail(
                from_addr=my_email,
                to_addrs="joey.ohannesian@yahoo.com",
                msg=f"Subject:Happy Birthday!\n\n"
                    f"{finished_letter}")

# instructor's method to determine if today's date matches a birthday
# if todays_tuple in birthdays_dict:
#     birthday_person = birthdays_dict[todays_tuple]
#     file_path = f"letter_templates/letter_{random.randint(1,3).txt}"
#     with open(file_path) as letter_file:
#         contents = letter_file.read()
#         contents.replace("[NAME]", birthday_person["name"])

# my method to send email was same as instructor's
