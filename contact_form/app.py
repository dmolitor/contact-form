from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
from shiny import App, reactive, render, ui
import smtplib

# Get GMAIL password from GitHub Secrets
GMAIL_PASS = dict(os.environ)['GMAIL_PASS']

app_ui = ui.page_fluid(
    ui.row(
        ui.column(4),
        ui.column(
            4,
            ui.h1("Contact Form", style="text-align:center; padding-top:1%;"),
            ui.br(),
            """
            Thanks for visiting my awesome contact form! If you want to drop me
            a line and let me know just how much you love it, simply fill out
            the form below and I'll be in touch with you never.
            """,
            ui.hr(),
            ui.input_text(
                id="userName",
                label=ui.span("Name", ui.span("*", style="color:red")),
                placeholder="John Doe",
                width="100%"
            ),
            ui.input_text(
                id="userPhone",
                label="Phone Number",
                placeholder="(123) 456-7890",
                width="100%"
            ),
            ui.input_text(
                id="userEmail",
                label=ui.span("Email", ui.span("*", style="color:red")),
                placeholder="john.doe@gmail.com",
                width="100%"
            ),
            ui.input_text_area(
                id="userMessage",
                label=ui.span(
                    "Message",
                    ui.span("*", style="color:red")
                ),
                width="100%"
            ),
            ui.help_text(
                ui.span(
                    ui.span("*", style="color:red"),
                    "Indicates required field"
                ),
                ui.br()
            ),
            ui.br(),
            ui.input_action_button(
                id="userSubmit",
                label="Submit",
                width="100%",
                style="background-color:#4caf50; color:white;"
            ),
            align="justify"
        ),
        ui.column(4)
    ),
    title="Contact Form"
)

def server(input, output, session):
    @reactive.Calc
    def send_email():
        user_name = input.userName()
        user_name = input.userName()
        user_phone = input.userPhone()
        user_email = input.userEmail()
        user_message = input.userMessage()
        # Don't allow submission of the form if required fields are empty
        if user_name == "":
            submit_status = ui.help_text(
                ui.span(ui.HTML("<b>Name is missing</b>"), style="color:red;"),
                id="submitStatus"
            )
            return submit_status
        elif user_email == "":
            submit_status = ui.help_text(
                ui.span(ui.HTML("<b>Email is missing</b>"), style="color:red;"),
                id="submitStatus"
            )
            return submit_status
        elif user_message == "":
            submit_status = ui.help_text(
                ui.span(ui.HTML("<b>Message is missing</b>"), style="color:red;"),
                id="submitStatus"
            )
            return submit_status
        # Construct and send email
        mail_content = (
            f"Name : {user_name}"
            + f"\nPhone Number : {user_phone}"
            + f"\nEmail : {user_email}"
            + f"\n{'-'*80}"
            + f"\n{user_message}"
        )
        sender_address = "molitdj97@gmail.com"
        sender_pass = GMAIL_PASS
        receiver_address = "molitdj97@gmail.com"
        message = MIMEMultipart()
        message['From'] = sender_address
        message['To'] = receiver_address
        message['Subject'] = f"Personal Website Contact Form - {user_name}"
        message.attach(MIMEText(mail_content, 'plain'))
        session = smtplib.SMTP('smtp.gmail.com', 587)
        session.starttls()
        session.login(sender_address, sender_pass)
        text = message.as_string()
        session.sendmail(sender_address, receiver_address, text)
        session.quit()
        # Return confirmation to user
        submit_status = ui.help_text(
            ui.span(ui.HTML("<b>Form submitted successfully!</b>"), style="color:blue;"),
            id="submitStatus"
        )
        return submit_status
    
    @reactive.Effect
    @reactive.event(input.userSubmit)
    def _():
        btn_value = input.userSubmit()
        email_status = send_email()
        if btn_value > 0:
            ui.remove_ui("#submitStatus")
        ui.insert_ui(ui=email_status, selector="#userSubmit", where="afterEnd")

app = App(app_ui, server)
