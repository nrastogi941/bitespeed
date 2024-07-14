from src.databases import db
from src.resources.model import Contact
from sqlalchemy import false


def upsert_contact(request_data):
    email = request_data.get("email")
    phone_number = request_data.get("phoneNumber")

    if not (email or phone_number):
        return {"At least one of email or phoneNumber must be provided"}, 400

    existing_email_contact = None
    existing_phonenumber_contact = None
    parent_id = None
    if email:
        existing_email_contact = Contact.query.filter(
            Contact.email == email,
            Contact.is_deleted == false(),
        ).first()

    if phone_number:
        existing_phonenumber_contact = Contact.query.filter(
            Contact.phoneNumber == phone_number,
            Contact.is_deleted == false(),
        ).first()

    contact_data = None
    if existing_email_contact and existing_phonenumber_contact:
        parent_id = existing_email_contact.id
        if existing_email_contact.id == existing_phonenumber_contact.id:
            return parent_id, 200
        existing_phonenumber_contact.update(
            {
                "email": email,
                "phoneNumber": phone_number,
                "linkedId": parent_id,
                "linkPrecedence": "secondary",
            }
        )
    elif existing_email_contact or existing_phonenumber_contact:
        parent_id = (
            existing_email_contact.id
            if existing_email_contact
            else existing_phonenumber_contact.id
        )
        existing_linked_precedence = (
            existing_email_contact.linkPrecedence
            if existing_email_contact
            else existing_phonenumber_contact.linkPrecedence
        )
        existing_linked_id = (
            existing_email_contact.linkedId
            if existing_email_contact
            else existing_phonenumber_contact.linkedId
        )
        if existing_linked_precedence == "secondary":
            return existing_linked_id, 200
        contact_data = Contact(
            email=email,
            phoneNumber=phone_number,
            linkedId=parent_id,
            linkPrecedence="secondary",
        )
        db.session.add(contact_data)
    else:
        contact_data = Contact(
            email=email,
            phoneNumber=phone_number,
        )
        db.session.add(contact_data)
        parent_id = contact_data.id
    db.session.commit()
    parent_contact_id = parent_id if parent_id else contact_data.id
    return parent_contact_id, 200
