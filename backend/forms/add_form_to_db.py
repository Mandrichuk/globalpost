import sqlite3
import json

with sqlite3.connect("forms.db") as connect:
    cursor = connect.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS forms (
            sender TEXT,
            sender_country TEXT,
            sender_city TEXT,
            sender_street TEXT,
            sender_houseNumber TEXT,
            sender_zipCode TEXT,
            sender_email TEXT,
            sender_phoneNumber TEXT,
            recipient TEXT,
            recipient_country TEXT,
            recipient_city TEXT,
            recipient_street TEXT,
            recipient_houseNumber TEXT,
            recipient_zipCode TEXT,
            recipient_email TEXT,
            recipient_phoneNumber TEXT,
            shippingForm_addressInput TEXT,
            paymentForm_contactAfter TEXT,
            paymentForm_acceptRules TEXT
        );
    """
    )



def add_form_to_db(formData):
    with sqlite3.connect("forms.db") as connect:
        cursor = connect.cursor()

        # # Convert nested dictionaries to JSON strings
        # formData['sender_country'] = json.dumps(formData['sender_country'])
        # formData['recipient_country'] = json.dumps(formData['recipient_country'])

        # Execute the SQL query
        cursor.execute(
            """
            INSERT INTO forms (
                sender, 
                sender_country, 
                sender_city, 
                sender_street, 
                sender_houseNumber, 
                sender_zipCode, 
                sender_email, 
                sender_phoneNumber,
                recipient,
                recipient_country,
                recipient_city,
                recipient_street,
                recipient_houseNumber,
                recipient_zipCode,
                recipient_email,
                recipient_phoneNumber,
                shippingForm_addressInput,
                paymentForm_contactAfter,
                paymentForm_acceptRules
            ) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?); 
            """,
            (
                formData.sender,
                formData.sender_country,
                formData.sender_city,
                formData.sender_street,
                formData.sender_houseNumber,
                formData.sender_zipCode,
                formData.sender_email,
                formData.sender_phoneNumber,
                formData.recipient,
                formData.recipient_country,
                formData.recipient_city,
                formData.recipient_street,
                formData.recipient_houseNumber,
                formData.recipient_zipCode,
                formData.recipient_email,
                formData.recipient_phoneNumber,
                formData.shippingForm_addressInput,
                formData.paymentForm_contactAfter,
                formData.paymentForm_acceptRules,
            ),
        )

    return 0